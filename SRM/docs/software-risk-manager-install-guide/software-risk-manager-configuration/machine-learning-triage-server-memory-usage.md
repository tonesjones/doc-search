---
title: "Machine Learning Triage Server Memory Usage"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/machine-learning-triage-server-memory-usage.html"
content_id: "FmbieDGpaVA956EuM_aADw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:35.447893+00:00"
content_hash: "41686d089a811e6ceccd5e866a111620369039a2431b97504c5cc65b27dc8c6c"
---

# Machine Learning Triage Server Memory Usage

The Software Risk Manager machine learning aided triage functionality is handled by a
separate process, the *Machine Learning Triage Server*, which Software Risk Manager
spawns and manages. Training a new prediction model is computationally intensive and can
use large amounts of memory. There are times where training performance can be improved
with the availability of more memory. The upper bound on the amount of memory that the
*Machine Learning Triage Server* JVM can use during training and making
predictions can be configured by setting the following properties setting:

`mltriage.service.maxheap` [default: none] - sets the max heap size (in
megabytes) of the *Machine Learning Triage Server* JVMs.
