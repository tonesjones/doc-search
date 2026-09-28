---
title: "Local notes: command-line flags and workflows (community reference)"
source_url: "local:///C:/TestCode/bdsca-c-cpp-demo/bd-ccpp-scanner.md"
content_id: "local-bd-ccpp-scanner"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-19T00:00:00.000000+00:00"
local_addition: true
note: >
  This topic is NOT scraped from docs.blackduck.com. It was hand-added from a
  locally authored reference file (C:\TestCode\bdsca-c-cpp-demo\bd-ccpp-scanner.md)
  that a field/SE team maintains as a condensed cheat-sheet for the blackduck-c-cpp
  CLI. Treat it as a secondary/community reference, not official documentation.
  Cross-check flag names against the official topics in this same section
  (installation.md, executing-the-black-duck-c-cpp-tool.md, api-token.md,
  frequently-asked-questions.md) before relying on any flag not also confirmed
  there.
---

# Local notes: command-line flags and workflows (community reference)

> Source: locally authored file, not scraped from docs.blackduck.com. See
> frontmatter `note` field.

## Overview

The Black Duck C/CPP Tool generates a Bill of Materials (BOM) for C and C++ projects by building the project, capturing source and binary files, and delivering BDIO output and signatures to Black Duck SCA. It addresses the unique challenge of C/CPP dependency management by using Coverity Build Capture to instrument the build process.

## Problem Statement

C and C++ projects lack a standard package manager or dependency management system, making it difficult to create accurate BOMs. The Black Duck C/CPP tool solves this by:
- Wrapping the build process with Coverity Build Capture
- Capturing all compiler and linker invocations
- Recording compiled source files, header files, and linked object files
- Matching files using multiple analysis methods
- Generating comprehensive BOM and sending to Black Duck SCA

## How the Tool Works

### Scan Pipeline

1. **Coverity Build Capture**: Wraps build, observing all compiler/linker invocations
2. **Package Manager Scan**: Runs on compiled code to identify dependencies
3. **BDBA Scan** (if licensed): Analyzes unmatched files
4. **Signature Scan**: Scans remaining unmatched files
5. **Snippet Scan** (if enabled): Identifies code snippets

### Build Modes

**cov-cli (Default - Version 2.0.0+):**
- Layer of automation on top of cov-build
- Automatically guesses correct cov-configure options
- Easier to use but may require manual fixes

**cov-build (Optional):**
- Direct Coverity build capture
- More control but requires manual cov-configure setup

To use cov-build instead of cov-cli:

```yaml
set_coverity_mode: 'cov-build'
```

## Platform Support

### Supported Platforms

- Debian
- Redhat
- Ubuntu
- openSUSE
- Fedora
- CentOS
- macOS (Intel and Apple Silicon)
- Windows

**Important Notes:**
- macOS ARM platform NOT currently supported
- Windows: No package manager scan; no BDIO file generation
- Linux: Full package manager scan support
- Signature and binary scans available on all supported platforms

### System Requirements

**Minimum Black Duck SCA Version:** 2020.10.0

**Coverity Requirements:**

Starting with Coverity build capture 2022.12.0, glibc_2.18 is required.

**For CentOS 7 (glibc_2.17 or older):**
- Tool attempts to download Coverity 2022.9
- If download fails, manually specify:

```yaml
force_pull_coverity_vers: 'old'
```

**GCP Access (for Coverity download):**
- Must open connection toward `*.googleapis.com:443`
- Auto-download requires authorized Black Duck customer access
- Older Black Duck versions (<2021.10) require manual Coverity download

## Installation

### Prerequisites

- Black Duck SCA 2020.10.0 or later installed
- Black Duck SCA API authentication token
- Registered Black Duck SCA account
- Python 3.6 or later (for running the tool)

### Install from PyPI

```bash
pip install blackduck-c-cpp
```

### Install Specific Version

```bash
pip install blackduck-c-cpp==3.0.4
```

## Quick Start

### Basic Command

```bash
blackduck-c-cpp -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd bd_url -a api_token
```

### Parameters

