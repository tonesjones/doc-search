---
title: "Install an ingress controller"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/install-an-ingress-controller.html"
content_id: "nzcNmCzYx4CeLDbg95mKUQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:53.657087+00:00"
---

# Install an ingress controller

In all Kubernetes deployments, you need an ingress controller to allow external traffic
to enter the Kubernetes cluster. Black Duck has tested the
NGINX ingress controller which is available on dockerhub at <https://hub.docker.com/_/nginx>. However, you
can use any of a number of other ingress controllers, including those hosted by cloud
providers. The ingress controller facilitates communication between local Coverity
clients and the Coverity server located in the Kubernetes cluster.

For information on working with an ingress controller, see also [Ingress Controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) .

Important: For information on an ingress controller in Red
Hat OpenShift, see .

Important: If you are using a Kubernetes/ingress-nginx
controller ([kubernetes/ingress-nginx](https://github.com/kubernetes/ingress-nginx)), be aware of the following
security issue: [CVE-2025-1974: ingress-nginx admission controller RCE
escalation #131009](https://github.com/kubernetes/kubernetes/issues/131009).

Depending on the selected ingress controller, you might need to override Helm chart
properties in the `values.yaml` file for the ingress controller. For more
information, see Configure NGINX ingress-class controllers or the gateway API.

Also, secure the ingress using a secret that contains a TLS private key and certificate.
You will need to provide the TLS certificate information. Make sure that the TLS
certificate contains a Common Name (CN), also known as a Fully Qualified Domain Name
(FQDN).

For cloud provider ingress information, see:

- For Amazon AWS: AWS: Install an ingress controller
- For Google GCP: GCP: Install an ingress controller
- For Microsoft Azure: Azure: Install an ingress controller
- For Red Hat OpenShift: OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster

## Connect and ingress management considerations

- We recommend various limits that provide good Connect and PostgreSQL database
  performance. For information on the recommended maximum limits in Coverity
  Connect, see the section Recommended maximum limits in Coverity
  Connect in the document Coverity 2026.6.0 Installation and Upgrade Guide. The stated limits are recommended or soft
  limits. You can exceed these limits, however performance will degrade as you
  exceed these limits.
- If the Coverity cloud deployment uses NGINX for ingress, and if Coverity
  Connect Web users who request 'Users and Groups' data begin to experience
  [504
  Gateway Timeout](https://http.dev/504) errors, Refer to the Troubleshooting section,
  NGINX HTTP error 504: Gateway Timeout.
- For Red Hat OpenShift routing: OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster
