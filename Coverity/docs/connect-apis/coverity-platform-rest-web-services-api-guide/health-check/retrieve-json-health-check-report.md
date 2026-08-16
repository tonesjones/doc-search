---
title: "Retrieve JSON health check report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-json-health-check-report.html"
content_id: "xyeNSZ~IuWhrPe57de~8tg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:53.816310+00:00"
---

# Retrieve JSON health check report

Example GET request to retrieve the user's most recently generated health check report as
a JSON response.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/healthcheck/data" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "projectStats": [
    {
      "componentMaps": "Default",
      "currentOutstandingTriaged": 0,
      "currentOutstandingUntriaged": 11,
      "defectDensity": 0.6,
      "firstSnapshot": "2022-01-02",
      "latestSnapshot": "2022-03-17",
      "loc": 18481,
      "projectDescription": "C/C++ xref testing",
      "projectName": "testcpp",
      "server": my_server,
      "streams": "testcppstream"
    },
    {
      "componentMaps": "Default,Default",
      "currentOutstandingTriaged": null,
      "currentOutstandingUntriaged": null,
      "defectDensity": null,
      "firstSnapshot": "2022-01-05",
      "latestSnapshot": "2022-04-17",
      "loc": 18481,
      "projectDescription": "Advanced triage testing",
      "projectName": "testcpp-multistream",
      "server": my_server,
      "streams": "testcppstream-A,testcppstream-B"
    }
  ],
  "projectTrends": [
    {
      "dismissedFalsePositiveCount": 0,
      "dismissedIntentionalCount": 0,
      "fixedCount": 0,
      "loc": 18362,
      "metricsDate": "2022-01-02",
      "newCount": 11,
      "outstandingCountTriaged": 0,
      "outstandingCountUntriaged": 11,
      "projectName": "testcpp",
      "server": my_server,
      "totalCount": 11,
      "triagedCount": 0
    },
    {
      "dismissedFalsePositiveCount": 0,
      "dismissedIntentionalCount": 0,
      "fixedCount": 0,
      "loc": 18362,
      "metricsDate": "2022-01-03",
      "newCount": 11,
      "outstandingCountTriaged": 0,
      "outstandingCountUntriaged": 11,
      "projectName": "testcpp",
      "server": my_server,
      "totalCount": 11,
      "triagedCount": 0
    }
  ],
  "checkerStats": [
    {
      "checker": "PW.EXPR_HAS_NO_EFFECT",
      "dismissedFalsePositive": 0,
      "dismissedIntentional": 0,
      "fixed": 1,
      "outstandingTriaged": 0,
      "outstandingUntriaged": 0,
      "projectName": "testcpp",
      "server": my_server
    },
    {
      "checker": "PW.DEPRECATED_STRING_CONV",
      "dismissedFalsePositive": 0,
      "dismissedIntentional": 0,
      "fixed": 1,
      "outstandingTriaged": 0,
      "outstandingUntriaged": 0,
      "projectName": "testcpp",
      "server": my_server
    },
    {
      "checker": "PW.PARAMETER_HIDDEN",
      "dismissedFalsePositive": 0,
      "dismissedIntentional": 0,
      "fixed": 1,
      "outstandingTriaged": 0,
      "outstandingUntriaged": 0,
      "projectName": "testcpp",
      "server": my_server
    }
  ],
  "defectStatsByImpact": [
    {
      "allTimeFixedHighImpact": 0,
      "allTimeFixedLowImpact": 2,
      "allTimeFixedMediumImpact": 1,
      "currentOutstandingTriagedHighImpact": 0,
      "currentOutstandingTriagedLowImpact": 0,
      "currentOutstandingTriagedMediumImpact": 0,
      "currentOutstandingUntriagedHighImpact": 4,
      "currentOutstandingUntriagedLowImpact": 4,
      "currentOutstandingUntriagedMediumImpact": 5,
      "dateRangeFixedHighImpact": 0,
      "dateRangeFixedLowImpact": 2,
      "dateRangeFixedMediumImpact": 1,
      "projectName": "testcpp",
      "server": my_server
    },
    {
      "allTimeFixedHighImpact": 0,
      "allTimeFixedLowImpact": 0,
      "allTimeFixedMediumImpact": 0,
      "currentOutstandingTriagedHighImpact": 0,
      "currentOutstandingTriagedLowImpact": 0,
      "currentOutstandingTriagedMediumImpact": 0,
      "currentOutstandingUntriagedHighImpact": 4,
      "currentOutstandingUntriagedLowImpact": 4,
      "currentOutstandingUntriagedMediumImpact": 5,
      "dateRangeFixedHighImpact": 0,
      "dateRangeFixedLowImpact": 0,
      "dateRangeFixedMediumImpact": 0,
      "projectName": "testcpp-multistream",
      "server": my_server
    }
  ],
  "defectStatsBySeverity": [
    {
      "allTimeFixedMajorSeverity": 0,
      "allTimeFixedMinorSeverity": 0,
      "allTimeFixedModerateSeverity": 0,
      "allTimeFixedUnspecifiedSeverity": 3,
      "currentOutstandingTriagedMajorSeverity": 0,
      "currentOutstandingTriagedMinorSeverity": 0,
      "currentOutstandingTriagedModerateSeverity": 0,
      "currentOutstandingTriagedUnspecifiedSeverity": 0,
      "currentOutstandingUntriagedMajorSeverity": 0,
      "currentOutstandingUntriagedMinorSeverity": 0,
      "currentOutstandingUntriagedModerateSeverity": 0,
      "currentOutstandingUntriagedUnspecifiedSeverity": 13,
      "dateRangeFixedMajorSeverity": 0,
      "dateRangeFixedMinorSeverity": 0,
      "dateRangeFixedModerateSeverity": 0,
      "dateRangeFixedUnspecifiedSeverity": 3,
      "projectName": "testcpp",
      "server": my_server
    },
    {
      "allTimeFixedMajorSeverity": 0,
      "allTimeFixedMinorSeverity": 0,
      "allTimeFixedModerateSeverity": 0,
      "allTimeFixedUnspecifiedSeverity": 0,
      "currentOutstandingTriagedMajorSeverity": 0,
      "currentOutstandingTriagedMinorSeverity": 0,
      "currentOutstandingTriagedModerateSeverity": 0,
      "currentOutstandingTriagedUnspecifiedSeverity": 0,
      "currentOutstandingUntriagedMajorSeverity": 0,
      "currentOutstandingUntriagedMinorSeverity": 0,
      "currentOutstandingUntriagedModerateSeverity": 0,
      "currentOutstandingUntriagedUnspecifiedSeverity": 11,
      "dateRangeFixedMajorSeverity": 0,
      "dateRangeFixedMinorSeverity": 0,
      "dateRangeFixedModerateSeverity": 0,
      "dateRangeFixedUnspecifiedSeverity": 0,
      "projectName": "testcpp-multistream",
      "server": my_server
    }
  ],
  "defectStatsByCategory": [
    {
      "allTimeFixedCodeMaintainability": 0,
      "allTimeFixedCweTop25": 0,
      "allTimeFixedMemoryCorruption": 0,
      "allTimeFixedOwaspTop10": 0,
      "allTimeFixedProgramCrash": 0,
      "allTimeFixedProgramHang": 0,
      "allTimeFixedRaceCondition": 0,
      "allTimeFixedResourceLeak": 0,
      "allTimeFixedSecurity": 0,
      "allTimeFixedUnintendedBehavior": 1,
      "currentOutstandingTriagedCodeMaintainability": 0,
      "currentOutstandingTriagedCweTop25": 0,
      "currentOutstandingTriagedMemoryCorruption": 0,
      "currentOutstandingTriagedOwaspTop10": 0,
      "currentOutstandingTriagedProgramCrash": 0,
      "currentOutstandingTriagedProgramHang": 0,
      "currentOutstandingTriagedRaceCondition": 0,
      "currentOutstandingTriagedResourceLeak": 0,
      "currentOutstandingTriagedSecurity": 0,
      "currentOutstandingTriagedUnintendedBehavior": 0,
      "currentOutstandingUntriagedCodeMaintainability": 0,
      "currentOutstandingUntriagedCweTop25": 0,
      "currentOutstandingUntriagedMemoryCorruption": 3,
      "currentOutstandingUntriagedOwaspTop10": 0,
      "currentOutstandingUntriagedProgramCrash": 0,
      "currentOutstandingUntriagedProgramHang": 0,
      "currentOutstandingUntriagedRaceCondition": 0,
      "currentOutstandingUntriagedResourceLeak": 2,
      "currentOutstandingUntriagedSecurity": 0,
      "currentOutstandingUntriagedUnintendedBehavior": 6,
      "dateRangeFixedCodeMaintainability": 0,
      "dateRangeFixedCweTop25": 0,
      "dateRangeFixedMemoryCorruption": 0,
      "dateRangeFixedOwaspTop10": 0,
      "dateRangeFixedProgramCrash": 0,
      "dateRangeFixedProgramHang": 0,
      "dateRangeFixedRaceCondition": 0,
      "dateRangeFixedResourceLeak": 0,
      "dateRangeFixedSecurity": 0,
      "dateRangeFixedUnintendedBehavior": 1,
      "projectName": "testcpp",
      "server": my_server
    },
    {
      "allTimeFixedCodeMaintainability": 0,
      "allTimeFixedCweTop25": 0,
      "allTimeFixedMemoryCorruption": 0,
      "allTimeFixedOwaspTop10": 0,
      "allTimeFixedProgramCrash": 0,
      "allTimeFixedProgramHang": 0,
      "allTimeFixedRaceCondition": 0,
      "allTimeFixedResourceLeak": 0,
      "allTimeFixedSecurity": 0,
      "allTimeFixedUnintendedBehavior": 0,
      "currentOutstandingTriagedCodeMaintainability": 0,
      "currentOutstandingTriagedCweTop25": 0,
      "currentOutstandingTriagedMemoryCorruption": 0,
      "currentOutstandingTriagedOwaspTop10": 0,
      "currentOutstandingTriagedProgramCrash": 0,
      "currentOutstandingTriagedProgramHang": 0,
      "currentOutstandingTriagedRaceCondition": 0,
      "currentOutstandingTriagedResourceLeak": 0,
      "currentOutstandingTriagedSecurity": 0,
      "currentOutstandingTriagedUnintendedBehavior": 0,
      "currentOutstandingUntriagedCodeMaintainability": 0,
      "currentOutstandingUntriagedCweTop25": 0,
      "currentOutstandingUntriagedMemoryCorruption": 3,
      "currentOutstandingUntriagedOwaspTop10": 0,
      "currentOutstandingUntriagedProgramCrash": 0,
      "currentOutstandingUntriagedProgramHang": 0,
      "currentOutstandingUntriagedRaceCondition": 0,
      "currentOutstandingUntriagedResourceLeak": 2,
      "currentOutstandingUntriagedSecurity": 0,
      "currentOutstandingUntriagedUnintendedBehavior": 6,
      "dateRangeFixedCodeMaintainability": 0,
      "dateRangeFixedCweTop25": 0,
      "dateRangeFixedMemoryCorruption": 0,
      "dateRangeFixedOwaspTop10": 0,
      "dateRangeFixedProgramCrash": 0,
      "dateRangeFixedProgramHang": 0,
      "dateRangeFixedRaceCondition": 0,
      "dateRangeFixedResourceLeak": 0,
      "dateRangeFixedSecurity": 0,
      "dateRangeFixedUnintendedBehavior": 0,
      "projectName": "testcpp-multistream",
      "server": my_server
    }
  ],
  "defectAgeStats": [
    {
      "allTimeAverageDaysToFix": 34,
      "currentOutstandingTriagedAverageDays": 0,
      "currentOutstandingUntriagedAverageDays": 618,
      "dateRangeFirstDetectedAverageDaysToFix": 34,
      "dateRangeFirstDetectedOutstandingTriagedAverageDays": 0,
      "dateRangeFirstDetectedOutstandingUntriagedAverageDays": 649,
      "dateRangeFixedAverageDaysToFix": 34,
      "projectName": "testcpp",
      "server": my_server
    },
    {
      "allTimeAverageDaysToFix": 0,
      "currentOutstandingTriagedAverageDays": 0,
      "currentOutstandingUntriagedAverageDays": 618,
      "dateRangeFirstDetectedAverageDaysToFix": 0,
      "dateRangeFirstDetectedOutstandingTriagedAverageDays": 0,
      "dateRangeFirstDetectedOutstandingUntriagedAverageDays": 649,
      "dateRangeFixedAverageDaysToFix": 0,
      "projectName": "testcpp-multistream",
      "server": my_server
    }
  ],
  "componentStats": [
    {
      "componentName": "Default.Other",
      "dismissedFalsePositiveCount": 0,
      "dismissedIntentionalCount": 2,
      "fixedCount": 3,
      "loc": 18481,
      "metricsDate": "2023-10-13",
      "newCount": 13,
      "outstandingTriagedCount": 0,
      "outstandingUntriagedCount": 13,
      "projectName": "testcpp",
      "server": my_server,
      "totalCount": 18,
      "triagedCount": 0
    },
    {
      "componentName": "Default.Other",
      "dismissedFalsePositiveCount": 0,
      "dismissedIntentionalCount": 2,
      "fixedCount": 0,
      "loc": 18481,
      "metricsDate": "2023-10-13",
      "newCount": 16,
      "outstandingTriagedCount": 0,
      "outstandingUntriagedCount": 16,
      "projectName": "testcpp-multistream",
      "server": my_server,
      "totalCount": 18,
      "triagedCount": 0
    }
  ],
  "snapshotTrends": [
    {
      "analysisHost": "SIG-OS192112004",
      "analysisTime": 8,
      "analysisVersion": "main",
      "buildHost": "SIG-OS192112004",
      "buildTime": 8,
      "projectName": "testcpp",
      "server": my_server,
      "snapshotId": 10009,
      "snapshotDate": "2022-01-02",
      "stream": "testcppstream"
    }
  ],
  "previewDefects": [
    {
      "server": my_server,
      "projectName": "testcpp",
      "cid": 10063,
      "checkerName": "PW.DEPRECATED_STRING_CONV",
      "status": "New"
    }
  ],
  "reportMetadata": [
    {
      "connectVersion": "main",
      "endDate": "2022-01-03",
      "generationDate": "2023-10-13",
      "selectionCount": 2/75,
      "startDate": "2022-01-01"
    }
  ]
}
```
