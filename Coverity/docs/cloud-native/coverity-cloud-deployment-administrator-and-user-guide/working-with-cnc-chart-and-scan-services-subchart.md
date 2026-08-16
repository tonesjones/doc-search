---
title: "Working with cnc chart and scan-services subchart"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/working-with-cnc-chart-and-scan-services-subchart.html"
content_id: "4JeniUoFjKxAv~djxkmkMg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:12.866924+00:00"
---

# Working with cnc chart and scan-services subchart

This chapter provides guidance of how you might work with the Helm charts and keys when
planning and configuring a Coverity cloud deployment. This covers the following:

- Introduces the `cnc` and `scan-services` Helm charts
  and Helm keys, and how to work with the charts and keys.
- Describes hhow you can view the default Helm charts.

When configuring Helm overrides, you must be:

- knowledgeable of the Helm chart changes, and
- knowledgeable of parent charts, subcharts, and global key values.

Also, you need to consider the following:

- The `cnc` chart can override values in the
  `scan-services` subchart; a parent chart can override subchart
  values.
- The `scan-services` subchart can not access values from the parent
  `cnc` chart.
- Global Helm key values can be accessed by both charts.
- Global Helm key values can be overridden by service-specific values.

For further information on working with subcharts, refer to [Subcharts and Global Values](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).

When you either create a custom `.yaml` file or set a Helm key within a
command such as a `helm install` command, you must:

- **For `cnc` chart keys**: Include `cnc` chart Helm
  keys using the syntax defined in the `cnc` chart's
  `values.yaml` file. The `cnc` chart is the parent
  chart, therefore you do not need to prepend keys with the chart name to identify the
  chart.
- **For `scan-services` subchart keys**: You must prepend any keys
  from a subchart with the subchart name. Therefore, you must prepend
  `scan-services` subchart Helm keys with
  `scan-services` to identify them as
  `scan-services` subchart keys.
- **For `global` keys**: Provide global Helm keys using the global
  syntax specified in the Helm chart.
