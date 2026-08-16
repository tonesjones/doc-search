---
title: "Subscriptions and Entitlements in Polaris"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/subscriptions-and-entitlements-in-polaris.html"
content_id: "9JaMs68KogQV8w0f0RAjpA"
product_key: "polaris-platform-latest"
section: "Understand Polaris"
scraped_at: "2026-08-12T19:55:40.424239+00:00"
content_hash: "a9c0c5e6582e98021c2ce250b2e51f97664c6f4b7db5b4516ac0ebe9df9ffaea"
---

# Subscriptions and Entitlements in Polaris

A subscription is a license that allows an organization to run tests in Polaris. The entitlements in a subscription control the types and quantities of tests a subscription can run.

Subscriptions always contain several properties:

- A start date
- An expiration date
- Triage availability (first-time-only or no-triage)
- One or more entitlements, which control:
  - What types of tests (DAST, External Analysis, SAST, SCA, or Binary Analysis) a subscription can run
  - The quantity of tests a subscription can run
  - The maximum number of branches per SAST & SCA project

  Note: Only a concurrent (team member) subscription can include Binary Analysis.

After an organization purchases subscriptions, an Organization Admin or Organization Application Manager must associate a subscription with an application before users can begin using tests and services.
