---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "UrN5ms2MEAOkaPaS2LQTRw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:14.658812+00:00"
---

# Examples

Commit data to host coverity_server1 for the `xalan` stream:

```
> cov-commit-defects --url https://admin:1256@coverity_server1:8443 --stream xalan --dir xalan_int_dir
```

Commit data to host coverity_server1 for the and `xalan` stream, using an
XML configuration file for all settings except the intermediate directory:

```
> cov-commit-defects  --dir xalan_int_dir --config test_cim_commit.xml
```

The
test_cim_commit.xml XML configuration file contents are shown
next:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE coverity SYSTEM "coverity_config.dtd">
<coverity>
    <config>
        <cim>
            <url>coverity_server1:9090</url>                                
            <client_security>
                <user>admin</user>                     
                <password>1256</password>            
            </client_security>
            <commit>  
                <source-stream>xalanSource</source-stream>
            </commit>
        </cim>
    </config>
</coverity>
```

The port element in this example refers to the commit port
(equivalent to the `--dataport` option).
