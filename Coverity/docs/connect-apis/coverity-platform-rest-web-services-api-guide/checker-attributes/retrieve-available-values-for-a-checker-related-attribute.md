---
title: "Retrieve available values for a checker-related attribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-available-values-for-a-checker-related-attribute.html"
content_id: "s7gbCxcn3dMKEsCiddBNdg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:34.970690+00:00"
---

# Retrieve available values for a checker-related attribute

Example GET request to retrieve the available values for the Category checker
attribute.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/checkerAttributes/displayCategory" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "checkerAttribute": {
    "name": "displayCategory",
    "displayName": "Category"
  },
  "checkerAttributedata": [
    {
      "key": "Miscellaneous",
      "value": "Miscellaneous"
    },
    {
      "key": "API usage errors",
      "value": "API usage errors"
    },
    {
      "key": "Build system issues",
      "value": "Build system issues"
    },
    {
      "key": "Class hierarchy inconsistencies",
      "value": "Class hierarchy inconsistencies"
    },
    {
      "key": "Code maintainability issues",
      "value": "Code maintainability issues"
    },
    {
      "key": "Compiler dependency",
      "value": "Compiler dependency"
    },
    {
      "key": "Concurrent data access violations",
      "value": "Concurrent data access violations"
    },
    {
      "key": "Control flow issues",
      "value": "Control flow issues"
    },
    {
      "key": "Data race undermines locking",
      "value": "Data race undermines locking"
    },
    {
      "key": "Error handling issues",
      "value": "Error handling issues"
    },
    {
      "key": "Exceptional resource leaks",
      "value": "Exceptional resource leaks"
    },
    {
      "key": "High impact security",
      "value": "High impact security"
    },
    {
      "key": "Incorrect expression",
      "value": "Incorrect expression"
    },
    {
      "key": "Insecure data handling",
      "value": "Insecure data handling"
    },
    {
      "key": "Integer handling issues",
      "value": "Integer handling issues"
    },
    {
      "key": "Low impact security",
      "value": "Low impact security"
    },
    {
      "key": "Medium impact security",
      "value": "Medium impact security"
    },
    {
      "key": "Memory - corruptions",
      "value": "Memory - corruptions"
    },
    {
      "key": "Memory - illegal accesses",
      "value": "Memory - illegal accesses"
    },
    {
      "key": "Microsoft: Miscellaneous",
      "value": "Microsoft: Miscellaneous"
    },
    {
      "key": "Null pointer dereferences",
      "value": "Null pointer dereferences"
    },
    {
      "key": "Parse warnings",
      "value": "Parse warnings"
    },
    {
      "key": "Performance inefficiencies",
      "value": "Performance inefficiencies"
    },
    {
      "key": "Possible Control flow issues",
      "value": "Possible Control flow issues"
    },
    {
      "key": "Program hangs",
      "value": "Program hangs"
    },
    {
      "key": "Resource leaks",
      "value": "Resource leaks"
    },
    {
      "key": "Rule violations",
      "value": "Rule violations"
    },
    {
      "key": "Security best practices violations",
      "value": "Security best practices violations"
    },
    {
      "key": "Strict rule violations",
      "value": "Strict rule violations"
    },
    {
      "key": "Test advisor issues",
      "value": "Test advisor issues"
    },
    {
      "key": "Uninitialized members",
      "value": "Uninitialized members"
    },
    {
      "key": "Uninitialized variables",
      "value": "Uninitialized variables"
    },
    {
      "key": "Unreliable locking behavior",
      "value": "Unreliable locking behavior"
    },
    {
      "key": "FindBugs: Bad practice",
      "value": "FindBugs: Bad practice"
    },
    {
      "key": "FindBugs: Bogus random noise",
      "value": "FindBugs: Bogus random noise"
    },
    {
      "key": "FindBugs: Correctness",
      "value": "FindBugs: Correctness"
    },
    {
      "key": "FindBugs: Dodgy code",
      "value": "FindBugs: Dodgy code"
    },
    {
      "key": "FindBugs: Experimental",
      "value": "FindBugs: Experimental"
    },
    {
      "key": "FindBugs: Internationalization",
      "value": "FindBugs: Internationalization"
    },
    {
      "key": "FindBugs: Malicious code vulnerability",
      "value": "FindBugs: Malicious code vulnerability"
    },
    {
      "key": "FindBugs: Multithreaded correctness",
      "value": "FindBugs: Multithreaded correctness"
    },
    {
      "key": "FindBugs: Performance",
      "value": "FindBugs: Performance"
    },
    {
      "key": "FindBugs: Security",
      "value": "FindBugs: Security"
    },
    {
      "key": "Array access before checking the index",
      "value": "Array access before checking the index"
    },
    {
      "key": "Audit impact security",
      "value": "Audit impact security"
    },
    {
      "key": "Bad call to a virtual method",
      "value": "Bad call to a virtual method"
    },
    {
      "key": "Bad comparison of floating-point expressions",
      "value": "Bad comparison of floating-point expressions"
    },
    {
      "key": "Detekt",
      "value": "Detekt"
    },
    {
      "key": "Exposed non-const static field",
      "value": "Exposed non-const static field"
    },
    {
      "key": "High impact quality",
      "value": "High impact quality"
    },
    {
      "key": "Insecure random category",
      "value": "Insecure random category"
    },
    {
      "key": "Low impact quality",
      "value": "Low impact quality"
    },
    {
      "key": "Medium impact quality",
      "value": "Medium impact quality"
    },
    {
      "key": "Overly broad exception",
      "value": "Overly broad exception"
    },
    {
      "key": "PMDApex",
      "value": "PMDApex"
    },
    {
      "key": "PMDVisualForce",
      "value": "PMDVisualForce"
    },
    {
      "key": "Sigma",
      "value": "Sigma"
    },
    {
      "key": "SpotBugs: Bad practice",
      "value": "SpotBugs: Bad practice"
    },
    {
      "key": "SpotBugs: Bogus random noise",
      "value": "SpotBugs: Bogus random noise"
    },
    {
      "key": "SpotBugs: Correctness",
      "value": "SpotBugs: Correctness"
    },
    {
      "key": "SpotBugs: Dodgy code",
      "value": "SpotBugs: Dodgy code"
    },
    {
      "key": "SpotBugs: Experimental",
      "value": "SpotBugs: Experimental"
    },
    {
      "key": "SpotBugs: Internationalization",
      "value": "SpotBugs: Internationalization"
    },
    {
      "key": "SpotBugs: Malicious code vulnerability",
      "value": "SpotBugs: Malicious code vulnerability"
    },
    {
      "key": "SpotBugs: Multithreaded correctness",
      "value": "SpotBugs: Multithreaded correctness"
    },
    {
      "key": "SpotBugs: Performance",
      "value": "SpotBugs: Performance"
    },
    {
      "key": "SpotBugs: Security",
      "value": "SpotBugs: Security"
    },
    {
      "key": "Implicit type conversion",
      "value": "Implicit type conversion"
    },
    {
      "key": "Unused entity",
      "value": "Unused entity"
    },
    {
      "key": "Non-optimal type conversion",
      "value": "Non-optimal type conversion"
    },
    {
      "key": "Information",
      "value": "Information"
    },
    {
      "key": "Syntax error",
      "value": "Syntax error"
    },
    {
      "key": "Undefined entity",
      "value": "Undefined entity"
    },
    {
      "key": "Code improvement",
      "value": "Code improvement"
    },
    {
      "key": "Undeclared entity",
      "value": "Undeclared entity"
    },
    {
      "key": "Multiple declaration of entity",
      "value": "Multiple declaration of entity"
    },
    {
      "key": "Portability",
      "value": "Portability"
    },
    {
      "key": "Incorrect usage of entity",
      "value": "Incorrect usage of entity"
    },
    {
      "key": "Coding standard violation",
      "value": "Coding standard violation"
    },
    {
      "key": "$category$",
      "value": "$category$"
    }
  ],
  "code": null,
  "message": null
}
```
