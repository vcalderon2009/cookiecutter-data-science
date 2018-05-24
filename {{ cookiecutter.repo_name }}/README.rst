|RTD| |License| |Issues|

.. _main_title:
************************************************************************
{{cookiecutter.project_name}}
************************************************************************

{{cookiecutter.description}}

**Author**: {{ cookiecutter.authorname }}(`{{cookiecutter.author_email}} <mailto:{{cookiecutter.author_email}}>`_)


.. contents:: **Table of Contents**
    :local:

Installing Environment & Dependencies
=====================================

To use the scripts in this repository, you must have `Anaconda <https://www.anaconda.com/download/#macos>`_ installed on the systems that will
be running the scripts. This will simplify the processes of installing 
all the dependencies.

For reference, see: `Manage Anaconda Environments <https://conda.io/docs/user-guide/tasks/manage-environments.html>`_ 

The package counts with a **Makefile** with useful commands and functions.
You must use this Makefile to ensure that you have all of the necessary 
*dependencies*, as well the correct **conda environment**.

Show all available functions in the Makefile
--------------------------------------------

You can use the *Makefile* for running common tasks like 
*updating environments*, *cleaning extra files*, and more.

To show all available functions in the Makefile, run:

.. code-block:: console

    make show-help

    Available rules:

    clean               Deletes all build, test, coverage, and Python artifacts
    clean-build         Remove build artifacts
    clean-pyc           Removes Python file artifacts
    clean-test          Remove test and coverage artifacts
    environment         Set up python interpreter environment - Using environment.yml
    lint                Lint using flake8
    remove_environment  Delete python interpreter environment
    test_environment    Test python environment is setup correctly
    update_environment  Update python interpreter environment

.. _create_env:
Create environment
-------------------

In order to properly run the commands of this project, you should install the 
**necessary packages** before. For this, you will to have installed 
**Anaconda**, because otherwise you will not be able to use this command.

The name of the environment and its dependencies are explicitely shown in the 
``environment.yml`` file.
In order to create the environment, you must run:

.. code-block:: console

    make environment

The main file that lists all of the dependencies for the project can 
be found as ``environment.yml``.

.. _activate_env:
Activating the environment
----------------------------

Once the environment has been **installed**, you can now *activate* the 
environment by typing

.. code-block:: console

    source activate {{cookiecutter.conda_python_env}}

.. note::

    Depending on your installation of Anaconda, you might have to use the 
    command: 

    .. code-block:: console
    
        conda activate {{cookiecutter.conda_python_env}}

    instead.

.. _updating_env:
Updating environment
--------------------

You can always update the project's environment. The package dependencies
are handled by the ``environment.yml`` file, and sometimes these packages 
need to updaetd.

You can updated the project's environments by running:

.. code-block:: console

    make update_environment

This will update the versions of each of the necessary packages.

.. _deactivating_env:
Deactivating environment
-------------------------

Once you are done running the scripts of this project, you should 
**deactivate** the environment. To do so, run:

.. code-block:: console

    source deactivate

.. note::

    Depending on your installation of Anaconda, you might have to use the 
    command: 

    .. code-block:: console
    
        conda deactivate

    instead.

.. _auto_activate_env:
Auto-activate environment
-------------------------

To make it easier to activate the necessary environment, one can use the 
`conda-auto-env <https://github.com/chdoig/conda-auto-env>`_ package,
which **activates** the necessary environment **automatically**.

See the link above for more information!

.. _usage:
Usage
=====

In order to use the scripts, you can execute the next set of commands.




.. _proj_structure:
Project Structure
=================

The organization of the project is the following:


.. code-block:: text

        ├── LICENSE
        ├── Makefile           <- Makefile with commands like `make data` or `make train`
        ├── README.md          <- The top-level README for developers using this project.
        ├── data
        │   ├── external       <- Data from third party sources.
        │   ├── interim        <- Intermediate data that has been transformed.
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
        │
        ├── models             <- Trained and serialized models, model predictions, or model summaries
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jqp-initial-data-exploration`.
        │
        ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
        │
        ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
        │   └── figures        <- Generated graphics and figures to be used in reporting
        │
        ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
        │                         generated with `pip freeze > requirements.txt`
        │
        ├── environment.yml    <- The Anaconda environment requirements file for reproducing the analysis environment.
        │                         This file is used by Anaconda to create the project environment.
        │
        ├── src                <- Source code for use in this project.
        │   ├── __init__.py    <- Makes src a Python module
        │   │
        │   ├── data           <- Scripts to download or generate data
        │   │   │
        │   │   └── make_dataset.py
        │   │
        │   ├── features       <- Scripts to turn raw data into features for modeling
        │   │   └── build_features.py
        │   │
        │   ├── models         <- Scripts to train models and then use trained models to make
        │   │   │                 predictions
        │   │   ├── predict_model.py
        │   │   └── train_model.py
        │   │
        │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
        │       └── visualize.py
        │
        └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org

Project based on the `modified <https://github.com/vcalderon2009/cookiecutter-data-science-vc>`_  version of
`cookiecutter data science project template <https://drivendata.github.io/cookiecutter-data-science/>`_ 


.. |Issues| image:: https://img.shields.io/github/issues/{{cookiecutter.github_project}}.svg
   :target: https://github.com/{{cookiecutter.github_project}}/issues
   :alt: Open Issues

.. |RTD| image:: https://readthedocs.org/projects/{{cookiecutter.github_project}}/badge/?version=latest
   :target: http://{{cookiecutter.github_project}}.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |License| image:: https://img.shields.io/badge/license-{{cookiecutter.open_source_license}}-brightgreen.svg
   :target: https://github.com/{{cookiecutter.github_project}}/LICENSE
   :alt: Project License

