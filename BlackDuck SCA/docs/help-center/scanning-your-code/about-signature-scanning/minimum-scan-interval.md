---
title: "Minimum Scan Interval"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/minimum-scan-interval.html"
content_id: "kzO6sCFXHw0yWP2ZYoLrSg"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:10.794918+00:00"
content_hash: "200d4aae63223f39367e31153ca5f92d9987485492a0c0ca4cb36052b200ca70"
---

# Minimum Scan Interval

This setting allows users to change the maximum hourly frequency of which signature scans can be performed for a given code location when using the enhanced signature scanning. This will allow customers to reduce the load on their servers, thus making scans running faster and with less errors which result from overloading the server.

The default setting is set to 0, or no maximum scan interval, meaning scans are not prevented from occurring regardless of frequency. If set to greater than 0, signature scans will not be processed if they occur before the set scan interval. For example, a setting of 4 will not allow signature rescans before 4 hours of time have elapsed.

Note: For users of Detect 8 and 9, Detect will only finish with a success message in this scenario if the `detect.force.success.on.skip` value has been changed to true. (Default is false). Please see [Detect's Configuration Property Details](https://docs.blackduck.com/access?ft:originId=9c0814dc6c47bd8e1b015657cf47a869/fd537c29bc43c6f14b90ef2461ac87b0.topic) page for more information.

## Changing the minimum scan interval

Users with the system administrator role can change this setting by:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Select **System Settings**.
4. Click **Scan**.
5. Under **Minimum Scan Interval**, enter an integer for the number of hours between subsequent signature scans.
6. Click **Save**. To indicate that the default value has changed, the button changes to **Saved**.
