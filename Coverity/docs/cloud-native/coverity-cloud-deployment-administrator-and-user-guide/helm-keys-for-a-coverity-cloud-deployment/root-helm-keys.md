---
title: "Root Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/root-helm-keys.html"
content_id: "qTd7DdwAqgauNnBdCnlBZA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:03.143598+00:00"
---

# Root Helm keys

The following Helm keys define image, license, registry, and volume creation.

As of 2024.6.0, root Helm keys are available at the following chart levels:

- Global root Helm keys are prepended with `global` to identify them as
  global values. The global values apply to both the `cnc` chart and
  the `scan-services` subchart.
- In the `cnc` chart, root keys apply only to the `cnc`
  chart. Changing a root value here overrides the global value for only the
  `cnc` chart.
- In the `scan-services` subchart, root keys apply only to the
  `scan-services` subchart. Changing a root value here overrides
  the global value for only the `scan-services` subchart.

Important: When you either create a custom
`.yaml` file or set a root Helm key within a command such as
`helm install`, you must:

- **For cnc chart root keys**: Include cnc chart root Helm keys using the
  syntax as defined in the cnc chart's `values.yaml` file.
- **For scan-services chart root keys**: Prepend scan-services subchart root
  Helm keys with `scan-services` to identify them as scan-services
  chart values.
- **For global root keys**: Provide global root Helm keys using the global
  syntax specified in the Helm chart.

`global` keys apply to both charts where applicable.

The root keys in either the `cnc` chart or the
`scan-services` subchart override global values for only that
chart.

Table 1. Root Helm keys

| Key | Default value | Description |
| --- | --- | --- |
| `extraVolumeMounts:` | `[]` | Use this Helm key to mount volumes created in the `extraVolumes` Helm key. This mounts volumes for Connect admin tools and Connect database tools.  `cnc` chart: In the `cnc` chart, this key adds additional volume mounts to Connect webapp, Connect admin tools, and Connect database tools.  `scan-services` subchart: In the scan-services subchart, this key adds additional volume mounts to all containers and jobs except AnalysisJob and cleanUpJob. |
| `extraVolumes:` | [] | This single Helm key, if configured, provides additional volumes for the following Coverity Connect pods: Connect webapp, Connect admin tools, and Connect database tools. See the `extraVolumeMounts` Helm key to mount these volumes.  `cnc` chart: In the `cnc` chart, this key adds additional volumes to all Connect pods and jobs.  `scan-services` subchart: In the scan-services subchart, this key adds additional volumes to all scan-services pods and jobs except syncJob, AnalysisJob, and cleanUpJob. |
| `imagePullPolicy:` | `""` | See the Kubernetes page: <https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy>. This is set on each Coverity cloud deployment pod to control its image pull policy. Valid values are:   - `"IfNotPresent"` - Kubernetes checks if the image   exists on the node. If it does, it uses the cached copy;   otherwise, it pulls the image from the registry. With   imagePullPolicy set to ifNotPresent, the container images are   good for the life of the node. Numerous pods can be spun up and   down from the cached image(s). - `"Always"` - Kubernetes always attempts to pull   the image from the registry to ensure the latest version is   used. - `"Never"` - Kubernetes never pulls images. The   images must already be locally available. If an image is not   available locally, pod creation fails.  See the Kubernetes page: [Kubernetes documents](https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy). `cnc` chart: In the `cnc` chart, this is set on each `cnc` pod to control its image pull policy.  `scan-services` subchart: In the `scan-services` subchart, this is set on each scan-services pod to control its image pull policy. |
| `imagePullSecret:` | `""` | Specify the name of the secret that contains the credentials needed to connect to the repository/Docker registry that contains the container images and client images used to deploy the Coverity cloud containers and jobs. This must be set for images that are pulled from a registry that requires authentication. The Coverity images must be kept in a private Docker registry requiring credentials to access. Also, the secret must exist in the same namespace.  For information on creating an image pull secret, refer to:   - Create a container image pull secret - <https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod>   The Black Duck container image repository is: `repo.blackduck.com/containers/`.  This key must be configured if images are pulled from a registry requiring authentication. |
| `imageRegistry:` | `""` | The registry from which Kubernetes nodes pull the cnc or scan service images, if this registry is different from the `global.imageRegistry` registry. Use these keys if you have multiple registries.  Note: You can pull these images from the Black Duck registry, however, we recommend that you use a local private registry for faster image pulls.  `cnc` chart: In the `cnc` chart, set the `imageRegistry` Helm key value if the `cnc` chart images are not in the registry identified by the `global.imageRegistry` Helm key.  `scan-services` subchart: In the `scan-services` subchart, set the value in this Helm key if the scan service images are in a registry which is separate from the `global.imageRegistry` registry. |
| `imageTagSuffix:` | `""` | If you are installing Coverity on OpenShift, you need to specify a `-ubi` suffix in the Coverity image name using this Helm key.  Valid values for this key are:   - `"-ubi"` - use this value for an image you will   install in Red Hat OpenShift. For example, if you are deploying   Coverity cloud version 2026.6.0 in OpenShift,   you need to use image version `2026.6.0-ubi`. - `""` - this is the default value for Kubernetes   images. For example, if you are deploying Coverity cloud version   2026.6.0 in Kubernetes, you need to use   image version `2026.6.0`.   `cnc` chart: In the `cnc` chart, specifies the suffix that appends to all Black Duck images tag. For example, `-ubi`  `scan-services` subchart: In the scan-services subchart, the suffix that appends to all Black Duck images tag. like -ubi |
| `imageVersion:` | `""` | The container image tag used for all Black Duck images. This can be overridden on a service-by-service basis in the `values.yaml` file.  `cnc` chart: The docker image tag used for all Black Duck images. This can be overridden on a service-by-service# basis in subordinate stanzas of the values file  `scan-services` subchart: In the scan-services subchart, the docker image tag used for all Black Duck images. This can be overridden on a service-by-service# basis in subordinate stanzas of the values file |
| `tolerations:` | [] | This is a global tolerations parameter that sets the tolerations on all of the Coverity cloud pods.  By default, Coverity is deployed on AMD pods. To deploy on only ARM64 pods, you would provide the following toleration:   ``` tolerations:   - key: "kubernetes.io/arch"     operator: "Equal"     value: "arm64"     effect: "NoSchedule" ```   Note: Refer to:  - Setting up ARM64 support - <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/>   `cnc` chart: Sets the tolerations on the Connect deployment.  `scan-services` subchart: Sets the tolerations on all the scan-services pods. |
