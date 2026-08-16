---
title: "Custom database queries"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/custom-database-queries.html"
content_id: "X8UM6JKLbRXt8bkiM1LLxw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:09.186165+00:00"
---

# Custom database queries

An administrator can create custom database queries and set them to appear in the
Database tab. The queries are entered into a file as a YAML document, with the format
shown in this example:

```
queries:
       - name: A
         sql: select * from users
       - name: B
         sql: select * from project
       - name: C
         sql: select * from user_group
```

Note: Do not perform any data definition language (DDL) or data manipulation language (DML)
operations on the content of a Coverity Connect database unless Coverity Support
specifically instructs you to do so. Otherwise, all of your Coverity Connect data may
become unusable and unrecoverable. This restriction applies whether you are using the
embedded database or an external one.

Coverity Support will not assist you in the
recovery of data that gets corrupted due to such an update of the
database.

For more information about YAML, a type of markup language, see <https://yaml.org/>.

**To create a custom query:**

1. Create a text file using the format shown above.
2. Save the text file in the installation directory of Coverity Connect, with the
   name `customQueries.yml`.
3. Select the **Query** drop-down on the **Database** tab, and select the name of a custom query.
