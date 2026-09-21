---
title: "Pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/pipeline.html"
content_id: "DArwSyn0S1rUURa1nSf4aQ"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:38.928230+00:00"
---

# Pipeline

## Declarative pipeline syntax example

Add the following code snippet to your Jenkinsfile in your project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `polaris_server_url`, `polaris_access_token`, `polaris_application_name`, `polaris_project_name`**,** `polaris_branch_name` and `polaris_assessment_types`, with the appropriate values.)

```
pipeline {
    agent any
    stages {
        stage("BlackDuckSecurityScan") {
           steps {
               script {
                  def status = security_scan product: "polaris", polaris_server_url: "POLARIS_SERVER_URL", polaris_access_token: "POLARIS_TOKEN", 
                      polaris_application_name: "YOUR_POLARIS_APPLICATION_NAME", polaris_project_name: "YOUR_POLARIS_PROJECT_NAME", 
                      polaris_branch_name: "POLARIS_BRANCH_NAME", polaris_assessment_types: "SCA, SAST"
                      // polaris_reports_sarif_create: true,
                      // mark_build_status: 'UNSTABLE',
                      // polaris_test_sca_type: "SCA-SIGNATURE",
                      // Uncomment this if you configure polaris_test_sca_type: "SCA-BINARY"
                      // polaris_artifactToUpload: "/path/to/binary-file"
                      // polaris_test_sast_type: "SAST_RAPID",
                      // Uncomment this to use Source Upload method. Default value is hybrid (build based)
                      // polaris_test_sast_location: 'remote',
                      // polaris_test_sca_location: 'remote',
                      // project_source_archive: "PROJECT_SOURCE_ARCHIVE",
                      // project_source_excludes: "PROJECT_SOURCE_EXCLUDES",
                      // project_source_preserveSymLinks: "PROJECT_SOURCE_PRESERVESYMLINKS",
                      // Uncomment this to use Local Analysis feature
                      // Please use Local Analysis or Source Upload exclusively
                      // polaris_test_sast_location: 'local'
                  
                   // Uncomment to add custom logic based on return status
                  // if (status == 8) { unstable 'policy violation' }
                  // else if (status != 0) { error 'plugin failure' }
               }
           }
       }
    } 
}
```

Note: `polaris_access_token` accepts an access token created in the Polaris UI or a service account token.

## Scripted pipeline syntax example

Add the following code snippet to your Jenkinsfile in your project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `polaris_server_url`, `polaris_access_token`, `polaris_application_name`, `polaris_project_name`**,** `polaris_branch_name` and `polaris_assessment_types`, with the appropriate values.)

```
node {
      checkout scm             
      stage("BlackDuckSecruityScan") {
            def status = security_scan product: "polaris", polaris_server_url: "POLARIS_SERVER_URL", polaris_access_token: "POLARIS_TOKEN",         
                polaris_application_name: "YOUR_POLARIS_APPLICATION_NAME", polaris_project_name: "YOUR_POLARIS_PROJECT_NAME", 
                polaris_branch_name: "POLARIS_BRANCH_NAME", polaris_assessment_types: "SCA, SAST" 
                // polaris_reports_sarif_create: true,
                // mark_build_status: 'UNSTABLE',
                // polaris_test_sca_type: "SCA-SIGNATURE",
                // Uncomment this if you configure polaris_test_sca_type: "SCA-BINARY"
                // polaris_artifactToUpload: "/path/to/binary-file"
                // polaris_test_sast_type: "SAST_RAPID",
                // Uncomment this to use Source Upload method. Default value is hybrid (build based)
                // polaris_test_sast_location: 'remote',
                // polaris_test_sca_location: 'remote',
                // project_source_archive: "PROJECT_SOURCE_ARCHIVE",
                // project_source_excludes: "PROJECT_SOURCE_EXCLUDES",
                // project_source_preserveSymLinks: "PROJECT_SOURCE_PRESERVESYMLINKS",
                // Uncomment this to use Local Analysis feature
                // Please use Local Analysis or Source Upload exclusively
                // polaris_test_sast_location: 'local
                
             // Uncomment to add custom logic based on return status
            // if (status == 8) { unstable 'policy violation' }
            // else if (status != 0) { error 'plugin failure' }
      }
}
```

Note:

- If `polaris_server_url`and `polaris_access_token` are configured in Jenkins Global Configuration, then it is not necessary to pass these values as a pipeline input parameter.
- If these values are set both from Jenkins Global Configuration and as a pipeline input parameter, then the pipeline input values will take precedence.
- PR comments are not supported for pipeline job types.
- `polaris_access_token` accepts an access token created in the Polaris UI or a service account token.

With global configuration, the script will simplify as follows:

```
security_scan product: "polaris", polaris_application_name: "YOUR_POLARIS_APPLICATION_NAME", polaris_project_name: "YOUR_POLARIS_PROJECT_NAME", polaris_branch_name: "POLARIS_BRANCH_NAME", polaris_assessment_types: "SCA, SAST"
```
