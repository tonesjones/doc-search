---
title: "Using Machine Learning with Project Findings"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/using-machine-learning-with-project-findings.html"
content_id: "tPBFclVEW_wvuH810n7~Mw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:04:14.315392+00:00"
content_hash: "8866212b1db4218641474d7bbca6056e53f9fa83cb381559baa6be7cfe00cf12"
---

# Using Machine Learning with Project Findings

**Note:** This section is only applicable to Software Risk Manager users with the
Machine Learning Triage Assistance add-on and requires that machine learning is enabled.

Users of Software Risk Manager may review findings and change their statuses. When a finding's status
has been changed, we say that that finding has been *actively triaged*. The act of
*actively triaging* a finding is considered a *past triaging decision*.
Software Risk Manager is capable of learning from users' past triaging decisions in
order to make predictions about findings that have yet to be *actively triaged*.
More details will be described in the sections that follow.

## Actionability of a Finding

We use the terms *Actionable* and *Non-Actionable* to denote findings that are “real”
issues and “not-real” issues, respectively. A finding is said to be
*Actionable* if it was actively triaged as Fixed, To Be Fixed, Mitigated,
or Assigned, if it has a status of Gone, or if it has an issue tracker association.
A finding is said to be *Non-Actionable* if it was actively triaged as False
Positive or Ignored.

## Training a Prediction Model

In order for Software Risk Manager to make predictions for findings, users will need to train a
*prediction model*. Training a prediction model will collect all relevant
data for findings that have been actively triaged and use that data to learn from
users' past triaging decisions. See Machine Learning Control Panel for more
information about how to train a prediction model.

## Predicted Status and Prediction Confidence

When Software Risk Manager is making a prediction for a finding, we mean that Software Risk
Manager is determining a *Predicted Status* for it. A *Predicted Status*
for a finding is its *Actionability*. If Software Risk Manager predicts that a
finding is *Actionable*, then we say that its *Predicted Status* is
*To Be Fixed*, since Software Risk Manager thinks it's a real issue. If
Software Risk Manager predicts that a finding is *Non-Actionable*, then we say
that its *Predicted Status* is *False Positive*, since Software Risk
Manager does not think it's a real issue. Every prediction that Software Risk
Manager makes has a *Prediction Confidence*. A *Prediction Confidence* for
a *Predicted Status* represents how certain Software Risk Manager is of its
*Predicted Status* relative to the one it did not predict. Note that this
is a prediction of a finding's *Actionability*. That being said, Software Risk
Manager's prediction may not be correct.

## Requirements for Making Predictions

Software Risk Manager will only attempt to make predictions for findings if a prediction model
has been trained. See Machine Learning Control Panel for more
information about how to train a prediction model.

## When Will Software Risk Manager Make Predictions

Software Risk Manager will makes predictions for findings during the following
situations:

- During an analysis
- After a manual result has been created
- After a prediction model has been (re)trained

In these situations, all predictions are being made automatically. During the first
and third situations, predictions are automatically made for every finding in
Software Risk Manager. During the second situation, a prediction is only made for
the single manually created result. Since predictions are made automatically, a user
may note that predictions for findings might differ between reviewing sessions.

## Predicted Status Column

Every value in this column consists of a *Predicted Status* and a *Prediction
Confidence*.
