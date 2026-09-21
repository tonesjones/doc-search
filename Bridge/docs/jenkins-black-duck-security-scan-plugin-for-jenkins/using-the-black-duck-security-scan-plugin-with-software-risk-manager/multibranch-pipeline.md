---
title: "Multibranch pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/multibranch-pipeline.html"
content_id: "OJcdt6hP_lgTUDjFktBHQg"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:46.823573+00:00"
---

# Multibranch pipeline

## Declarative pipeline syntax

Simplified example

```
pipeline {
    agent any
    stages {
        stage('BlackDuckSecruityScan') {
            when {
                anyOf {
                    branch 'master'
                    branch pattern: "PR-\\d+", comparator: "REGEXP"
                }
            }
            steps {
                script {
                    def status = security_scan product: 'srm',
                        // Uncomment if below parameters are not set in global configuration
                        // srm_url: 'SRM_URL',
                        // srm_apikey: 'SRM_APIKEY',
                           srm_assessment_types: "SCA,SAST",

                        // Mark build status if issues found
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

Detailed example

```
pipeline {
    agent any
    stages {
        stage('BlackDuckSecruityScan') {
            when {
                anyOf {
                    branch 'master'
                    branch pattern: "PR-\\d+", comparator: "REGEXP"
                }
            }
            steps {
                script {
                    def status = security_scan product: 'srm',
                       // Uncomment if below parameters are not set in global configuration
                       // srm_url: 'SRM_URL',
                       // srm_apikey: 'SRM_APIKEY',
                          srm_assessment_types: "SCA,SAST",
                
                       // Optional parameters
                          srm_project_name: 'SRM_PROJECT_NAME',
                          srm_project_id: 'SRM_PROJECT_ID',
                          srm_branch_name: 'SRM_BRANCH_NAME',
                          srm_branch_parent: 'SRM_BRANCH_PARENT',
                       // srm_waitForScan: false,    // Used to support the async mode
                          detect_execution_path: 'DETECT_EXECUTION_PATH',
                          coverity_execution_path: 'COVERITY_EXECUTION_PATH',
                       // project_directory: 'PROJECT_DIRECTORY',
                        
                        // Uncomment below to add arbitrary CL parameters
                        // detect_search_depth: 1
                        // detect_config_path: '/USER/application.properties'
                        // detect_args: '--detect.diagnostic=true'
                        // coverity_build_command: 'mvn clean install'
                        // coverity_clean_command: 'mvn clean'
                        // coverity_config_path: '/USER/coverity.yml'
                        // coverity_args: '--config-override capture.build.build-command=mvn install'
                                
                        // Mark build status if issues found
                        //   mark_build_status: 'UNSTABLE'
                    
                    // Uncomment to add custom logic based on return status
                    // if (status == 8) { unstable 'policy violation' }
                    // else if (status != 0) { error 'plugin failure' }
                }
            }
        }
    }
}
```

## Scripted pipeline syntax

Simplified example

```
node {
    checkout scm
    stage("BlackDuckSecruityScan") {
        if (env.BRANCH_NAME == 'master' || env.BRANCH_NAME =~ /^PR-\d+$/) {
            def status = security_scan product: 'srm',
                // Uncomment if below parameters are not set in global configuration
                // srm_url: 'SRM_URL',
                // srm_apikey: 'SRM_APIKEY',
                   srm_assessment_types: "SCA,SAST",
                  
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
        if (env.BRANCH_NAME == 'master' || env.BRANCH_NAME =~ /^PR-\d+$/) {
            def status = security_scan product: 'srm',
                // Uncomment if below parameters are not set in global configuration
                // srm_url: 'SRM_URL',
                // srm_apikey: 'SRM_APIKEY',
                  srm_assessment_types: "SCA,SAST",
              
                // Optional parameters
                  srm_project_name: 'SRM_PROJECT_NAME',
                  srm_project_id: 'SRM_PROJECT_ID',
                  srm_branch_name: 'SRM_BRANCH_NAME',
                  srm_branch_parent: 'SRM_BRANCH_PARENT',
                  detect_execution_path: 'DETECT_EXECUTION_PATH',
                // srm_waitForScan: false,    // Used to support the async mode
                  coverity_execution_path: 'COVERITY_EXECUTION_PATH',
                // project_directory: 'PROJECT_DIRECTORY',
                
                // Uncomment below to add arbitrary CL parameters
                // detect_search_depth: 1
                // detect_config_path: '/USER/application.properties'
                // detect_args: '--detect.diagnostic=true'
                // coverity_build_command: 'mvn clean install'
                // coverity_clean_command: 'mvn clean'
                // coverity_config_path: '/USER/coverity.yml'
                // coverity_args: '--config-override capture.build.build-command=mvn install'
                        
                // Mark build status if issues found
                //  mark_build_status: 'UNSTABLE'
                           
            // Uncomment to add custom logic based on return status
            // if (status == 8) { unstable 'policy violation' }
            // else if (status != 0) { error 'plugin failure' }
        }
    }
}
```
