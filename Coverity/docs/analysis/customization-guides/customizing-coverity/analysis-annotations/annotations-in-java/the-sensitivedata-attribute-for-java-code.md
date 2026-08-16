---
title: "The '@SensitiveData' attribute for Java code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-sensitivedata-attribute-for-java-code.html"
content_id: "fZM9ezVS_u_4g9avbVyrMg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:29.814613+00:00"
---

# The '@SensitiveData' attribute for Java code

In the following example, if the return value of `returnsPassword` or
the argument passed to `storesPasswordInParam` passes to a sink, the
checker will report a defect of type `Cleartext sensitive data in
<sink>`:

```
@SensitiveData({SensitiveDataType.SDT_PASSWORD})

Object returnsPassword() {
    // This function returns password data.
}
    
void storesPasswordInParam(
    @SensitiveData( {SensitiveDataType.SDT_PASSWORD} ) Object arg1 ) {
        // The parameter arg1 will be treated as password data.
    }
    
    // The field pw will be treated as password data.
    @SensitiveData( {SensitiveDataType.SDT_PASSWORD} ) String pw;
```

As with Coverity primitives, you can use Coverity annotations to specify multiple sensitive
data types. To do so, simply provide a comma-separated list of
`SensitiveDataType` enumerations within the curly braces for the
`@SensitiveData annotation`. For more information on sensitive
data types and modeling sensitive data sources, see Sensitive data source types.
