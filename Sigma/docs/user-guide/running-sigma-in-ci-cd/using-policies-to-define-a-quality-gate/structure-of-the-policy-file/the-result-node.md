---
title: "The result Node"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/the-result-node.html"
content_id: "kqrpTg0Bfcr0VrVT7X2tIg"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:28.560063+00:00"
---

# The result Node

The `result` node defines the exit code and message for the Sigma CLI when
policies are violated.

The `result` node and its fields are optional. If you omit this node,
Sigma will return an exit code of 1 and will display no message to the user.

The `result` node has the following structure:

```
result:
	exit-code: 1
                  message: <RESULT_MESSAGE>
```

- The exit code is a POSIX exit/return code. You can define your own exit codes for
  this field.

  - If there is a policy violation and you omit the
    `exit-code` field, Sigma will use the default exit
    code of 1.
  - If there are no policy violations, the exit code is 0.
- The `message` specified is displayed to the user in command line
  output or in the integrations.

  If you omit the `message` field, Sigma results will not include
  the policy violation message in the result.
