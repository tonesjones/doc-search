---
title: "API reference"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-reference.html"
content_id: "35ZTEo17VlIE7clJL0Z5vQ"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:31.477712+00:00"
---

# API reference

Black Duck APIs offer a convenient way to retrieve ad-hoc information from Black Duck or
to perform automated review or workflows. However, customers looking to build out
customized views or dashboards using bulk data from Black Duck would be best served by
using the [Black Duck Reporting DB schema](https://docs.blackduck.com/access?ft:originId=dad2192abc2e53d01fcee1313e1aa841/1d44685a2d2cfd2e5a8c52a38e7b898d.topic).

Tip: Although APIs offer a way to do most functions that Black Duck UI can do, you might
choose the Black Duck Bridge command line interface or an SCM integration for building
tests or automation into your pipeline.

After tests run, APIs can help with the following:

- Generate and download a notices file or SBOM
- Collate component copyright information
- Automatically assign issues to developers
- Add comments to Pull Requests with Black Duck data

To explore what Black Duck SCA APIs have to offer:

- Access the REST API documentation found in Black Duck SCA by opening the Help
  menu from the top navigation bar and selecting **REST API Developers
  Guide**.
- Visit the REST API documentation directly at https://<Black Duck Server
  URL>/api-doc/public.html.

## Black Duck REST API Python bindings

This Python library provides a streamlined interface to interact with Black Duck
APIs, enabling customers to efficiently automate and customize their workflows. This
library is distributed as an open-source extension of Black Duck and is licensed
under the Apache 2.0 license.

For more details or to contribute, visit the [Black Duck API Python bindings GitHub repository](https://github.com/blackducksoftware/hub-rest-api-python).

## Downloading the Black Duck API Specification

Black Duck provides the capability to download the full API specification using
either a Postman collection or an OpenAPI Specification (OAS). These options allow
customers to directly import the documentation into tools like Postman, simplifying
the process of working with the APIs.

- **Postman Collection**: You can generate a Postman collection from the API
  documentation by downloading the
  `postman-collection-public.json` file from
  `/api-doc/postman-collection-public.json`. This file can
  be imported into Postman to interact with the Black Duck APIs.
- **OpenAPI Specification (OAS)**: Similarly, the OpenAPI Specification can
  be generated via the `/api-doc/openapi3-public.json`
  endpoint. This allows you to explore and document the Black Duck API with
  tools that support OAS.

## Integrating Black Duck with Business Intelligence tools

Black Duck offers a Reporting Database (Reporting DB) interface that enables seamless
integration with Business Intelligence (BI) tools, such as PowerBI. This interface
provides customers with the flexibility to generate custom reports, visualize data,
and build comprehensive dashboards that reflect key performance indicators (KPI) and
risk management views.

To accelerate the integration process, Black Duck provides sample reports
specifically designed for use with PowerBI. These templates serve as an efficient
starting point for customers, allowing them to quickly build customizable dashboards
using data from Black Duck's Reporting DB.

For more details, visit [Black Duck Dashboards using Microsoft Power
BI](https://community.blackduck.com/s/article/Blackduck-Dashboards-using-Microsoft-Power-BI).
