---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "7dHwzgJW~zzeHE58jodhOQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:47.235591+00:00"
---

# Examples

**Example request for JSON output**

`curl --user admin:password "localhost:8080/api/view/v1/views"`

**Example request for CSV file**

`curl --header "Accept: text/csv" --user admin:password
"localhost:8080/api/view/v1/views" > outputFile.csv`

**Example JSON response body**

```
{
  "All Views Status": [
    {
      "viewId":"10002",
      "viewName":"Currently Failing",
      "owner": {
        "username":"admin",
        "ldapServer":"my_ldap_server.my_domain.com"
      },
      "sharedUsers": [],
      "sharedGroups":[],
      "hasViewNotifications":false,
      "ownerActive":true,
      "ownerDeleted":false
    },
    {
      "viewId":"10006",
      "viewName":"Uncovered By Tests",
      "owner": {
        "username":"admin",
        "ldapServer":"my_ldap_server.my_domain.com"
      },
      "sharedUsers":[],
      "sharedGroups":[],
      "hasViewNotifications":false,
      "ownerActive":true,
      "ownerDeleted":false
    }
  ]
}
```

**Example CSV file**

```
curl -H "Accept: text/csv" --user "admin:pass" "http://localhost:8080/api/view/v1/views"
VIEW ID|VIEW NAME|OWNER|SHARED USERS|SHARED GROUPS|ACTIVE OWNER|DELETED OWNER|HAS NOTIFICATIONS
10002,Currently Failing,(admin;my_ldap_server.my_domain.com),,,true,false,false
10006,Uncovered By Tests,(admin;my_ldap_server.my_domain.com),,,true,false,false
10114,High Issue Density (>1),(testing;my_ldap_server.my_domain.com),,,true,false,false
```
