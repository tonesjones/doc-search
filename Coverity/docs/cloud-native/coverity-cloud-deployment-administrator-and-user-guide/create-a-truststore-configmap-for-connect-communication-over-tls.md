---
title: "Create a truststore ConfigMap for Connect communication over TLS"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-truststore-configmap-for-connect-communication-over-tls.html"
content_id: "0EDG5HGD6G~pAUYfSdNWyA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:09.995093+00:00"
---

# Create a truststore ConfigMap for Connect communication over TLS

Coverity Connect communicates over TLS to establish secure connections. It relies on
certificates located in Java keystores and truststore ConfigMaps to validate all network
targets. In Coverity Cloud, truststore ConfigMaps are used to store and manage trusted
certificates for secure TLS or SSL connections within the Kubernetes cluster.

In a Kubernetes cluster, a truststore ConfigMap is a Kubernetes object that is used to
store a truststore file as configuration data. A truststore is a repository of trusted
certificates that are used to establish secure connections, typically for TLS/SSL
communication. The truststore contains certificates from Certificate Authorities (CAs)
or other entities that applications trust for secure communications.

During a TLS or SSL handshake, the Connect client looks up root certificates in its
truststore. For all external integrations such as LDAP, PostgreSQL, Bugzilla, Jira,
SMTP, etc., the Coverity Connect client looks up the corresponding root certificate in
its truststore.

If the Connect server is not using a TLS certificate signed by an authority trusted by
Java, the certificate needs to be imported into the Connect client's truststore. This
includes self-signed certificates and any other certificates that Java does not
trust.

Table 1. Truststore ConfigMap integrations

| Integration | Type | Comment |
| --- | --- | --- |
| PostgreSQL | For a Connect server instance, create a truststore ConfigMap that contains certificates for all relevant software. See Creating a truststore ConfigMap for a Connect instance. | For PostgreSQL, this is not needed if the PostgreSQL certificate is already included in the default truststore. |
| LDAP |  |
| Jira |
| Bugzilla |
| SMTP (email) |
| TLS | If not already done, generate public and private certificate keys as described in Generating a Connect TLS certificate. |

Note: To create a truststore ConfigMap, refer to Creating a truststore ConfigMap for a Connect instance.
