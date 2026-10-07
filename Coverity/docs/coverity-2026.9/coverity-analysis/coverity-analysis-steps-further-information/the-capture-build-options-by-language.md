---
title: "The capture: Build options by language"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/the-capture-build-options-by-language.html"
content_id: "~TJj1OKYoMf2SVr18M5pVw"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:23.518420+00:00"
---

# The capture: Build options by language

The build options you have might depend on the source language, as shown in the following table:

| Language | Build options |
| --- | --- |
| C, C++, CUDA, Objective-C, Objective-C++ | - Use build capture. |
| C#, Visual Basic C# support relies upon the .NET 10 run time that ships with Coverity Analysis, and any Linux platform that Coverity Analysis build-capture is run on must support .NET 10.  See .NET build capture; also see "C# compilers" in the Coverity Installation and Upgrade Guide. | - Use build capture if you are looking for the most accurate   results and you are okay with integrating the capture into your   build process. - Use the Coverity CLI `coverity capture` command without a build command   if you are looking for the easiest option. |
| Dart | - Use the Coverity CLI `coverity capture` command without   a build command. |
| Docker | - For any version of Docker, use the Coverity CLI   `coverity capture` command without a build command. |
| Go | - If you are looking for the most accurate   results and you are okay with integrating the capture into your   build process, use build capture. - If you are looking for the easiest option, use the Coverity CLI `coverity capture` command without   specifying a build command.   Your project must meet the conditions outlined for Go in the "Support matrix"   section of the Guide to the Coverity Point and Scan UI and the Coverity CLI. |
| Groovy | - For any version of Groovy, use the Coverity CLI   `coverity capture` command without a   build command. |
| HTML, JavaScript, TypeScript | - Use the Coverity CLI `coverity   capture` command without a build command. |
| Java | - Use build capture if you are looking for the most accurate   results and you are okay with integrating the capture into your   build process. - Use the Coverity CLI `coverity capture` command without a build command   if you are looking for the easiest option. |
| Kotlin | - Use the Coverity CLI `coverity   capture` command without a build command. |
| PHP, Python, Ruby | - Use the Coverity CLI `coverity   capture` command without a build command. |
| Rust | - Use build capture. |
| Scala | - For any version of Scala, use the Coverity CLI   `coverity capture` command without a build command. |
| Swift | - For any version of Swift, use the Coverity CLI   `coverity capture` command without a build command. |
| Terraform | - For any version of Terraform, use the Coverity   CLI `coverity capture` command without a build command. |
