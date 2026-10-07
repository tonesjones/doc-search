---
title: "Overview of Black Duck Signal"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/overview-of-black-duck-signal.html"
content_id: "dB8K2SDHD53lShGOyuhOKg"
version: "latest"
section: "Overview of Black Duck Signal"
scraped_at: "2026-10-04T23:27:50.018552+00:00"
---

# Overview of Black Duck Signal

**Signal** introduces a new approach to application security, designed for agentic software development. We coupled Large Language Models with the Black Duck KnowledgeBase™, a repository containing more than 20 years of expert-vetted security insights, and together they deeply analyze software in ways not possible before.

Signal integrates directly with AI coding assistants and focuses on high-fidelity, high-priority issues most likely to be exploited. It works at machine speed and secures apps with minimal human effort.

## What it can do

- **Find and fix issues** in code, whether the code was written by humans or agentic AI. Signal can work with coding assistants like Gemini, Copilot, and Claude.
- **Let you decide** whether to scan your code changes or the entire codebase.
- **Scan any programmatic language**. Because it is LLM-based, it can discover bugs in any language and doesn’t need any configuration to get started. It’s ideal for scanning languages that your other tools don’t support.
- **Find bugs that would go undetected** by rule-based engines.
- **Suggest fixes**. Signal output includes guidance that AI agents can use to fix the code.

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

## Signal operating system support

Signal runs on these operating systems.

- linux-arm64
- linux-x86_64
- macos-arm64
- macos-x86_64
- windows_x86

## Language support

Signal scans code effectively in any language.

Traditional SAST tools define what they can analyze by maintaining rules for each language and framework they support. Signal works differently. It analyzes code based on semantics — meaning, structure, and context — reasoning about it the way a security engineer would, regardless of the language or frameworks used. This means Signal isn’t bound by a fixed list of supported languages; it understands your code on its own terms.
