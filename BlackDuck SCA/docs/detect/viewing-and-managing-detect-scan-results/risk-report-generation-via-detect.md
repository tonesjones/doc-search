---
title: "Risk Report generation via Detect"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/risk-report-generation-via-detect.html"
content_id: "xNMRY8q_3dMKg1lTzELM8A"
version: "11.5.1"
section: "Viewing and managing Detect scan results"
scraped_at: "2026-08-08T23:45:49.555831+00:00"
---

# Risk Report generation via Detect

Black Duck® Detect can generate a Black Duck® SCA risk report in PDF and JSON format.
Detect looks for risk report generation details in the properties whose names start with detect.risk.report, including:

- detect.risk.report.pdf (enable report generation in pdf format by setting to "true")
- detect.risk.report.pdf.path (path where the generated pdf report will be located)
- detect.risk.report.json (enable report generation in json format by setting to "true")
- detect.risk.report.json.path (path where the generated json report will be located)

## Fonts

Default font files are used to create the risk report pdf.

You may specify a custom regular font and/or a custom bold font by placing a .ttf font file in a directory called "custom-regular" and/or "custom-bold", respectively, that is a child to the directory at `detect-output-directory/tools/fonts`, where 'detect-output-directory' is determined by detect.output.path

Examples

- `/path-I-passed-to-detect-output-path/tools/fonts/custom-regular/my-custom-regular-font.ttf`
- `/Users/user/blackduck/tools/fonts/custom-regular/my-custom-regular-font.ttf` on Unix
- `C:\Users\blackduck\tools\fonts\custom-bold\my-custom-bold-font.ttf` on Windows

## File Naming

When generating the risk report file, non-alphanumeric characters separating portions of the project name or version will be replaced with underscores. For example, in a case with hyphens and periods like "Project-Name" and "Project.Version.Name", the resulting file name would be `Project_Name_Project_Version_Name_BlackDuck_RiskReport.pdf`

### Air Gap

Normally, font files used in creating the risk report PDF are downloaded from Artifactory. If you are using the Detect air gap zip, the font files are retrieved from a directory called 'fonts' that is a child to the root of the air gap directory

To specify custom fonts when using the Detect air gap zip, you must unzip the produced airgap zip file and then place a .ttf font file in a directory called "custom-regular" and/or "custom-bold" that is a child to the directory airGapRoot/fonts.

Example

- `detect-detect_version-air-gap/fonts/custom-regular/my-custom-regular-font.ttf`
