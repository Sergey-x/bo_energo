[![Coverage Status](https://coveralls.io/repos/github/Sergey-x/bo_energo/badge.svg?branch=master)](https://coveralls.io/github/Sergey-x/bo_energo?branch=master)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Тестовые задания
=======================

### Install:

* Prerequisites:
    * Docker (docker-compose)

* Clone repo:
    ```bash
    $ git clone git@github.com:Sergey-x/bo_energo.git
    ```

* [Optional] Setup dev environment:
    ```bash
    $ poetry shell && poetry install
    ```

### How to run:

* inside docker:
    ```bash
    $ docker-compose up
    ```

### Run tests (in dev environment):

```bash
$ make test
```

or

```bash
$ pytest .
```

With coverage:

```bash
$ make test-cov
```
