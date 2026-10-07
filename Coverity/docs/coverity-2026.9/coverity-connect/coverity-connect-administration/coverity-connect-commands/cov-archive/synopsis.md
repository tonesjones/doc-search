---
title: "Synopsis"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/synopsis.html"
content_id: "guT2d8S0TqQ_bWmyHoVQQw"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.944525+00:00"
---

# Synopsis

This command has three main variants. These depend on whether you want to export, import, or
get information. A fourth variant returns help information; it can specify one of the first three variants.

**Export information**

```
cov-archive [--debug] export-streams 
            [--remove [--silent]] 
            --archive <archive-file> 
            [--project <project-name>...]... 
            [--stream <stream-name>...]...
```

**Import information**

```
cov-archive [--debug] import-streams 
            --archive <archive-file> 
            [--cluster-config <cluster-config-file>]
```

**Get information**

```
cov-archive [--debug] list 
            --archive <archive-file>
```

**Get help**

```
cov-archive help [<command>]
            
cov-archive -h
            
cov-archive --help
```
