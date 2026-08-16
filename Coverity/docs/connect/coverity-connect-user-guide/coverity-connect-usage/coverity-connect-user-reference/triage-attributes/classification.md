---
title: "Classification"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/classification.html"
content_id: "BmkokrHGuAfZ9_8kRQETOA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:38.670494+00:00"
---

# Classification

Unclassified
:   Default for a new issue. It is intended for issues that have yet to be viewed
    by a developer.

Pending
:   An issue that should be fixed eventually, but perhaps it is not critical
    enough to fix in the current source code base, or there are other
    dependencies that prevent it from being fixed at this time.

False Positive
:   An issue that a developer has examined and deemed not a true (actual) bug. If
    a false positive appears to reflect shortcomings or flaws in the analysis
    engine, please report the issue at
    <https://community.blackduck.com/s/contactsupport>.

Intentional
:   An issue that might be a true (actual) bug according to the code's
    programming language but that is not a bug in this code because either the
    code is not important or the code can never be exercised in a dangerous way
    in deployment environments.

Bug
:   Reflects a determination that the issue found through a Coverity analysis
    process is an issue in the code, and is not a false positive or intentional
    issue.

Untested
:   Reflects a determination that a section of the code analyzed by Test Advisor
    requires that a test be added to the code. This classification is no longer
    valid since Test Advisor is end-of-life and unavailable as of the 2021.9.0
    release.

No Test Needed
:   Reflects a determination that even though the Test Advisor analysis found a
    section of code that is not covered by a test, you are aware of the
    violation and that there is an accepted reason that the code is not covered.
    This classification is no longer valid since Test Advisor is end-of-life and
    unavailable as of the 2021.9.0 release.

Tested Elsewhere
:   Indicates that a section of code is tested by a test outside the tests
    specified in the Test Advisor analysis process. This classification is no
    longer valid since Test Advisor is end-of-life and unavailable as of the
    2021.9.0 release.
