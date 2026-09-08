---
title: "Trust Certificates Pre-work"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/trust-certificates-pre-work.html"
content_id: "tQtyLsyWh2Ee~wBLprq8ww"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:04.379787+00:00"
content_hash: "12cbf85480a671153ed7068680b703b5342674566459264011f281db90ad1df6"
---

# Trust Certificates Pre-work

Your Software Risk Manager instance can trust self-signed certificates or certificates issued
by certificate authorities that are not trusted by default. Obtain a copy of the [cacerts](https://en.wikipedia.org/wiki/Java_KeyStore) file from a Java 21 distribution, which will include the [keytool](https://cr.openjdk.org/~jjg/8261930/docs/specs/man/keytool.html) program that you will need to run the following command:

```
keytool -import -trustcacerts -keystore ./cacerts -file /path/to/cert -alias cert-name
```

Note: The default password for a Java cacerts file is `changeit`.

You can mount your cacerts file by adding a line to the volumes list in the codedx-tomcat
section:

```
    codedx-tomcat:
        ...
        volumes:
            - codedx-appdata:/opt/codedx
            - /path/to/cacerts:/opt/java/openjdk/lib/security/cacerts
        ...
```

Note: Append `:Z` to the extra volume mount when using [selinux](https://docs.docker.com/storage/bind-mounts/#configure-the-selinux-label).
