---
title: "NGINX redeploy Coverity cloud"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nginx-redeploy-coverity-cloud.html"
content_id: "Y933KwO5rA~ZJ8QS8L6OmA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:50.076316+00:00"
---

# NGINX redeploy Coverity cloud

Note: Do not perform this step if you created the proxy timeouts in an
NGINX configMap.

After creating annotations within the Helm chart, in order to apply the new values and
override the default proxy timeout values, you must re-deploy Coverity cloud. For
example, use a `helm install` or `helm upgrade` command
and refer to the new or modified `values.yaml` file as needed.
