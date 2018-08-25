|RTD| |License| |Issues| |Version_RTD| |Version_Astropy|

.. _proj_structure:

=================
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