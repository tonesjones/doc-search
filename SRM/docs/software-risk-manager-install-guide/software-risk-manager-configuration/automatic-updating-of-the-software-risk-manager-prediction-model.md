---
title: "Automatic Updating of the Software Risk Manager Prediction Model"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/automatic-updating-of-the-software-risk-manager-prediction-model.html"
content_id: "3nF96j9gPqC8dg3kACPqyA"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:36.052582+00:00"
content_hash: "9055cd604a9e3bbc2d5f3b1d20c030ac7cf0771a925e9f068676dda96b37a13f"
---

# Automatic Updating of the Software Risk Manager Prediction Model

Software Risk Manager can automatically update your prediction model. This feature can be
configured or turned off completely by setting the following props settings in your
`codedx.props` file:

- `mltriage.enable-periodic-retrain` [default: true] - enables
  Software Risk Manager to periodically train a prediction model.
- `mltriage.model-train-time` [default: 01:45:00] - the time at
  which Software Risk Manager will check if the threshold set in
  mltriage.retrain-threshold has been met, and if it has, train a prediction
  model.
