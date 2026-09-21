---
title: "Configuring tools using Bridge"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/configuring-tools-using-bridge.html"
content_id: "SaoNuDEGAhwd0_Q~slkzTA"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:52.386899+00:00"
---

# Configuring tools using Bridge

## Overview

Bridge allows users to pass configuration and arguments to the underlying tools, thus providing an easy way for users to use these tools. Bridge has dedicated resources for some of the common configurations, and also provides a generic argument for both Coverity and Black Duck® SCA configrations. This may eliminate the need for configuration files (eg coverity.yml) to be present in the project root. Examples are:

## Coverity Configurations

- Passing build and clean commands to Coverity
- Passing the path to coverity.yml file
- Passing generic arguments to Coverity

## Black Duck® SCA Detect

- Passing search depth to Black Duck SCA Detect
- Passing the configuration file path to Black Duck SCA Detect
- Passing generic arguments to Black Duck SCA Detect

## Passing build and clean commands to Coverity

JSON Example:

```
{
    "data": {
        "coverity": {
            "build": {
              "command":"mvn clean install"
            },
            "clean": {
                "command": "mvn clean"
            }
        }
    }
}
```

Command line example:

```
bridge-cli --stage polaris coverity.build.command="mvn clean install" coverity.clean.command="mvn clean"
```

Environment variable example:

```
export BRIDGE_COVERITY_CLEAN_COMMAND="mvn clean"
export BRIDGE_COVERITY_BUILD_COMMAND="mvn clean install"
bridge-cli --stage polaris
```

## Passing the path to coverity.yml file

JSON Example:

```
{
    "data": {
        "coverity": {
            "config": {
                "path": "</path/to/config.file>"
            }
        }
    }
}
```

Command line example:

```
coverity.config.path="</path/to/config.file>"
```

Environment variable example:

```
export BRIDGE_COVERITY_CONFIG_PATH="</path/to/config.file>"
```

## Passing generic arguments to Coverity

JSON Example:

```
"data": {
        "coverity": {
            "args": "--compiler-config-file <file-name> ..."
        }
    }
}
```

Command line example:

```
coverity.args="--compiler-config-file <value> ..."
```

Environment variable example:

```
export BRIDGE_COVERITY_ARGS="--compiler-config-file <value> ..."
```

## Passing search depth to Black Duck® SCA Detect

JSON Example:

```
{
    "data": {
        "detect": {
            "search": {
                "depth": 2
            }
        }
    }
}
```

Command line example:

```
detect.search.depth=2
```

Environment variable example:

```
export BRIDGE_BLACKDUCK_SEARCH_DEPTH="2"
```

## Passing the configuration file path to Black Duck® SCA Detect

JSON Example:

```
{
    "data": {
        "detect": {
            "config": {
                "path": "</path/to/config.file>"
            }
        }
    }
}
```

Command line example:

```
detect.config.path="</path/to/config.file>"
```

Environment variable example:

```
export BRIDGE_BLACKDUCK_CONFIG_PATH="</path/to/config.file>"
```

## Passing generic arguments to Black Duck® SCA Detect

JSON example:

```
"data": {
        "detect": {
            "args": "--detect.cleanup=false ..."
        }
    }
}
```

Command line example:

```
detect.args="--detect.cleanup=false ..."
```

Environment variable example:

```
export BRIDGE_BLACKDUCK_ARGS="--detect.cleanup=false ..."
```
