---
title: "Tainted data overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tainted-data-overview.html"
content_id: "ymJyzmc5Hfaco0xeYec9Kg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:19.808118+00:00"
---

# Tainted data overview

Some kinds of data can be dangerous for programs to consume, and lead to system
crashes, corruption, escalation of privileges, or denial of service. Data of this sort is
known as *tainted data*.

If tainted data is passed through a filter, or sanitizer, it can be made safe for
consumption. A number of security checkers perform this kind of sanitization.

Tainted data can come from a number of different kinds of sources, such as user input,
network connections, and filesystems or databases.

Based on the origin of the data, tainted data has a particular *taint kind* such as
`filesystem`, `cookie`, `network`, and
so on.
For example, the `llm` taint kind indicates data that is considered unsafe because it comes from
the output of a large language model (LLM) system.

A tainted data checker can be configured to distrust only certain taint kinds and
trust the other kinds. For example, network connections could be treated dangerous by
distrusting the `network` taint kind, while filesystem contents could be
treated as safe by trusting the `filesystem` taint kind.

For best results, the default configuration of our checkers trusts certain taint kinds
that in practice are less likely to be dangerous. The default trust model can be changed
to trust or distrust a particular taint kind by changing the analysis settings: either
globally for all tainted-data checkers, or individually per checker by setting checker
options.

A separate category, *sensitive data,* deals with data that is not necessarily
dangerous, but that should be managed as a secret. Examples include personal
information, business information, and information categorized as *classified* by a
government agency.

Data can be considered sensitive independently of whether it is considered tainted. A
checker is typically concerned with only one of these two aspects and ignores the other
aspect. See Sensitive data overview.

Checkers concerned with tainted data include the following (remember that the set of
checkers can change with each release of Coverity):

- ANGULAR_EXPRESSION_INJECTION
- COOKIE_INJECTION
- EL_INJECTION
- FORMAT_STRING_INJECTION
- HEADER_INJECTION
- JAVA_CODE_INJECTION
- JCR_INJECTION
- JSP_SQL_INJECTION
- LDAP_INJECTION
- NOSQL_QUERY_INJECTION
- OGNL_INJECTION
- OS_CMD_INJECTION
- REGEX_INJECTION
- SCRIPT_CODE_INJECTION
- SQLI
- TAINT_ASSERT
- TAINTED_ENVIRONMENT_WITH_EXECUTION
- TAINTED_SCALAR
- TAINTED_STRING
- TEMPLATE_INJECTION
- UNKNOWN_LANGUAGE_INJECTION
- XML_INJECTION
- XPATH_INJECTION
- XSS
