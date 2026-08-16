---
title: "Verification"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/verification.html"
content_id: "JeEvxtCfk_JlOv2G6M4gXw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:47.597843+00:00"
---

# Verification

**Check all Gateway API
resources**

```
# Gateway status (look for Programmed: True)
kubectl get gateway <release>-gateway -n <namespace> -o wide

# HTTPRoutes (look for Accepted: True, ResolvedRefs: True)
kubectl get httproute -n <namespace>

# Describe for detailed status
kubectl describe httproute <release>-cim -n <namespace>
kubectl describe httproute <release>-http-redirect -n <namespace>
kubectl describe httproute <release>-commit-server -n <namespace>
```

**Check IP allowlisting
resources**

```
# Per-route SnippetsFilter
kubectl get snippetsfilter <release>-cim-ip-allowlist -n <namespace>

# Gateway-level SnippetsPolicy
kubectl get snippetspolicy <release>-gateway-ip-allowlist -n <namespace>
```

**Check ClientSettingsPolicy (if maxSize is
set)**

```
kubectl get clientsettingspolicy <release>-client-settings -n <namespace>
```

**Check HealthCheckPolicy (GKE
only)**

```
kubectl get healthcheckpolicy -n <namespace>
# Both <release>-cim-healthcheck and <release>-commit-server-healthcheck should show Attached: True
kubectl describe healthcheckpolicy <release>-cim-healthcheck -n <namespace>
kubectl describe healthcheckpolicy <release>-commit-server-healthcheck -n <namespace>
```

**End-to-end tests**

```
# HTTPS — expect 200
curl -sk -o /dev/null -w "HTTPS: %{http_code}\n" https://coverity.example.com/login/login.htm

# HTTP redirect — expect 301
curl -sk -o /dev/null -w "HTTP: %{http_code} → %{redirect_url}\n" http://coverity.example.com/

# Blocked IP test (run from an IP not in allowedSourceRanges) — expect 403
curl -sk -o /dev/null -w "Blocked: %{http_code}\n" https://coverity.example.com/
```
