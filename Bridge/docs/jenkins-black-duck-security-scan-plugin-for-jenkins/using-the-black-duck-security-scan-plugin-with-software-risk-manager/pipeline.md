---
title: "Pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/pipeline.html"
content_id: "HpnPe0Dsdiy1hnnll3WOoA"
version: "latest"
section: "Jenkins Integrations"
scraped_at: "2026-10-04T23:28:30.942566+00:00"
content_hash: "931dfa6895e82cae0b7f08c35ebd8418b66dcade9541c901f3f815e09b58aa80"
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
