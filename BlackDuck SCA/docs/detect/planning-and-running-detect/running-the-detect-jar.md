---
title: "Running the Detect .jar"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/running-the-detect-.jar.html"
content_id: "Wm9ENZ2Id3cvlkmtdcuUaw"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:30.684489+00:00"
---

# Running the Detect .jar

Recent versions of the Detect .jar file are available for download from the location specified in download locations.

To run Detect by invoking the .jar file:

```
java -jar {path to .jar file}
```

For example:

```
curl -O https://repo.blackduck.com/bds-integrations-release/com/blackduck/integration/detect/11.3.0/detect-11.3.0.jar
java -jar detect-11.3.0.jar
```

You can use the Detect Bash script (detect11.sh) to download the Detect .jar file:

```
export DETECT_DOWNLOAD_ONLY=1
./detect11.sh
```
