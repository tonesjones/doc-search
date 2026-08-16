---
title: "AWS: Downloading certificates and creating a truststore ConfigMap"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-downloading-certificates-and-creating-a-truststore-configmap.html"
content_id: "Sfx8IEJUe~TwdLHfThZFSQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:11.547801+00:00"
---

# AWS: Downloading certificates and creating a truststore ConfigMap

In an Amazon AWS cloud deployment of a Coverity cluster, to support SSL, you can provide
a regional AWS certificate bundle and create a ConfigMap containing the public
certificates.

If you are deploying a Coverity cluster in the AWS cloud and if you are using a
certificate bundle for a specific Amazon region, this procedure describes how to
download regional AWS certificates and create a truststore ConfigMap. Completing this
procedure enables SSL/TLS in this environment. This procedure assumes that you are:

- deploying Coverity Connect in a cluster within the AWS cloud.
- Using a certificate bundle for a specific Amazon region.

To download a regional AWS certificate bundle and create a ConfigMap:

1. Download the bundled certificate, which contains the chain of public key
   certificates, based on the AWS region where the Kubernetes Coverity instance
   will be deployed. Refer to [Certificate bundles for specific AWS
   regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.RegionCertificates).

   Note: Ensure that you keep the downloaded bundled PEM
   certificate in its original format; do not make any changes to it.
2. From the bundled `.pem` certificate file, create a separate
   `.pem` file for each certificate within the bundle.

   Copy each certificate from `-----BEGIN CERTIFICATE-----` through
   `-----END CERTIFICATE-----` into its own file. For example,
   from a bundle named `postgres-root.pem` and containing five
   certificates, you might create the following individual certificate files:

   - `postgres-root-1.pem`
   - `postgres-root-2.pem`
   - `postgres-root-3.pem`
   - `postgres-root-4.pem`
   - `postgres-root-5.pem`
3. Using the `kubectl` command, create a truststore ConfigMap, adding
   the bundled .pem certificate file plus all of the individual .pem certificate
   files. For example:

   ```
   kubectl create configmap "${TruststoreConfigmapName}" \
     --from-file=postgres-root.pem=<certificate-bundle>.pem \
     --from-file=postgres-root-1.pem=<certificate-1>.pem \
     --from-file=postgres-root-2.pem=<certificate-2>.pem \
     --from-file=postgres-root-3.pem=<certificate-3>.pem \
     .
     .
     --from-file=postgres-root-x.pem=<certificate-x> \
     -n "${CNC_NS}"
   ```

   where:

   - `"${TruststoreConfigmapName}"` is the name of the
     Truststore Configmap that you are creating. The default name in the Helm
     `values.yaml` file is
     `connect-trust-stores`. If you use another name, you
     will need to update the `trust-stores.configmapName` Helm
     key
   - `<bundled-certificate>` is the file path of the
     original bundled PEM certificate file.
   - `<certificate-1>` ,`<certificate-2>`
     ,…,`<certificate-x>` is each individual
     certificate file, including the path if needed.

   Note: All public key certificates that go into the truststore
   ConfigMap must be in PEM format.

   For example:

   ```
   kubectl create configmap "connect-trust-stores" \
     --from-file=postgres-root.pem=bundle.pem \
     --from-file=postgres-root-1.pem=cert1.pem \
     --from-file=postgres-root-2.pem=cert2.pem \
     --from-file=postgres-root-3.pem=cert3.pem \
     --from-file=postgres-root-4.pem=cert4.pem \
     --from-file=postgres-root-5.pem=cert5.pem \
     -n "cnc"
   ```
