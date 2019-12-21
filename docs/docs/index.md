# GriP on Data Science

_Based on [Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science), this Data Science
project template aims to provide a more opinionated and firm framework,
especially tailored towards beginners._

## Why use this project structure?

While the [Cookiecutter Data
Science](https://github.com/drivendata/cookiecutter-data-science) template aims
at being a great starting point, it leaves you with a lot of design choices:

- What kind of `make` targets should you provide?
- How to organize training and evaluating models?

Certainly, one could argue that the answer to these questions depends on the
concrete project at hand. However, I think that beginning Data Scientists
especially (or rather beginners in any field, really) need a firm and more
refined framework to start their journey. To be honest, when I found out about the Data Science
cookiecutter, I was overwhelmed by the potential and the choices I had to make
when starting my first Data Science project based on the template.

Furthermore, there are a lot of [forks of the Cookiecutter Data Science
template](https://github.com/drivendata/cookiecutter-data-science/network/members),
a lot of which aim at providing more orientation. The main example I was
inspired by is [Cookiecutter
EasyData](https://github.com/hackalog/cookiecutter-easydata) that provides a
plethora of additional make targets, is able to manage dependencies via `conda`,
and adds a lot of boilerplate code assisting in building up a Data Science
project.

While the aforementioned template tackles a lot of the weaknesses of the
Cookiecutter Data Science template, I find that it is too sophisticated and not
well-documented enough to be easy to use. Thus, I decided to take the middle
ground between the two.

## Getting started

### Requirements

### Starting a new project

Starting a new project is as easy as running this command at the command line. No need to create a directory first, the cookiecutter will do it for you.

```nohighlight
cookiecutter https://github.com/waveFrontSet/cookiecutter-data-science
```

## Directory structure

```nohighlight
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
├── setup.py           <- Make this project pip installable with `pip install -e`
├── {{ cookiecutter.module_name }}                <- Source code for use in this project.
│   ├── __init__.py    <- Makes {{ cookiecutter.module_name }} a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── generic_processing.py
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
├── tests              <- Folder for test code with initial tests for 100% coverage
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

### Keep secrets and configuration out of version control

You _really_ don't want to leak your AWS secret key or Postgres username and password on Github. Enough said — see the [Twelve Factor App](http://12factor.net/config) principles on this point. Here's one way to do this:

#### Store your secrets and config variables in a special file

Create a `.env` file in the project root folder. Thanks to the `.gitignore`, this file should never get committed into the version control repository. Here's an example:

```nohighlight
# example .env file
DATABASE_URL=postgres://username:password@localhost:5432/dbname
AWS_ACCESS_KEY=myaccesskey
AWS_SECRET_ACCESS_KEY=mysecretkey
OTHER_VARIABLE=something
```

#### Use a package to load these variables automatically.

If you look at the stub script in `{{ cookiecutter.module_name }}/data/make_dataset.py`, it uses a package called [python-dotenv](https://github.com/theskumar/python-dotenv) to load up all the entries in this file as environment variables so they are accessible with `os.environ.get`. Here's an example snippet adapted from the `python-dotenv` documentation:

```python
# {{ cookiecutter.module_name }}/data/dotenv_example.py
import os
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

database_url = os.environ.get("DATABASE_URL")
other_variable = os.environ.get("OTHER_VARIABLE")
```

#### AWS CLI configuration
When using Amazon S3 to store data, a simple method of managing AWS access is to set your access keys to environment variables. However, managing mutiple sets of keys on a single machine (e.g. when working on multiple projects) it is best to use a [credentials file](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html), typically located in `~/.aws/credentials`. A typical file might look like:
```
[default]
aws_access_key_id=myaccesskey
aws_secret_access_key=mysecretkey

[another_project]
aws_access_key_id=myprojectaccesskey
aws_secret_access_key=myprojectsecretkey
```
You can add the profile name when initialising a project; assuming no applicable environment variables are set, the profile credentials will be used be default.
