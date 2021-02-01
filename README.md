# automatic-pypi-release
[![Latest Version][pypi-image]][pypi-url]

Automatically build and release to pypi, incrementing the version without user intervention.

This repository does the following:
* Increase minor version (If not a x.x.0 tagged)
* Build and uploadpypi package
* push the new tag to the repository

## Requirements
This project is setup to use [semver](https://semver.org/), so it will need an initial tag in the format of "x.y.0" (The last number must be 0).

Your project must have the following files:

* [Versioneer](https://pypi.org/project/fdns-versioneer/) changes:
	* setup.py
	* setup.cfg
	* versioneer.py
	* MANIFEST.in
	* automatic_pypi_release/\_\_init\_\_.py
	* automatic_pypi_release/_version.py
* Githun Actions:
	* .github/workflows/publish-to-test-pypi.yml

[pypi-image]: https://img.shields.io/pypi/v/automatic-pypi-release.svg
[pypi-url]: https://pypi.python.org/pypi/automatic-pypi-release/
