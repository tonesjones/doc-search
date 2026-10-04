---
title: "Signal FAQ"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/signal-faq.html"
content_id: "adLfX1KuRGF8aOKdT8kkBg"
version: "latest"
section: "Signal FAQ"
scraped_at: "2026-10-04T23:27:49.981044+00:00"
---

# Signal FAQ

Frequently asked questions about Black Duck Signal, including general product questions, LLM usage, and source code privacy.

## Contents

- General
- Large Language Models (LLMs) Usage
- Source Code Privacy

## General

**Q: What is Signal?**

Black Duck Signal is an agentic application security solution that uses the power of LLMs to automatically find, prioritize, and fix security and other defects in source code, binaries, supply chain components, and running applications. Signal augments and refines AI analysis with context from Black Duck ContextAI™ containing over 20 years of human expert vetted knowledge, including insecure coding patterns; open source components, vulnerabilities, and licenses; and secure coding standards and best practices. With Signal, development and security teams get deep AI analysis of software risks without the noise, hallucinations, and inconsistencies found in solutions that do not have this context.

**Q: What problem does this solve?**

Fundamentally, Signal is designed to use AI to address the central problem with traditional application security tools. They generate too much "noise" in the form of large volumes of false-positive and low-value findings that require considerable human effort — both from developers and security analysts — to triage and prioritize. To compensate for this, teams often need to apply additional technologies, such as ASPM, cloud security integrations, and reachability analysis.

Signal takes a different approach to eliminate noise before it can be generated. By leveraging the intuitive nature of AI, Signal dramatically reduces security findings to those that are real and high priority to fix.

In the near term, Signal focuses on addressing four key customer needs:

- Developers want to quickly find issues in code they just wrote or generated.
- Developers are adopting AI-coding assistants and want code generation, testing, and defect fixing to all happen through those interfaces.
- Security teams want to focus their efforts on the highest-risk security issues in the software they deliver.
- Security teams waste a lot of time manually reviewing code in languages not supported by traditional SAST solutions.

**Q: How is this different from asking a code assistant to analyze the code?**

From a user perspective there is little to no difference between asking a coding assistant like Copilot or Claude versus asking Signal. In fact, by registering Signal with these coding assistants via MCP, the user simply asks the assistant to scan their code, and the request is directed to Signal by the coding assistant itself.

The key difference is in the fidelity of the findings. In our tests, Signal produced significantly better findings than general-purpose AI coding assistants.

**Q: Is this replacing Coverity?**

No. AI complements traditional static analysis solutions like Coverity and Polaris fAST Static by providing:

- Support for languages for which static analysis rulesets are not available.
- Better real-time analysis and code fixing in developer workflows.
- Identification of security defects that rule-based analysis misses.

**Q: What are the key features and benefits?**

Signal addresses the four key customer needs with:

- **Real-time incremental analysis** of new and modified code. Signal's context-aware AI analysis delivers accurate findings without the need to perform a full application scan.
- **Direct integration** into AI-coding assistants via agent and Model Context Protocol (MCP) interfaces.
- **AI insights and context** that complement traditional AST by identifying issues — including those often missed by rules engines — most likely to be exploited.
- **Universal language support.** Signal's AI-based analysis is language-agnostic and able to analyze code in any modern or legacy programming language.

**Q: Is the Black Duck knowledge base used for Signal agents?**

The knowledge base used for Signal is branded as Black Duck ContextAI™. It combines the OSS component and BDSA information from the KnowledgeBase™ used by Black Duck SCA, as well as other security data and rules used by our SAST and SCA engines, analytics from our SaaS offerings, and best practices from our security consulting.

The initial code analysis use case at launch makes use of issue taxonomy information derived from Coverity. As Signal is expanded to cover other use cases, additional information from Black Duck ContextAI™ will be leveraged.

## Large Language Models (LLMs) Usage

**Q: Do you support customer-managed LLMs?**

Users can optionally configure Signal to use supported customer-managed LLM providers through the BYOLLM feature. See BYOLLM for supported providers and configuration options.

**Q: Where are the LLMs hosted?**

We use a combination of LLMs hosted in Azure, AWS, and GCP.

## Source Code Privacy

**Q: Where is my source code going?**

Signal programmatically crawls targeted source code on the user's system and sends individual files and excerpts to LLMs for analysis.

**Q: Is my source code stored or cached anywhere?**

No caching occurs on the Black Duck side.

**Q: Does Signal use my code for training LLM models?**

No, Signal does not use customer code for training LLM models.

**Q: Does Signal modify my source code?**

Signal does not modify source code. If using Signal Developer within the IDE, coding assistants can interface with Signal to identify vulnerabilities and suggested fixes, but the application of those fixes is handled by the developer and coding assistant.
