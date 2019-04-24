#!/usr/bin/env python

from setuptools import setup

# setup parameters
setup(name="univariate_linear_regression",
      version="0.1.0",
      description="Univariate linear regression of housing price against housing area",
      author="Dibya",
      packages=["src"],
      author_email = "dibyachakravorty@gmail.com",
      install_requires=["jupyter==1.0.0",
                        "matplotlib==3.0.3",
                        "numpy==1.16.2",
                        "pytest==4.3.1",
                        "scipy==1.2.1",
                        ],
      )
