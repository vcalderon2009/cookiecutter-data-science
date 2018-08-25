|RTD| |License| |Issues| |PDF_Latest|

.. _proj_structure:

=================
Project Structure
=================

The organization of the project is the following:

.. code-block:: text

        ├── Extras <- Folder with documents like main `aliases`, `packages`, etc.
        │    ├── commands.tex <- List of commands used throughout the paper.
        │    └── packages.tex <- List of packages to load for the paper.
        │
        ├── Figures <- Directory for project figures.
        │    └── .gitkeep
        │
        ├── Paper
        │    ├── mnras.bst                             <-- MNRAS bibliography style file.
        │    ├── mnras.cls                             <-- MNRAS class file.
        │    └── paper.tex                             <- Main TeX file for compiling.
        │
        ├── Script_files
        │    ├── modify_bib.sh
        │    ├── hyperlink-year-only-natbib-patch.tex. <- File that fixed the bibliography style.
        │    └── nat2jour.pl
        │
        ├── Section_files
        │   ├── 01_abstract.tex                        <-- File for the 'abstract'.
        │   ├── 02_introduction.tex                    <-- File for the 'Introduction'.
        │   ├── 03_data_methods.tex                    <-- File for the 'Data and Methods'.
        │   ├── 04_results.tex                         <-- File for the 'Results'.
        │   ├── 05_summary_discussion.tex              <-- File for the 'Summary and Discussion'.
        │   └── 06_acknowledgements.tex                <-- File for the 'Acknowledgements'.
        │
        ├── .gitignore                                 <- File that dictates which files to ignore when using `git`.
        ├── Makefile                                   <- Makefile with command, i.e. `make main.tex` or `make clean`
        ├── Makefile.inc                               <- File with input parameters for the `Makefile`.
        ├── Mendeley.bib                               <- Bibliography of the project. You can replace this file if needed.
        ├── README.md                                  <- The top-level README for students
        ├── LICENSE                                    <- License used for the distribution of the paper.
        └── requirements.txt                           <- File with a list of packages required for running this.

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