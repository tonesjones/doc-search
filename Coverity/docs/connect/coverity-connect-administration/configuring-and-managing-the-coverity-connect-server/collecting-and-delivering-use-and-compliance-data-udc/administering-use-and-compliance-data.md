---
title: "Administering use and compliance data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/administering-use-and-compliance-data.html"
content_id: "nz42sVjbXf25xNrSkQICZw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:04.171963+00:00"
---

# Administering use and compliance data

The Use and Compliance Data screen allows you to download data that Coverity Connect
sends to Coverity. In addition, some of the fields on the screen, such as
Notification Email, are editable. However, most are
informational only and therefore not editable.

**To use the screen:**

1. Open the Use and Compliance Data screen.

   Navigate to Configuration > System > Usage Data Collection.
2. If you have not done so already, configure and enable email delivery in Coverity
   Connect.

   Navigate to Configuration > System > Email Configuration.

   For the setup procedure, see Configuring Email notification and delivery.
3. Determine which tiers of data Coverity Connect can deliver to Coverity:

   - Compliance data: Coverity product license
     compliance data.
   - Aggregate Usage data: Basic Coverity Connect usage
     data, plus Compliance data.
   - Detailed data: Additional Coverity Connect usage
     data, plus Aggregate Usage data and Compliance data.

   Note: The data tiers are fully described in the PLAs.

   The following data delivery rules are possible:

   - Mandatory: Coverity Connect delivers a given tier
     of data to Coverity at the specified interval. This option is not
     editable.
   - Optional: You can enable or disable the delivery
     of a given tier of data to Coverity. This option defaults to Off. You
     cannot edit the delivery interval.
   - Disabled: Coverity Connect will not deliver a
     given tier of data to Coverity. This option is not editable.

   The following delivery intervals are possible:

   - Weekly: Once per week.
   - Monthly: Once per month.
   - Quarterly: Four times per year.
   - Semi-annually: Two times per year.
   - Annually: Once per year.
4. Receive notification by email of Coverity Connect data collection and delivery
   dates.

   - Notification Email: Coverity Connect sends data
     collection notifications to the email address that you provide in the
     subscription field.

     - To activate notification emails, enter your email address, and
       click Done.

     Upon collection, Coverity Connect will send you one notification per
     enabled tier (Compliance, Aggregate
     Usage, Detailed). All Mandatory
     tiers are enabled. Administrators can enable Optional tiers.

     The notification contains a link to the Use and Compliance Data screen
     and information about the next date on which the data will be sent to
     Coverity. It also identifies the PLA that applies to the data.

     Note: The field will be uneditable if Coverity Connect email is not enabled
     and configured. For the setup procedure, see Configuring Email notification and delivery.

     If
     Coverity Connect email was disabled after an email address was
     added, the disabled subscription field will display that email
     address. To edit the field, you must re-enable Coverity Connect
     email.
5. Download data files that Coverity Connect sends to Coverity:

   - Click the Download button to download an
     *unencrypted* zip file that contains the CSV files. These files
     are generated from the most recent data collection.

     This feature allows you to see what Coverity Connect sends to Coverity.
     On the specified delivery date, Coverity Connect emails the most current
     version of this data to Coverity in an encrypted file.
   - Click the Download Encrypted button to download an
     encrypted file that contains CSV files from the most recent data
     collection. The encrypted file is used for official Coverity
     audits.

   Note: If data delivery is disabled for all tiers, neither button will appear.

   If
   the buttons are not visible even though delivery is enabled for at least one
   of the tiers, then no data files are available for download yet. This
   scenario can occur when you commit data to a new Coverity Connect stream.
   The buttons will appear after the first data collection from the stream
   takes place.
