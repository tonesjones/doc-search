---
title: "Erlang/Hex/Rebar support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/erlang/hex/rebar-support.html"
content_id: "iXx2grr8bN_Q7eHJWnfoOw"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:45:05.015431+00:00"
---

# Erlang/Hex/Rebar support

## Related properties

Detector properties

## Overview

The Rebar detector discovers dependencies of Erlang projects that use the Hex package manager.

The Rebar detector runs if Detect finds a *rebar.config* file in your project.
A *rebar3* executable must be found on the PATH, or must be provided.

The Rebar detector runs the *rebar3 tree* command and parses the output for dependency information.
