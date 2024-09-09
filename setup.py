import sys
import os.path
from setuptools import setup, find_packages

PKG_NAME = 'filesender'

# Extract version number from module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), PKG_NAME))
from version_ import __version__  # @IgnorePep8 @UnresolvedImport
sys.path.pop(0)

setup(
    name=PKG_NAME,
    version=__version__,
    author='Mike Thang',
    author_email='m.thang@qfab.org',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['filesender = filesender.filesender:cmd']},
    url='https://github.com/mthang/filesender',
    license='BSD 3-Clause License',
    description=(
        'Send data to remote site'),
    long_description=open('README.rst').read(),
    install_requires=['requests',
                      'urllib3',
                      'cryptographye'],
    python_requires='>=3.6',
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD 3-Clause License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Bio-Informatics"])
