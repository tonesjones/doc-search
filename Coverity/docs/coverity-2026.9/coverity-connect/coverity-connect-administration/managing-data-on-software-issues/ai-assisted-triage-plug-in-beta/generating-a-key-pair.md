---
title: "Generating a key pair"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/generating-a-key-pair.html"
content_id: "WryyRjnFi~JLUq5opnzWXA"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:11.799635+00:00"
---

# Generating a key pair

Generate and distribute the key pair used by the triage service and Coverity
Cloud.

Ensure that:

- OpenSSL installed on the machine where the keys will be generated.
- You have access to the target deployment environment (Helm/Kubernetes, Docker,
  or bare binary host).
- You have sufficient permissions to create Kubernetes Secrets/ConfigMaps,
  bind-mount files into containers, or set environment variables, depending on
  your deployment model.

The key pair is generated once at deployment time and then distributed according to
your deployment model.

1. Generate the key pair.

   On a secure machine, run the following OpenSSL commands to generate an EC
   (P-256) key pair:

   ```
   openssl ecparam -name prime256v1 -genkey -noout -out ec-private.pem
   openssl ec -in ec-private.pem -pubout -out ec-public.pem
   ```

   This produces two files:

   - `private.pem` — the private key. Distribute only to the
     triage service.
   - `public.pem` — the public key. Distribute to Coverity
     Cloud.

   Warning: Treat `private.pem` as a sensitive secret.
   Do not commit it to source control, and restrict file permissions to the
   service account that will read it.
2. Distribute the keys according to your deployment model.

   - **Docker**
     1. Bind-mount each PEM file into its respective
        container:

        ```
        # Triage service
        docker run \
          -v $PWD/private.pem:/secrets/llm-key-encryption/llm-key-private.pem:ro \
          -e ENCRYPTION_PRIVATE_KEY_FILE=/secrets/llm-key-encryption/llm-key-private.pem \
          ...

        # Coverity Connect
        docker run \
          -v $PWD/public.pem:/secrets/triage-llm-key-encryption/llm-key-public.pem:ro \
        ```
     2. Add the following line to `cim.properties` on the
        Coverity Cloud
        side:

        ```
        encryption.public.key.file=/secrets/triage-llm-key-encryption/llm-key-public.pem
        ```
   - **Bare binary**

     Place the PEM files on disk with permissions
     readable only by their respective service users. Set
     `ENCRYPTION_PRIVATE_KEY_FILE` for the triage
     service, and configure `encryption.public.key.file`
     in Coverity Connect's `cim.properties` to point at
     `public.pem`.
3. Verify the deployment.

   - Confirm the triage service can read `private.pem` from
     its configured location.
   - Confirm Coverity Cloud can read `public.pem` from its
     configured location.
   - Validate end-to-end encryption and decryption between Coverity Cloud and
     the triage service before promoting the deployment to production.
