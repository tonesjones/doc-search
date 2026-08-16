---
title: "Generating a key pair"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generating-a-key-pair.html"
content_id: "WryyRjnFi~JLUq5opnzWXA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:31.216073+00:00"
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

   - **Helm/Kubernetes**
     1. Create a single Kubernetes Secret containing both PEM files in
        the same namespace where Coverity Connect and the triage service
        will
        run:

        ```
        kubectl create secret generic triage-suggestion-service-llm-key-encryption \
          --namespace=<your-namespace> \
          --from-file=llm-key-private.pem=./private.pem \
          --from-file=llm-key-public.pem=./public.pem
        ```
     2. Reference that Secret from both sides in your umbrella chart
        values file. Both keys point to the same Secret name; the chart
        picks the correct PEM from each side using the file-name
        key:

        ```
        # Triage service: mount the private key
        triage-suggestion-service:
          llmKeyEncryption:
            existingSecret: "triage-suggestion-service-llm-key-encryption"
            secretKey: "llm-key-private.pem"

        # Coverity Connect: mount the public key (from the same Secret)
        cim:
          cimweb:
            triageSuggestionService:
              llmPublicKeySecret:
                name: "triage-suggestion-service-llm-key-encryption"
                key:  "llm-key-public.pem"
                mountPath: "/secrets/triage-llm-key-encryption"
        ```

     The chart wires the rest up automatically:
     - The triage-suggestion-service API and Worker pods get the
       private key mounted at
       /secrets/llm-key-encryption/llm-key-private.pem
       and the ENCRYPTION_PRIVATE_KEY_FILE
       environment variable set to that path.
     - The Coverity Cloud cimweb pod gets the public key mounted at
       /secrets/triage-llm-key-encryption/llm-key-public.pem,
       and `cim.properties` is generated with
       `encryption.public.key.file=/secrets/triage-llm-key-encryption/llm-key-public.pem
       and
       ai.triage.suggestion.service.auth.key=${TRIAGE_SUGGESTION_AUTH_KEY}`(sourced
       from the authentication-secrets Secret).

     Tip: If you need a different Secret name, override
     both
     `triage-suggestion-service.llmKeyEncryption.existingSecret`
     and
     `cim.cimweb.triageSuggestionService.llmPublicKeySecret.name`
     to the same value so the two sides resolve to the same
     Secret.
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
