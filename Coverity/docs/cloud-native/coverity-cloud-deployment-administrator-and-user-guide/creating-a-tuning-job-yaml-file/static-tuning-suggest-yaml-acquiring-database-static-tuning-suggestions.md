---
title: "static-tuning-suggest.yaml - Acquiring database static tuning suggestions"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/static-tuning-suggest.yaml-acquiring-database-static-tuning-suggestions.html"
content_id: "PBBF86g5JjiCNMsErKCPXw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:17.378019+00:00"
---

# static-tuning-suggest.yaml - Acquiring database static tuning suggestions

Using the `static-tuning-suggest.yaml` template returns suggested
PostgreSQL settings within tuning logs generated for the pod. For tuning-suggest, you need to
configure only physical resources and image details which are expected as input in
`static-tuning-suggest.yaml`. Because tuning-suggest does not change any
PostgreSQL settings, you do not need to provide permissions. The parameters are described in
the sections that follow.

```
apiVersion: "batch/v1"
kind: Job
metadata:
  name: static-tuning-suggest
  annotations:
    "helm.sh/hook-weight": "-10"
    helm.sh/hook: post-upgrade, post-install
  labels:
    app.kubernetes.io/name: cnc
spec:
  backoffLimit: 0
  template:
    metadata:
      labels:
        app.kubernetes.io/name: cnc
    spec:
      securityContext:
        runAsNonRoot: true
      imagePullSecrets:
        - name: <IMAGE-PULL-SECRETS>
      restartPolicy: "Never"
      containers:
        - name: static-tuning-suggest
          image: <IMAGE-NAME>
          imagePullPolicy: IfNotPresent
          command: ["/bin/sh", "/coverity/static-tuning-suggest.sh"]
          resources:
            limits:
              cpu: "0.5"
              memory: 1Gi
            requests:
              cpu: "0.5"
              memory: 1Gi
        env:
          - name: CNC_DATABASE_TUNING
            value: "true"
          - name: PROPERTIES_PATH
            value: "/coverity/config/cim.properties"
          - name: PROCESSOR_COUNT
            value: "<PROCESSOR-COUNT>"
          - name: PHYSICAL_MEMORY
            value: "<PHYSICAL-MEMORY>"
          - name: OPERATING_SYSTEM
            value: "Linux"
          - name: IS_SSD
            value: "<IS-SSD>"
          - name: TRUST-STORE-PATH
            value: "/coverity/config/trust-stores/trust-stores.jks"
        volumeMounts:
          - name: cnc-cim-cim-tools-properties
            mountPath: /coverity/config/cim.properties
            subPath: cim.properties
          - name: coverity-trust-stores
            mountPath: /coverity/config/trust-stores
    volumes:
      - name: cnc-cim-cim-tools-properties
        secret:
          secretName: <CIM-PROPERTIES>
      - name: coverity-trust-stores
        emptyDir: {}
```
