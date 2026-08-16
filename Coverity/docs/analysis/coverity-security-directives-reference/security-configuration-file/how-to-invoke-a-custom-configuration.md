---
title: "How to invoke a custom configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/how-to-invoke-a-custom-configuration.html"
content_id: "rffcrfafzcM~8DfXwCCpsw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:28.507863+00:00"
---

# How to invoke a custom configuration

When you have created a custom configuration file, you can use it in analysis by passing
it to the `cov-analyze` command.

The `--directive-file` option can specify a configuration file that uses
any directives *other than*
`dc_checker_name` and `method_set_for_dc_checker`. For
examples of what these other kinds of directives can do, see Uses of directives.

For example, here is a configuration to define a dataflow checker that identifies and
warns about an API to which user-controllable data should not be passed:

```
{
  sink_for_checker : "DF.DANGEROUS_ROBOT",
  sink : {
    to_callsite : {
      callsite_with_static_target : {
        "named" : "battle.robot.api.RobotService.run(java.lang.String, int)void"
      },
    },
    input : "arg1"
  }
}
```

To use DF.DANGEROUS_ROBOT in an analysis, you might save this configuration as
dangerous_robot.json and then use a command line such as the
following:

```
cov-analyze --dir localTempDir --directive-file dangerous_robot.json
```

(For more information about this sample checker, see the description of
"DF.*CUSTOM_CHECKER"* in the
Coverity 2026.6.0 Checker Reference.)

Note: To specify the configuration file for a DC.*CUSTOM_CHECKER,* whose use is now
discouraged, required a different `cov-analyze` option,
`--dc-config`.

When you invoke `cov-analyze`, you can specify more than one
configuration file, in order to use more than one configuration in your analysis. For
example, you might want to test both C++ and Java source in a single scan.
