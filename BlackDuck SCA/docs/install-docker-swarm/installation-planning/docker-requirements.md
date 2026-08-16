---
title: "Docker requirements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/docker-requirements.html"
content_id: "oDHAfxv35l3D8MgmC_Tmvg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:28.351966+00:00"
---

# Docker requirements

Docker Swarm, which is the preferred method for installing Black Duck SCA,
is a clustering and scheduling tool for Docker containers. With Docker Swarm, you can
manage a cluster of Docker nodes as a single virtual system.

Note: For scalability, Black Duck recommends running Black Duck SCA on a single node Swarm
deployment. For full scalability sizing guidelines, see the Container Scalability
section of the Black Duck SCA Release Notes.

There are these restrictions when using Black Duck in Docker Swarm:

CAUTION:

Do not run anti-virus scans on the PostgreSQL data directory. Antivirus
software opens lots of files, puts locks on files, etc. Those things interfere with
PostgresSQL operations. Specific errors vary by product, but usually involve the
inability of PostgresSQL to access its data files. One example is that PostgresSQL fails
with the error "too many open files in system".

- The PostgreSQL database must always run on the same node in the cluster so that
  data is not lost (blackduck-database service).

  This does *not* apply to installations using an external PostgreSQL
  instance.
- The blackduck-webapp service and the blackduck-logstash service must run on the
  same host.

  This is required so that the blackduck-webapp service can access the logs that
  need to be downloaded.
- The blackduck-registration service must always run on the same node in the
  cluster or be backed by an NFS volume or a similar system, so that registration
  data is not lost.

  It does not need to be the same node as used for the blackduck-database service
  or the blackduck-webapp service.
- The blackduck-upload-cache service must always run on the same node in the
  cluster or be backed by an NFS volume or a similar system, so that data is not
  lost.

  It does not need to be the same node as used by other services.

## Docker Version

Black Duck SCA installation supports Docker versions 25.0.2, 28.x, and
29.x.

Note: Docker versions 23.x, 26.x and 27.x are no longer supported as of Black Duck SCA 2026.4.0.

## Installing Docker Engine on RHEL

Please note that Docker currently only provides packages for RHEL on s390x (IBM Z). Other
architectures are not yet supported for RHEL. Please refer to the [Docker](https://docs.docker.com/engine/install/rhel/) and [Redhat](https://access.redhat.com/solutions/3696691) pages for details.
