---
title: "Pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/pipeline.html"
content_id: "pI2wpG9UeoyLTo2eZFdD6Q"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:44.650141+00:00"
---

# Pipeline

## Declarative pipeline syntax example

Add the following code to your Jenkinsfile in the project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `coverity_url`, `coverity_user`, `coverity_passphrase`, `coverity_stream_name`, and `coverity_project_name`, with the appropriate values.)

```
pipeline {
    agent any
    stages {
        stage("BlackDuckSecruityScan") {
            steps {
                script {
                    def status = security_scan product: "coverity", coverity_url: "COVERITY_URL", 
                        coverity_user: "COVERITY_USER_NAME", coverity_passphrase: "COVERITY_PASSWORD", 
                        coverity_stream_name: "COVERITY_STREAM_NAME", coverity_project_name: "COVERITY_PROJECT_NAME"
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

Add the following code to your Jenkinsfile in the project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `coverity_url`, `coverity_user`, `coverity_passphrase`, `coverity_stream_name`, and `coverity_project_name`, with the appropriate values.)

```
node {
    checkout scm                   
    stage("BlackDuckSecruityScan") {                  
        def status = security_scan product: "coverity", coverity_url: "COVERITY_URL", 
              coverity_user: "COVERITY_USER_NAME", coverity_passphrase: "COVERITY_PASSWORD", 
              coverity_stream_name: "COVERITY_STREAM_NAME", coverity_project_name: "COVERITY_PROJECT_NAME"
              // mark_build_status: 'UNSTABLE'
                    
         // Uncomment to add custom logic based on return status
        // if (status == 8) { unstable 'policy violation' }
        // else if (status != 0) { error 'plugin failure' }
    }
}
```

Note:

- If `coverity_url`, `coverity_user`, and `coverity_passphrase` are configured in Jenkins Global Configuration, then it is not necessary to pass these values as a pipeline input parameter.
- If these values are set both from Jenkins Global Configuration and as a pipeline input parameter, then the pipeline input values will take precedence.
- PR comment is not supported through the Pipeline job type.

With global configuration, the script will simplify as follows:

```
security_scan product: "coverity", coverity_stream_name: "COVERITY_STREAM_NAME", coverity_project_name: "COVERITY_PROJECT_NAME"
```
