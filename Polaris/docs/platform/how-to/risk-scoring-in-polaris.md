---
title: "Risk scoring in Polaris"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/risk-scoring-in-polaris.html"
content_id: "Abs2P0wg4JZkcqStgCKt1w"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:46.210900+00:00"
content_hash: "aa02512f1be92a813942168d75672bf947e44e61676eabafdd0d400062cd4354"
---

# Risk scoring in Polaris

Learn about the application and issue risk scoring features, key concepts, and how risk scores are calculated.

Risk scoring allows you to qualify the significance of applications in your portfolio with:

- Application risk factors you define
- Issue risk factors (for SCA issues only)

After you enable risk scoring, Polaris assigns a composite score (ranging between 0–100) to each application in your Portfolio. Higher risk scores indicate an application's vulnerabilities pose a larger threat to your organization. Each application's risk score is a function of:

- The quantity of DAST, SAST, and SCA issues detected in the application's projects (default branches only).
- The application risk factors you create and enable, and the categories assigned to the application.
- The issue risk factors you enable, and the maximum issue risk score adjustment.
- The significance (or weight) of different application and issue risk factors in your organization.

## Risk factors

Each risk factor is a collection of categories, and each category is assigned an impact value. In the following screenshot, you can see the categories and impact values assigned to the default risk factor, **Business Criticality** (which is created automatically when you enable application risk scoring).

[image: Screenshot of the categories and impact values assigned to the default application risk factor, Business Criticality (which is created automatically when you enable application risk scoring).]

Application risk factors are user-defined and can be modified. Issue risk factors are largely preconfigured.

### Categories

Categories are values that correspond with characteristics or attributes of applications or issues, and are used to quickly classify the applications and issues in your portfolio. Categories in application risk factors differ from categories in issue risk factors.

- Categories in application risk factors can be modified, added, or removed.
- You can adjust the impact value of categories in issue risk factors, but cannot rename, add, or remove categories.

Note: The first category in an application risk factor is the default category. The default category is assigned to all of the applications in your portfolio when risk scoring is enabled, and is selected by default when you create new applications. The default category can have a negative, neutral, or positive impact value.

### Impact values

An impact value is mapped to each category. Impact values range between -5 and 5, where:

- A negative impact value lowers risk scores.
- An impact value of 0 (a neutral impact value) doesn't change risk scores.
- A positive impact value raises risk scores.

### Risk factor weights

Weights are used to control the relative significance of:

- Different application risk factors
- Different issue risk factors
- Application risk factors and issue risk factors

[image: Screenshot demostrating the weights assigned to different risk factors.]

### Maximum issue risk score adjustment

The maximum issue risk score adjustment limits how much issue risk scores can change based on application and issue risk factors.

## Base issue risk scores

While only neutral categories (risk factor categories with an impact value of 0) are assigned to an application, its risk score is only derived from the issues captured in its projects, and calculated using base issue risk scores. The base issue risk scores of DAST and SAST issues correspond with severity.

Table 1. DAST and SAST issues, base issue risk scores per severity

| Issue severity | Base issue risk score |
| --- | --- |
| Critical | 95 |
| High | 80 |
| Medium | 50 |
| Low | 20 |
| Info | 0 |

SCA base issue risk scores are calculated by multiplying the issue's Vulnerability: Overall Score (found on the Issue Details tab) by 10.

Note: Issues with a base issue risk score below 20 (including informational severity issues) are ignored, and do not affect risk scores.

## Calculating issue and application risk scores

Polaris uses issue risk scores to calculate application risk scores.

### Part 1: Calculating issue risk scores

You can see how Polaris calculates DAST, SAST, and SCA issue risk scores in the Risk Score Breakdown panel (found in the Issue Details tab).

[image: Screenshot of the Risk Score Breakdown window.]

Here, you can see:

- Each issue's base and adjusted risk scores.
- How application risk factors affect the issue's risk score (when enabled).
- How issue risk factors affect the issue's risk score (when enabled, SCA issues only).

For more information, see [View issue risk score calculations](risk-scoring-in-polaris/view-issue-risk-score-calculations.md).

### Part 2: Calculating application risk scores

Polaris calculates application risk scores using a weighted average of the issue risk scores in each application. Issues with higher risk scores have a greater impact on application risk scores.

Important: Issues found on non-default branches in SAST and SCA projects are not used to calculate application risk scores.

Table 2. Issue risk score weights

| Issue risk score | Weight |
| --- | --- |
| 95 or higher | 50% |
| 80–94 | 30% |
| 50–79 | 15% |
| 20–49 | 5% |
| 0–19 | 0% |

Note: Application risk scores are capped at 100. If the weighted average of issue risk scores exceeds 100, the application risk score is set to 100.

For example, consider an application with the following issues:

Table 3. Example application risk score calculation

| Issue | Issue risk score | Weight | Weighted scores |
| --- | --- | --- | --- |
| Critical severity SCA issue | 98 | 50% | 98 × 0.5 = 49 |
| Medium severity SCA issue | 55 | 15% | 55 × 0.15 = 8.25 |
| Critical severity SAST issue | 95 | 50% | 95 × 0.5 = 47.5 |
| Medium severity SAST issue | 50 | 15% | 50 × 0.15 = 7.5 |
| High severity DAST issue | 80 | 30% | 80 × 0.3 = 24 |
| Informational severity issue | 0 | 0% | 0 × 0 = 0 |

The application's risk score is calculated by dividing the sum of weighted issue scores (136.25) by the sum of weights (1.6): 136.25 ÷ 1.6 = 85.15. In this example, rounded to the nearest whole, the application's risk score is 85.
