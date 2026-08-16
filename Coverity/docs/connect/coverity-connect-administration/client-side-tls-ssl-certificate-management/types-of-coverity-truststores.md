---
title: "Types of Coverity truststores"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/types-of-coverity-truststores.html"
content_id: "5kY5PUDSBzOwpRfOkcWGLw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:25.838544+00:00"
---

# Types of Coverity truststores

This section is relevant to customers whose server certificates are issued by private
CAs. In this situation, the administrator must provide users with CA root certificates,
and a way for client applications to use them.

In order to facilitate use of private CAs, Coverity provides several different truststores.
Generally, truststores used by Coverity software are sequences of PEM-formatted
certificates. They are in ASCII, which makes them easy to manipulate.

Installation truststore
:   This file is installed with Coverity client applications. It is called
    ca-certs.pem and is located in the
    certs directory. It contains public CA
    certificates, and private CA root certificates can be added to it. If it is
    not present, Java applications use the CA certificate file
    cacerts installed with Java. This is not a PEM file
    but a Java keystore file with the password
    `changeit`.

Extra CA truststore
:   This optional CA certificates file is passed to command-line applications
    using the `--certs` option or to GUI applications via their
    Connection pages.

User truststore
:   This file is stored under the user's home directory:

    - (Windows)
      %APPDATA%\Coverity\certs\ca\ca-certs.pem
    - (Unix/Linux)
      $HOME/.coverity/certs/ca/ca-certs.pem

Operating System truststore
:   Some operating systems (Windows, Linux, Mac OS) provide mechanisms for
    storing CA root certificates.

    Windows: Azure Entra ID administrators can remotely manage the user's Root
    Certificate Store, or users can update the store themselves using a wizard,
    the certmgr.msc executable.

    Additional References:

    - [Azure Entra ID Certificate
      Services](https://technet.microsoft.com/en-ca/windowsserver/dd448615.aspx)
    - [Azure Entra ID Certificate
      Services Step-by-Step Guide](https://technet.microsoft.com/en-us/library/cc772393(v=ws.10).aspx)

    Mac OS X: Certificates are stored in the user and system keychains. The user
    uses the `Keychain` graphical application or the
    `security` command to add certificates. The Keychain
    API may also be used.

    Additional References:

    - [Keychain Access: Add certificates to a
      keychain](https://support.apple.com/kb/PH20129?)

    Unix/Linux: certificates are stored in
    /etc/ssl/certs/ca_certificates.crt, a PEM-format
    file. The administrative procedures for updating certificates vary by OS
    brand, but they all require root permission. Truststores can be updated
    remotely using scripting or SSH.

    Additional References:

    - [OpenSSL
      Cookbook](https://www.feistyduck.com/books/openssl-cookbook/)
