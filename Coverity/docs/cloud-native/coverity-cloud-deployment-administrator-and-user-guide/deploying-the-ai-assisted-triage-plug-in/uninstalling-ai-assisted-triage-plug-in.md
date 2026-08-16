---
title: "Uninstalling AI-Assisted Triage Plug-in"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/uninstalling-ai-assisted-triage-plug-in.html"
content_id: "hzlx0bJWILf9clTr8UGxUg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:33.282844+00:00"
---

# Uninstalling AI-Assisted Triage Plug-in

This topic describes the steps to uninstall AI-Assisted Triage Plug-in from your
environment.

**To uninstall a distributed deployment of the triage suggested
service**:

1. In Coverity Connect, clear the configured LLM key for each project, and the
   global key if set, to stop Connect from issuing triage requests: 

   - `PUT /config/projects/llmKey` with an empty value
   - `PUT /config/system/ai/globalLlmKey` with an empty
     value
2. Disable the triage suggestion service in your values overrides file:

   ```
   triage-suggestion-service:
   enabled: false
   ```
3. Apply the updated values using Helm. This removes the triage subchart pods and
   services, along with triage-related `cim.properties` entries,
   environment variables, and volume mounts on the cimweb pod, while keeping the
   rest of Coverity Connect operational: `helm upgrade <release>
   <chart> -n <namespace> -f <your-values.yaml>`.
4. Delete any Secrets created outside the installation process that are no longer
   referenced after the `triage-suggestion-service:enabled` is set
   to `false`. For more information, see Configuring authentication secrets and Generating a key pair:

   - `kubectl delete secret triage-suggestion-service-secrets
     triage-suggestion-service-llm-key-encryption -n
     <namespace>`
5. Verify and delete PVCs owned by the triage subchart:

   - `kubectl get pvc -n <namespace> -l
     app.kubernetes.io/name=triage-suggestion-service`
   - `kubectl delete pvc -n <namespace> -l
     app.kubernetes.io/name=triage-suggestion-service`
6. (Optional) Delete the local PEM files generated, such as
   `./private.pem` and .`/public.pem` from the
   workstation where you ran `kubectl create secret
   --from-file=...`. For more information, see Generating a key pair.

   Note: The Secret deleted in step 9 is created from these
   files. However, the local copies are not removed automatically.
