---
title: "IP allowlisting"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ip-allowlisting.html"
content_id: "5EnjuDxmns9KXAhoVFkt_w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:38.781582+00:00"
---

# IP allowlisting

Two modes are available. Both require NGINX Gateway Fabric installed with:

```
--set nginxGateway.snippets.enable=true
```

**Per-route allowlist (`allowedSourceRanges`**)

Applies IP restrictions to the CIM and commit-server HTTPRoute rules individually using a
`SnippetsFilter` resource. Use this when you need fine-grained
control per route.

```
cim:
  gateway:
    allowedSourceRanges:
      - "10.0.0.0/8"
      - "192.168.1.0/24"
      - "203.0.113.50/32"
```

The following is created:

- `SnippetsFilter` named `<release>-cim-ip-allowlist`
  with `allow` or `deny all` NGINX directives. nginx
  directives
- `ExtensionRef` filter added to every rule in the CIM HTTPRoute
- `ExtensionRef` filter added to every rule in the commit-server
  HTTPRoute

Any source IP not in the list receives a **403 Forbidden**.

**Gateway-level allowlist (`gatewayAllowedSourceRanges`**)

Applies IP restrictions at the Gateway level using a `SnippetsPolicy` that
targets the Gateway resource. All routes attached to the Gateway are automatically
covered — no per-route configuration needed. Recommended for dev clusters or when one
policy should cover everything.

```
cim:
  gateway:
    gatewayAllowedSourceRanges:
      - "10.0.0.0/8"
```

The following is created:

- `SnippetsPolicy` named
  `<release>-gateway-ip-allowlist` targeting the Gateway
  (`spec.targetRefs`)
- No changes to HTTPRoute resources

Any source IP not in the list receives a **403 Forbidden** on all routes.

**Comparison**

Both can be set simultaneously if needed — the gateway-level policy applies at server
level and the per-route filter applies at location level.

| `allowedSourceRanges` | `gatewayAllowedSourceRanges` | Notes |
| --- | --- | --- |
| Scope | Per HTTPRoute rule | Entire Gateway (all routes) |
| Resource created | `SnippetsFilter` | `SnippetsPolicy` |
| HTTPRoute changes | Adds `ExtensionRef` to each rule | None |
| nginx context | `http.server.location` | `http.server` |
| Best for | Production fine-grained control | Dev clusters, all-or-nothing access |
