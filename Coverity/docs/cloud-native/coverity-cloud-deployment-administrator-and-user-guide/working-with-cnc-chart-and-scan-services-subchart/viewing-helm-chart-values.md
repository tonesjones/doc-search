---
title: "Viewing Helm chart values"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/viewing-helm-chart-values.html"
content_id: "XqYn3PWjQh9O2~g0mP2sOA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:18.166425+00:00"
---

# Viewing Helm chart values

You can view the Helm chart values in the values.yaml file using one of the following
methods or your preferred method:

- Open the file in an IDE (integrated development environment) such as Xcode.
- Open the file in a text editor such as vi or vim.
- Use the `cat values.yaml` command.
- Use the `helm show values [CHART] [flags]` command. See <https://helm.sh/docs/helm/helm_show_values/>. For
  example, the `cnc` Helm chart:

  ```
  % helm show values cnc

  # see https://helm.sh/docs/chart_template_guide/subcharts_and_globals/#global-chart-values
  # Global values are values that can be accessed from any chart or subchart by exactly the same name
  # these values are commonly applied for both main chart and its sub-charts if any.
  global:
    # See https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy.
    # This is set on each CNC and scan-services pod to control its image pull policy.
    # Allowed values: Always, IfNotPresent, Never.
    imagePullPolicy: IfNotPresent

    # See https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod.
    # This must be set if the images are pulled from a repository requiring authentication; the value
    # must be the name of a secret in the same namespace.
    imagePullSecret: ""
  ...

    postgres:
      host: ""
      password: ""
      port: 5432
      # This has to be one of the values: ""/disable/allow/prefer/require/verify-ca/verify-full
      sslmode: "verify-ca"
      user: ""
      # the existing k8s secret name with keys: `host`, `port`, `username`, `password`
      existingSecret: ""
      # The container spec to attach as a sidecar for the pods which requires DB connection
      #   it will be added as a native sidecar which is nothing but an init container with restartPolicy:Alway
      #   so if this container wants to add as a sidecar please use restartPolicy:Always in the spec
      #   require kubernetes 1.28 to use native-sidecar
      #   see https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/
      sidecars: []

      # The container spec to attach as a sidecar for the jobs which requires DB connection
      #   it will be added as a native sidecar which is nothing but an init container with restartPolicy:Alway
      #   so if this container wants to add as a sidecar please use restartPolicy:Always in the spec
      #   require kubernetes 1.28 to use native-sidecar
      #   see https://kubernetes.io/blog/2023/08/25/native-sidecar-container
      jobSidecars: []

    # Redis related variables needed by the serverworker,storageproxy and cache-service(if enabled)
    redis:
      # Enable authentication for Redis. In case set to true, password secret also need to be provided
      authEnabled: false

      # Secret containing CA cert to be used for Redis Communication in case TLS enabled
      # This secret must contain follwing key
      # - ca.crt
      cacertSecret: ""

      # Redis Host
      host: ""

      # Secret containing Redis password (must contain a key named `password`) considering Redis is secured with password
      passwordSecret: ""

      # Redis Port
      port: 6379

      # If TLS enabled for communication with Redis
      secure: true

      # If Host name need to be verified for Redis communication in case TLS enabled
      verifyHostName: false

    trust-stores:
  ...

  # See https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy.
  # This is set on each CNC pod to control its image pull policy.
  # Allowed values: Always, IfNotPresent, Never.
  imagePullPolicy: IfNotPresent

  # See https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod.
  # This must be set if the images are pulled from a repository requiring authentication; the value
  # must be the name of a secret in the same namespace.
  imagePullSecret: ""
  ...

  cim:

    # sets the pod security context
    podSecurityContext: {}

    # sets the affinity on the Connect deployment
    affinity: {}

    # sets the node selector on the Connect deployment
    nodeSelector: {}

    # sets the tolerations on the Connect deployment
    tolerations: []

    # This is used to provide static files for downloads from the Connect UI.
    # It is implemented via init containers in the cim-webapp pod and includes:
    # - client-side binaries
    # - documentation
    cimdownloads:

      # if true, the init container is enabled; otherwise, it is not enabled
      enabled: true

      # The image name to use
      image: "cim-downloads"

      # The image registry to use
      registry: ""

      # The image version to use
      version: "CIM_VERSION"

    # This creates a k8s statefulset which provides administrator functionality:
    # - cov-archive
    # - reset-admin-password (cov-admin-db)
    # The statefulset is initially set to replica count 0; it must first be scaled
    # up to create a pod before use.
    cimtools:

      # if true, the statefulset is created; otherwise, it is not
      enabled: true
  ...
  ```

  Or for example, the `scan-services` Helm
  subchart:

  ```
  % helm show values scan-services

  # see https://helm.sh/docs/chart_template_guide/subcharts_and_globals/#global-chart-values
  # Global values are values that can be accessed from any chart or subchart by exactly the same name
  # these values are commonly applied for both main chart and its sub-charts if any.
  global:
    # See https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy.
    # This is set on each CNC and scan-services pod to control its image pull policy.
    # Allowed values: Always, IfNotPresent, Never.
    imagePullPolicy: IfNotPresent

    # See https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod.
    # This must be set if the images are pulled from a repository requiring authentication; the value
    # must be the name of a secret in the same namespace.
    imagePullSecret: ""
  ...
    postgres:
      host: ""
      password: ""
      port: 5432
      # This has to be one of the values: ""/disable/allow/prefer/require/verify-ca/verify-full
      sslmode: "verify-ca"
      user: ""
      # the existing k8s secret name with keys: `host`, `port`, `username`, `password`
      existingSecret: ""
      # The container spec to attach as a sidecar for the pods which requires DB connection
      #   it will be added as a native sidecar which is nothing but an init container with restartPolicy:Alway
      #   so if this container wants to add as a sidecar please use restartPolicy:Always in the spec
      #   require kubernetes 1.28 to use native-sidecar
      #   see https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/
      sidecars: []

      # The container spec to attach as a sidecar for the jobs which requires DB connection
      #   it will be added as a native sidecar which is nothing but an init container with restartPolicy:Alway
      #   so if this container wants to add as a sidecar please use restartPolicy:Always in the spec
      #   require kubernetes 1.28 to use native-sidecar
      #   see https://kubernetes.io/blog/2023/08/25/native-sidecar-container
      jobSidecars: []

    # Redis related variables needed by the serverworker,storageproxy and cache-service(if enabled)
    redis:
      # Enable authentication for Redis. In case set to true, password secret also need to be provided
      authEnabled: false

      # Secret containing CA cert to be used for Redis Communication in case TLS enabled
      # This secret must contain follwing key
      # - ca.crt
      cacertSecret: ""
  ...
    trust-stores:
  ...
  # See https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy.
  # This is set on each SCANFARM pod to control its image pull policy.
  # Allowed values: Always, IfNotPresent, Never.
  imagePullPolicy: IfNotPresent

  # See https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod.
  # This must be set if the images are pulled from a repository requiring authentication; the value
  # must be the name of a secret in the same namespace.
  imagePullSecret: ""
  ...
  ingress:

    # additional annotations to provide to the ingress object
    annotations: {}

    # value for "kubernetes.io/ingress.class" annotation key
    class: "nginx"

  ...

  # Cache service provides analysis caching capabilities
  cache-service:

    # name of the Bucket used by cache service.  NB: this is called
    #   something different in Azure: it's the "blob container" name within the storage account.
    #   whereas AWS, MinIO, GCP call it a bucket name
    bucketName: ""

    # if true, cache service is enabled for capture and analysis;
    #   if false, capture and analysis will run without caching
    enabled: true
  ...
  # This performs setup tasks related to certificates and configuration.
  common-infra:

    # schedule to use for cleanup cronjob.  must be a valid schedule for a k8s cronjob
    cleanupSchedule: "*/5 * * * *"

    # The image name to use
    image: "common-infra"
  ...
  # scan-service creates a k8s deployment which manages scans: scheduling, failures, resources, retries.
  scan-service:

    # additional annotations to add to the deployment metadata.  This is a dictionary
    annotations: {}

    # additional volumes to add to the scan-service pod
    extraVolumes: []

    # init containers to inject into the scan-service pod
    initContainers: []
  ...
  ```

