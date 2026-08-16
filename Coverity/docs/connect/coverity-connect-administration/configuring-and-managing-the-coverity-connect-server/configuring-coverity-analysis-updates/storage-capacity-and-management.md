---
title: "Storage capacity and management"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/storage-capacity-and-management.html"
content_id: "FwoiS2Nf_YdcKT53MVI0fA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:11.278138+00:00"
---

# Storage capacity and management

As Coverity Connect continues to download updates, you can manage the storage space used
for these updates on the Coverity Connect server. The Storage Usage section displays the
current amount of storage being used and also has settings to manually or automatically
remove update files. You can remove updates based on storage limits or the age of the
update file.

The smaller the storage capacity (5 GB is the minimum requirement), the faster the file
purge turnover. This can be desirable if storage space is an issue. However, if network
bandwidth is an issue, then a larger storage capacity can ensure that all update files
are available to the Coverity Analysis user without the need to download update files
from Black Duck each time Coverity Analysis requests an update.

- If no check boxes are selected, then there is no storage limit set and there are
  no daily purges.
- To manage storage on a daily schedule, based on storage limits, select the
  Allow up to check box, then in the
  GB text box, enter the number of GB to set as the
  storage limit. For example, if you want to set the storage capacity to 10 GB,
  enter 10 into the GB text box. (You must allow at least 5
  GB of storage.)

  Now Coverity Connect stores update files only up to the set capacity limit. As
  Coverity Connect continues to download more update files and the storage
  capacity is surpassed, Coverity Connect removes the oldest update files until
  the combined size of the files is within the defined storage capacity.
- To manage storage based on the age of the update file, select the
  Purge files older than check box, then in the
  days text box, enter the number of days to represent
  the update file age limit. For example, if you want to set the age limit to 10
  days, enter 10 into the days text box.

  Now Coverity Connect stores update files only up to the set age limit. As an
  existing update file's age limit is surpassed, Coverity Connect removes the
  update file.
- To immediately purge update files, based on the Storage Usage settings, click the
  Purge Now button. (One or both of the check boxes
  must be selected to use the Purge Now button.) Only update files that match the
  Storage Usage settings are purged. For example, you normally set the daily purge
  storage limit to 10 GB, but you want to free up some storage so that you can
  download more update files and store them locally for the Coverity Analysis user
  to download. In this case, you can enter 5 into the GB text box, and click
  Purge Now. Afterwards, return the storage capacity
  setting to what you previously had it set to. In this case, set it back to 10
  GB.
