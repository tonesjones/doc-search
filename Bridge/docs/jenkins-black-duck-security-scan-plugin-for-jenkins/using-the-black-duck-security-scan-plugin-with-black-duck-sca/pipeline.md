---
title: "Pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/pipeline.html"
content_id: "g8Q3~NtOVq7shGyCsJWbdA"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:41.820579+00:00"
---

# Pipeline

## Declarative pipeline syntax example

Add the following code snippet to your Jenkinsfile in the project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `blackducksca_url`, and `blackducksca_token`, with appropriate values.)

```
pipeline {
    agent any
    stages {
        stage("BlackDuckSecruityScan") {
           steps {
               script {
                    def status = security_scan product: "blackducksca", blackducksca_url: "BLACKDUCKSCA_URL", 
                        blackducksca_token: "YOUR_BLACKDUCKSCA_TOKEN"
                        // blackducksca_reports_sarif_create: true 
                        // mark_build_status: 'UNSTABLE'
                    
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

Add the following code snippet to your Jenkinsfile in the project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `blackducksca_url`, and `blackducksca_token`, with appropriate values.)

```
node {
      checkout scm            
      stage("BlackDuckSecruityScan") {                  
          def status = security_scan product: "blackducksca", blackducksca_url: "BLACKDUCKSCA_URL", 
              blackducksca_token: "YOUR_BLACKDUCKSCA_TOKEN"
              // blackducksca_reports_sarif_create: true
              // mark_build_status: 'UNSTABLE'
                    
           // Uncomment to add custom logic based on return status
          // if (status == 8) { unstable 'policy violation' }
          // else if (status != 0) { error 'plugin failure' }
      }
}
```

Note:

- If `blackducksca_url` and `blackducksca_token` are configured in Jenkins Global Configuration, then it is not necessary to pass these values as a pipeline input parameter.
- If these values are set both from Jenkins Global Configuration and as a pipeline input parameter, then the pipeline input values will take precedence.
- PR comment is not supported through the Pipeline job type.

With global configuration, the script will simplify as follows:

```
security_scan product: "blackducksca"
```
