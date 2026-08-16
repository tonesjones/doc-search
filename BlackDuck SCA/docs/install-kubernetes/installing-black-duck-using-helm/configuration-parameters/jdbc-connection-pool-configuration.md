---
title: "JDBC Connection Pool Configuration"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/jdbc-connection-pool-configuration.html"
content_id: "YK3xes7ElYals9hqtR547A"
version: "2026.7"
section: "Installing Black Duck using Kubernetes and OpenShift"
scraped_at: "2026-08-08T15:33:08.243676+00:00"
---

# JDBC Connection Pool Configuration

Black Duck services use a JDBC connection pool to manage database connections. The
default pool size is sufficient for most deployments. However, large enterprise
environments with high API throughput (for example, 1000+ scans per hour) may need to
increase the connection pool to avoid pool exhaustion errors.

## Symptoms of an undersized connection pool

If the JDBC connection pool is too small for your workload, you may see errors like
the following in your webapp pod logs:

```
org.apache.tomcat.jdbc.pool.PoolExhaustedException:
Timeout: Pool empty. Unable to fetch a connection in 30 seconds,
none available [size:32; busy:32; idle:0; lastwait:30000].
```

Other indicators include:

- HTTP API responses exceeding normal duration thresholds (e.g., 30 seconds or
  more for notification or project version endpoints).
- Webapp pods restarting frequently under sustained load.

## Configuring `dbPoolMaxActive`

You can tune the maximum number of active JDBC connections for a given service by
setting the `dbPoolMaxActive` property in your Helm chart
`values.yaml` file under the appropriate service section.

**Syntax:**

```
<service>:
  dbPoolMaxActive: <integer>
```

**Example — increasing the webapp connection pool to 64:**

```
webapp:
  replicas: 1
  hubMaxMemory: "13824m"
  dbPoolMaxActive: 64
  resources:
    limits:
      cpu: "5000m"
      memory: "15360Mi"
    requests:
      cpu: "3000m"
      memory: "15360Mi"
```

The `dbPoolMaxActive` property can be set on any service that
maintains a database connection pool (e.g., `webapp`,
`jobrunner`, `bomengine`,
`scan`).

## Important considerations

Note: Tuning the connection pool is not required for most customers. The default values
are appropriate for standard deployments. Only adjust this setting if you are
experiencing pool exhaustion under sustained high-throughput workloads.

Before increasing `dbPoolMaxActive`, consider the following:

- **PostgreSQL** `max_connections`: Each active connection in
  the pool consumes a PostgreSQL backend connection. Ensure your PostgreSQL
  instance's `max_connections` setting can accommodate the
  total pool size across all services and replicas. For example, if you set
  `dbPoolMaxActive: 64` on `webapp` with 2
  replicas, that service alone may use up to 128 PostgreSQL connections.
- **Database server resources:** Higher connection counts increase memory
  and CPU usage on the database server. Verify that your PostgreSQL host has
  sufficient resources.
- **Incremental changes:** Increase the pool size incrementally (e.g., from
  32 → 64 → 96) and monitor the impact rather than making large jumps.
- **Holistic tuning:** Connection pool changes should be aligned with your
  overall API throughput requirements and PostgreSQL configuration. Revision
  should be managed with considered planning and caution.
