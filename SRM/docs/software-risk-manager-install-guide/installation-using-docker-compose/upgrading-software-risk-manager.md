---
title: "Upgrading Software Risk Manager"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/upgrading-software-risk-manager.html"
content_id: "ZnwsCCr3y0zJyn6bx3KlUw"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:12.337258+00:00"
content_hash: "1b12a75a1046f7da4ccfc2f62cd49529e7dd47b908c564e8a42a3c4d9712ecad"
---

# Upgrading Software Risk Manager

This section details how to upgrade Software Risk Manager to the latest version.

Note: It is recommended that you create a backup of your Software Risk
Manager Docker Compose environment before upgrading to the latest Software Risk Manager
version.

Remove your Software Risk Manager container(s) before starting the upgrade. (Do not use the
`-v` switch with the `down` command because it will delete
your data volumes.)

```
docker-compose -f /path/to/your-docker-compose-file down
```

The recommended upgrade method is to pull the latest changes from GitHub. The Docker Compose
file is updated with each Software Risk Manager release to reference the latest Docker image
versions. Edits to local files, such as your Docker Compose file, may block your pull from
GitHub, so use the following commands to stash your changes and reapply them after your
pull:

```
cd /path/to/srm-docker
git stash save before-upgrade
git pull
git stash apply
```

If you see a "Merge conflict" message when you run `git stash apply`, edit the
flagged file to resolve the conflict, then run `git add /path/to/file` to mark
the file as merged.

If you do not want to use Git, you can alternatively download the latest [ZIP file](https://github.com/codedx/srm-docker/archive/refs/heads/master.zip) from GitHub. (If you use the ZIP to replace an existing folder, you must
reapply any local edits, such as the changes you made to your Docker Compose file.)

Once you have the latest changes, run your Docker Compose `up` command to
start Software Risk Manager:

```
docker-compose -f /path/to/your-docker-compose-file up
```
