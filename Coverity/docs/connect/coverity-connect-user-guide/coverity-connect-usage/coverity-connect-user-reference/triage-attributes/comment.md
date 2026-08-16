---
title: "Comment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/comment.html"
content_id: "no9jbuecy_gRoLLTQZ5BRA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:42.982353+00:00"
---

# Comment

You can provide a comment about the issue in the text field. For example, if an issue is
marked as a Bug, you might use the field to document the reason
for that designation.

## Requiring comments in the triage process

Configure Coverity Connect to require users to provide a
mandatory comment whenever they change a triage attribute on a defect, ensuring a
complete audit trail for all triage decisions.

Before you begin, ensure you have:

- Administrator access to the Coverity Connect
  server
- Ability to restart the Coverity Connect server
- Access to the Coverity Connect configuration or
  `cim.properties` file

1. Locate the Coverity Connect configuration file.
   Navigate to the Coverity Connect server's
   configuration directory and open the server configuration properties file
   where system-level settings are managed.
2. Add or update the following property in the configuration file:

   ```
   triage.require.comment.on.change=true
   ```

   Note: The default value is `false`. When set to
   `false`, triage changes can be made without a comment,
   matching the behavior of previous releases.
3. Restart the Coverity Connect server. Notify all
   active users of the brief downtime before restarting.
4. Verify the feature behavior. Once the server is back online, confirm the
   following behaviors are in effect:

   - **Comment required on attribute changes** — Any attempt to change a
     triage attribute (classification, severity, action, or custom attributes)
     must include a non-empty comment.
   - **Empty comments rejected** — Whitespace-only or blank comments are
     not accepted.
   - **Error on missing comment** — If no comment is provided, the
     operation fails with the error: `A comment is required when
     modifying triage attributes`
   - **Bulk operations enforced** — For bulk triage operations, the entire
     operation fails if no comment is provided; no partial updates
     occur.
   - **No-change saves unaffected** — Triage operations that do not modify
     any attribute do not require a comment.
5. Notify all team members and relevant stakeholders of the change.

   - A comment is now mandatory when modifying any triage attribute on
     defects.
   - Include a clear reason or justification with every triage change.
   - Bulk triage operations require a comment and fail entirely if one is not
     provided.
6. Optional: To revert to the default behavior, set the property to
   `false` and restart the server:

   ```
   triage.require.comment.on.change=false
   ```
