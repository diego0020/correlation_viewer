__author__ = 'Diego'

from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    windows = ["vcorr/view_correlations.py"],
    name = "Correlations_Viewer",
    version = "0.0.1a",
    author = "Diego A",
    author_email = "da.angulo39@uniandes.edu.co",
    description = "A simple application for exploring correlations in a data set",
    license = "MIT",
    keywords = "correlations regression",
    url = "imagine.uniandes.edu.co",
    packages=["vcorr"],
    long_description=read('README.md'),
    install_requires=['numpy','scipy','matplotlib','PyQt4','pandas','seaborn'],
)