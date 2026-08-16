---
title: "Create TLS certificate, keystore, and secrets"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-tls-certificate-keystore-and-secrets.html"
content_id: "aRMHGGlgrNxfyQiA4x_97w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:58.190781+00:00"
---

# Create TLS certificate, keystore, and secrets

This chapter describes how to create a TLS certificate, keystore, and many secrets
that enable secure user and service access to Coverity cloud networks and resources.
These components are defined and used as follows:

A **TLS (Transport Layer Security) certificate** is a digital certificate that is
used to establish secure communications over networks. Services within the
Kubernetes cluster use TLS certificates to establish secure connections with each
other, especially when implementing mTLS (Mutual TLS) for service-to-service
communication. A TLS certificate includes a public key and a private key, defined as
follows:

- Public Key: The public key is used in the encryption process and is part of
  the certificate that is shared with clients.
- Private Key: The private key is kept secret by the server and is used to
  decrypt data sent by clients.

A **keystore** is a secure storage mechanism that holds cryptographic keys and
certificates used for secure communications, such as SSL/TLS encryption. The
keystore is essential for managing the keys and certificates necessary for
establishing secure connections between services within the cluster and with
external systems.

**Secrets** securely store sensitive information, such as passwords, OAuth tokens,
SSH keys, and certificate data. Secrets allow you to manage and protect sensitive
data needed by your applications while minimizing the risk of exposure.

Note: The sections that follow assume that you are working in a
shell or script where you have already set variables to hold the names of the secret
keys. For example, `"${INGRESS_SECRET_NAME}"` or
`"${CONNECT_SECRET_NAME}"` in the examples. Other variables
contain values for things that were configured as part of the infrastructure setup;
for example, `${NS}` contains the namespace name for the related
component.
