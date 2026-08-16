---
title: "BDSA Auto Remediation"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/bdsa-auto-remediation.html"
content_id: "F~sQfP94EgKdvjV8WU2lBA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:18.967312+00:00"
---

# BDSA Auto Remediation

When the Black Duck Security Advisory (BDSA) team analyzes a CVE vulnerability, they
check to see what component versions are affected by the vulnerability. Sometimes they
find that the vulnerability applies to a different set of versions. This feature will
give you the ability to automatically ignore CVE vulnerabilities if the BDSA team has
found that the vulnerability does not apply to that component version.

This setting only applies to CVE vulnerabilities with a related BDSA vulnerability. If
the CVE is mapped to a component version, but its related BDSA is not also mapped to
that component version then the system may automatically remediate the CVE vulnerability
based on the feature setting.

  
 [image: image]

## Changing the BDSA Auto Remediation setting

To change the BDSA Auto Remediation setting:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: image] .
3. Select **System Settings**.
4. Click **BDSA Auto Remediation**.
5. Check the **Enable BDSA auto remediation** checkbox to activate the
   feature or remove the check to disable it.
6. Click the **Save** button to save the current setting (on or off) for the BDSA Auto
   Remediation feature and apply the changes going forward for all new scans.
   It will not update any existing CVEs.

   - **Save and Apply**: Clicking this button will save the current
     setting and apply the changes going forward for all new scans as
     well as updating all existing CVE vulnerabilities. The button's
     behavior changes depending on whether the feature is being activated
     or deactivated.

     If you have activated the BDSA Auto Remediation feature, NEW status
     CVEs with a related BDSA that are not also mapped to that component
     version will be auto remediated by changing the remediation status
     from NEW to IGNORED. The system will also add a message to describe
     why the vulnerability was remediated

     If you have deactivated the BDSA Auto Remediation feature, click the
     Save and Apply button will undo all auto remediations performed
     prior. Undoing an auto remediation will change the remediation
     status of an auto remediated vulnerability from IGNORED to NEW as
     well as remove the message that was added to the remediation.

     Changing this setting will initiate the AutoRemediateUnmappedJob job
     which will process the changes above. This process may take some
     time depending on the quantity of updates needed to perform. You can
     cancel this job by clicking the Cancel Job button.

       
      [image: image]   

     Note: Canceling this process will not revert changes made during the process. The **Save**
     and **Save and Apply** buttons will also be disabled during this
     process.

For more information regarding Black Duck Security Advisories and how to remediate
vulnerabilities, please refer to:

- Black Duck Security
  Advisories
- Remediating
  security vulnerabilities
