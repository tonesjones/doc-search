---
title: "Pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/pipeline.html"
content_id: "HpnPe0Dsdiy1hnnll3WOoA"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:47.438077+00:00"
---

# Pipeline

## Declarative pipeline syntax example

```
pipeline {
    agent any
    stages {
        stage("BlackDuckSecruityScan") {
           steps {
               script {
                    def status = security_scan product: "srm", srm_url: "SRM_URL", 
                        srm_apikey: "YOUR_SRM_APIKEY", srm_assessment_types: "SCA,SAST",
                        srm_project_name: 'SRM_PROJECT_NAME' 
                        //, mark_build_status: 'UNSTABLE'
                     // Uncomment to add custom logic based on return status
                    // if (status == 8) { unstable 'policy violation' }
                    // else if (status != 0) { error 'plugin failure' }
                }
            }           
        }
    }
}
```

## Scripted pipeline syntax example

```
node {
      checkout scm            
      stage("BlackDuckSecruityScan") {                  
          def status = security_scan product: "srm", srm_url: "SRM_URL", 
              srm_apikey: "YOUR_SRM_APIKEY", srm_assessment_types: "SCA,SAST",
              srm_project_name: 'SRM_PROJECT_NAME'
              // , mark_build_status: 'UNSTABLE'
           // Uncomment to add custom logic based on return status
          // if (status == 8) { unstable 'policy violation' }
          // else if (status != 0) { error 'plugin failure' }
      }
}
```
