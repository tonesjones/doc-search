---
title: "Configuring automatic scan retry header"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-automatic-scan-retry-header.html"
content_id: "tWI8dFNWiKVxm_w6fLaq4Q"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:11.615592+00:00"
---

# Configuring automatic scan retry header

The automatic scan retry header can help ensure that scans are successfully completed
even if there are temporary issues such as network instability, service interruptions,
or other issues that may interfere with scans. By automatically retrying scans using a
queuing system, the system can reduce the need for manual intervention. Configuring the
automatic scan retry header allows Administrators to tailor the retry behavior to their
specific needs and environment. This customization helps optimize the retry process,
ensuring that it aligns with the system’s performance and operational requirements.

You can modify the Retry-After header found in the 429 response for Detect to know when
to attempt a rate limited scan again by adding the following properties in the
`blackduck-config.env` file:

- `BLACKDUCK_USE_QUEUE_RATE_LIMITING`: Set to `true`
  to enable queue base rate limiting in your environment. Default value is
  `false`.
- `BLACKDUCK_INITIAL_RATE_LIMIT_DURATION_BRACKET_THRESHOLD_MINUTES`:
  Dictates the duration the system must be rate limiting before the system moves
  from the first retry duration to the second retry duration. Default value is 2
  minutes.
- `BLACKDUCK_RATE_LIMIT_DURATION_THRESHOLD_BRACKET_INCREMENT_MINUTES`:
  Dictates the duration that the system will stay in a rate limiting bracket
  before going to the next retry duration and multiplier. Default value is 2
  minutes.
- `BLACKDUCK_INITIAL_RETRY_DURATION_MINUTES`: The initial duration
  of the Retry-After header in the first rate limiting bracket. Default value is 1
  minute.
- `BLACKDUCK_RETRY_DURATION_MULTIPLIER_MINUTES`: The amount to
  multiply the Retry-After Duration by each time the system reaches a new rate
  limit duration bracket. Default value is 2 minutes.

```
BLACKDUCK_USE_QUEUE_RATE_LIMITING=TRUE
BLACKDUCK_INITIAL_RATE_LIMIT_DURATION_BRACKET_THRESHOLD_MINUTES=2
BLACKDUCK_RATE_LIMIT_DURATION_THRESHOLD_BRACKET_INCREMENT_MINUTES=2
BLACKDUCK_INITIAL_RETRY_DURATION_MINUTES=1
RETRY_DURATION_MULTIPLIER_MINUTES_KEY=2
```
