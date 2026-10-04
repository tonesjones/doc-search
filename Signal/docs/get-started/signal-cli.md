---
title: "Signal CLI"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-cli.html"
content_id: "OHhk5dWIw9oUxRLShfedOw"
version: "latest"
section: "Get Started with Black Duck Signal"
scraped_at: "2026-10-04T23:27:49.462775+00:00"
---

# Signal CLI

How to install, configure and run a standalone Signal scan from the command line and view results in a SARIF report.

## Contents

- Prerequisites
- Install the binary
- Configure the LLM connection
- Run a scan
- Review the results

## Prerequisites

- An API Key for the LLM that Signal will use.
- A Signal Enterprise or Developer subscription.

For more information about available Signal flags, see Signal Reference Guide.

## Install the binary

Follow the steps to scan your code with Signal CLI standalone:

1. Go to [Signal CLI Binary](https://repo.blackduck.com/signal/external/) to download and extract the file.
2. Rename the extracted executable to `signal`.
3. Move the executable to a directory on your PATH.

   Note:
   - Linux or macOS: `/usr/local/bin` or `~/.local/bin`
   - Windows: `%LOCALAPPDATA%\Programs\Signal\`

   On Windows, add the folder to PATH through System Properties > Environment Variables
4. Verify that Signal is available on your PATH by running the command:

   ```
   signal --version
   ```

## Configure the LLM connection

Signal requires an LLM endpoint URI and an API key. You can provide them using either of the following methods:

**Option A: Provide the values directly on the CLI**

```
signal --llm-uri https://llm.core.blackduck.com \
--llm-key YOUR_API_KEY \
src
```

To avoid storing the key in your shell history, you can assign it to an environment variable:

**Linux or macOS using Bash or Zsh**

```
export MY_LLM_KEY=YOUR_API_KEY

signal --llm-uri https://llm.core.blackduck.com \
  --llm-key "$MY_LLM_KEY" \
  src
```

**Windows PowerShell**

```
$env:MY_LLM_KEY = "YOUR_API_KEY"

signal --llm-uri https://llm.core.blackduck.com `
  --llm-key $env:MY_LLM_KEY `
  src
```

**Option B: Use a `.signal` configuration file**

You can set the LLM key using the configuration file, but if the same setting appears in both the configuration file and the command line, the **explicit CLI flag takes precedence**.

1. Create a minimal `.signal` file in the root of your project:

   ```
   [SCAN]
   llm_uri = https://llm.core.blackduck.com
   llm_key = ${MY_LLM_KEY}
   llm_model = claude-sonnet-4-6
   ```
2. Configuration-file values support `${VAR}` interpolation from the environment, allowing you to keep the API key out of the file.
3. Verify the LLM credentials with the following code:

   ```
   signal src \
     --check-llm True \
     --llm-uri https://llm.core.blackduck.com \
     --llm-key YOUR_API_KEY
   ```

   That way, Signal probes each configured LLM endpoint and exits before scanning.

For more details, see Signal config file.

## Run a scan

After installing and configuring Signal, follow the steps to run a scan:

1. From the root of your project, point Signal at the directory you want to scan. Replace `src` with the path to your source code:

   ```
   signal --llm-uri https://llm.core.blackduck.com \
     --llm-key YOUR_API_KEY \
     src
   ```
2. Signal analyzes the files under `src` and writes its findings to `results.sarif` in the current working directory.

   Important: Signal overwrites results.sarif on each run.
3. The default model used for the scan is `claude-sonnet-4-6`. To select a different model, add the `--llm-model` option:

   ```
   signal --llm-model MODEL_NAME src
   ```

For per-agent model overrides, including `--llm-model-agent` and `--llm-model-sca`, and for all other available flags, see the Signal Reference Guide.

## Review the results

To review the results, open `results.sarif` file in a SARIF-compatible viewer. Some examples you could use are:

- **Visual Studio Code:** Install the SARIF Viewer extension, and then open `results.sarif`.
- **Visual Studio:** Open the file with the Microsoft SARIF Viewer extension.
- **GitHub code scanning:** Upload the SARIF file through the code-scanning API or a GitHub Actions workflow.
