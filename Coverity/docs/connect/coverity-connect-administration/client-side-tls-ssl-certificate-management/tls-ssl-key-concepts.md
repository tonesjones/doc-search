---
title: "TLS/SSL key concepts"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tls/ssl-key-concepts.html"
content_id: "qy3hg2qC8QokrimPbnHBQg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:23.232959+00:00"
---

# TLS/SSL key concepts

Certificates
:   TLS/SSL uses digital certificates. Certificates are passed from servers to
    clients in order to authenticate the server and create encrypted
    connections. Certificates are data files that contain information such as
    the Subject and Issuer of the certificate.

    The Subject identifies the party that proffers the certificate. In effect,
    "this is who I am."

    The Issuer identifies the party that asserts the veracity of the Subject. In
    effect, "this is who vouches for me."

    The certificates are digitally signed, which achieves two goals:

    - Makes the certificates attributable: you can confirm whom they come from.
    - Makes the certificates non-forgeable: anyone can verify that the
      contents are exactly as the issuer intended.

Certificate Authority
:   A Certificate Authority (CA) is an entity that digitally signs the
    certificates it issues. When a Certificate Authority issues a certificate,
    it is making the public claim that it has investigated the party named in
    the certificate's Subject, and found it to be authentic. When a CA signs a
    certificate, it puts its own identifier in the Issuer field.

Self-signed certificates
:   A self-signed certificate has the same Issuer and Subject. In effect, it says
    "I vouch for myself." This feature implies that a self-signed certificate
    can act as its own CA certificate in a TLS/SSL handshake (see below).

    It can be used to establish encrypted communications between a client and
    server, but it does not provide authentication. However, within a secure
    corporate network, the convenience of self-signed certificates may outweigh
    the absence of authentication.

Certificate chain
:   A certificate chain is a series of one or more certificates returned by the
    server. Each certificate has a Subject, "who I am", and an Issuer, "who
    vouches for me." The Issuer of one certificate is the Subject of the next
    certificate in the chain. The chain links the certificate from the server
    itself (called the server certificate) back to a certificate issued by the
    Certificate Authority. A client receives this certificate chain, and
    verifies that each certificate vouches for the next one. The final
    certificate, called the CA root certificate, is a self-signed certificate.
    If the client "trusts" the CA root certificate (explained below), the chain
    is called a "chain of trust."

    Figure 1. TLS/SSL certificate chain
      
     [image: image]

    In the figure, each numbered box represents a certificate, with an Issuer (I)
    and a Subject (S). Certificate 1 is the Server Certificate. The letters A,
    B, C, and D represent entities that issue or are the subject of
    certificates. Certificates 1, 2, and 3 comprise the certificate chain sent
    by the server to the client; certificate 4 is the CA root
    certificate.

TLS/SSL Handshake
:   To establish a connection, the client contacts the server. Following that,
    the client and server exchange messages that verify the server's identity
    and set up an encrypted channel. This exchange is called the "TLS/SSL
    handshake."

    The first part of the handshake is to authenticate the server. First, the
    server sends its certificate chain, except for the CA root certificate,
    which the client supplies. The client must construct a verified "chain of
    trust" starting with the server certificate and ending with a CA root
    certificate. The client application verifies each certificate in the chain.
    Since the CA root certificate is implicitly trusted by the client, and that
    trust flows from the CA root certificate to the server certificate, the
    client can trust that the server's identity is truly what is stated in the
    server certificate's subject.

    After establishing a chain of trust, the client verifies that the server
    hostname in the server certificate Subject field matches the hostname given
    by the user in the `--host` option or connection page. This
    match must be exact, except for letter case. For example, if
    `cov-commit-defects` has `--host foo`
    but the server certificate has foo.example.com in its Subject, the handshake
    will fail. This step is called "hostname verification" and is the last step
    in the authenticating the server.

    Note that a server with a self-signed certificate can put anything it wants
    in the Subject field. Coverity software therefore does not do hostname
    verification when accepting self-signed certificates.

Truststores
:   A client application knows it can trust a CA root certificate because it fetches the certificate
    from a trusted location within itself or in its environment. These trusted
    locations store collections of CA root certificates, and they are called
    truststores.

    The browser is a common Coverity Connect client that comes preconfigured with a truststore
    containing CA certificates from the largest CA vendors. The browser checks
    the server's certificate chain against the certificates in its truststore to
    find one that completes the chain. If a certificate is found in the
    truststore that completes the chain, then the client authenticates the
    server, and an TLS/SSL connection can be established.