Note: When editing a yaml file to provide new Helm key values:

- Always enclose string values in quotes to avoid type conversion errors.
- Most of the default values in the `values .yaml` file do not need to be
  changed.

For Helm key information, see Helm keys for a Coverity cloud deployment.

Here are a few ways you might manage the Helm charts and their key:value pairs:

- Copy each of the `cnc` chart and `scan-services` chart
  `values.yaml` file to new `[filename].yaml` files and
  change values as needed for your deployment. Then you can run a `helm
  install` command specifying your new yaml file(s). For example, to use overrides
  in two files `mycncvalues.yaml` and `myscanvalues.yaml`:

  ```
  helm install cnc -f mycncvalues.yaml -f myscanvalues.yaml
  ```
- Create a new `yaml` file that contains overrides as needed for both the
  `cnc` and `scan-services` charts. Then you can run a
  `helm install` command specifying your new yaml file. For example, to use
  overrides in `myvalues.yaml`:

  ```
  helm install cnc -f myvalues.yaml
  ```
- Create yaml values files specific to features, for example `ha.yaml` which
  contains keys for Coverity Connect web app high availability, or `pg.yaml`
  which contains PostgreSQL Helm keys. You would then include both files as well as the
  `values.yaml` file in the `helm install` command. For
  example:

  ```
  helm install cnc -f values.yaml -f ha.yaml -f pg.yaml
  ```

  The values in `ha.yaml` and `pg.yaml` override those in
  `values.yaml.`
- Override specific values within the `helm install` or `helm
  update` command. For example, to enable Coverity Connect high availability with
  2 replicas during deployment:

  ```
  helm install cnc -f values.yaml --set cim.cimweb.replicas=2
  ```
