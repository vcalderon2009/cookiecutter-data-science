|RTD| |License| |Issues| |PDF_Latest|

.. _INSTALL_MAIN:

************************************************************************
Downloading and Creating your own Paper
************************************************************************

**Author**: `Victor Calderon <http://vcalderon.me>`_ (`victor.calderon@vanderbilt.edu <mailto:victor.calderon@vanderbilt.edu>`_)

**Description**: An easy, reasonably standardized, but flexible template for creating paper for
the `Monthly Notices of the Royal Astronomical society <https://academic.oup.com/mnras>`_

.. contents:: Table of Contents
    :local:

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

.. _creating_new_paper:

=====================
Creating a new Paper
=====================

After having done the steps in :ref:`install_requirements`, you can start
creating the skeleton for the new MNRAS paper.

To start a new paper, run:

.. code-block:: bash

    cookiecutter https://github.com/vcalderon2009/MNRAS_Cookiecutter

This will prompt you to answer a few questions like:

Next, it will prompt you for some answers.
The different prompts are:

+----------------------------+-----------------------------------------------+
|Question                    | Description                                   |
+============================+===============================================+
|:code:`author_first_name`   | Author's first name. :code:`author_first_name`|
|                            | will be used for the *title* of the paper     |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * Adam                                        |
|                            | * Rose                                        |
+----------------------------+-----------------------------------------------+
|:code:`author_last_name`    | Author's **last** name. :code:`last_name`     |
|                            | will be used for the *title* of the paper     |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * Calderon                                    |
|                            | * Piscionere                                  |
+----------------------------+-----------------------------------------------+
|:code:`author_name`         | Author's first name. :code:`author_name`      |
|                            | will be used for the *title* of the paper     |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * Adam Sanchez                                |
|                            | * Rose Roserberg                              |
+----------------------------+-----------------------------------------------+
|:code:`author_email`        | Author's first name. :code:`author_email`     |
|                            | will be used for the *title* of the paper     |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * some_email@gmail.com                        |
|                            | * another_email@yahoo.com                     |
+----------------------------+-----------------------------------------------+
|:code:`author_affiliation`  | Name of the department.                       |
|                            | Should **not** have '_' (underscores) symbols |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * Vanderbilt University                       |
|                            | * Some other University                       |
+----------------------------+-----------------------------------------------+
|:code:`paper_title`         | Title of the thesis. Should not have '_'      |
|                            | symbols in it.                                |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * Understanding Exoplanets and Other Sources  |
|                            | * The Clustering of Galaxies on the           |
|                            |   Smallest Scales Across Cosmic Time          |
+----------------------------+-----------------------------------------------+
|:code:`paper_pubyear`       | Year of the publication. Must be numeric.     |
|                            |                                               |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * 2018                                        |
|                            | * 2017                                        |
+----------------------------+-----------------------------------------------+
|:code:`repo_name`           | Name of the directory/repository,             |
|                            | paper will be saved.                          |
|                            | This name is selected by default, but can be  |
|                            | changed. This field                           |
|                            | *should not contain spaces*                   |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * Calderon_Victor_Astro_PhD_Thesis            |
|                            | * Szewciw_Adam_Astro_PhD_Thesis               |
+----------------------------+-----------------------------------------------+
|:code:`github_username`     | Author's Github username. This will be use to |
|                            | link to the paper to the Github repository.   |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * username                                    |
|                            | * username2018                                |
+----------------------------+-----------------------------------------------+
|:code:`github_project`      | Name of the project on Github                 |
|                            |                                               |
|                            | Examples:                                     |
|                            |                                               |
|                            | * Awesome_Paper_username_2018                 |
|                            | * Another_awesome_paper                       |
+----------------------------+-----------------------------------------------+
|:code:`open_source_license` | Type of License for the paper. Without this,  |
|                            | one cannot use any of.                        |
|                            |                                               |
|                            | Options:                                      |
|                            |                                               |
|                            | * MIT                                         |
|                            | * BSD 3-Clause                                |
|                            | * GNU GPL v3+                                 |
|                            | * Apache Software Licence 2.0                 |
|                            | * BSD 2-Clause*                               |
+----------------------------+-----------------------------------------------+

.. _using_template:

=====================
Using the Template
=====================

Now that one has answered the questions from :ref:`creating_new_paper`,
you just need to fill in the documents in the ``Section_files`` directory
according to your project's needs.

The structure of the finalized project can be found in the
:ref:`proj_structure` section.

.. _uploading_overleaf:

==================================
Uploading your Project to Overleaf
==================================

Once you have completed setting up your paper, and are ready to start
the writing process, you can upload your paper to
`Overleaf <https://www.overleaf.com/>`_.

Overleaf, as explained on their website, is:

.. epigraph::

   Overleaf is a free service that lets you create, edit and share your
   scientific ideas easily online using LaTeX, a comprehensive and powerful
   tool for scientific writing.

   -- Overleaf Team

For a more in-depth tutorial on how to use
`Overleaf <https://www.overleaf.com/>`_, you can visit
`Overleaf Tutorial <https://www.overleaf.com/tutorial>`_ and watch the
attached video.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; max-height: 100%; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/g8Ejj0T0yG4" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

.. _steps_overleaf:

--------------------------------------------------
Steps to follow to upload your project to Overleaf
--------------------------------------------------

In order to upload your project to Overleaf, you need to follow the
following steps:

- Compress the output of ``cookiecutter`` template to a ``zip`` file.
- Create an account on Overleaf. Go to `Overleaf Sign-up <https://www.overleaf.com/signup>`_ 
- Create a **new, empty** "New Project"
- Click on **"Upload Project"**
- **Drag and drop** or click on **Select a .zip file**
- Connect your `Mendeley <https://www.mendeley.com/>`_ account. Open one if
  you don't have one. This will link your bibliography with Overleaf.
  See more `here <https://www.overleaf.com/blog/184-mendeley-integration-is-here-import-your-mendeley-reference-library-into-overleaf#.W4FGoZNKhhE>`_ 
- Remove the current 'Mendeley.bib' file from the project tree
- Click on "New file" > "From Mendeley" and name it **Mendeley.bib** and put
  it in the *root* directory of the project.

For a brief video on how to do this, see the following video:

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; max-height: 100%; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/t21IDEdGAUw" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

**And now you have a new, working MNRAS paper**

You can start writing now!


.. ----------------------------------------------------------------------------

Project based on the `modified <https://github.com/vcalderon2009/MNRAS_Cookiecutter>`_  version of the
`MNRAS LaTeX Template <https://www.overleaf.com/latex/templates/monthly-notices-of-the-royal-astronomical-society-mnras-latex-template-and-guide-for-authors/kqnjzrwjwjth>`_.

.. |Issues| image:: https://img.shields.io/github/issues/vcalderon2009/MNRAS_Cookiecutter.svg
   :target: https://github.com/vcalderon2009/MNRAS_Cookiecutter/issues
   :alt: Open Issues

.. |RTD| image:: https://readthedocs.org/projects/mnras-cookiecutter/badge/?version=latest
   :target: https://mnras-cookiecutter.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/vcalderon2009/MNRAS_Cookiecutter/blob/master/LICENSE
   :alt: Project License

.. |PDF_Latest| image:: https://img.shields.io/badge/PDF-Latest-orange.svg
   :target: https://cdn.rawgit.com/vcalderon2009/MNRAS_Cookiecutter/777d6518/docs/documents/MNRAS_output_example.pdf
   :alt: PDF Latest
