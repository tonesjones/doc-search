---
title: "Issue Management MCP server"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/issue-management-mcp-server.html"
content_id: "Tqp0gNcIJcroDco7RSu3Ow"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:23.841310+00:00"
content_hash: "aa7ad61e0ce9edd8851ad83350c8d17c7e481b4923ecb1b1dfe6b906b7350180"
---

# Issue Management MCP server

Use the Issue Management MCP server to query your organization's data in Polaris using natural language through AI assistants like Claude Code.

## Overview

The Model Context Protocol (MCP) is an open standard that allows AI assistants to securely access data from external systems. The Issue Management MCP server implements this protocol to connect AI assistants to your organization's data in Polaris.

With this MCP server, you can use natural language to query your portfolio data through AI assistants that support the Model Context Protocol, like Claude Code or other MCP-compatible applications. The MCP server translates your questions into API calls, retrieves the data from Polaris, and returns it to your AI assistant for analysis.

Example queries you can ask include:

- "What's the most vulnerable project in my portfolio?"
- "Show me all critical SQL injection issues"
- "List my open issues"
- "How do I fix issue [issue-id]?"
- "What's the most common vulnerability type in [project-name]?"
- "Which applications have the highest risk scores?"

The Issue Management MCP server is hosted in Polaris. Because it uses Polaris APIs to retrieve data, access controls configured in Polaris still apply—users only receive information they have access to.

## Available tools

The Issue Management MCP server provides 9 tools organized into four functional categories. When you ask questions in natural language, your AI assistant automatically selects and invokes the appropriate tools to answer your query. Advanced users can also invoke these tools directly using the MCP protocol.

Table 1. Issue Management MCP server tools

| Tool category | Tool name | Description | Required parameters |
| --- | --- | --- | --- |
| Issue query tools | `list_issues` | List and search security issues with comprehensive filtering. Supports RSQL filters for severity, CWE, triage status, tool type, and more. Includes pagination and sorting capabilities. | applicationId or projectId |
| `get_issue` | Get detailed information about a specific security issue, including remediation guidance, detection date, occurrence properties, and triage status. | issueId; applicationId or projectId |
| Portfolio navigation tools | `get_portfolio_id` | Retrieve the portfolio ID associated with the authenticated user's organization. This ID is required for most other tools. | None |
| `get_portfolio_applications` | Retrieve a list of all applications (portfolio items) within a portfolio. Returns basic application metadata including ID, name, and description. Supports RSQL filtering, sorting, and pagination. | portfolioId |
| `get_portfolio_projects` | Retrieve a list of all projects (portfolio sub-items) within a portfolio or specific application. If applicationId is provided, returns projects only for that application; otherwise returns all projects. Supports RSQL filtering, sorting, and pagination. | portfolioId |
| `get_branches` | Filter and retrieve branches across the organization. Supports RSQL filtering by id, name, description, source, defaultFlag, projectId, createdAt, and updatedAt. Includes sorting and pagination. | portfolioId |
| Dashboard and metrics tools | `get_application_dashboard` | Retrieve dashboard metrics for one or more applications within a portfolio. Includes security findings breakdown by severity, total issue counts, policy violations, risk scores, scan types, and last scan timestamps. Supports RSQL filtering, sorting, and pagination. | portfolioId |
| `get_project_dashboard` | Retrieve dashboard metrics for one or more projects within a specific application. Includes security findings breakdown by severity, policy violations, project type, branch information, scan types, and last scan timestamps. Supports RSQL filtering, sorting, and pagination. | portfolioItemId |
| Configuration tools | `get_application_entitlements_info` | Retrieve entitlement information for a specific application. Shows which security analysis capabilities (SAST, SCA, DAST) are enabled for the application and how scans can be executed (PARALLEL, CONCURRENT). | portfolioId, applicationId |

## Limitations

Tools in the Issue Management MCP server perform read-only operations, and cannot create, update, or delete data in Polaris.
