---
title: "Erlang/Hex/Rebar support"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/erlang/hex/rebar-support.html"
content_id: "iXx2grr8bN_Q7eHJWnfoOw"
version: "12.0.0"
section: "Package Manager information for Detect"
scraped_at: "2026-10-04T23:33:20.993192+00:00"
content_hash: "014c1ebf23ac9aa4032b378ef8f99d1d14e078b3bdd46a8ab332619f678fefc5"
---

# Erlang/Hex/Rebar support

## Related properties

Detector properties

## Overview

The Rebar detector discovers dependencies of Erlang projects that use the Hex package manager.

The Rebar detector runs if Detect finds a *rebar.config* file in your project.
A *rebar3* executable must be found on the PATH, or must be provided.

The Rebar detector runs the *rebar3 tree* command and parses the output for dependency information.
