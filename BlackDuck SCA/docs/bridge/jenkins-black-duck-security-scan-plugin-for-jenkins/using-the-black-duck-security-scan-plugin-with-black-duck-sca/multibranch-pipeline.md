---
title: "Multibranch pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/multibranch-pipeline.html"
content_id: "LPnnyVxe_LZkQtddIVhp4A"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:41.213545+00:00"
---

# Multibranch pipeline

## Declarative pipeline syntax example

Add the following code snippet to your Jenkinsfile in the project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `blackducksca_url`, and `blackducksca_token`, with appropriate values.)

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
                    def status = security_scan product: 'blackducksca'
                        // Uncomment if below parameters are not set in global configuration
                        // blackducksca_url: 'BLACKDUCKSCA_URL'
                        // blackducksca_token: 'BLACKDUCKSCA_TOKEN',
                        // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                        // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 

                        // Pull Request Comments
                        // blackducksca_prComment_enabled: true
                        
                        // Fix pull request creation
                        // blackducksca_fixpr_enabled: true

                        // SARIF report generation
                        // blackducksca_reports_sarif_create: true
                        
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

Note: Jenkins supports automating Fix PR creation for GitHub, GitLab and Bitbucket repositories through multi branch pipeline. The Fix PR feature is not supported for freestyle and pipeline jobs.

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
                    def status = security_scan product: 'blackducksca',
                        // Uncomment if below parameters are not set in global configuration
                        // blackducksca_url: 'BLACKDUCKSCA_URL'
                        // blackducksca_token: 'BLACKDUCKSCA_TOKEN',
                        // blackducksca_waitForScan: false,    // Used to support the async mode
                        // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                        // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
                        // project_directory: "PROJECT_DIRECTORY",

                        // Pull Request Comments
                        blackducksca_prComment_enabled: true,
                        
                        // Fix pull request creation
                        // blackducksca_fixpr_enabled: true,
                        // blackducksca_fixpr_filter_severities : "CRITICAL, MEDIUM",
                        // blackducksca_fixpr_maxCount: 1,
                        // blackducksca_fixpr_useUpgradeGuidance: 'SHORT_TERM'

                        // SARIF report generation
                        blackducksca_reports_sarif_create: true,

                        // Optional parameters
                        // blackducksca_reports_sarif_file_path: 'SARIF_FILE_PATH',
                        // blackducksca_reports_sarif_groupSCAIssues: true,
                        // blackducksca_reports_sarif_severities: 'CRITICAL, HIGH',

                        // To enable the use of self-signed certificates
                        // network_ssl_trustAll: true
                        
                        // Uncomment below to add arbitrary CL parameters
                        // detect_search_depth: 1
                        // detect_config_path: '/USER/application.properties'
                        // detect_args: '--detect.diagnostic=true'
                        
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

Add the following code snippet to your Jenkinsfile in the project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `blackducksca_url`, and `blackducksca_token`, with appropriate values.)

Simplified example

```
node {
    checkout scm
    
    stage("BlackDuckSecruityScan") {
        if (env.BRANCH_NAME == 'master' || env.BRANCH_NAME =~ /^PR-\d+$/) {
            def status = security_scan product: 'blackducksca'
               // Uncomment if below parameters are not set in global configuration
               // blackducksca_url: 'BLACKDUCKSCA_URL',             
               // blackducksca_token: 'BLACKDUCKSCA_TOKEN',
               // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
               // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 

                // Pull Request Comments
                // blackducksca_prComment_enabled: true

                // SARIF report generation
                // blackducksca_reports_sarif_create: true
                
                // Fix pull request creation
                // blackducksca_fixpr_enabled: true
                
                // Mark build status if issues found
                // mark_build_status: 'UNSTABLE'
                
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
            def status = security_scan product: 'blackducksca',
                // Uncomment if below parameters are not set in global configuration
                // blackducksca_url: 'BLACKDUCKSCA_URL',             
                // blackducksca_token: 'BLACKDUCKSCA_TOKEN',
                // blackducksca_waitForScan: false,    // Used to support the async mode
                // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
                // project_directory: "PROJECT_DIRECTORY",
               
                // Pull Request Comments
                blackducksca_prComment_enabled: true,

                // Fix pull request creation
                // blackducksca_fixpr_enabled: true,
                // blackducksca_fixpr_filter_severities : "CRITICAL, MEDIUM",
                // blackducksca_fixpr_maxCount: 1,
                // blackducksca_fixpr_useUpgradeGuidance: 'SHORT_TERM'

                // SARIF report generation
                blackducksca_reports_sarif_create: true,
               
                // Optional parameters
                // blackducksca_reports_sarif_file_path: 'SARIF_FILE_PATH',
                // blackducksca_reports_sarif_groupSCAIssues: true,
                // blackducksca_reports_sarif_severities: 'CRITICAL',

                // To enable the use of self-signed certificates
                // network_ssl_trustAll: true
                
                // Uncomment below to add arbitrary CL parameters
                // detect_search_depth: 1
                // detect_config_path: '/USER/application.properties'
                // detect_args: '--detect.diagnostic=true'
                
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

- If `blackducksca_url` , `blackducksca_token`, and `bitbucket_token` are configured in Jenkins Global Configuration, then it is not necessary to pass these values as a pipeline input parameter.
- If these values are set both from Jenkins Global Configuration and as a pipeline input parameter, then the pipeline input values will take precedence.
- For GitHub and GitLab, use the appropriate parameter `github_token` or `gitlab_token` in place of the `bitbucket_token`.
