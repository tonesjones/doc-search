---
title: "Software Risk Manager Scoring Calculations"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/software-risk-manager-scoring-calculations.html"
content_id: "kpSUuqTECuDtbfs3az1hng"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:37.259177+00:00"
content_hash: "f391e8a12d827ed8636a7947c00816445a4825f99f23ba933814dae79c6bcc95"
---

# Software Risk Manager Scoring Calculations

In analysing risk, Software Risk Manager calculates a "code score" (Critical, High,
Medium, and Low) by averaging a "custom code score" and a "component score." This is
done through a configurable function in the form `f(severity, count)` for
certain metrics (shown below). However, this formula can be customized if needed. (For
more information on Risk Scoring, see the *Risk
Score* section in the *User Guide.*)

The metrics used for this calculation are as follows:

- `componentFindingVolume` - in which the count represents the
  number of component findings for a given severity.
- `customCodeFindingVolume` - in which the count represents the
  number of non-component findings for a given severity.
- `customCodeFindingVariety` - in which the count represents the
  number of finding types for a given severity.

These metrics are used to calculate a "penalty," which is removed from a top score of 100
down to a minimum score of 0. The "component score" uses the first of the metrics listed
above; "custom code score" uses the sum of the other two.

The `f` function can be configured by name; for example, the *base
config path* for the `componentFindingVolume` formula would be
`dashboard.score.componentFindingVolume`.

Once the function is configured, there are three suffixes that control the formula:

- `.formulaType`
  - If set to `log`, the formula is `(severity, count)
    => log_<logBase>(count) * criticalWeight / (critical -
    severity)^2`
  - If set to `linear`, the formula is `(severity,
    count) => count * criticalWeight / (critical -
    severity)^2`

    (The
    `customCodeFindingVolume` metric uses the
    `log` formula by default, while the rest use
    `linear`.)
- `.criticalWeight` represents how much weight a Critical severity
  holds in the formula. "High" will have 1/2 the weight; "Medium," 1/4. (The
  default is 3.0.)
- `.logBase` is used as the base number for the log function in the
  `log` formulaType; for example, log-base-2 or log-base-10.
  (The default is 2.0.)

Here is an example of a default configuration for the
`componentFindingVolume` metric:

```
dashboard.score.componentFindingVolume.formulaType = log
dashboard.score.componentFindingVolume.criticalWeight = 3.0
dashboard.score.componentFindingVolume.logBase = 2.0
```
