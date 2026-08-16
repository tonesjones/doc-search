---
title: "Limitations and considerations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/limitations-and-considerations.html"
content_id: "qAquvPsCBWUarHvTP0n_gQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:51:17.944639+00:00"
---

# Limitations and considerations

cov-archive command.

Limitations
:   - The following data are not exported:

      - Cross references
      - Issue categorization maps
      - Component maps
      - Components
      - Licenses and users ("Committed by") associated with snapshots
      - The `bindPassword` of LDAP configurations

        This must be set after importing either manually or via the
        Web Services API: See the Coverity Platform 2026.6.0 SOAP Web Services API Reference and the Coverity Platform 2026.6.0 REST Web Services API Guide for more
        information.
    - You cannot import individual streams from an archive.

Considerations
:   - Imported triage stores (and associated data) are not merged.
      Instead, a new triage store is created in the target database.
    - Attribute definitions in the target database must be the same
      (and defined using the same index order), otherwise the import
      will fail.
    - LDAP configurations are merged based on their display name. If
      the target database has a configuration with the same UUID but a
      different display name, the import will fail.
    - Users are imported in a disabled state, and user preferences are not
      exported.
      - If a user in the archive is already present in the target
        database, that user will not be disabled and preferences will be
        preserved.
      - Users are merged if they have the same login name, deleted
        status, and LDAP configuration (which may or may not be merged,
        as described above).
    - Only stream-level user/group role assignments are exported. Role
      permissions are not exported because importing them may change
      access to other entities in the target Coverity Connect
      instance. When importing role assignments, each role is imported
      (without its permissions) if it does not exist in the target
      database, otherwise the existing role is used.
    - CIDs of imported issues are preserved unless they are empty or
      they belong to a different pre-existing issue.