| Parameter | Short | Required | Description |
|-----------|-------|----------|-------------|
| `--build_dir` | `-d` | Yes | Directory from which to run build |
| `--project_name` | `-proj` | Yes | Black Duck project name |
| `--project_version` | `-vers` | Yes | Project version |
| `--blackduck_url` | `-bd` | Yes | Black Duck SCA server URL |
| `--api_token` | `-a` | Yes | Black Duck API token |
| `--config` | `-c` | No | YAML configuration file path |
| `--build_cmd` | `-bc` | No | Command to execute the build |
| `--coverity_root` | `-Cov` | No | Base directory for Coverity |
| `--cov_output_dir` | `-Cd` | No | Target directory for Coverity output |
| `--output_dir` | `-od` | No | Target directory for tool output |
| `--codelocation_name` | `-Cl` | No | Custom code location name in Black Duck |
| `--skip_build` | `-s` | No | Skip build; use previously captured data |
| `--insecure` | `-i` | No | Disable SSL certificate verification |
| `--force` | `-f` | No | Force re-download of dependencies |
| `--verbose` | `-v` | No | Enable verbose logging |
| `--debug` | `-dg` | No | Enable debug mode |

### Full Command Example

```bash
blackduck-c-cpp \
  -d /path/to/project \
  -proj MyApp \
  -vers 1.0.0 \
  -bd https://bd.company.com \
  -a YOUR_API_TOKEN \
  -bc "make clean && make" \
  -od /path/to/output \
  -v
```

## Configuration with YAML File

### YAML Configuration File

Create configuration file (e.g., `config.yaml`):

```yaml
# Required settings
build_dir: /path/to/project
project_name: MyApp
project_version: 1.0.0
blackduck_url: https://bd.company.com
api_token: YOUR_API_TOKEN

# Optional settings
build_cmd: make clean && make
codelocation_name: MyApp-main
cov_output_dir: /tmp/coverity_output
output_dir: /tmp/blackduck_output

# Coverity settings
set_coverity_mode: 'cov-cli'  # or 'cov-build'
force_pull_coverity_vers: 'old'  # for glibc_2.17 or older

# Build capture options
cov_configure_args: "--compiler gcc"
additional_coverity_params: "--emit-link-units"

# Signature scan options
additional_sig_scan_args: "--max-depth 3"

# Logging
verbose: true
debug: false
```

### Run with Configuration File

```bash
blackduck-c-cpp --config /path/to/config.yaml
```

Or with short flag:

```bash
blackduck-c-cpp -c /path/to/config.yaml
```

## Bazel Support

### Bazel Setup

The tool supports Bazel-based C/C++ projects.

### YAML Configuration for Bazel

```yaml
build_dir: /path/to/bazel/project
project_name: MyBazelProject
project_version: 1.0.0
blackduck_url: https://bd.company.com
api_token: YOUR_API_TOKEN

# Bazel-specific
build_cmd: bazel build //...
additional_coverity_params: "--bazel"
```

### Bazel Command Example

```bash
blackduck-c-cpp \
  -d /path/to/bazel/project \
  -proj MyBazelProject \
  -vers 1.0.0 \
  -bd https://bd.company.com \
  -a YOUR_API_TOKEN \
  -bc "bazel build //..."
```

## Output and Results

### BDIO File (Bill of Distribution)

- Generated on Linux platforms with package manager support
- Not generated on Windows (no OS package manager)
- Contains dependency information and signatures
- Automatically uploaded to Black Duck SCA

### Signature Output

- Generated on all supported platforms
- Contains file signatures for unmatched files
- Sent to Black Duck for matching against known components

### BOM Contents

The generated BOM includes:

1. **Direct Dependencies**: Explicitly declared dependencies
2. **Transitive Dependencies**: Dependencies of dependencies
3. **System Libraries**: OS-level dependencies (Linux only)
4. **File Signatures**: Matched against Black Duck signature database
5. **Unmatched Components**: Files without recognized signatures

### Output Directories

**Default Locations:**

- Coverity output: `~/.blackduck/blackduck-ccpp/output/PROJECT_NAME`
- Tool output: `~/.blackduck/blackduck-ccpp/output/PROJECT_NAME`

**Custom Directories:**

```bash
blackduck-c-cpp \
  -d BUILD_DIR \
  -Cd /custom/coverity/output \
  -od /custom/tool/output \
  # ... other parameters
```

