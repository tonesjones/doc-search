---
title: "Import Coverity Connect license file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/import-coverity-connect-license-file.html"
content_id: "vdB9OBYlduR9AONfdi1YZQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:13.926243+00:00"
---

# Import Coverity Connect license file

Example POST request to import a Coverity Connect license file
(`license.dat`).

**cURL request**

```
curl --location \
--request POST "http://my_connect_host:8080/api/v2/licenses" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "licenseDataFile":"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
  <!DOCTYPE coverity SYSTEM \"license.dtd\">\
  <coverity> <license> <version>8</version> <product>Integrity Manager</product>\
  <valid-until>2022-Jan-23 08:00:00 UTC</valid-until> <customer>Coverity</customer>\
  <project>Testing</project> <cov-0>532252800</cov-0>\
  <options> <option> <name>desktop-analysis</name> <value>no</value> </option>\
  <option> <name>max-lines-of-code</name> <value>1000000</value> </option>\
  <option> <name>max-users</name> <value>10</value> </option>\
  <option> <name>rbac</name> <value>no</value> </option>\
  <option> <name>record-id</name> <value>recordid</value> </option>\
  <option> <name>udc-tiers</name> <value>1mw2os3ua</value> </option>\
  <option> <name>valid-from</name> <value>20210123</value> </option> </options>\
  <cov-1>AAAAfEdc1dHQMR01rHLL0dch0avPXKQoiwD03OjuZfRxtwGbXC \
i15tEIKJEcdzn4Aao0TczVs33cMnZFSjdpTmRUzoH4Y2PHDUQz \
/6gCjh/8Dng8Gt/VSDm7DG7nU9mM+hEr5H5YPIWUNC9NFy2TSW \
Oq7kJnSHa6J9BgXEgVBJqJzDP5=</cov-1> </license> </coverity>"
}'
```
