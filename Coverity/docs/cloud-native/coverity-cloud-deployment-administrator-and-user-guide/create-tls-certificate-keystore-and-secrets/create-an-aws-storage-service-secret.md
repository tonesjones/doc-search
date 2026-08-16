---
title: "Create an AWS storage service secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-an-aws-storage-service-secret.html"
content_id: "GipOl0aJ3m6huGCKklAz5Q"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:06.734581+00:00"
---

# Create an AWS storage service secret

If you are deploying Storage Service in Amazon AWS, you need to provide access keys to
support access to the AWS Storage Service and Cache Service. The secret must contain
both the aws_access_key and the aws_secret_key, You need this secret for either S3
storage or S3 Express storage. You can either:

- create an AWS storage service as described in this section.
- create a role-based AWS service account as described in Using a role-based AWS service account for Storage Service and Cache Service, or

If you are deploying Storage Service in Amazon AWS, create a secret containing the AWS
keys, `aws_access_key` and `aws_secret_key` as
follows:

```
kubectl create secret generic "${AWS_SECRET_NAME}" \
  --namespace "${CNC_NS}" \
  --from-literal=aws_access_key="${AWS_ACCESS_KEY}" \
  --from-literal=aws_secret_key="${AWS_SECRET_KEY}" \
  -o yaml \
```

Note: In the kubectl command, do *not* change the names of these
keys: `aws_access_key` and `aws_secret_key`.