## API Token Configuration

### Generate Black Duck API Token

1. Log in to Black Duck SCA UI
2. Navigate to user menu → **Access Tokens**
3. Click **+ Create Token**
4. Provide:
   - Name (e.g., "C++ Scanner Token")
   - Description (optional)
   - Scope: **Read and Write Access**
5. Click Create and copy token

### Token Usage

**Command Line:**
```bash
blackduck-c-cpp -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd BD_URL -a YOUR_TOKEN
```

**Environment Variable (Recommended):**
```bash
export BD_HUB_TOKEN="YOUR_TOKEN"

blackduck-c-cpp -d BUILD_DIR -proj PROJECT_NAME -vers PROJECT_VERSION -bd BD_URL
```

**Configuration File:**
```yaml
api_token: YOUR_TOKEN
```

### Required Roles

The API token user must have appropriate roles in Black Duck:

- **For new projects**:
  - Global Code Scanner
  - Global Project Viewer
  - Project Creator

- **For existing projects**:
  - Project Code Scanner role

## Command-Line Flags Reference

### Required Flags

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--build_dir` | `-d` | Path | Directory from which to run build |
| `--project_name` | `-proj` | String | Black Duck project name |
| `--project_version` | `-vers` | String | Black Duck project version |
| `--bd_url` | `-bd` | URL | Black Duck SCA server URL |

### Authentication

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--api_token` | `-a` | String | Black Duck API token. Can also use `BD_HUB_TOKEN` environment variable (recommended) |
| `--insecure` | `-i` | Boolean | Disable SSL verification for self-signed certificates |

### Build Configuration

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--build_cmd` | `-bc` | String | Command to execute the build (required when `skip_build=False`) |
| `--skip_build` | `-s` | Boolean | Skip build and use previously generated build data. Requires initial build used `--emit-link-units` flag |
| `--config` | `-c` | Path | YAML configuration file path |
| `--set_coverity_mode` | `-scv` | String | Specify coverity mode: `'cov-build'` or `'cov-cli'` (default). cov-cli runs by default for Coverity >= 2023.9 |
| `--force_pull_coverity_vers` | `-fpc` | String | For Linux: force pull `'old'` (2022.9) or `'latest'` version of Coverity if not auto-downloaded correctly |

### Output Directories

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--output_dir` | `-od` | Path | Target directory for blackduck-c-cpp output files. Defaults to `~/.blackduck/blackduck-c-cpp/output/PROJECT_NAME`. Should be outside build directory |
| `--cov_output_dir` | `-Cd` | Path | Target directory for Coverity output files. Defaults to `~/.blackduck/blackduck-c-cpp/output/PROJECT_NAME` |
| `--coverity_root` | `-Cov` | Path | Base directory for Coverity. If not specified, downloads latest mini Coverity package from GCP for authorized Black Duck customers (2021.10+). For older versions, contact sales |

### Code Location & Metadata

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--codelocation_name` | `-Cl` | String | Custom code location name in Black Duck. Overwrites previous scans with same name (use with care) |
| `--project_group_name` | `-pgn` | String | Project Group to assign project to. Must match existing project group on Black Duck |
| `--project_description` | `-pgd` | String | Project description. Creates project with this description if specified |
| `--port` | `-po` | Integer | Set custom Black Duck port |

### Scan Modes & Methods

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--modes` | `-md` | String | Comma-separated list of modes: `'all'` (default), `'bdba'`, `'sig'`, `'pkg_mgr'` |
| `--verbose` | `-v` | Boolean | Enable verbose mode |
| `--debug` | `-dg` | Boolean | Enable debug mode. Sends all found files to all matching types (default: only undetected files to BDBA and Signature matching) |

### Dependency & File Filtering

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--skip_transitives` | `-st` | Boolean | Skip all transitive dependencies |
| `--skip_includes` | `-sh` | Boolean | Skip all `.h` & `.hpp` files from all scan types |
| `--skip_dynamic` | `-sd` | Boolean | Skip all dynamic (`.so`/`.dll`) files from all scan types |

### Signature Scan Options

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--additional_sig_scan_args` | `-as` | String | Additional arguments to pass to signature scanner. Individual File Matching is on by default. Multiple params: `'--snippet-matching --license-search'`. Accepts scan CLI properties only |
| `--expand_sig_files` | `-es` | Boolean | Create exploded directory instead of zip in signature scanner mode |

