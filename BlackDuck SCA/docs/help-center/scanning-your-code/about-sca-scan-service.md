---
title: "About SCA Scan Service"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-sca-scan-service.html"
content_id: "HkHsWBOWzutlf6yXa9Kl4w"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:33.672442+00:00"
---

# About SCA Scan Service

SCA Scan Service (SCASS) is a scalable solution for performing software composition
analysis scans outside of the traditional Black Duck SCA environment.
SCASS supports Package Manager, Signature, Binary, and Container scans, making it a
versatile choice for various scanning needs.

This services provides significant benefits for both on-premise and hosted
customers:

- On-premise customers: Resource requirements for non-specialized scanning are
  greatly reduced, steamlining infrastructure needs.
- Hosted customers: Cloud Infrastructure efficiency improves with dynamic scaling
  based on overall scan demand, enhancing performance and reducing operational
  overhead.

## Key functions of SCA Scan Service

SCA Scan Service enables the following functionality:

- Scanning of provided code artifacts using one or more scan type
  methodologies.

  - Build artifacts, repositories, binary, and Docker images.
  - Signature, package manager, binary, and Docker container scan type
    methodologies.
- Matching of evidence to OSS components.

  - Signatures, packages, and Docker layer digests.
  - Singular and correlative matching techniques.
- Results delivery.

  - Unopinionated results of identified components, their declared
    licenses, and their associated vulnerabilities.
  - Intermediate evidence data (BDIO) in support of replay and
    serviceability.

## Performance Improvements

We have conducted extensive performance and scalability testing with the SCA Scan
Service. As a result, scan performance has improved across the board, along with a
reduction in resource requirements.

We strongly recommend that customers utilize at least `Gen05/120sph`
hardware scale for production environments, as `10sph` is not
suitable or supported for production use. The Gen05 hardware configuration
demonstrates a significant reduction in resource requirements, utilizing
approximately 25% less hardware for the same scan volume compared to Gen04. This
improvement is largely attributed to enhancements and optimizations made in the SCA
Scan Service (SCASS).

However, please note that individual scan performance will vary based on specific
scan configurations, hardware setups, and network bandwidth.

For more information on hardware resource reductions, please refer to our
announcement in the [2025.1.0 Release Notes](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/e13a1e7c4121ed278184c9836596cbd3.topic) and the [Black Duck Hardware Scaling
Guidelines](https://docs.blackduck.com/access?ft:originId=f598e2689f20062534e28c8999b4550b/42e9daee77bcf342ae2692e1ec6e7746.topic).

## Security considerations

As part of the SCA Scan Service (SCASS) implementation, it is crucial to ensure the
security of communication sessions with the service hosted at
**scass.blackduck.com**. While there have been no changes to the data
transmitted, internal processing enhancements have been made to improve efficiency.
Customers are encouraged to engage their security teams, review relevant policies,
and stay informed about the rollout progress, especially concerning binary and
container scanning features. This proactive approach helps maintain robust security
practices while utilizing SCASS.

## Scan types

| Scan type | Configuration Options | Code Upload? | BDIO Upload? | Correlated Scan Support? | Match Support |
| --- | --- | --- | --- | --- | --- |
| Signature | - Explicit configuration - Automatic configuration | [image: image] | [image: image] | [image: image] | - File-based evidence - Component origin matches |
| Package manager | - Explicit configuration - Automatic configuration | [image: image] | [image: image] | [image: image] | - Package-based evidence - Component origin matches |
| Binary | - Explicit configuration - Automatic configuration | [image: image] | [image: image] | [image: image] | - File-based and package-based evidence - Component matches - Component version matches - Component origin matches |
| Docker container | - Explicit configuration - Automatic configuration | [image: image] | [image: image] | [image: image] | - File-based and package-based evidence - Component matches - Component version matches - Component origin matches |
| Snippet | - Explicit configuration | [image: image] | [image: image] | [image: image] | - File-based evidence - Component origin matches |

## Other features

SCASS also enables Correlated
Scanning, a new feature that leverages SCASS to enhance match results by
combining insights from multiple scanning techniques.

Additionally, SCASS delivers faster delivery of scanning bug fixes, independent of
Black Duck release cycles. While scan results are stored
transactionally, this streamlined service enhances the flexibility and scalability
of scanning across platforms.

Please note, this feature must be enabled on your product registration key to take
advantage of the service. With SCASS, you can simplify resource management and enjoy a
more scalable scanning experience. Contact your Black Duck
representative to learn more.

## SCASS system block diagram

[image: SCASS System Block diagram]
