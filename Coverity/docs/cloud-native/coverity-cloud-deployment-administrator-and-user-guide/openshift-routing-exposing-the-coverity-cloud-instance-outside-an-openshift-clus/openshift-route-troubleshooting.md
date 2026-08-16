---
title: "OpenShift route troubleshooting"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/openshift-route-troubleshooting.html"
content_id: "vzeQ~vWdL0PXxLl2z6nIWA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:56.515407+00:00"
---

# OpenShift route troubleshooting

## OpenShift route was not created

**Issue**: The route resource does not appear in OpenShift.

**Solution**:

1. Verify OpenShift cluster: `oc api-versions | grep
   route.openshift.io`
2. Check route enabled: `cim.route.enabled: true`
3. Verify CIM service enabled: `cim.cimweb.enabled: true`
4. Check central services disabled: `central-services.enabled:
   false`

## OpenShift route was created without TLS certificates

**Issue**: Route created without TLS certificates

**Solutions**:

1. Verify that the TLS secret exists: `oc get secret
   <secret-name>`
2. Check the format of the secret and ensure that it contains
   `tls.crt` and `tls.key`.
3. Validate that the certificates use base64 encoding. Certificates must be base64
   encoded.
4. Review inheritance: Make sure that TLS is configured for ingress and route.

## The route uses an incorrect hostname

**Issue**: Host name resolution

**Solutions**:

1. Check inheritance order: route → service ingress → global ingress.
2. Verify ingress configuration: Ensure hosts array is properly configured.
3. Override explicitly: Set `cim.route.hosts` to force specific
   hostname.
