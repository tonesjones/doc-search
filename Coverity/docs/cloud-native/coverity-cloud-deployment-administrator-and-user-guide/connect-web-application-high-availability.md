---
title: "Connect Web application high availability"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/connect-web-application-high-availability.html"
content_id: "Ydjc9JHZ5ufN57MQ2r54GA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:24.209959+00:00"
---

# Connect Web application high availability

You can allow Kubernetes to automatically distribute pods within available nodes or
optionally, you can use affinities, anti-affinities, and other Kubernetes tools to
distribute pods on specific nodes. The number of pods deployed is determined by a
`replicas` Helm parameter.

The following figure llustrates a Coverity Connect deployment with two
`cimweb` replicas and two `commit-server` replicas
within a single Web application node. With `cim.cimweb.replicas: 2` and
`cim.commit-server.replicas: 2`, the Kubernetes controller maintains
two pods for each service.

Figure 1. Sample Connect web application HA
[image: image]

Here are a few HA points:

- To support demand, a horizontally scaled application can deploy multiple
  instances of an application as multiple pods, as opposed to a vertically
  scalable application which deploys and expands a single large pod to service
  requests.
- When deploying multiple replicas, the node must possess adequate CPU and memory
  resources to support the replicas and any other containers that will run within
  the node.
- You can horizontally scale the number of pods up and down for high availability
  and/or high throughput.
- For any service, the Kubernetes controller keeps track of the desired number of
  pods that should be available for the service, and the ingress-controller
  (load-balancer) takes care of forwarding the requests to the desired
  service.
