---
title: "Overview of Black Duck Deployment with Docker Swarm"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/overview-of-black-duck-deployment-with-docker-swarm.html"
content_id: "5FR~kRvbGkzzIIGrYt1ICw"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:25.549894+00:00"
---

# Overview of Black Duck Deployment with Docker Swarm

This document provides instructions for installing Black Duck in a
Docker environment.

## Black Duck Architecture

Black Duck is deployed as a set of Docker containers.
"Dockerizing" Black Duck so that different components are
containerized allows third-party orchestration tools such as Swarm to manage all
individual containers.

The Docker architecture brings these significant improvements to Black Duck:

- Improved performance
- Easier installation and updates
- Scalability
- Product component orchestration and stability

See Docker containers, for more
information on the Docker containers that comprise the Black Duck
application.

Visit the Docker website: <https://www.docker.com/> for more information on
Docker.

To obtain Docker installation information, go to <https://docs.docker.com/engine/installation/>.
