---
title: "Python support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/python-support.html"
content_id: "2FxVx9OjRs90hVHFwEyXMQ"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:45:10.148003+00:00"
---

# Python support

## Related properties

Detector properties

## Overview

Detect detectors for discovery of dependencies in Python:

- Setuptools detectors

  - Setuptools CLI
  - Setuptools Parse
- PIPENV detectors

  - Pipenv lock detector
  - Pipfile lock detector
- PIP detectors

  - Pip Native Inspector
  - Pip Requirements File Parse
- Poetry detector
- UV detectors

  - UV CLI
  - UV Lock

## Setuptools detectors

Setuptools detectors attempt to run on your project if a pyproject.toml file containing a build section with `requires = ["setuptools"]` or equivalent line is located. (Setuptools scans can be run in both build, if a pip installation is available, and buildless mode, if not.)

Note: Setuptools CLI detector should be run in a virtual environment, or environment with a clean global pip cache, where a pip install has only been performed for the project being scanned.

Detect parses the pyproject.toml file determining if the `[build-system]` section has been configured for Setuptools Pip via the `requries = ["setuptools"]` setting. If the setting is located and pip is installed in the environment, either in the default location or specified via the `--detect.pip.path` property, Setuptools CLI detector will execute in a virtual environment, if configured as suggested, and analyze the pyproject.toml, setup.cfg, or setup.py files for dependencies. If a configured pyproject.toml file is discovered but a pip executable is not, the Setuptools Parse detector will parse dependencies from the pyproject.toml, setup.cfg, or setup.py files but may not be able to specify exact package versions. If no dependencies are located in the pyproject.toml, setup.cfg, or setup.py files, or if the detectors fail the BDIO file output will not be generated in build or buildless mode. Detect will also attempt to run additional detectors if their execution requirements are met.

For setup.cfg and setup.py file parsing, the Setuptools detectors support direct mentioning of dependency files. For reference, see
[Dependency Management in Setuptools](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html).

Tip: URL references, optional dependencies and `file: <path to file>` parameters found in setup.cfg are not supported. For setup.py files, Detect supports only literal `install_requires=[...]` lists with string literal entries. Programmatic population of the `install_requires` parameter (for example via variable references or function calls) is not supported.

Note: The `--detect.pip.only.project.tree`, `--detect.pip.project.name`, and `--detect.pip.project.version.name` properties do not apply to the Setuptools detectors.

## PIPENV Detectors

## Pipenv lock detector

The Pipenv lock detector attempts to run on your project if either a Pipfile or Pipfile.lock file is found.

Pipenv detector requires Python and Pipenv executables.

- Detect looks for python on $PATH. You can override this by setting the python path property.
- Detect looks for pipenv on $PATH.

The Pipenv detector runs `pipenv run pip freeze` and `pipenv graph --bare --json-tree` and derives dependency information from the output. The dependency hierarchy is derived from the output of `pipenv graph --bare --json-tree`. The output of `pipenv run pip freeze` is used to improve the accuracy of dependency versions.

To troubleshoot of the Pipenv detector, start by running `pipenv graph --bare --json-tree`, and making sure that the output looks correct since this is the basis from which Detect constructs the BDIO. If the output of `pipenv graph --bare --json-tree` does not look correct, make sure the packages (dependencies) are installed into the Pipenv virtual environment (`pipenv install`).

Note: The detect.pipfile.dependency.types.excluded property does not apply to the Pipenv detector.

## Pipfile lock detector

The Pipfile lock detector attempts to run on your project if either a Pipfile.lock or Pipfile file is found AND neither of the Pip or Pipenv detectors applied.

Pipfile lock detector parses the Pipfile.lock file for dependency information. If the detector discovers a Pipfile file but not a Pipfile.lock file, it will prompt the user to generate a Pipfile.lock file by running `pipenv lock` and then run Detect again.
Pipfile.lock dependencies can be filtered using the detect.pipfile.dependency.types.excluded property.

## PIP Detectors

## Pip Native Inspector

Pip Native Inspector attempts to run on your project if any of the following are true: a setup.py file is found, a pyproject.toml file is found, a requirements.txt is found, or a requirements file is provided using the --detect.pip.requirements.path property.

Pip Native Inspector requires Python and pip executables.

- Detect looks for python on $PATH. You can override this by setting --detect.python.path
- Detect looks for pip on $PATH. You can override this by setting --detect.pip.path

Pip Native Inspector runs the [pip-inspector.py script](https://github.com/blackducksoftware/detect/blob/master/src/main/resources/pip-inspector.py), which uses Python/pip libraries to query the pip cache for the project, which may or may not be a virtual environment, for dependency information:

1. pip-inspector.py queries for the project dependencies by project name, which can be discovered using setup.py, pyproject.toml, or provided using the --detect.pip.project.name property. If your project is installed into the pip cache, this discovers dependencies specified in setup.py, or pyproject.toml file.
2. If one or more requirements files are found or provided, pip-inspector.py queries each requirements file for possible additional dependencies and details of each.

Tip: Only those packages which have been installed; using, for example, `pip install`, into the pip cache and appearing in the output of `pip list`, are included in the output of pip-inspector.py. There must be a match between the package version on which your project depends and the package version installed in the pip cache.

Note: If the packages are installed into a virtual environment for your project, you must run Detect from within that virtual environment.

### Recommendations for Pip Detector

- Be sure that Detect is locating the correct version of the Python executable; this can be done by running the logging level at DEBUG and then reading the log. This is a particular concern if your system has multiple versions of Python installed.
- Create a setup.py or pyproject.toml file for your project.
- Install your project and dependencies into the pip cache:

```
python setup.py install or pip install . (from directory where pyproject.toml is present)
pip install -r requirements.txt
```

- Pip detector attempts to derive the project name using your setup.py or pyproject.toml file if you have one. If you do not have a setup.py or pyproject.toml file, you can provide the correct project name using the property `--detect.pip.project.name`.
- If there are any dependencies specified in requirements.txt that are not specified in setup.py or pyproject.toml file, then provide the requirements.txt file using the Detect property.

  Important:
- Ensure that the paths to the Python and pip executables are correctly configured, either via system environment variables or Detect properties. For projects using `pyproject.toml` file(s), incorrect paths may lead to Detect failures.
- If you are using a virtual environment, be sure to switch to that virtual environment when you run Detect. This also applies when you are using a tool such as Poetry that sets up a Python virtual environment.
