---
title: "Enabling and disabling checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enabling-and-disabling-checkers.html"
content_id: "jq0RM0_hYtkRvM2z_abqsg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:15.914826+00:00"
---

# Enabling and disabling checkers

Coverity Analysis runs checkers that are enabled and are covered by
your license. Many Coverity checkers are enabled by default, so they will run unless you
explicitly disable them. Other checkers are disabled by default, and will not run unless
explicitly enabled.

Coverity Analysis allows you to enable or disable any checker. Default
enablement often varies by programming language, so a checker that supports multiple
languages might be enabled by default for one language but disabled by default for
another. You can explicitly enable a checker for all languages to which it applies, or
you can disable the checker entirely. (Specifying exactly which checkers to run for a
particular language is only possible with separate analysis by language.)

The decision to disable or enable a checker or checker group depends on the types of
issues that your organization wants Coverity Analysis to detect. It
might also depend on Coverity Analysis performance requirements,
because the greater the variety of checkers that you run, the longer it can take for Coverity Analysis to complete the analysis.

Remember: In addition to enabling and disabling checkers, you can use checker
options to tune the analysis. For example, to improve the value of
`NULL_RETURNS` defects to your organization, you might raise or lower
the threshold used by that checker. To specify checker option values, you use the option
`--checker-option` to the `cov-analyze`
command. For details, see the Coverity 2026.6.0 Checker Reference.

In this section:

- Enabling and disabling checkers with 'cov-analyze'
- Enabling compilation warning checkers (PW.*, RW.*, SW.*)
