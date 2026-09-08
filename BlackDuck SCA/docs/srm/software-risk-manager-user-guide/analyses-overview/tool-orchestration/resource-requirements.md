---
title: "Resource Requirements"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/resource-requirements.html"
content_id: "70PpxZudfzCJDM4GoadnVQ"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:43.365249+00:00"
content_hash: "187e5046cc287cca21829d1721a4e2e78474996946aa006d0f903c68d4acd33c"
---

# Resource Requirements

When the Tool Orchestration Service is enabled, Software Risk Manager can create
orchestrated analyses that run one or more application security testing tools where each
tool has access to its host's memory and CPU resources. Using Kubernetes (k8s) tools,
you can control the memory and CPU capacity available to analyses. You can also improve
k8s scheduling outcomes by requesting CPU or memory capacity for specific tools or
projects. Resource requirements can also include a node selector and pod toleration,
with taint effects NoSchedule and NoExecute, to influence further where tools run on
your cluster.

The resource requirements feature cannot be configured using the Software Risk Manager
user interface, but you can use the k8s kubectl command to define configuration maps
(configmaps) that cover specific scope determined by a special naming convention. The
tool service will look for and read optional configmaps to determine how resource
requirements apply to a specific tool run.

Resource requirements containing CPU and memory instructions translate to k8s resource
requests and limits and fit with any other related k8s configuration, such as a resource
limit defined for a k8s namespace. You can specify resource requirement data by using
the following configmap field names:

- **requests.cpu** – k8s CPU request (e.g., 1).
- **requests.memory** – k8s memory request (e.g., 1G).
- **limits.cpu** – k8s CPU limit (e.g., 2).
- **limits.memory** – k8s memory limit (e.g., 2G).
- **nodeSelectorKey** – key portion of a label associated with a node selector
  (e.g., purpose).
- **nodeSelectorValue** – value portion of a label associated with a node
  selector.
- **podTolerationKey** – key portion of a taint with the NoSchedule and
  NoExecute taint effects (e.g., dedicated).
- **podTolerationValue** – value portion of a taint with the NoSchedule and
  NoExecute taint effects (e.g., tools).

There are four types of configmaps that can contain resource requirements:

- Global
- Global Tool
- Project
- Project Tool

Software Risk Manager deployment creates the Global Resource Requirement, which provides
default resource requirements for tools across every Software Risk Manager project.
Global Tool requirements override Global requirements for specific tools. Project
requirements override both Global and Global Tool requirements by providing default
resource requirements for tools associated with a given project. And Project Tool
requirements override other requirements by specifying values for a specific tool in a
specific project.

## Scope Overlap

The following is an example of how the scopes can overlap:

**Global Resource Requirement:**

- CPU Request = 1
- CPU Limit = 4
- Memory Request = 11G
- Memory Limit = 12G

**Global Tool Resource Requirement:**

- CPU Request = 3

**Project Resource Requirement:**

- Memory Request = 13G

**Project Tool Resource Requirement:**

- Memory Limit = 14G

Here are the effective resource requirements resulting from the above:

**Effective Resource Requirement:**

- CPU Request = 3
- CPU Limit = 4
- Memory Request = 13G
- Memory Limit = 14G

**The naming convention determines the scope of a resource requirement configmap:**

- Global: cdx-toolsvc-resource-requirements
- Global Tool: cdx-toolsvc-**ToolName**-resource-requirements
- Project: cdx-toolsvc-project-**ProjectID**-resource-requirements
- Project Tool:
  cdx-toolsvc-project-**ProjectID**-**ToolName**-resource-requirements

  where **ProjectID** is the integer value representing the Software Risk Manager
  project identifier and **ToolName** is the tool name converted to an acceptable k8s
  resource name by the following rules:
  - Uppercase letters must be converted to lowercase.
  - Any character other than a lowercase letter,
    number, dash, or period must be converted to a dash.
  - An initial character that is neither a number
    nor a lowercase letter must be preceded by the letter "s."
  - A name whose length is greater than 253, must be
    truncated to 253 characters.

## Example 1 - Project Resource Requirement

To create a resource requirement for all tool runs of a Software Risk Manager project
represented by ID 21, create a file named
`cdx-toolsvc-project-21-resource-requirements.yaml` and enter the
following data:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: cdx-toolsvc-project-21-resource-requirements
data:
  requests.cpu: "1"
  limits.cpu: "2"
  requests.memory: "1G"
  limits.memory: "2G"
```

Note: You can find a project's ID at the end of its Findings page URL. For example, a
project with the ID 21 will have a Findings page URL that ends with
`/srm/projects/21`.

Run the following command to create the configmap resource (replacing the cdx-svc k8s
namespace, if
necessary).

```
kubectl -n cdx-svc create -f ./cdx-toolsvc-project-21-resource-requirements.yaml
```

## Example 2 - Global Tool Resource Requirement

To create a Global Tool resource requirement for ESLint, create a file named
cdx-toolsvc-eslint-resource-requirements.yaml and enter the
following data:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: cdx-toolsvc-eslint-resource-requirements
data:
  requests.cpu: "2"
  limits.cpu: "3"
  requests.memory: "4G"
  limits.memory: "5G"
```

Run the following command to create the configmap resource (replacing the cdx-svc k8s
namespace, if
necessary).

```
kubectl -n cdx-svc create -f ./cdx-toolsvc-eslint-resource-requirements.yaml
```

## Example 3 - Node Selector

To create a Global Tool resource requirement for running a tool named MyTool on
cluster nodes labeled with `canrunmytool=yes`, create a file named
cdx-toolsvc-mytool-resource-requirements.yaml and enter the
following data:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: cdx-toolsvc-mytool-resource-requirements
data:
  nodeSelectorKey: canrunmytool
  nodeSelectorValue: yes
```

Run the following command to create the configmap resource (replacing the cdx-svc k8s
namespace, if
necessary):

```
kubectl -n cdx-svc create -f ./cdx-toolsvc-mytool-resource-requirements.yaml
```
