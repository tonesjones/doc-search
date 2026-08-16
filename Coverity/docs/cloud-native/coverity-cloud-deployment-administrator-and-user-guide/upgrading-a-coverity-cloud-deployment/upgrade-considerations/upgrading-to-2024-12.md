---
title: "Upgrading to 2024.12"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-to-2024.12.html"
content_id: "xC6GVhshcdJmp3ST8eAMOg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:35.492579+00:00"
---

# Upgrading to 2024.12

The 2024.12 release introduces the following changes that can impact the upgrade
process:

- The 2024.12.0 release adds a Helm chart validation function that verifies all
  required minimum Helm values are set. This makes sure that the Helm chart
  satisfies minimum Helm key value requirements. If a value is missing, an error
  message is returned to the commmand line and logged, indicating the Helm key
  value that must be set. This will help you verify that required Helm values are
  set before proceeding to install the chart. See Helm chart validation and error logging​.
- The 2024.12.0 release improves error logging to help debug and fix a
  deployment​.
- The 2024.12.0 release enables you to more easily set up TLS forward proxy for
  secure communication between scan services and the internet. This includes new
  proxy Helm keys. See Configuring TLS forward proxy.
- The 2024.12.0 release enforces new Connect Web application administator password
  requirements. For these password requirements, see Connect Web application administator password requirements.

  Note: When you upgrade to 2024.12.0 or newer from an older
  release, you will still be able to use your non-compliant password. However,
  once you change the password, you must comply with the password requirements
  from then on. Changing the password triggers the compliance mechanism.
- The 2024.12.0 release updates MinIO support and configuration, adding new MinIO Helm
  keys with default key values. See Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service.
- The 2024.12.0 release updates Redis support and configuration, adding new Redis Helm
  keys with default key values. See Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service.
- The 2024.12.0 release supports a Beta release of the new Read Replica database
  feature for customers who join the Beta test program. This is for test
  deployments only; do NOT use in a production deployment.
