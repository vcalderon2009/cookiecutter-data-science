|RTD| |License| |Issues| |Version_RTD| |Version_Astropy|

.. _INSTALL_MAIN:

************************
Structuring your Project
************************

**Author**: `Victor Calderon <http://vcalderon.me>`_ (`victor.calderon@vanderbilt.edu <mailto:victor.calderon@vanderbilt.edu>`_)

**Description**: A logical, reasonably standardized, but flexible project structure for doing and sharing data science work.

Now that your have a *working* version of **python** on your computer,
you can start doing research.

One of the key elements of a project is for it to be **reproducible** by 
others. Having this in mind when you're structuring your project will 
allow others to look at your code, understand it well enough to be able 
to **recreate** your results.

This is a short guide on 2 ways to structure your code, without having 
to do much of creating documets, etc.

.. contents:: Table of Contents
    :local:

.. _proj_struc_cookiecutter_sec:

=================================
Cookiecutter and Folder structure
=================================

`Cookiecutter <https://github.com/audreyr/cookiecutter>`_ is a command-line
utility that creates projects from cookiecutters (project templates), 
e.g. Python package projects, LaTeX documents, etc.

Cookiecutter has been widely used for many projects, and each team and 
organization can create their own *template*. For more information,
visit the 
`cookiecutter documentation <https://cookiecutter.readthedocs.io/en/latest/>`_.

As the famous say goes:

.. epigraph::

   Don't reinvent the wheel!

You can always create your own folder and file structures, and organize 
your documents the old-fashioned way. The problem with this is that 
it may **vary** from project to project, and it will be more difficult to 
be consistent and effective throught your projects.

For this reason, I rely on ``cookiecutter`` templates to create the 
file and folder structure of a project.

There are many different ``cookiecutter`` templates out there, but 
after trying to find the best one that suits my needs in **research** and 
**programming**, I found one that works great! And after some modifications,
I came up with a *version* of this template.

These two templates are shown in :ref:`proj_struc_cookiecutter_DS` and 
:ref:`proj_struc_cookiecutter_VC`. But first, let's make sure you have
``cookiecutter`` installed correctly.

.. _install_requirements:

============================================
Requirements to use `cookiecutter` templates
============================================

The minimum rquirements for creating `cookiecutter` templates are:

- Python 2.7 or 3.5
- `Cookiecutter Python package <http://cookiecutter.readthedocs.org/en/latest/installation.html>`_ >= 1.4.0: This can be installed with `pip` or `conda` depending on how you manage your Python packages.

You  can install it by typing this on the terminal

.. code-block:: bash

    pip install cookiecutter

or via Anaconda:

.. code-block:: bash

    conda config --add channels conda-forge
    conda install cookiecutter

Now you can use `cookiecutter` to create new templates for projects and papers!

.. _proj_struc_cookiecutter_DS:

===========================
Data Science - Cookiecutter
===========================

`Cookiecutter Data Science <https://drivendata.github.io/cookiecutter-data-science/>`_ is best described as

    A logical, reasonably standardized, but flexible project structure for 
    doing and sharing data science work.

This folder structure allows everyone looking at your code to understand 
it right away. It also provides many different functions (as part of a 
``Makefile``) that simplify the workflow of your project.

In a nutshell, this cookiecutter includes:

- A **Makefile** file with **useful functions.
- **Documentation** to make your project easily accessible and readable
- And more!

In order to use this template, you follow the documentation in 
`Cookiecutter Data Science <https://drivendata.github.io/cookiecutter-data-science/>`_.

.. _proj_struc_cookiecutter_VC:

================================
Personal version - Cookiecutter 
================================

If you need more than the *normal* Data Science Cookiecutter template, you can 
use my version. Some of the differences are:

- It includes and easy-to-use ``environment.yml`` file that makes it easy to 
  install dependencies.
- Extra functions in the ``Makefile``.
- Choice of what kind of documenation to use. One has the option choose from 
  *traditional* `Read The Docs <https://readthedocs.org/dashboard/>`_ style or 
  the `Astropy Sphinx Theme <https://github.com/astropy/sphinx-astropy>`_.

You can check how these two styles look like:

- |RTD_rtdtheme| - **Read The Docs Version**
- |RTD_astropytheme| - **Astropy Version**

Next, you can create your own Project based on this *cookiecutter* version

.. _cookiecutter_prompts:

----------------------------------
To start a new project and prompts
----------------------------------

To start a new project, type the following:

.. code-block:: text

    $ cookiecutter https://github.com/vcalderon2009/cookiecutter-data-science

If you want the **default** project scheme from *DrivenData* (see above), run:

.. code-block:: text

    cookiecutter https://github.com/drivendata/cookiecutter-data-science

Depending on what kind of folder structure you want, you might want to choose from the different types.

After running this command, **you will be prompted some questions** regarding 
the parameters for the project. This will prompt you to answer a few
questions like:

