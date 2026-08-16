---
title: "AI security, data protection, and trust"
source_url: "https://docs.blackduck.com/r/signal/black-duck-signal/ai-security-data-protection-and-trust.html"
content_id: "SeKsRfoJBm40f_Zq4N3HQw"
version: "latest"
section: "AI security, data protection, and trust"
scraped_at: "2026-08-13T00:04:59.199748+00:00"
---

# AI security, data protection, and trust

Black Duck Signal is designed as a responsible, human-centered AI security analysis platform, with strong controls around LLM access, data isolation, and enterprise compliance.

This topic describes the security posture, data handling practices, and large language model (LLM) usage for Black Duck Signal, addressing common customer questions around AI trust, privacy, and compliance.

## LLM models used

Signal AI Scanner uses large language models exclusively through the Black Duck–managed LLM Gateway. LLM selection, access, and orchestration are managed entirely by Black Duck.

Signal is designed with a model-agnostic architecture, and Black Duck currently uses and validates integrations with publicly available foundational models, including:

- Anthropic (Claude)
- OpenAI (GPT series)
- Google Cloud AI (Vertex AI)
- Azure OpenAI Service

## Commercial LLMs and model training

The models accessed through the Black Duck LLM Gateway are public, commercial foundational models.

Black Duck does not:

- Apply proprietary fine-tuning
- Train or retrain models using customer data or source code
- Use customer inputs to improve or modify model behavior

Customer data is used only at inference time to generate security findings.

## LLM access architecture

Signal uses Black Duck's managed LLM gateway to perform AI-based scans.

- Signal does not use customer-hosted LLM infrastructure
- Signal does not require customers to connect their own LLM accounts
- All LLM access is orchestrated, secured, and audited by Black Duck

This centralized approach ensures consistent security controls, monitoring, and governance across all customers.

## Hosting locations

Signal uses Black Duck LLM infrastructure when performing scans. Customers do not provide or manage LLM infrastructure.

The validated LLM providers used by Black Duck operate on US-based infrastructure, including:

- Anthropic: US-based infrastructure
- OpenAI: US-based infrastructure
- Google Cloud AI: US-based infrastructure
- Azure OpenAI Service: US-based infrastructure

Black Duck centrally manages security controls, access policies, and auditing for all LLM interactions.

## Human-in-the-loop safeguards

Signal is designed as a human-supervised analysis tool, not an autonomous decision-maker.

- LLMs generate analytical findings and recommendations only
- Signal does not directly modify customer code
- At most, Signal may create merge requests requiring explicit human approval
- Developers retain full authority to accept, modify, or reject recommendations

All findings require human judgment before any corrective action is taken.

## Data privacy and isolation

Signal enforces strong data isolation and multi-tenancy controls:

- Isolation enforced at the LLM provider API level
- Per-organization authentication, authorization, and rate limiting
- No cross-customer data sharing or visibility
- Black Duck does not access or reuse customer source code across tenants

Each organization's usage and credentials remain fully isolated.

## Monitoring, auditing, and logging

Signal implements comprehensive monitoring and observability for AI usage:

- API call logging (timestamps, model used, token usage, latency)
- Error tracking for failed scans and model timeouts
- Usage metrics per customer, including performance and cost indicators
- Audit trails covering scan requests, outputs, and user interactions
- Eligibility for human review of high-risk or anomalous results

To balance scale, performance, and data minimization, full prompt and response content is not logged at scale. Sampling-based logging may be introduced for high-risk findings.

## Training, updates, and model evolution

Black Duck does not train or fine-tune any LLMs used by Signal.

- Foundational model updates occur per each provider's release schedule
- Black Duck-owned updates focus on prompt engineering, orchestration logic, and scanning heuristics
- Improvements are driven by security research, user feedback, and real-world testing
- Model evolution is independent of customer data

## Compliance and responsible AI practices

Signal is designed to support enterprise compliance and governance requirements:

- Inference-only model usage (no training on customer or personal data)
- Data Processing Agreements (DPAs) in place with supported LLM providers
- Customer data retention and deletion policies enforced
- Transparency that findings are generated using LLMs
- All recommendations are user-overridable

**HIPAA notice:** Signal AI Scanner is not intended for processing HIPAA-regulated patient data in the current release, and no HIPAA compliance claims are made at this time.

**Security certifications:** Black Duck maintains SOC 2 Type II certification. Supported LLM providers offer their own enterprise security and compliance reports.