### BDIO/JSON Splitting (for Large Scans)

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--disable_bdio_json_splitter` | `-djs` | Boolean | Disable JSON splitter; upload as single scan. For JSON/BDIO splitter, dryrun required (run offline mode first) |
| `--json_splitter_limit` | `-jsl` | Integer | Set limit for scan size in bytes. Requires dryrun (offline mode first) |
| `--bdio_split_max_file_entries` | `-bsfl` | Integer | Set max scan node entries per generated BDIO file |
| `--bdio_split_max_chunk_nodes` | `-bscn` | Integer | Set max scan node entries per single bdio-entry file |

### Offline Mode

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--offline` | `-off` | Boolean | Store BDBA and sig zip files, sig scan JSON, and raw_bdio.csv to disk. For scans over 5GB using BDIO/JSON splitter, run offline mode first. `scan_cli_dir` required when offline |
| `--use_offline_files` | `-uo` | Boolean | Use offline-generated files for upload in online mode |
| `--scan_cli_dir` | `-sc` | Path | Scan CLI directory (e.g., `/home/../../Black_Duck_Scan_Installation/` instead of version-specific path) |

#### Critical Notes for Offline Mode

**`--scan_cli_dir` is REQUIRED when using `--offline`**

The tool cannot generate signature scan output files (`sig_scan/sig_files/`) without access to the Black Duck Scan CLI. If you omit `-sc` or set it incorrectly, the signature scan phase will fail during upload.

**Correct `-sc` Path vs. Output Directory**

- WRONG: Point `-sc` to your **output directory** (e.g., `/home/user/.blackduck/blackduck-c-cpp/output/MyProject/`)
- CORRECT: Point `-sc` to your **Black Duck Scan CLI installation** (e.g., `/home/user/blackduck/tools/Black_Duck_Scan_Installation/`)

The `-sc` path should contain or lead to a `scan.cli-x.x.x` subdirectory. The tool will use the latest version automatically.

**Offline Mode Output Files**

When running with `--offline`, the tool generates:
1. `bdba_ready.zip` — Binary analysis data (required for upload phase)
2. `sig_scan/sig_files/` — Pre-scanned signature data (required for upload phase if signature scanning enabled)
3. `raw_bdio.csv` — Package manager BOM (required for upload phase)
4. `offline_config.yaml` — Configuration snapshot (preserves skip_* parameters for upload phase)
5. `idir/` — Coverity intermediate representation (required for Cov Manage Emit phase)
6. `cov_emit_output_files/` — Coverity emit output for cross-machine analysis (required for Cov Manage Emit phase)

**Cross-Machine Workflows**

All of the above files must be transferred to the upload machine. The tool looks for them in:
```
~/.blackduck/blackduck-c-cpp/output/{PROJECT_NAME}/
```

On Windows, this expands to:
```
C:\Users\{YourUsername}\.blackduck\blackduck-c-cpp\output\{PROJECT_NAME}\
```

### Upload & Timing

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--scan_interval` | `-si` | Integer | Set seconds to wait between scan uploads (for multiple scans) |
| `--force` | `-f` | Boolean | Force use of older Coverity version if available (in case of GCP failure) |

### Coverity Configuration

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--cov_configure_args` | `-Cc` | JSON | Additional cov-configure commands for different compilers. Format: `'{"compiler":"compiler-type"}'`. Supports wildcards: `'{"*g++":"gcc"}'` for template configs |
| `--additional_coverity_params` | `-ac` | String | Additional arguments for Coverity build command (e.g., `"--record-with-source"`) |
| `--bazel` | `-ba` | Boolean | Use if this is a Bazel build. Follow Coverity setup instructions for Bazel |

### Utility

| Flag | Short | Type | Description |
|------|-------|------|-------------|
| `--help` | `-h` | N/A | Show help message and exit |

## Common Workflows

### Workflow 1: Simple C++ Build

