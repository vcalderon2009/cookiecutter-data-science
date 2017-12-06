{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

**Author**: Victor Calderon ([victor.calderon@vanderbilt.edu](mailto:victor.calderon@vanderbilt.edu))

## Installing Environment & Dependencies

To use the scripts in this repository, you must have _Anaconda_ installed on the systems that will be running the scripts. This will simplify the process of installing all the dependencies.

For reference, see: [https://conda.io/docs/user-guide/tasks/manage-environments.html](https://conda.io/docs/user-guide/tasks/manage-environments.html)

The package counts with a __Makefile__ with useful functions. You must use this Makefile to ensure that you have all the necessary _dependencies_, as well as the correct _conda environment_. 

* Show all available functions in the _Makefile_

```
$:  make show-help
    
    Available rules:
    
    clean               Delete all compiled Python files
    create_environment  Set up python interpreter environment
    data                Make Dataset
    environment         Set up python interpreter environment - Using environment.yml
    lint                Lint using flake8
    remove_environment  Delete python interpreter environment
    requirements        Install Python Dependencies
    sync_data_from_s3   Download Data from S3
    sync_data_to_s3     Upload Data to S3
    test_environment    Test python environment is setup correctly
    update_environment  Update python interpreter environment
```

* __Create__ the environment from the `environment.yml` file:

```
    make environment
```

* __Activate__ the new environment __{{cookiecutter.conda_python_env}}__.

```
    source activate {{cookiecutter.conda_python_env}}
```

* To __update__ the `environment.yml` file (when the required packages have changed):

```
  make update_environment
```

* __Deactivate__ the new environment:

```
    source deactivate
```

### Auto-activate environment
To make it easier to activate the necessary environment, one can check out [*conda-auto-env*](https://github.com/chdoig/conda-auto-env), which activates the necessary environment automatically.

Usage
------


Project Organization
------------

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
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
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


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
