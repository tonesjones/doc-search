---
title: "About the report database"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-the-report-database.html"
content_id: "Xqvs~QijXklEyCi7_ceGYw"
version: "2026.7"
section: "Reporting Database"
scraped_at: "2026-08-08T15:34:31.921643+00:00"
---

# About the report database

Reporting schemas in the PostgreSQL database, `bds_hub`, provide access to
Black Duck data for reporting purposes. Use any reporting tool that
supports JDBC connections, such as Jasper Reports, to access the data.

With the report database, for example, you can:

- Create a report of the components in a project version.
- Create a report of the vulnerabilities in a component version.
- Query the database to obtain similar information across all of your projects, such as:
  - Selecting all projects with a particular license, phase, and/or
    distribution.
  - Selecting all components using a particular license.
  - Selecting all project/project versions having a particular
    component/component version.

Important: Users should not delete data from the Black Duck database
(`bds_hub`) unless specifically directed to by a Black Duck Technical
Support representative. Deletion of data can cause errors ranging from UI glitches to
complete failure of Black Duck to start.

Important: Note that Black Duck Technical Support cannot recover deleted data and will
only be able to suggest to restore from database backups. If no backups are available,
support from Black Duck will be best-effort only.

Note the following:

- Database name: `bds_hub`
- Username: blackduck_reporter. This user only has read-only access to the
  reporting schema of the database.
- Exposed port: 55436

  If your Black Duck server is hosted by Black Duck Software, the exposed port is 5432.
- Password for blackduck_reporter.
  - If using the database container that is automatically installed by Black Duck, set the password before connecting to the
    database. For more information, see the installation guide for the
    orchestration tool you used to install Black Duck.
  - If using an external PostgreSQL database, use your preferred PostgreSQL
    administration tool to configure the password.

  Once the password is set you can connect to the report database. For
  example, using
  psql:

  ```
  psql -U blackduck_reporter -p 55436 -h localhost -W bds_hub
  ```

  Note: There
  will be a delay for any changes made in Black Duck to appear in
  the report database. The length of time for this delay depends on the value you
  specified for the BLACKDUCK_REPORTING_DELAY_MINUTES environment variable, which
  by default, equals 8 hours. For more information, see the installation guide for
  the orchestration tool you used to install Black Duck.

- The schemas are created automatically when you install or upgrade Black Duck. You will not be able to query the views until after
  the first run of the report database job - the ReportingDatabaseTransferJob. To
  determine if a view is populated, run the following command:

  ```
  SELECT ispopulated FROM pg_catalog.pg_matviews WHERE schemaname = 'reporting' AND matviewname = '<ViewName>'
  ```

  where `ViewName` is the name of the view that interests you.

  For example, to determine if the component policies view is populated, run the
  following command:

  ```
  SELECT ispopulated FROM pg_catalog.pg_matviews WHERE schemaname = 'reporting' AND matviewname = 'component_policies'
  ```
- Black Duck recommends that you write queries with the assumption that columns will
  be added in the future; select specific columns, instead of using the
  all-columns "*" selection method.
- While Black Duck provides the blackduck_reporter user which only has read-only
  access to the reporting schemas of the `bds_hub` database, you
  can configure additional users which have the same permissions as the
  blackduck_reporter.

  Run the following commands, replacing `blackduck_reporter` with
  the username:

  ```
  GRANT USAGE ON SCHEMA reporting TO ${blackduck_reporter}; 
  GRANT SELECT ON ALL TABLES IN SCHEMA reporting TO ${blackduck_reporter}; 
  REVOKE INSERT, UPDATE, TRUNCATE, DELETE, REFERENCES ON ALL TABLES IN SCHEMA reporting FROM ${blackduck_reporter};
  REVOKE ALL ON SCHEMA st FROM ${blackduck_reporter};
  ```
