---
title: "Overview of Black Duck Signal"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/overview-of-black-duck-signal.html"
content_id: "dB8K2SDHD53lShGOyuhOKg"
version: "latest"
section: "Overview of Black Duck Signal"
scraped_at: "2026-08-13T00:04:49.053553+00:00"
---

# Overview of Black Duck Signal

## About Signal

**Signal** introduces a new approach to application security, designed for agentic software development. We coupled Large Language Models with the Black Duck KnowledgeBase™, a repository containing more than 20 years of expert-vetted security insights, and together they deeply analyze software in ways not possible before.

Signal integrates directly with AI coding assistants and focuses on high-fidelity, high-priority issues most likely to be exploited. It works at machine speed and secures apps with minimal human effort.

## What it can do

- **Find and fix issues** in code, whether the code was written by humans or agentic AI. Signal can work with coding assistants like Gemini, Copilot, and Claude.
- **Let you decide** whether to scan your code changes or the entire codebase.
- **Scan any programmatic language**. Because it is LLM-based, it can discover bugs in any language and doesn’t need any configuration to get started. It’s ideal for scannning languages that your other tools don’t support.
- **Find bugs that would go undetected** by rule-based engines.
- **Suggest fixes**. Signals output includes guidance that AI agents can use to fix the code.

## The use cases

You can use Signal in two ways:

- Scan only your code changes, the way you would in a pull request
- Scan all the code in your project.

Signal comes in two varieties: Developer and Enterprise. You should choose the variety that matches your workflow.

Table 1. Developer versus Enterprise

| Scenario | Signal Developer | Signal Enterprise |
| --- | --- | --- |
| Scan code owned by one contributor with the help of Agentic AI. Report only the issues owned by that contributor. | Yes | Yes |
| Scan code in an entire project. Easily add AI scans to existing automated workflows. | No | Yes |

**How does it work**

The Black Duck MCP server is an NPM package that can be installed with a single command, if you have already installed Node and NPM. It automatically downloads Black Duck Signal.

Once installed, it uses a combination of LLMs hosted in Azure, AWS, and GC. Black Duck MCP server can be used by your agentic coding assistant to connect with Black Duck’s infrastructure, including a purpose-built LLM and the Black Duck KnowledgeBase.

Additionally, Signal Enterprise can connect with Polaris, our SaaS platform for viewing and managing issues, and it can be used by the Bridge CLI to include AI scanning in existing automated workflows.

For existing Polaris customers, Signal can be an add-on. If you bought only Signal Enterprise, access to Polaris is included, and you can choose to manage issues in Polaris or generate a SARIF report when you run a Signal scan.

Signal Developer path to adoption

1. Register the MCP with the coding assistant you normally use (See our documentation for popular coding assistants.)
2. Ask your agentic coding assistant to perform a scan with Black Duck

Enterprise path to adoption:

1. If you want to see results in Polaris, add an external analysis subscription to your project in Polaris. (To see results locally, forego Polaris and rely on SARIF files saved in your project directory.)
2. Install Bridge, if you haven't already.
3. Include settings in your Bridge configuration file for the scan type "AI."

## Signal operating system support

Signal runs on these operating systems.

- linux-arm64
- linux-x86_64
- macos-arm64
- macos-x86_64
- windows_x86

## Language support

Black Duck Signal scans code effectively in any language.

Traditional SAST tools define what they can analyze by maintaining rules for each language and framework they support. Signal works differently. It analyzes code based on semantics — meaning, structure, and context — reasoning about it the way a security engineer would, regardless of the language or frameworks used. This means Signal isn’t bound by a fixed list of supported languages; it understands your code on its own terms.

## Black Duck MCP Environment Variables

The Black Duck Signal MCP server supports the following environment variables:

| Variable | Default | Description |
| --- | --- | --- |
| `BLACKDUCK_MCP_GATEWAY_KEY` | None (required) | API key for enhanced AI analysis |
| `BLACKDUCK_HOME` | User's home directory | Override the default `.blackduck` folder location |
| `BLACKDUCK_MCP_TOOL_TIMEOUT` | `1800000` (30 min) | Scan timeout in milliseconds |
| `BLACKDUCK_MCP_LOG_LEVEL` | `info` | Log level: `error`, `warn`, `info`, or `debug` |

## Black Duck MCP configuration

You can set these variables in your MCP client configuration:

```
 {
  "servers": {
    "black-duck": {
      "type": "stdio",
      "command": "npx",
      "args": ["@black-duck/mcp-server@latest"],
      "env" : {
        "BLACKDUCK_MCP_GATEWAY_KEY": "YOUR_LLM_API_KEY"
        "BLACKDUCK_MCP_LOG_LEVEL": "info" 
    }
    }
  }
}
```

## Logging and Troubleshooting

Log Location

All MCP logs are written to /Users/<username>/.blackduck/mcp/logs/ for linux/mac and C:\Users\<Username>\AppData\Roaming\BlackDuck\mcp\logs\ (customizable via `BLACKDUCK_HOME`):

- `black-duck-mcp.log` - Combined log (all levels)
- `black-duck-mcp-error.log` - Error-only log

## **IP Allowlist**

The following URLs and IP addresses must be accessible for the MCP server to function properly:

| URL | IP Address |
| --- | --- |
| `repo.blackduck.com` | `34.149.5.115` |
| `llm.core.blackduck.com` | `104.18.36.253` |

Note:

Ensure your firewall allows outbound HTTPS (port 443) connections to these endpoints
