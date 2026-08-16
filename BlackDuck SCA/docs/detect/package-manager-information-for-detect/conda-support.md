---
title: "Conda Support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/conda-support.html"
content_id: "PAcnLeWfNyvzwS4U23adlQ"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:52.036803+00:00"
---

# Conda Support

## Related properties

Detector properties

## Overview

The Conda detector discovers dependencies of python projects utilizing the Conda package and environment manager.

### Conda Tree Detector

Detect will automatically run the Conda Tree scanner whenever your project contains an `environment.yml` or `environment.yaml` file.
For the Conda Tree detector to work, both the conda and conda-tree executables must be available on your system’s PATH. If they are not, you can manually provide their locations using the `--detect.conda.path` and `--detect.conda.tree.path` options.

During the scan, the detector executes the following commands to gather dependency information:

- `conda list -n [environment_name] --json`
- `conda-tree -n [environment_name] deptree --full`

It then parses the outputs to identify all dependencies.

**Prerequisite**:
Ensure the conda-tree package is installed in the conda environment you intend to scan and [activate the environment](https://www.anaconda.com/docs/getting-started/working-with-conda/environments#activating-an-environment) before running the Detect scan.

**Optional environment selection**:

To target a specific conda environment with the detector, supply the environment name using --detect.conda.environment.name. If you do not provide this option, the detector runs without the -n flag.

### Conda CLI Detector

Detect runs the Conda CLI Detector if an environment.yml or environment.yaml file is found in your project.

The Conda CLI detector requires that the *conda* executable is on the PATH, or that its path is passed in via `--detect.conda.path`.

The Conda CLI detector runs `conda list -n [environment_name] --json` and `conda info --json`, and parses the output of both commands to discover dependencies.

Note: To specify a Conda environment to be referenced when running `conda list`, pass the name of the environment using `--detect.conda.environment.name` (if not passed, `-n` flag is omitted).
Refer to Properties for details.
