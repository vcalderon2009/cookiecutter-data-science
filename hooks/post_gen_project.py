#!/usr/bin/env python

import os
import shutil


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def copy_file(original_filepath, new_filepath):
    shutil.copyfile(os.path.join(PROJECT_DIRECTORY, original_filepath),
                    os.path.join(PROJECT_DIRECTORY, new_filepath))


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

license_files = {"BSD 3-Clause": 'BSD3.rst',
                 "GNU GPL v3+": 'GPLv3.rst',
                 "Apache Software Licence 2.0": 'APACHE2.rst',
                 "BSD 2-Clause": 'BSD2.rst'}


def process_licence(licence_name):
    """
    Processes the License file for the document.

    Parameters
    ----------
    licence_name : str
        Name of the License to use.
    """
    if licence_name in license_files:
        shutil.copyfile(os.path.join(PROJECT_DIRECTORY, 'licenses', license_files[licence_name]),
                        os.path.join(PROJECT_DIRECTORY, 'LICENSE.rst'))
    ##
    ## Remove `licenses` folder
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, 'licenses'))

def process_conf_docs():
    """
    Selects the correct `conf.py` file for the project documentation.
    """
    if '{{ cookiecutter.use_astropy_theme_or_RTD}}' == 'RTD':
        shutil.copyfile(os.path.join(PROJECT_DIRECTORY, 'docs', 'read_docs', 'conf_rtd.rst'),
                        os.path.join(PROJECT_DIRECTORY, 'docs', 'conf.py'))
    ##
    ## Removing `read_docs` folder
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, 'docs','read_docs'))


if __name__ == '__main__':

    process_licence('{{ cookiecutter.license }}')

    if '{{ cookiecutter.use_travis_ci }}' != 'y':
        remove_file('.travis.yml')

    if '{{ cookiecutter.use_read_the_docs }}' != 'y':
        remove_file('.rtd-environment.yml')
        remove_file('readthedocs.yml')

    ##
    ## Astropy Helpers
    try:
        from git import Repo

        new_repo = Repo.init(PROJECT_DIRECTORY)
        new_repo.git.add('.')
        new_repo.index.commit(
            "Creation of {{ cookiecutter.repo_name }} from astropy package template"
        )
        if '{{{cookiecutter.use_astropy_theme_or_RTD}}}' == 'Astropy':
            astropy_helpers_version = "{% if cookiecutter.minimum_python_version == '2.7' %}v2.0.6{% else %}v3.0.1{% endif %}"
            Repo.create_submodule(
                new_repo, "astropy_helpers", "astropy_helpers",
                "https://github.com/astropy/astropy-helpers.git",
                "{}".format(astropy_helpers_version))
            new_repo.submodules[0].update()
            copy_file('astropy_helpers/ah_bootstrap.py', 'ah_bootstrap.py')
            new_repo.git.add('ah_bootstrap.py')
            new_repo.index.commit(
                "Initialize astropy_helpers at version {}".format(
                    astropy_helpers_version))
    except ImportError:
        print(
            "gitpython is not installed so the repository will not be initialised "
            "and astropy_helpers not downloaded.")