- Reminder: If you are upgrading from 2024.9.0 or older, you must consider the
  following:
  - Black Duck Coverity supports a new
    registry/repository that has public and private folders for container
    images, tool files, Helm chart, and other files. See About Black Duck repositories.
  - All repository data has been migrated to the new Black Duck repository, [repo.blackduck.com](http://repo.blackduck.com/) at 34.149.5.115. Make sure that you point to
    and use data from the public and private repository folders within this new
    repository. See About Black Duck repositories.

    Note: The repository [sig-repo.synopsys.com](http://sig-repo.synopsys.com/) at IP address 34.110.245.127 does NOT
    support 2024.9.1 or newer. Also, this repository will become unavailable
    on February 14, 2025.
  - If you use IP Whitelist to access [repo.blackduck.com](http://repo.blackduck.com/), add the
    following IP address to the IP whitelist: 34.149.5.115. See About Black Duck repositories.
  - Change all registry URLs from the Synopsys SIG repositories to Black Duck
    repositories. The Synopsys SIG repository will redirect requests to the
    Black Duck repository through February 14, 2025.
  - If you use any internal scripts that link to the Synopsys SIG
    registries/repositories, you need to redirect the links to the new Black
    Duck repositories identified in About Black Duck repositories.
  - As recommended, copy all container images from the new Black Duck repository
    to a local repository and use your local repository to deploy Coverity
    cloud. To create your own private Coverity cloud repository, see Create your own private Docker registry.
  - If upgrading to 2024.12.0, you must obtain and deploy the new 2024.12.0
    Helm chart. See Downloading the Helm chart from the Black Duck public Docker registry.

The following table identifies Helm keys added in the 2024.12.0 release.

Table 1. Helm keys added in 2024.12.0

| Helm key | Refer to | Notes |
| --- | --- | --- |
| ``` global:   proxy:      enabled: false     host: ""     port: 3128     tlsmode: "tls"     existingSecret: "" ``` | `cnc` chart or `scan-services` subchart. See:   - To configure TLS forward proxy, see Configuring TLS forward proxy - To define global TLS forward proxy keys, see cnc_global_chart_values.html#cnc_global_chart_values__section_uwy_ftp_jdc | Use these global keys or the `scan-services` subchart keys to set up TLS proxy. |
| ``` proxy:    enabled: false   host: ""   port: 3128   tlsmode: "tls"   existingSecret: "" ``` | `scan-services` subchart. See:   - To configure TLS forward proxy, see Configuring TLS forward proxy - To define chart-level TLS forward proxy keys, see proxy Helm keys | Use these keys or the global keys to set up TLS proxy. |
| ``` onPrem:   redis: false   minio: false ``` | `cnc` chart. Enable onPrem OCI Redis and MinIO. See:   - Enabling OCI Redis, MinIO, and PostgreSQL | Use these keys to enable onPrem OCI Redis or MinIO. |
| ``` # minio: #   onPrem: true #   fullnameOverride: "cnc-minio"  #   image: #     debug: true  #   apiIngress: #     enabled: true #     ingressClassName: nginx #     hostname: local.connect.example.com #     extraTls: #       - hosts: #           - local.connect.example.com #         secretName: cnc-cim-tls-nginx #     path: "/upload(/|$)(.*)" #     annotations: #       ingress.kubernetes.io/hsts: "true" #       ingress.kubernetes.io/ssl-redirect: "true" #       nginx.ingress.kubernetes.io/enable-access-log: "true" #       nginx.ingress.kubernetes.io/proxy-body-size: 8g #       nginx.ingress.kubernetes.io/proxy-connect-timeout: "5" #       nginx.ingress.kubernetes.io/proxy-next-upstream: error timeout #       nginx.ingress.kubernetes.io/proxy-next-upstream-timeout: "0" #       nginx.ingress.kubernetes.io/proxy-next-upstream-tries: "3" #       nginx.ingress.kubernetes.io/rewrite-target: /$2  #   podAnnotations: #     prometheus.io/scrape: "true" #     prometheus.io/path: "/minio/v2/metrics/cluster" #     prometheus.io/port: "9000" #   persistence: #     size: 50Gi  #   sidecars: #     - name: minio-lifecycle #       image: docker.io/minio/mc:latest #       imagePullPolicy: IfNotPresent #       env: #         - name: cache_bucket_name #           value: coverity-cache #         - name: cache-retention-limit #           value: "30" #         - name: minio-host #           value: cnc-minio #         - name: minio-port #           value: "9000" #         - name: minio-access-key #           valueFrom: #             secretKeyRef: #               name: cnc-minio #               key: root-user #         - name: minio-secret-key #           valueFrom: #             secretKeyRef: #               name: cnc-minio #               key: root-password #   command: ["/bin/bash","-c"] #   args: #     - | #       echo "waiting for minio..."  #       until (mc alias set cnc http://$(minio-host):$(minio-port)            $(minio-access-key) $(minio-secret-key) && mc ls cnc/$(CACHE_BUCKET_NAME)) #       do sleep 5; #       done; #       mc ilm add --expiry-days $(cache-retention-limit) cnc/$(cache_bucket_name); #       tail -f /dev/null; ``` | `cnc` chart. Set up minio cache management. See:   - `cnc` chart. Enable onPrem OCI MinIO.   See:    - Deploy Connect and Scan Service with onPrem OCI Redis and MinIO   - Enabling OCI Redis, MinIO, and PostgreSQL   - Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service | To deploy onPrem OCI MinIO, set `onPrem.minio: true` and uncomment the `minio:` Helm keys. |
| ``` # redis: #   fullnameOverride: "cache-redis" #   architecture: standalone #   metrics: #     enabled: true #   master: #     persistence: #       enabled: false #     resources: #       limits: #         cpu: "0.5" #         memory: 1.1Gi #       requests: #         cpu: "0.5" #         memory: 1.1Gi #   tls: #     enabled: true #     autoGenerated: true #     certFilename: "certificate.pem" #     certKeyFilename: "key.pem" #     certCAFilename: "ca.crt" #     authClients: false #   commonConfiguration: |- #     save "" #     appendonly no #     maxmemory 1gb #     maxmemory-policy noeviction ``` | `cnc` chart. Set up Redis storage management. See:   - `cnc` chart. Enable onPrem OCI Redis. See:    - Deploy Connect and Scan Service with onPrem OCI Redis and MinIO   - Enabling OCI Redis, MinIO, and PostgreSQL   - Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service | To deploy onPrem OCI Redis, set `onPrem.redis: true` and uncomment the `redis:` Helm keys. |
| ``` cim:   pgpool: ``` | `cnc` chart.   - cim.pgpool Helm keys - PostgreSQL read replicas | `cim.pgpool` contains many keys that will be available in a future release to deploy multiple PostgreSQL database read replicas. These Helm keys are Beta and are supported in a non-production environment only and only for customers who join the Beta test program.  Important: Beta customer use only. |
| ``` cim:   serviceAnnotations: ``` |  | Additional annotations to add to the `cim/commit-server` service metadata. This is a dictionary. |
| ``` global:   licenseSecretName: ``` | Added reference to Keygen and `license.json`: Do NOT use Keygen. | Important: Keygen is for Black Duck internal use only. Do NOT use Keygen. |
| ``` global:   keygen:     enabled: false ``` |  | Important: Black Duck internal use only. Do NOT enable. |

The following table identifies Helm key default values changed in the 2024.12.0
release.

Table 2. Helm key default values changed in 2024.12.0

| Helm key | Default value change | Notes |
| --- | --- | --- |
| ``` cim.postgres.database ``` | From `""` to `"cim"` | `cnc` chart. |

Table 3. `Chart.yaml` file new MinIO and Redis dependencies in
2024.12.0

| Dependencies | Notes |
| --- | --- |
| ``` dependencies:     - name: minio     condition: onPrem.minio     version: "14.8.5"     repository: oci://registry-1.docker.io/bitnamicharts ``` | `cnc` chart.  Added to support onPrem OCI MinIO,  Refer to: Redis and MinIO dependencies in cnc/Chart.yaml​ |
| Old obsolete bitnami repository - Do not use:   ``` dependencies:   - name: redis     version: "20.3.0"     condition: onPrem.redis     repository: oci://registry-1.docker.io/bitnamicharts ``` | `cnc` chart.  Added to support onPrem OCI Redis,  Refer to: Redis and MinIO dependencies in cnc/Chart.yaml​ |
