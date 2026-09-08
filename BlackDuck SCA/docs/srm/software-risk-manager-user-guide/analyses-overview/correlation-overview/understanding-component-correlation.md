---
title: "Understanding Component Correlation"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/understanding-component-correlation.html"
content_id: "2E7Urfdu5XzSCnB2kx0Jag"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:57.518678+00:00"
content_hash: "27c469f2adc741aeeba445cf807931ee44ac772edaa14738a7362dedf24d9210"
---

# Understanding Component Correlation

There are five ways to correlate components (for more information, see Analysis Correlation Options). Component correlation modes control how
Software Component Analysis (SCA) tool results are correlated to findings. SRM can be
configured to correlate component results using different combinations of the following data:

- vulnerability (e.g., BDSA-2021-0069, CVE-2021-24122)
- component name and version (e.g., Spring Framework version 3.2.4)
- type (e.g., Vulnerable Component)
- component identifier (e.g., org.springframework:spring-aop:3.2.8.RELEASE)

You will get one finding per unique set of values for each option. For example, selecting
"vulnerability, component name/version, and type" will result in a finding for each
vulnerability for each component and type that you have. However, if "vulnerability and
type" is selected, you will only get a finding per vulnerability and type that covers
all components. The default mode is "vulnerability, component identifier, and type."
