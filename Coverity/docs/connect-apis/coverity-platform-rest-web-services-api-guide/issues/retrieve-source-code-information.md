---
title: "Retrieve source code information"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-source-code-information.html"
content_id: "kljVj3GaGRCSGAQl4PyFUw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:06.172563+00:00"
---

# Retrieve source code information

Example GET request to retrieve source code-related information for a specified
issue.

Note: In order to return non-null values for
`issueOccurrences.secureCodeWarrior`, the
`securecodewarrior.enabled` property must be set to `true`
in the `cim.properties` file on the Coverity Connect server.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/issues/sourceCodeInfo?\
cid=10033&streamName=testcpp&includeTotalIssueOccurrencesCount=true" \
--header 'Content-Type: application/json' \
--user my_username:my_password
```

**Response body**

```
{
  "checkerName": "USE_AFTER_FREE",
  "domain": "static",
  "issueOccurrences": [
    {
      "domain": "STATIC_C",      
      "events": [
        {
          "eventDescription": "\"operator delete\" frees \"z\".",
          "eventTag": "freed_arg",
          "eventKind": "NORMAL",
          "eventNumber": "1",
          "eventSet": "0",
          "moreInformationUrl": null,
          "pathCondition": null,
          "polarity": null,
          "main": false,
          "lineNumber": "43",
          "file": {
            "contentsMD5": "60b4287fb322aa6ef5f5750599c14aae",
            "filePathname": "/src/test.cpp"
          }
        },
        {
          "eventDescription": "Calling \"f1\" dereferences freed pointer \"z\".",
          "eventTag": "deref_arg",
          "eventKind": "MODEL",
          "eventNumber": "2",
          "eventSet": "0",
          "moreInformationUrl": null,
          "pathCondition": null,
          "polarity": null,
          "main": true,
          "lineNumber": "44",
          "file": {
            "contentsMD5": "60b4287fb322aa6ef5f5750599c14aae",
            "filePathname": "/src/test.cpp"
          }
        }
      ],
      "id": "1085",
      "localEffect": "This could cause an immediate crash or incorrect values might be read subsequently resulting in incorrect computations.",
      "longDescription": "A pointer to freed memory is dereferenced, used as a function argument, or otherwise used",
      "secureCodeWarrior": {
        "learningVideoUrls": [
          "https://media.securecodewarrior.com/v2/Module_63_Use_After_Free_v2.mp4"
        ],
        "portalUrl": "https://portal.securecodewarrior.com/"
      }
    },
    {
      "domain": "STATIC_C",      
      "events": [
        {
          "eventDescription": "\"operator delete\" frees \"z\".",
          "eventTag": "freed_arg",
          "eventKind": "NORMAL",
          "eventNumber": "1",
          "eventSet": "0",
          "moreInformationUrl": null,
          "pathCondition": null,
          "polarity": null,
          "main": false,
          "lineNumber": "42",
          "file": {
            "contentsMD5": "34b13f5ebdcdf3715a1a5e3e6ef460cc",
            "filePathname": "/src/pretest.cpp"
          }
        },
        {
          "eventDescription": "Calling \"f1\" dereferences freed pointer \"z\".",
          "eventTag": "deref_arg",
          "eventKind": "MODEL",
          "eventNumber": "2",
          "eventSet": "0",
          "moreInformationUrl": null,
          "pathCondition": null,
          "polarity": null,
          "main": true,
          "lineNumber": "43",
          "file": {
            "contentsMD5": "34b13f5ebdcdf3715a1a5e3e6ef460cc",
            "filePathname": "/src/pretest.cpp"
          }
        }
      ],
      "id": "1076",
      "localEffect": "This could cause an immediate crash or incorrect values might be read subsequently resulting in incorrect computations.",
      "longDescription": "A pointer to freed memory is dereferenced, used as a function argument, or otherwise used",
      "secureCodeWarrior": {
        "learningVideoUrls": [
          "https://media.securecodewarrior.com/v2/Module_63_Use_After_Free_v2.mp4"
        ],
        "portalUrl": "https://portal.securecodewarrior.com/"
      }
    }
  ],
  "issueOccurrencesCount": 2
}
```
