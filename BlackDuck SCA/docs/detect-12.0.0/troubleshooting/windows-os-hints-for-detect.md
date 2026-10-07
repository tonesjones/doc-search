---
title: "Windows OS hints for Detect"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/windows-os-hints-for-detect.html"
content_id: "gpiRbhU_jARlNy28RAW8nw"
version: "12.0.0"
section: "Troubleshooting"
scraped_at: "2026-10-04T23:33:23.186818+00:00"
content_hash: "448c08d25a2d53539bc453d8055e31456eaa381ce6e46421051e942aa8c12705"
---

# Windows OS hints for Detect

## Passing spaces in arguments

- Windows considers space as a separator for arguments and discards all the values which would be within double quotes. Eg: If you pass --detect.project.name=" Windows Project ", then that is being interpreted as "--detect.project.name=" "Windows" "Project". To pass spaces inside an argument in Windows OS, then you can either use single quotes ('single') or you can use backtick character (`) to escape spaces.

## Using multi-byte characters

- Using Windows with multibyte characters for different languages such as Korean or Japanese, you must configure Windows by using the chcp command to change the character code for cmd shell.
