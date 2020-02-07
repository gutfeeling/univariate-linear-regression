[![Build Status](https://travis-ci.com/gutfeeling/univariate-linear-regression.svg?branch=master)](https://travis-ci.com/gutfeeling/univariate-linear-regression)
[![codecov](https://codecov.io/gh/gutfeeling/univariate-linear-regression/branch/master/graph/badge.svg)](https://codecov.io/gh/gutfeeling/univariate-linear-regression)


This repository holds the code for the DataCamp course [Unit Testing for Data Science in Python by Dibya Chakravorty](https://www.datacamp.com/courses/unit-testing-for-data-science-in-python). 

Please make sure that you have installed the package `univariate_linear_regression` in this repo using `pip` before running `pytest`. Otherwise, you may get `ImportError`s.

To install it, first clone the repo.

```
git clone https://github.com/gutfeeling/univariate-linear-regression.git
```

Then install the package locally using `pip`, making sure that you are using Python version `>=3.6`.

```
pip install -e univariate_linear_regression
```

Once the installation finishes, you can run all the tests by doing 

```
cd univariate_linear_regression
pytest --mpl
```

