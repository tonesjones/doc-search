---
title: "Self-signed certificates and trust-first-time TLS/SSL"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/self-signed-certificates-and-trust-first-time-tls/ssl.html"
content_id: "tJzv9K9uMPeoz77yhLNVlQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:25.208371+00:00"
---

# Self-signed certificates and trust-first-time TLS/SSL

This section is relevant if the Coverity Connect server is configured with self-signed
certificates. This is the default configuration, since the installer generates a
self-signed certificate for the server.

Self-signed certificates do not permit the client to authenticate the server, so they are
inherently less secure than CA-signed certificates, which do allow authentication.
However, CA-signed certificates require more administrative overhead than self-signed
certificates. With this in mind, Coverity applications allow the server to use
self-signed certificates for the benefit of customers for whom the additional overhead
does not justify the benefit of authentication of the server.

All Coverity TLS/SSL client applications now accept self-signed certificates, provided the
user permits it. (Previous to Coverity 8.0, only `cov-commit-defects`,
`cov-run-desktop` and `cov-manage-history`
accepted self-signed certificates.) Coverity's algorithm for conditionally accepting
them, called Trust First Time (TFT), is designed to minimize the number of times the
user is asked to permit a TLS/SSL handshake with self-signed certificates. The algorithm,
modeled after that of SSH, has these characteristics:

- A handshake with a self-signed certificate will fail unless the user permits it
  to succeed.
- This permission is stored by the client.
- Subsequent handshakes with the same self-signed certificate for the same server
  host and port automatically succeed.
- An attempt by the server or an impostor to use a different self-signed
  certificate is rejected by the client.

TFT has two modes of operating: one for attended applications and one for unattended
applications. It is assumed that the former will always have a user present to be able
to accept alerts and answer questions, while this may not be true of the latter. The
attended applications in Coverity 8.0 are all the GUI applications. All the command-line
applications are considered unattended.

TFT is triggered when the server sends a self-signed certificate to the client. If the server's
certificate is not present in the truststore of self-signed certificates, the
application's response is based on the user's intentions with respect to self-signed
certificates:

- Attended applications describe the self-signed certificate for the user and ask
  whether it should be trusted (i.e., accepted for the handshake) and stored for
  future handshakes. If the user assents, e.g. by clicking the OK button, the
  application completes the handshake and stores the certificate.
- Unattended applications cannot ask the user what to do. Instead they rely on a
  command-line directive. A new option, `--on-new-cert`, specifies
  what to do. It has two values: "trust" and "distrust". The default is
  "distrust". (The default behavior previous to Coverity 8.0 was "trust".)

  - "trust" indicates that the application should behave as if the user
    assented to use of the self-signed certificate: the handshake is
    completed and the certificate is stored.
  - "distrust" indicates that the application should fail the handshake and
    not store the certificate.

    The old `--authenticate-ssl` option for
    `cov-commit-defects` is a synonym for
    `--on-new-cert` distrust.

If the server sends a different self-signed certificate than in the past, the TFT
algorithm detects this and displays a warning for the user. This is important because it
may indicate that the server is an impostor. In this situation,

- Attended applications ask the user if the stored certificate should be replaced
  with the new one. If the user says yes, it stores the new certificate and
  permits the handshake to succeed.
- Unattended applications fail.

The truststore for self-signed certificates is a directory under the user's home directory:

- (Windows) %APPDATA%\Coverity\certs\tft
- (elsewhere) $HOME/.coverity/certs/tft
