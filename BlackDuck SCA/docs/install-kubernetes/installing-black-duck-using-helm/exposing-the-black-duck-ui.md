---
title: "Exposing the Black Duck UI"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/exposing-the-black-duck-ui.html"
content_id: "fF4xf0_ap4XASx2W5hEdlQ"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:01.400883+00:00"
---

# Exposing the Black Duck UI

The Black Duck User Interface (UI) can be accessed via several
methods, described below.

## NodePort

`NodePort` is the default service type set in the values.yaml. If you
want to use a custom NodePort, set the following parameters in values.yaml to the
desired port:

```
# Expose Black Duck's User Interface
exposeui: true
# possible values are NodePort, LoadBalancer or OpenShift (in case of routes)
exposedServiceType: NodePort
# custom port to expose the NodePort service on
exposedNodePort: "<NODE_PORT_TO_BE_USED>"
```

You can access the Black Duck UI via
`https://${NODE_IP}:${NODE_PORT}`.

## Load balancer

Setting the `exposedServiceType` to LoadBalancer in the values.yaml,
will instruct Kubernetes to deploy an external Load Balancer service. You can use
the following command to get the external IP address of the Black Duck web
server:

```
$ kubectl get services ${BD_NAME}-blackduck-webserver-exposed -n ${BD_NAME}
```

If the external IP address is shown as pending, wait for a minute and enter the same
command again.

You can access the Black Duck UI by https://${EXTERNAL_IP}.

## Ingress

This is typically the most common method of exposing the application to users.
Firstly, set `exposeui` in the values.yaml to `false`
since the ingress will route to the service.

```
# Expose Black Duck's User Interface
exposeui: false
```

A typical ingress manifest would be representative of the example below. Note, the
configuration of the ingress controller and TLS certificates themselves are outside
of the scope of this guide.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ${BD_NAME}-blackduck-webserver-exposed
  namespace: ${BD_NAME}
spec:
  rules:
  - host: blackduck.foo.org
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: ${BD_NAME}-blackduck-webserver
            port:
              number: 443
  ingressClassName: nginx
```

Once deployed, the UI will be available on port 443 on the Public IP of your ingress
controller.

## OpenShift

Setting the `exposedServiceType` to OpenShift in the values.yaml, will
instruct OpenShift to deploy route service.

```
# Expose Black Duck's User Interface
exposeui: true
# possible values are NodePort, LoadBalancer or OpenShift (in case of routes)
exposedServiceType: OpenShift
```

You can use the following command to get the OpenShift routes:

```
$ oc get routes ${BD_NAME}-blackduck -n ${BD_NAME}
```

You can access the Black Duck UI by
`https://${ROUTE_HOST}`.
