---
title: "Coding standard configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coding-standard-configuration.html"
content_id: "Z9_ASx052Dw9nRHBo~lN3Q"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:08.643066+00:00"
---

# Coding standard configuration

Use these keys to control the application of coding standards.

| Key | Type | Description |
| --- | --- | --- |
| `ignore-deviated-findings` | Boolean | For C, C++, Java: If `true`, any defects found in code annotated using the `#pragma` Coverity compliance directive will not be reported in Coverity Connect. You can then find information about the defects that were suppressed in two files:   - deviations.txt - deviations-warnings.txt   Default: `false` |
| `autosarcpp14` | specific coding standard configuration | C++: Enables AUTOSAR code compliance checking according to the given configuration. |
| `cert-c` | specific coding standard configuration | C: Enables CERT-C code compliance checking according to the given configuration. |
| `cert-c-recommendation` | specific coding standard configuration | C: Enables CERT-C Recommendation code compliance checking according to the given configuration. |
| `cert-cpp` | specific coding standard configuration | C++: Enables CERT-CPP code compliance checking according to the given configuration. |
| `cert-java` | specific coding standard configuration | Java: Enables CERT-Java code compliance checking according to the given configuration. |
| `hyundai-c` | specific coding standard configuration | C: Enables Hyundai Coding Standard 4.1 reporting. |
| `hyundai-c-4.1` | specific coding standard configuration | C: Enables Hyundai Coding Standard 4.1 reporting. |
| `hyundai-cpp` | specific coding standard configuration | C++: Enables Hyundai Coding Standard 4.1 reporting. |
| `hyundai-cpp-4.1` | specific coding standard configuration | C++: Enables Hyundai Coding Standard 4.1 reporting. |
| `hyundai-java` | specific coding standard configuration | Java: Enables Hyundai Coding Standard 4.1 reporting. |
| `hyundai-java-4.1` | specific coding standard configuration | Java: Enables Hyundai Coding Standard 4.1 reporting. |
| `iso-ts17961` | specific coding standard configuration | C: Enables ISO TS 17961 code compliance checking according to the given configuration. |
| `misrac2004` | specific coding standard configuration | Enables MISRA C 2004 code compliance checking according to the given configuration. |
| `misrac2012` | specific coding standard configuration | Enables MISRA C 2012 code compliance checking according to the given configuration. |
| `misrac2023` | specific coding standard configuration | Enables MISRA C 2023 code compliance checking according to the given configuration. |
| `misrac2025` | specific coding standard configuration | Enables MISRA C 2025 code compliance checking according to the given configuration. |
| `misrac++2008` | specific coding standard configuration | Enables MISRA C++ 2008 code compliance checking according to the given configuration. |
| `misrac++2023` | specific coding standard configuration | Enables MISRA C++ 2023 code compliance checking according to the given configuration. |
