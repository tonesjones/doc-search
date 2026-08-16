---
title: "Collecting and delivering use and compliance data (UDC)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/collecting-and-delivering-use-and-compliance-data-udc-.html"
content_id: "Ad1lY_fLAmJVCAOtjOJypw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:03.534620+00:00"
---

# Collecting and delivering use and compliance data (UDC)

Starting in version 5.4, Coverity Connect collects Use and Compliance data from streams
on a regular basis. If permitted under the terms of your Product License Agreement
(PLA), Coverity Connect also sends a set of this data to Black Duck. The PLA sets forth
the frequency of data delivery and the types of stream data that Coverity Connect can
send to Black Duck.

Data Collection
:   Coverity Connect collects data from the most recent commit to Coverity
    Connect streams. If the Coverity Connect server is down during the
    collection period, Coverity Connect skips the data collection process that
    week and resumes the next week. Data collection takes place on
    Saturdays.

    You can receive notification when Coverity Connect collects data. For
    details, see Administering use and compliance data.

Data Delivery
:   Coverity Connect delivers the data to Black Duck at an interval that is
    specified in the PLA. Each PLA applies to Coverity commands that analyze
    source code and commit the results to Coverity Connect streams, for example,
    the Coverity Analysis `cov-analyze` and
    `cov-commit-defects` commands. PLAs can indicate which
    portion of the data collected from the stream, if any, Coverity Connect will
    deliver to Black Duck.

    The data is contained in a set of CSV files, which Coverity Connect packages
    into an encrypted file that it sends to Black Duck.

    If the PLA allows, you can enable or disable the delivery of data to
    Black Duck. For details, see Administering use and compliance data.

Important: For Coverity Connect to email data to Black Duck, you must configure
and enable Coverity Connect email. Setting up Coverity Connect email also allows
Coverity Connect to send data collection and delivery notifications to you. For the
setup procedure, see Configuring Email notification and delivery.

The
<install_dir>/logs/cim.log file provides license
information for each commit of analyzed data to Coverity Connect.
