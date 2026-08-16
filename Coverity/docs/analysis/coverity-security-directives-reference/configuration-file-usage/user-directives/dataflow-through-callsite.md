---
title: "dataflow_through_callsite"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/dataflow_through_callsite.html"
content_id: "1SBTedwJ~WyDOccyAEeviw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:40.554741+00:00"
---

# dataflow_through_callsite

**Languages: JavaScript**

The `dataflow_through_callsite` directive tells the analysis how data
flows from arguments to return values or to other function outputs for calls to a
particular function.

## Fields

This directive uses the following fields:

`dataflow_through_call_site`
:   Specifies a CallsiteSet that indicates
    the function call sites to which this directive applies.

`from`
:   Specifies a non-empty JSON array of InputAndAccessPathSpecifier values that indicate the inputs to the function that flow to the
    outputs specified in the `to` field.

`to`
:   Specifies a non-empty JSON array of OutputAndAccessPathSpecifier values that indicate the outputs of the function that correspond to
    the inputs specified in the `from` field.
