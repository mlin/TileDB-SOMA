# Overview

This is a POC Python implementation of the proposed [Unified Single-cell Data Model](https://github.com/single-cell-data/SOMA).

This branch, `main`, implements the [updated specfication](https://github.com/single-cell-data/SOMA/blob/main/abstract_specification.md).  Please also see the `main-old` branch which implements the [original specification](https://github.com/single-cell-data/TileDB-SOMA/blob/main-old/spec/specification.md).

# Installation

## Using pip

This code is hosted at [PyPI](https://pypi.org/project/tiledbsoma/), so you can do

```
python -m pip install tiledbsoma
```

To install a specific version:

```
python -m pip install git+https://github.com/single-cell-data/TileDB-SOMA.git@0.0.6#subdirectory=apis/python
```

To update to the latest version:

```
python -m pip install --upgrade tiledbsoma
```

## From source

* This requires [`tiledb`](https://github.com/TileDB-Inc/TileDB-Py) (see [./setup.cfg](setup.cfg) for version), in addition to other dependencies in [setup.cfg](./setup.cfg).
* Clone [this repo](https://github.com/single-cell-data/TileDB-SOMA)
* `cd` into your checkout and then `cd apis/python`
* `python -m pip install .`
* Or, if you wish to modify the code and run it, `python setup.py develop`
* Optionally, if you prefer, you can run that inside `venv`:
```
python -m venv venv
. ./venv/bin/activate
python -m pip install .
```
* In either case:

```
python -m pytest tests
```

# Status

Please see [https://github.com/single-cell-data/TileDB-SOMA/issues](https://github.com/single-cell-data/TileDB-SOMA/issues).
