---
title: "kernelCall"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/kernelcall.html"
content_id: "gvFCJzdiuOKj41P98D5g1A"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:29:28.353006+00:00"
---

# kernelCall

Matches calls to launch a CUDA kernel.

These calls have the scheme `launchNewKernel<<< Dg, Db, Ns >>>( parameters, ... )`.

Remember: To find `kernelCall` patterns, your program needs
to include `` `CUDA` `` as the language library. See The CUDA extension.

## Properties

`kernelCall` produces a record that contains the following properties:

| Name | Type | Description |
| --- | --- | --- |
| `associatedStream` | `expression` | The associated stream to launch |
| `blockDimension` | `expression` | The dimension of each block |
| `callExpression` | `functionCall` | The call itself, excluding its configuration arguments |
| `gridDimension` | `expression` | The dimension of the grid |
| `sharedMemoryBytes` | `expression` | The number of bytes per block in shared memory that is dynamically allocated for this call |

**Inherits properties from:**

- astnode
- expression