+----------------------------------+------------------------------------------+
|Question                          | Description                              |
+==================================+==========================================+
| :code:`project_name`             | Name of the project. This can be         |
|                                  | similar to one on Github.                |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * SDSS_analysis                          |
|                                  | * Lung_cancer_analysis                   |
+----------------------------------+------------------------------------------+
| :code:`repo_name`                | Name of the directory/repository,        |
|                                  | the project will be saved.               |
|                                  | This field *should not contain spaces*   |
|                                  | *should not contain spaces*              |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * Calderon_Victor_Astro_PhD_Thesis       |
|                                  | * Szewciw_Adam_Astro_PhD_Thesis          |
+----------------------------------+------------------------------------------+
| :code:`author_name`              | Author's first name. It can include      |
|                                  | spaces                                   |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * Adam Sanchez                           |
|                                  | * Rose Roserberg                         |
+----------------------------------+------------------------------------------+
| :code:`author_email`             | Author's email address.                  |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * some_email@gmail.com                   |
|                                  | * another_email@yahoo.com                |
+----------------------------------+------------------------------------------+
| :code:`short_description`        | A short description of the project.      |
|                                  | This can be a *brief* overview of the    |
|                                  | project.                                 |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * Repository for lung cancer analysis    |
|                                  | * Analysis on galaxies and cosmology     |
+----------------------------------+------------------------------------------+
| :code:`long_description`         | A longer version of                      |
|                                  | :code:`short_description`                |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * Repository for lung cancer analysis    |
|                                  | * Analysis on galaxies and cosmology     |
+----------------------------------+------------------------------------------+
| :code:`open_source_license`      | Type of License for the paper. Without   |
|                                  | this, one cannot use any of.             |
|                                  |                                          |
|                                  | Options:                                 |
|                                  |                                          |
|                                  | * MIT                                    |
|                                  | * BSD 3-Clause                           |
|                                  | * GNU GPL v3+                            |
|                                  | * Apache Software Licence 2.0            |
|                                  | * BSD 2-Clause*                          |
+----------------------------------+------------------------------------------+
| :code:`s3_bucket`                | Path to AWS storage.                     |
|                                  | This is **temporarily** disabled!!       |
|                                  |                                          |
+----------------------------------+------------------------------------------+
| :code:`aws_profile`              | AWS profile name.                        |
|                                  | This is **temporarily** disabled!!       |
|                                  |                                          |
+----------------------------------+------------------------------------------+
| :code:`conda_python_env`         | Name of the project's anaconda           |
|                                  | environment. In order to use the         |
|                                  | packages of this project, you need       |
|                                  | to first ``activate`` this environment.  |
|                                  |                                          |
|                                  |                                          |
|                                  |                                          |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * lung_cancer_env                        |
|                                  | * SDSS_galaxies_env                      |
+----------------------------------+------------------------------------------+
| :code:`github_username`          | Author's Github username. This will      |
|                                  | be use tolink the project to the         |
|                                  | Github repository.                       |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * username                               |
|                                  | * username2018                           |
+----------------------------------+------------------------------------------+
| :code:`github_project`           | Name of the project on Github            |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * Awesome_lung_analysis_username_2018    |
|                                  | * Another_awesome_analysis               |
+----------------------------------+------------------------------------------+
| :code:`project_version`          | Version of the project.                  |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * 0.0.1                                  |
|                                  | * 0.1.2dev                               |
+----------------------------------+------------------------------------------+
| :code:`use_travis_ci`            | If 'y', '.travis.yml' will be installed  |
|                                  | This is useful when doing                |
|                                  | 'continuous integration'                 |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * y                                      |
|                                  | * n                                      |
+----------------------------------+------------------------------------------+
| :code:`use_read_the_docs`        | If 'y', it will use ReadTheDocs for docs |
|                                  |                                          |
+----------------------------------+------------------------------------------+
| :code:`project_url`              | URL of the project *on Github*!          |
|                                  | You need to create this repository       |
|                                  | separately.*                             |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * https://github.com/username/proj_name  |
+----------------------------------+------------------------------------------+
| :code:`minimum_python_version`   | Python version to use for this analysis. |
|                                  | This will set the python version in the  |
|                                  | 'environment.yml' file.                  |
|                                  |                                          |
+----------------------------------+------------------------------------------+
| :code:`python_interpreter`       | It assumes Python 3 version by *default* |
|                                  |                                          |
|                                  | Examples:                                |
|                                  |                                          |
|                                  | * Adam                                   |
|                                  | * Rose                                   |
+----------------------------------+------------------------------------------+
| :code:`use_astropy_theme_or_RTD` | Option for which kind of documentation   |
|                                  | to use.                                  |
|                                  | See the examples above to see which one  |
|                                  | you like.                                |
|                                  |                                          |
|                                  | Options:                                 |
|                                  |                                          |
|                                  | * **RTD**: Used ReadTheDocs-type of docs |
|                                  | * **Astropy**: Used Astropy-type of docs |
+----------------------------------+------------------------------------------+


