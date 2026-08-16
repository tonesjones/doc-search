---
title: "Managing Coverity Connect: cov-manage-im"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-coverity-connect-cov-manage-im.html"
content_id: "CqEWbvKJLIqig9HU2Etpmw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:46:11.320515+00:00"
---

# Managing Coverity Connect: cov-manage-im

The `cov-manage-im` is a command line tool that is used to manage and
query defects, projects, and streams in Coverity Connect. This command also outputs
logging information to /logs/cim.log.

When you execute the command, you use the same arguments that are used with the
`cov-manage-im` command described in the section
cov-manage-im within Coverity Connect commands in the Coverity 2026.6.0 Command Reference.

For the Coverity cloud deployment, the `cov-manage-im` tool is packaged in
a Docker image at
`repo.blackduck.com/containers/cov-manage-im:<version>`.

Pass all of the command line options that the Coverity installer expects to a container
invocation. Provide the IP address of your Coverity Connect instance in the cloud
through the host parameter, or add the `--add-host
<hostname>:<IP>` option to the command line invocation.

Note: When running `cov-manage-im` in a Coverity
cloud deployment environment, you can pass all of the command line options that a
non-cloud installer expects.

In the following examples, Coverity Connect is running on the HTTP protocol:

```
docker run --rm repo.blackduck.com/containers/cov-manage-im:<version> \
  --host $CONNECT_IP_ADDRESS \
  --port $CONNECT_PORT \
  --user $CONNECT_USER \
  --password $CONNECT_PASSWORD \
  --mode projects \
  --show
```

The following example first maps the container host name to the IP address using
`--add-host`, then identifies the container using
`--host`:

```
docker run \
  --rm \
  --add-host $CONNECT_HOST:$CONNECT_IP_ADDRESS \
  repo.blackduck.com/containers/cov-manage-im:<version> \
  --host $CONNECT_IP_ADDRESS \
  --port $CONNECT_PORT \
  --user $CONNECT_USER \
  --password $CONNECT_PASSWORD \
  --mode projects \
  --show
```

When Coverity Connect is running on HTTPS, pass the `--certs` option
with the cert file (similar to the non-cloud installer) along with `-v
$(pwd)/<cert-filename on host machine>:<desired path to cert inside
container>`. For example:

```
docker run \
  -ti \
  --rm \
  -v $LOCAL_PATH:$REMOTE_PATH \
  --add-host $CONNECT_HOST:$CONNECT_IP_ADDRESS \
  repo.blackduck.com/containers/cov-manage-im:<version> \
  --host $CONNECT_IP_ADDRESS \
  --port $CONNECT_PORT \
  --user $CONNECT_USER \
  --password $CONNECT_PASSWORD \
  --ssl \
  --certs $CERT_PATH \
  --mode projects \
  --show
```

Hostname verification can be disabled using an environment variable `--env
SSL_NO_DOMAIN_CHECK=true`. For example:

```
docker run \
  -ti \
  --rm \
  --env SSL_NO_DOMAIN_CHECK=true \
  -v $LOCAL_PATH:$REMOTE_PATH \
  --add-host $CONNECT_HOST:$CONNECT_IP_ADDRESS \
  repo.blackduck.com/containers/cov-manage-im:<version> \
  --host $CONNECT_IP_ADDRESS \
  --port $CONNECT_PORT \
  --user $CONNECT_USER \
  --password $CONNECT_PASSWORD \
  --ssl \
  --certs $CERT_PATH \
  --mode projects \
  --show
```
