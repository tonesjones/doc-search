---
title: "Generating and Managing Certificates"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/generating-and-managing-certificates.html"
content_id: "3oQeQJYxCYM1nH18NlditQ"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:43.677488+00:00"
---

# Generating and Managing Certificates

Managing certificates is essential for secure communication between Black Duck SCA and its clients. This guide outlines the steps needed to
generate and manage required certificates efficiently.

## Before You Begin

- Ensure you have OpenSSL installed on your system
- Have administrator access to your Black Duck SCA instance
- Know your organization's certificate requirements

## Generate a Certificate in Three Simple Steps

1. **Create Your Certificate Files**

   Run this single command to generate both your private key and certificate
   signing request:

   ```
   openssl req -new -newkey rsa:2048 -nodes -keyout privateKey.key -out certificateSigningRequest.csr
   ```

   You'll be prompted to enter information for your certificate. Complete each
   field as requested.
2. **Get Your Certificate Signed**

   Choose one option:

   - Option A: Self-signed certificate (for testing environments)

     ```
     openssl x509 -req -days 365 -in certificateSigningRequest.csr -signkey privateKey.key -out certificate.crt
     ```
   - Option B: CA-signed certificate (recommended for production) Submit
     your CSR file to your Certificate Authority and follow their
     process.
3. **Install Your Certificate**

   1. Place your certificate files in the appropriate directory
   2. Update your Black Duck SCA configuration to reference
      these files:

      ```
      # Example configuration entry
      hub.webserver.certificate.path=/path/to/certificate.crt
      hub.webserver.privatekey.path=/path/to/privateKey.key
      ```

## Verification

Test your certificate installation with:

```
curl -v https://your-blackduck-server.com/api/current-version
```

You should see your certificate details and a successful connection.