.. _using_template:

------------------
Using the Template
------------------

Now that one has answered the questions from :ref:`cookiecutter_prompts`,
you just need to populate the project with scripts, notebooks, and
**of course**, documentation!!

The structure of the finalized project can be found in the
:ref:`proj_structure` section.

.. _proj_struc_cookiecutter_VC_env:

------------------------
Editing your environment
------------------------

Now that you have a working proect from **cookiecutter**, you can start by
editing the *environment* of your project.

If you downloaded **my version of cookiecutter**, you should be able to edit 
the ``environment.yml`` file. This file states which packages 
need to be installed by Anaconda and ``pip``  in order to run the 
scripts of the package.

The ``environment.yml`` file looks like the following:

.. code-block:: text

    name: name_of_environment

    channels:
      - defaults

    dependencies:
      - python>=3.6
      - ipython
      - anaconda
      - astropy
      - h5py
      - numpy
      - pandas
      - scipy
      - seaborn
      - pip
      - pip:
        - GitPython
        - progressbar2

You can edit the ``environment.yml`` file to include/exclude packages 
needed by your project.

After having edited the list of packages needed by your project, you can 
execute the command 

.. code-block:: text

    $ make environment

to **create the environment**.

If you have done this step before, and you want to **update the environment**,
you need to run

.. code-block:: text

    $ make update_environment

instead.


.. _proj_struc_cookiecutter_VC_github:

========================================
Adding your Project repository to Github
========================================

If you follow the instructions from above, you should have

* Downloaded the repository
* Created your own project with the desired file and folder structure
* Created your working **environment** for you project

The next step is to add it to `Github <https://github.com/>`_ and make 
it accessible.

To do this, your should do the following:

1. Create a Github repository with the **same name** as the repository.
2. Type ``git add remote origin git@github.com:<username>/<project_name>.git``.
   In here you need to **replace** ``<username>`` and ``project_name`` with 
   your details.
3. ``git push origin master`` - This will push your project to Github.

To check that you did this correctly, type

.. code-block:: text

    git remote -v

and you should get something that looks like this:

.. code-block:: text

    origin  https://github.com/<username>/<project_name>.git (fetch)
    origin  https://github.com/<username>/<project_name>.git (push)

where ``username`` and ``project_name`` pertain to your repository on 
Github.

Now all of the files are online on Github, and should be ready to integrate 
them with `Read The Docs <https://readthedocs.org/>`_.

.. _proj_struc_cookiecutter_VC_RTD:

==================================
Documentation for your new project
==================================

Now that you have both a working local and online copy of your code, 
the next step is to create the documentation for the project.

For this, you can easily use `Read The Docs <https://readthedocs.org/>`_ (RTD).

You need to do the following:

* Create an account on "Read the Docs"
* Go to your ``Profile`` and select ``My Projects``
* From there, you should import the repository *manually* (it's easier). 
  Click on ``Import a Project`` and follow the instructions.
* You should add the project with the **same name** as the Github Repo if 
  possible. Otherwise, you might need to **change** the links to the *badges*
  on the ``README.md`` files in the project, among others.
* Make sure that the repository was correctly built by looking at the 
  ``Builds`` and see that it compiled correctly. If not, it should tell you 
  if there was an error and what the error was.
* Now you go and change the documentation depending on the project's needs.


.. _proj_struc_cookiecutter_VC_Travis:

=======================================
Continuous Integration for your Project
=======================================

**Continuous integration** deals with testing your code for possible errors,
and making sure that everything is working as expected. Depending on 
your project's needs.

This template includes a ``.travis.yml``, which the files used by 
`Travis CI <https://travis-ci.org/>`_. Travis CI is a *Continuous integration*
platform for testing your code, and checking the functionality of your
project.

.. ----------------------------------------------------------------------------

Project based on the `modified <https://github.com/vcalderon2009/cookiecutter-data-science-vc>`_  version of the
`cookiecutter data science project template <https://drivendata.github.io/cookiecutter-data-science/>`_.

.. |Issues| image:: https://img.shields.io/github/issues/vcalderon2009/cookiecutter-data-science-vc.svg
   :alt: GitHub issues
   :target: https://github.com/vcalderon2009/cookiecutter-data-science-vc/issues

.. |RTD| image:: https://readthedocs.org/projects/cookiecutter-data-science-vc/badge/?version=latest
   :target: https://cookiecutter-data-science-vc.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/vcalderon2009/cookiecutter-data-science-vc/blob/master/LICENSE
   :alt: Project License

.. |Version_RTD| image:: https://img.shields.io/badge/Version-RTD-orange.svg
   :target: http://test-cookieproj-rtd.rtfd.io/
   :alt: Version RTD

.. |Version_Astropy| image:: https://img.shields.io/badge/Version-Astropy-orange.svg
   :target: http://test-cookieproj-astropy.rtfd.io/
   :alt: Version Astropy
