---
title: "Configuring authentication secrets"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-authentication-secrets.html"
content_id: "7EuPoTzqOh_s6K1Zyks0Wg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:31.957929+00:00"
---

# Configuring authentication secrets

Generate and configure the four authentication secrets required for secure
communication between Coverity Cloud and the triage suggestion service.

Ensure that:

- OpenSSL is installed on your system.
- You have already generated the encryption key pair (private.pem /
  public.pem).
- You have admin access to both the triage suggestion service and Coverity Cloud.

The triage suggestion service requires four auth secrets in addition to the
encryption key pair. These secrets apply to all deployment modes.

| Secret | Environment Variable | Purpose |
| --- | --- | --- |
| `jwt_secret` | `jwt_secret` / `jwt_secret_file` | Signs JSON Web Tokens issued by the triage service |
| `jwt_encryption_key` | `jwt_encryption_key` / `jwt_encryption_key_file` | Encrypts JWT payload content |
| `auth_key` | `auth_key` / `auth_key_file` | Shared secret that authenticates requests between Coverity Cloud and the triage service |
| `auth_hmac_secret` | `auth_hmac_secret` / `auth_hmac_secret_file` | Signs HMAC digests for internal message integrity |

Important:

- `auth_key`is a shared secret. It must be identical on both
  the triage service and Cloud. The other three secrets are internal to the
  triage service and must not be shared.
- If you use the environment variable, secrets may be visible to other
  users.

1. Generate the four secrets by running the following commands and record each
   output securely: 

   ```
   openssl rand -base64 32   # jwt_secret
   openssl rand -base64 32   # jwt_encryption_key
   openssl rand -base64 32   # auth_key (shared with Connect)
   openssl rand -base64 32   # auth_hmac_secret
   ```
2. Create the Kubernetes Secret in the namespace where the triage suggestion
   service will run.

   If you have already generated and saved the four values (for example, because
   `auth-key` must match a value already configured on the
   Coverity Cloud side), populate the Secret from
   files:

   ```
   # Save each value to a file with no trailing newline, then:
     kubectl create secret generic triage-suggestion-service-secrets \
       --namespace=<your-namespace> \
       --from-file=jwt-secret=./jwt-secret \
       --from-file=jwt-encryption-key=./jwt-encryption-key \
       --from-file=auth-key=./auth-key \
       --from-file=auth-hmac-secret=./auth-hmac-secret
   ```

   If you have not yet generated the four values, generate fresh values and pipe
   them directly into `kubectl create secret generic` so the
   plaintext never lands on
   disk:

   ```
   kubectl create secret generic triage-suggestion-service-secrets \
       --namespace=<your-namespace> \
       --from-literal=jwt-secret=$(openssl rand -base64 32) \
       --from-literal=jwt-encryption-key=$(openssl rand -base64 32) \
       --from-literal=auth-key=$(openssl rand -base64 32) \
       --from-literal=auth-hmac-secret=$(openssl rand -base64 32)
   ```

   Run the following to verify that the Secret was created with all four
   keys:

   ```
   kubectl get secret triage-suggestion-service-secrets \
       --namespace=<your-namespace> \
       -o jsonpath='{.data}' | jq 'keys'
   ```

   Expected output:

   ```
   [
       "auth-hmac-secret",
       "auth-key",
       "jwt-encryption-key",
       "jwt-secret"
     ]
   ```

   Note: The Secret name (`triage-suggestion-service-secrets`) and
   key names (`jwt-secret, jwt-encryption-key, auth-key,
   auth-hmac-secret`) are the values the chart's deployment
   templates reference by default. If you change them, you must also update the
   envVarsFromSecret mapping in your Helm values to
   match.
3. Configure the secrets on the triage service based on your deployment
   model.

   Follow the instructions for your deployment model only.

   - Helm / Kubernetes: Store all four values in a Kubernetes Secret named
     `triage-suggestion-service-llm-key-encryption`. Mount
     the secret as files using `volumes.secrets`. The service
     reads each value through `*_FILE` environment variables.
     For example:

     ```
     auth_key_file=/etc/triage-suggestion-service/secrets/auth-key
     jwt_secret_file=/etc/triage-suggestion-service/secrets/jwt-secret
     jwt_encryption_key_file=/etc/triage-suggestion-service/secrets/jwt-encryption-key
     auth_hmac_secret_file=/etc/triage-suggestion-service/secrets/auth-hmac-secret
     ```

     Secrets
     are not exposed as pod environment variables.
   - Docker: Pass the values as environment variables using `docker
     run -e` flags or an `.env` file:

     ```
     docker run -e jwt_secret=<value> \
                -e jwt_encryption_key=<value> \
                -e auth_key=<value> \
                -e auth_hmac_secret=<value> \
                ...
     ```
   - Bare binary (standalone): Set the values as environment variables or add
     them to your configuration file (JSON or YAML).
4. Copy the `auth_key` to Coverity Cloud.

   Configure the same `auth_key` value on the Connect side.

   | Deployment | Where to configure |
   | --- | --- |
   | Helm / Kubernetes | Coverity Cloud properties or Kubernetes Secret |
   | Docker | Coverity Cloud container environment variables |
   | Bare binary | Coverity Cloud configuration file |

   Tip: For Helm/K8s deployments, never expose
   secrets as plain-text pod environment variables, always use mounted files
   with *_FILE env vars.

   CAUTION:

   The `auth_key` value must be exactly the
   same on both the triage service and Connect. A mismatch will cause
   authentication failures on `POST /auth`.
5. Configure the following properties in Coverity Cloud:

   ```
   encryption.public.key.file=<path_to_public_key_file>
   ai.triage.suggestion.service.auth.key=<auth_key>
   show.modern.ui.preview.button=true
   ai.triage.suggestion.service.url=<triage-service-url>
   ```
6. Verify the configuration.
   1. Restart both the triage-suggestion-service and Coverity Cloud.
   2. Send a test request to the triage service's `POST /auth`
      endpoint.
   3. Confirm the response returns `HTTP 200`. A 401 or 403
      response indicates an `auth_key` mismatch.

Rotate secrets periodically by generating new values and redeploying both services
simultaneously. To rotate the
secrets:

```
kubectl create secret generic triage-suggestion-service-secrets \
  --namespace=<your-namespace> \
  --from-literal=jwt-secret=$(openssl rand -base64 32) \
  --from-literal=jwt-encryption-key=$(openssl rand -base64 32) \
  --from-literal=auth-key=$(openssl rand -base64 32) \
  --from-literal=auth-hmac-secret=$(openssl rand -base64 32) \
  --dry-run=client -o yaml | kubectl apply -f -

kubectl rollout restart deployment/triage-suggestion-service-api \
  deployment/triage-suggestion-service-worker \
  --namespace=<your-namespace>
```
