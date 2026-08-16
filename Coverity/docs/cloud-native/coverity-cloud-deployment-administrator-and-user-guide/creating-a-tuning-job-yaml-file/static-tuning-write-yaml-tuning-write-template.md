---
title: "static-tuning-write.yaml - Tuning-write template"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/static-tuning-write.yaml-tuning-write-template.html"
content_id: "flk~ZMeqPZKwYxkSAVHDpg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:16.724724+00:00"
---

# static-tuning-write.yaml - Tuning-write template

The following template, `static-tuning-write.yaml`, provides PostgreSQL tuning
write settings. If you want PostgreSQL tuning settings to be written, use
`static-tuning-write.yaml`. In addition to providing job values, you will
need to configure permissions to write the tuning parameters. The parameters are described in
the sections that follow.

```
apiVersion: "batch/v1"
kind: Job
metadata:
  name: static-tuning-write
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
        - name: static-tuning-write
          image: <IMAGE-NAME>
          imagePullPolicy: IfNotPresent
          command: ["/bin/sh", "/coverity/static-tuning-write.sh"]
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
          - name: POSTGRES_DISTRO
            value: "<POSTGRES-DISTRO>"
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
          - name: INSTANCE_IDENTIFIER
            value: "<INSTANCE-IDENTIFIER>"
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
