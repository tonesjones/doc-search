---
title: "Multibranch pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/multibranch-pipeline.html"
content_id: "psQK~~k9LjK05YhztV468g"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:38.274584+00:00"
---

# Multibranch pipeline

## Declarative pipeline syntax example

Add the following code snippet to your Jenkinsfile in your project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `polaris_server_url`, `polaris_access_token`, and `polaris_assessment_types`, with the appropriate values.)

Simplified example

```
pipeline {
    agent any
    stages {
        stage("BlackDuckSecruityScan") {
            when {
                // Triggering Black Duck Security Scan on master branch or Pull Request
                anyOf {
                    branch 'master'
                    branch pattern: "PR-\\d+", comparator: "REGEXP"
                }
            }
            steps {
                script {
                    def status = security_scan product: 'polaris',
                        // Uncomment if below parameters are not set in global configuration
                        // polaris_server_url: 'POLARIS_SERVER_URL',
                        // polaris_access_token: 'POLARIS_TOKEN', 
                        // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                        // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
                            polaris_assessment_types: 'SAST,SCA'
    
                        // Pull Request Comments
                        //  polaris_prComment_enabled: true,
    
                        // Enable Polaris Fix PR
                        //  polaris_fixpr_enabled: true,

                        // SARIF report generation
                        //  polaris_reports_sarif_create: true,
                            
                        // Mark build status if issues found
                        //  mark_build_status: 'UNSTABLE'
                    
                    // Uncomment to add custom logic based on return status
                    // if (status == 8) { unstable 'policy violation' }
                    // else if (status != 0) { error 'plugin failure' }
                }
            }
        }
    }
}
```

Detailed example

