---
title: "Configure the cim.pgpool Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-the-cim.pgpool-helm-keys.html"
content_id: "WxOXv2KX9VrkSalJKdxwiQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:13.440423+00:00"
---

# Configure the cim.pgpool Helm keys

The `cim.pgpool` Helm keys are located in the `cnc` chart
`values.yaml` file. Use these keys to set up database read replicas,
as follows:

Important: For a complete list of `cim.pgpool`
Helm keys, see cim.pgpool Helm keys - PostgreSQL read replicas.

Important:

Except for the following Helm keys, you should not change or set values for any other
`cim.pgpool` Helm keys:

- `cim.pgpool.enable`
- `cim.pgpool.replicadb:`
- `cim.pgpool.maxConnections`

Contact Black Duck support before changing any other `cim.pgpool` Helm
keys.

Important: We do NOT recommend enabling read-only file system
for Pgpool.

## cim.pgpool.enable: Enable read replicas

To enable read replicas, set the `cim.pgpool.enable` Helm Key to
`true`. With Pgpool enabled, when you deploy read replicas, a
Pgpool container is created from the Pgpool container image, and read replicas is
set up.

## cim.pgpool.replicadb: Identify the replicas

When you create database read replicas, you uniquely identify each read replica. In
the `cnc` Helm chart, you need to provide the replica database ID and
port number as a list in the `cim.pgpool.replicas` Helm key:

```
cim: 
  pgpool: 
    replicadb: 
      - name: <replicaDBHost_1> 
        port: <replicaDBPort_1> 
      - name: <replicaDBHost_2> 
        port: <replicaDBPort_2> 
        .  
        .  
      - name: <replicaDBHost_N> 
        port: <replicaDBPort_N>
```

Where `name` is the replica database host name, and
`port` is the replica DB port number. Use port 5432.

For supported ports, see Ports.

For example, for two PostgreSQL database read replicas
(`pgpool-replica-1` and `pgpool-replica-2`) on
port 5432:

```
cim: 
  pgpool: 
    replicadb: 
      - name: “pgpool-replica-1” 
        Port: “5432” 
      - name: “pgpool-replica-2” 
        Port: “5432”
```

## cim.pgpool.maxConnections: Set max number of DB connections

The maximum number of connections set for the database.
`maxConnections` must be equal to or less than the PostgreSQL
`max_connections` parameter; it must never exceed it.

```
cim: 
  pgpool: 
    maxConnections: <max#ofDBConnections>
```

## Example

For example, for three PostgreSQL database read replicas (pgpool-replica-1,
pgpool-replica-2, and pgpool-replica-3) on Microsoft Azure at port 5432:

```
cim: 
  pgpool: 
    enabled: true 
    maxConnections: 830 
    replicadb:  
      - name: "pgpool-replica-1.postgres.database.azure.com" 
        port: "5432" 
      - name: "pgpool-replica-2.postgres.database.azure.com" 
        port: "5432" 
      - name: "pgpool-replica-3.postgres.database.azure.com" 
        port: "5432"
```

Entering these values within a `helm install` command might appear as
follows:

```
helm install "$CNC_APP_NAME" "${CNC_CHART_LOCATION:-"../../charts/cnc"}" \
  --wait \
  --timeout 60m0s \
  --debug \
  --namespace "$CNC_NS" \
  --set cim.pgpool.enabled=true \
  --set cim.pgpool.maxConnections=830 \
  --set cim.pgpool.replicadb[1].name="pgpool-replica-0.postgres.database.azure.com"" \
  --set cim.pgpool.replicadb[1].port="5432" \
  --set cim.pgpool.replicadb[2].name="pgpool-replica-1.postgres.database.azure.com" \
  --set cim.pgpool.replicadb[2].port="5432" \
  --set cim.pgpool.replicadb[3].name="pgpool-replica-2.postgres.database.azure.com" \
  --set cim.pgpool.replicadb[3].port="5432" \  .
  .
  .
  .
  -f values.yaml \
```
