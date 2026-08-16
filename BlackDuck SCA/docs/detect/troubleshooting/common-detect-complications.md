---
title: "Common Detect complications"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/common-detect-complications.html"
content_id: "2QP7cY8GzEOaz3SMPJYFXw"
version: "11.5.1"
section: "Troubleshooting"
scraped_at: "2026-08-08T23:45:51.427577+00:00"
---

# Common Detect complications

- Problems may occur due to incompatible Black Duck® Detect / Black Duck® SCA versions. Consult the [Compatibility Matrix](https://docs.blackduck.com/r/blackduck/black-duck-compatibility-reference/black-duck-sca-release-compatibility.html) to verify your combination. Attempting to reproduce the problem using the latest version of Black Duck SCA with the latest version of Black Duck SCA might also assist in determining if the issue has been resolved.
- Remember to consider the possibility that the Black Duck SCA user lacks the necessary permissions (to create the project, update the BOM, receive notifications, etc.) in Black Duck SCA. For more information, see Black Duck user role requirements.
- Confirm that the Black Duck SCA server (registration key) has the required capabilities enabled (binary upload, snippet scanning, etc.).

## Incorrect or missing components

- For issues related to tools invoked by Detect (Black Duck Signature Scanner, Docker Inspector, etc.), please check that tool's documentation.
- Issues related to incorrect components in the Black Duck SCA BOM.

  - Detect configuration has control over matches produced by detectors (that are written to BDIO files), but no control over matches produced by the Black Duck Signature Scanner / Black Duck SCA. When investigating an incorrect component in a Black Duck SCA BOM, you need to determine whether the component was contributed by a detector, or by the Black Duck Signature Scanner: On the Black Duck Components tab for the project/version: Click on the *N Matches* link next to the component. The next screen lists the matches on the right-hand side. Matches from the Black Duck Signature Scanner have a filename in the *Name* column. Matches from detectors have an external ID (such as "org.hamcrest:hamcrest-core:1.3") in the *Name* column.
- For issues related to components missing from, or incorrectly categorized, in the Black Duck SCA BOM.

  - Detect configuration has control over the production of BDIO files (use --detect.diagnostic to save these), but no control over how they are converted into a BOM by Black Duck SCA. A good first step is to determine whether the BDIO files produced are correct. If they are incorrect, the problem is related to what Detect is doing. If they are correct, but the BOM is incorrect, the problem is related to what Black Duck SCA is doing. Similarly, Detect is responsible for passing the correct arguments to the Black Duck Signature Scanner, but beyond that has no control over the results it produces.

## Spring Boot related issues

- Detect is a Spring Boot application, and leverages Spring Boot to provide various mechanisms to configure it through [property settings](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-external-config.html). Spring Boot flexibility makes it's possible for Detect to be influenced by files (application.properties, application.xml, etc.) that might exist in the directory from which Detect is run that are intended for some other application and produce unexpected results. If properties have unexpected values (see the Detect log), this should be reviewed. The best solution may be to run Detect from a different empty directory using the `--detect.source.path argument` parameter.
- Similarly, Detect might be influenced by environment variables via the same Spring Boot mechanism, so check the environment for variables that correspond to Detect property names.

## Exceeding configured timeouts

- When `--detect.wait.for.results` or `--detect.timeout CLI arguments` parameters are specified for Detect, the variable nature of scan completion times may cause Detect to indicate a timeout. Scan completion time is influenced by the size of the scanned code base and the extent of concurrent load on Black Duck SCA. Should no other Detect scan exceptions be indicated, Detect timeout may not indicate a scan failure. Users can continue to monitor the scan within Black Duck SCA itself after Detect stops waiting for results.