```
pipeline {
    agent any
    stages {
        stage("BlackDuckSecruityScan") {
            when {
                // Triggering Black Duck Security Scan on master branch or Pull Request
                anyOf {
                    branch 'master'
                    branch pattern: "PR-\\d+", comparator: "REGEXP"
                }
            }
            steps {
                script {
                    def status = security_scan product: 'polaris',
                      // Uncomment if below parameters are not set in global configuration
                      // polaris_server_url: 'POLARIS_SERVER_URL',
                      // polaris_access_token: 'POLARIS_TOKEN',
                      // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                      // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
                          polaris_assessment_types: 'SAST,SCA',
                      //Optional for multibranch pipeline
                      // polaris_application_name: 'POLARIS_APPLICATION_NAME', 
                      // polaris_project_name: 'POLARIS_PROJECT_NAME',
                      // polaris_branch_name: 'BRANCH_NAME',
                      // polaris_waitForScan: false,    // Used to support the async mode
                      // project_directory: "PROJECT_DIRECTORY",
                      // Uncomment this to use Source Upload method. Default value is hybrid (build based)
                      // polaris_test_sast_location: 'remote',
                      // polaris_test_sca_location: 'remote',
                      // project_source_archive: "PROJECT_SOURCE_ARCHIVE",
                      // project_source_excludes: "PROJECT_SOURCE_EXCLUDES",
                      // project_source_preserveSymLinks: "PROJECT_SOURCE_PRESERVESYMLINKS",
                      // Uncomment this to use Local Analysis feature
                      // Please use Local Analysis or Source Upload exclusively
                      // polaris_test_sast_location: 'local',
                      // Pull Request Comments
                          polaris_prComment_enabled: true,
                      // polaris_branch_parent_name: 'PARENT_BRANCH_NAME',
                      // Enable Polaris Fix PR
                      // polaris_fixpr_enabled: true,
                      // polaris_fixpr_filter_severities: 'CRITICAL,HIGH' // Severities eligible for Fix PRs (comma-separated)
                      // polaris_fixpr_maxCount: 5 // Max Fix PRs allowed per branch
                      // polaris_fixpr_useUpgradeGuidance: 'SHORT_TERM,LONG_TERM' // Order of upgrade guidance preference (comma-separated)
                      // SARIF report generation
                          polaris_reports_sarif_create: true,
                      // Optional parameters
                      // polaris_reports_sarif_file_path: 'SARIF_FILE_PATH',
                      // polaris_reports_sarif_groupSCAIssues: true,
                      // polaris_reports_sarif_issue_types: 'SAST, SCA',
                      // polaris_reports_sarif_severities: 'CRITICAL,HIGH',
                      // Signature scan
                      // polaris_test_sca_type:”SCA-SIGNATURE”,
                      // Binary analysis scan
      	             // polaris_test_sca_type:"SCA-BINARY",
                      // polaris_artifactToUpload: "/path/to/binary-file",
                      // Sigma Rapid scan
                      // polaris_test_sast_type: "SAST_RAPID",
                      // Uncomment below to add arbitrary CL parameters
                      // detect_search_depth: 1,
                      // detect_config_path: '/USER/application.properties',
                      // detect_args: '--detect.diagnostic=true',
                      // coverity_build_command: 'mvn clean install',
                      // coverity_clean_command: 'mvn clean',
                      // coverity_config_path: '/USER/coverity.yml',
                      // coverity_args: '--config-override capture.build.build-command=mvn install',
                      // coverity_version: '2025.9.0',
                      // Mark build status if issues found
                          mark_build_status: 'UNSTABLE'
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

Add the following code snippet to your Jenkinsfile in your project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `polaris_server_url`, `polaris_access_token`, and `polaris_assessment_types`, with the appropriate values.)

Simplified example

```
node {
    checkout scm
    
    stage("BlackDuckSecruityScan") {
        // Trigger Black Duck Security Scan on master branch or Pull Request
        if (env.BRANCH_NAME == 'master' || env.BRANCH_NAME =~ /^PR-\d+$/) {
            def status = security_scan product: 'polaris',
                // Uncomment if below parameters are not set in global configuration
                // polaris_server_url: 'POLARIS_SERVER_URL',
                // polaris_access_token: 'POLARIS_TOKEN', 
                // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
                polaris_assessment_types: 'SAST,SCA'

                
                // Pull Request Comments
                // polaris_prComment_enabled: true

                // Enable Polaris Fix PR
                // polaris_fixpr_enabled: true

                // SARIF report generation
                //  polaris_reports_sarif_create: true
                
                // Mark build status if issues found
                //  mark_build_status: 'UNSTABLE'
                
            // Uncomment to add custom logic based on return status
            // if (status == 8) { unstable 'policy violation' }
            // else if (status != 0) { error 'plugin failure' }

        }
    }
}
```

Detailed example

```
node {
    checkout scm
    stage("BlackDuckSecruityScan") {
        // Trigger Black Duck Security Scan on master branch or Pull Request
        if (env.BRANCH_NAME == 'master' || env.BRANCH_NAME =~ /^PR-\d+$/) {
            def status = security_scan product: 'polaris',
                // Uncomment if below parameters are not set in global configuration
                // polaris_server_url: 'POLARIS_SERVER_URL',
                // polaris_access_token: 'POLARIS_TOKEN', 
                // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
                polaris_assessment_types: 'SAST,SCA',
                // Optional for multibranch pipeline
                // polaris_application_name: 'POLARIS_APPLICATION_NAME', 
                // polaris_project_name: 'POLARIS_PROJECT_NAME',
                // polaris_branch_name: 'BRANCH_NAME',
                // polaris_waitForScan: false,    // Used to support the async mode
                // project_directory: "PROJECT_DIRECTORY",
                // Uncomment this to use Source Upload method. Default value is hybrid (build based)
                // polaris_test_sast_location: 'remote',
                // polaris_test_sca_location: 'remote',
                // project_source_archive: "PROJECT_SOURCE_ARCHIVE",
                // project_source_excludes: "PROJECT_SOURCE_EXCLUDES",
                // project_source_preserveSymLinks: "PROJECT_SOURCE_PRESERVESYMLINKS",
                // Uncomment this to use Local Analysis feature
                // Please use Local Analysis or Source Upload exclusively
                // polaris_test_sast_location: 'local',
                // Pull Request Comments
                polaris_prComment_enabled: true,
                // polaris_branch_parent_name: 'PARENT_BRANCH_NAME',
                // Enable Polaris Fix PR
                // polaris_fixpr_enabled: true,
                // polaris_fixpr_filter_severities: 'CRITICAL,HIGH' // Severities eligible for Fix PRs (comma-separated)
                // polaris_fixpr_maxCount: 5 // Max Fix PRs allowed per branch
                // polaris_fixpr_useUpgradeGuidance: 'SHORT_TERM,LONG_TERM' // Order of upgrade guidance preference (comma-separated)
                // SARIF report generation
                polaris_reports_sarif_create: true,
                // Optional parameters
                // polaris_reports_sarif_file_path: 'SARIF_FILE_PATH',
                // polaris_reports_sarif_groupSCAIssues: true,
                // polaris_reports_sarif_issue_types: 'SAST, SCA',
                // polaris_reports_sarif_severities: 'CRITICAL,HIGH',
                // Signature scan
                // polaris_test_sca_type:"SCA-SIGNATURE",
                // Binary analysis scan
      	       // polaris_test_sca_type:"SCA-BINARY",
                // polaris_artifactToUpload: "/path/to/binary-file",
                // Sigma Rapid scan
                // polaris_test_sast_type: "SAST_RAPID",
                // Uncomment below to add arbitrary CL parameters
                // detect_search_depth: 1,
                // detect_config_path: '/USER/application.properties',
                // detect_args: '--detect.diagnostic=true',
                // coverity_build_command: 'mvn clean install',
                // coverity_clean_command: 'mvn clean',
                // coverity_config_path: '/USER/coverity.yml',
                // coverity_args: '--config-override capture.build.build-command=mvn install',
                // coverity_version: '2025.9.0',
                // Mark build status if issues found
                mark_build_status: 'UNSTABLE'
            // Uncomment to add custom logic based on return status
            // if (status == 8) { unstable 'policy violation' }
            // else if (status != 0) { error 'plugin failure' }
        }
    }
}
```

Note:

- If `polaris_server_url`and `polaris_access_token` are configured in Jenkins Global Configuration, then it is not necessary to pass these values as a pipeline input parameter.
- If these values are set both from Jenkins Global Configuration and as a pipeline input parameter, then the pipeline input values will take precedence.
