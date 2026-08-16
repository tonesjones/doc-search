---
title: "Examples of tainted data"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples-of-tainted-data.html"
content_id: "mkCz9H~D32Gj3Vqn3a~JAw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:21.085720+00:00"
---

# Examples of tainted data

The HEADER_INJECTION checker can detect tainted data, but to do so it must be
configured to distrust the appropriate sources.

Here is sample code that uses a file to store HTTP headers:

```
class Test : Activity() {
    fun loadFunPage(
            context: Context,
            webView: WebView,
            additionalHeaders: MutableMap<String, String>
        ) {
              val file = File(
                       context.getExternalFilesDir(null),
                       "saved-extra-headers.txt"
                   )
              val content = file.readText()

              for (pair in content.split(",")) {
                  val (key, value) = pair.split("=")
                  additionalHeaders[key] = value
              }
    
              webView.loadUrl("www.fun.com", additionalHeaders)
          }
}
```

Suppose an attacker had read/write permissions for
saved-extra-headers.txt. In this case, the attacker could
control the HTTP headers of requests sent to the server.

By default, the HEADER_INJECTION checker trusts the `filesystem` taint
kind, so it would not detect this particular vulnerability. You could instruct
HEADER_INJECTION to *distrust* the `filesystem` taint kind, in which
case Coverity would report this vulnerability. The following command line has this
effect:

```
$cov-analyze --checker-option HEADER_INJECTION:trust_filesystem:false
```

You could also detect the header-injection vulnerability by invoking
`cov-analyze` as follows:

```
$cov-analyze --distrust-filesystem
```

... but this invocation applies to *all* checkers, and is more likely to generate
false positives than the checker-specific invocation.
