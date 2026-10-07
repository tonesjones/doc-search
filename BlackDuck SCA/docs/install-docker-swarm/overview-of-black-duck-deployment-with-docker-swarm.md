---
title: "Overview of Black Duck Deployment with Docker Swarm"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/overview-of-black-duck-deployment-with-docker-swarm.html"
content_id: "mFcbq1LBAwiACjBbNo1MkA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:23.665461+00:00"
content_hash: "6bc8ac30e3d7bd4c130b7029c238a0d387c1972ceb720ac06b8e8c75977592a1"
---

# Overview of Black Duck Deployment with Docker Swarm

This document provides instructions for installing Black Duck in a Docker environment.

## Black Duck Architecture

Black Duck is deployed as a set of Docker containers. "Dockerizing" Black Duck so that different components are containerized allows third-party orchestration tools such as Swarm to manage all individual containers.

The Docker architecture brings these significant improvements to Black Duck:

- Improved performance
- Easier installation and updates
- Scalability
- Product component orchestration and stability

See Docker containers, for more information on the Docker containers that comprise the Black Duck application.

Visit the Docker website: <https://www.docker.com/> for more information on Docker.

To obtain Docker installation information, go to <https://docs.docker.com/engine/installation/>.