```bash
cd /path/to/cpp/project

blackduck-c-cpp \
  -d . \
  -bc "make clean && make" \
  -proj MyApp \
  -vers 1.0.0 \
  -bd https://bd.company.com \
  -a YOUR_TOKEN
```

### Workflow 2: CMake Project

```bash
cd /path/to/cmake/project

blackduck-c-cpp \
  -d . \
  -bc "cmake . && make" \
  -proj CMakeApp \
  -vers 2.0.0 \
  -bd https://bd.company.com \
  -a YOUR_TOKEN
```

### Workflow 3: Bazel Project with Custom Coverity

```bash
blackduck-c-cpp \
  -d /path/to/bazel/project \
  -bc "bazel build //..." \
  -Cov /opt/coverity-2023.12 \
  -proj BazelApp \
  -vers 3.0.0 \
  -bd https://bd.company.com \
  -a YOUR_TOKEN \
  -od /tmp/bazel_scan_output
```

### Workflow 4: Re-run with Cached Build Data

Skip the build step and use previously captured data:

```bash
blackduck-c-cpp \
  -d /path/to/project \
  -s \
  -proj MyApp \
  -vers 1.0.1 \
  -bd https://bd.company.com \
  -a YOUR_TOKEN
```

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Build capture fails | Check build command syntax; verify compiler/linker available; check permissions |
| "glibc_2.18 requirement" error on CentOS 7 | Set `force_pull_coverity_vers: 'old'` in YAML config |
| Coverity download fails | Verify network connectivity to googleapis.com:443; check firewall rules; verify Black Duck customer status |
| Empty BOM | Ensure build succeeds and produces output; check Coverity logs; verify project contains C/C++ code |
| Black Duck connection refused | Verify Black Duck URL is correct (https://); check network connectivity; verify firewall rules |
| Invalid API token | Regenerate token from Black Duck UI; ensure no extra spaces; verify token has required roles |
| Scan takes too long | Use `--skip_build` flag on subsequent runs; optimize build command; consider using smaller project scope |
| "Out of memory" error | Increase available memory; reduce project scope; use custom output directories on large disk |

### Debug Logging

Enable debug output to troubleshoot issues:

```bash
blackduck-c-cpp \
  --verbose \
  --debug \
  -d BUILD_DIR \
  # ... other parameters
```

Review logs in tool output directory for detailed error messages.

## Best Practices

- **Build first**: Ensure project builds successfully before scanning
- **Keep token secure**: Use environment variables or YAML files; never hardcode tokens
- **Use meaningful versions**: Apply semantic versioning (e.g., 1.0.0, 2.1.3)
- **Save configuration**: Store YAML configs in version control for reproducibility
- **Test build command**: Verify build command works manually first
- **Monitor BDIO output**: Review generated BOM in Black Duck SCA
- **Use code location names**: Distinguish multiple scans of same version
- **Plan for time**: First scans take longer; subsequent scans faster with caching
- **Verify API token roles**: Ensure token has required permissions for project type
- **Archive outputs**: Save BDIO and signature outputs for compliance/audit

## Release Notes

### Version 2.0.0

**Major Changes:**
- Switched default from cov-build to cov-cli
- cov-cli provides better automation and ease of use
- Option available to revert to cov-build if needed

**Breaking Changes:**
- Default build behavior changed to use cov-cli
- Projects requiring cov-build must explicitly set `set_coverity_mode: 'cov-build'`

**New Features:**
- Improved Bazel support
- Better error handling and logging
- Enhanced configuration options

## Frequently Asked Questions

**Q: How does the tool work without a package manager?**
A: It uses Coverity Build Capture to instrument the build process, capturing all compiled files and libraries. These are then matched against Black Duck's component database using multiple methods.

**Q: Will this work for mixed language projects (C++ with some Java)?**
A: Yes. The tool runs package manager scans for detected languages (Java, Python, etc.) in addition to the C/CPP analysis.

**Q: Can I scan projects without building?**
A: No. The tool requires a build to capture source and binary information. This ensures accurate dependency detection.

**Q: How do I update the tool?**
A: Use `pip install --upgrade blackduck-c-cpp` to get the latest version.

**Q: Is there a GUI for this tool?**
A: No. The tool is command-line only, designed for CI/CD integration.
