---
title: "Multibranch pipeline"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/multibranch-pipeline.html"
content_id: "p8PejMeUgUQ0m8mjluq8iA"
version: "latest"
section: "Jenkins - Black Duck Security Scan Plugin for Jenkins"
scraped_at: "2026-08-08T23:48:44.037791+00:00"
---

# Multibranch pipeline

## Declarative pipeline syntax example

Add the following code snippet to your Jenkinsfile in your project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `coverity_url`, `coverity_user`, and `coverity_passphrase`, with the appropriate values.)

Simplified Example

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
                    def status = security_scan product: 'coverity'
                        // Uncomment if below parameters are not set in global configuration                  
                        // coverity_url:'COVERITY_URL',                           
                        // coverity_user: 'COVERITY_USER',
                        // coverity_passphrase: 'COVERITY_PASSPHRASE',
                        // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                        // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
        
                        // Pull Request Comments
                        //  coverity_prComment_enabled: true
                          
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

Detailed Example

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
                    def status = security_scan product: 'coverity',
                        // Uncomment if below parameters are not set in global configuration                   
                        // coverity_url: 'COVERITY_URL',    
                        // coverity_user: 'COVERITY_USER',
                        // coverity_passphrase: 'COVERITY_PASSPHRASE',
                        // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                        // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
                        //Optional for multibranch pipeline
                        // coverity_stream_name: "COVERITY_STREAM_NAME", 
                        // coverity_project_name: "COVERITY_PROJECT_NAME",
                        // coverity_waitForScan: false,    // Used to support the async mode
                        // project_directory: "PROJECT_DIRECTORY",
                        // Pull Request Comments
                          coverity_prComment_enabled: true,
                        // coverity_prComment_impacts: 'HIGH,MEDIUM',
                        // To enable the use of self-signed certificates
                        // network_ssl_trustAll: true
                        // network_ssl_cert_file: 'path/to/cert/cert.pem'
                        // Uncomment below to add arbitrary CL parameters
                        // coverity_build_command: 'mvn clean install'
                        // coverity_clean_command: 'mvn clean'
                        // coverity_config_path: '/USER/coverity.yml'
                        // coverity_args: '--config-override capture.build.build-command=mvn install'
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

Add the following code to your Jenkinsfile in the project root directory that you want to scan. (Make sure to provide the required parameters, such as `product`, `coverity_url`, `coverity_user`, and `coverity_passphrase`, with the appropriate values.)

Simplified Example

```
node {
      checkout scm             
      stage("BlackDuckSecruityScan") {

         if (env.BRANCH_NAME == 'master' || env.BRANCH_NAME =~ /^PR-\d+$/) {
            def status = security_scan product: "coverity"
                // Uncomment if below parameters are not set in global configuration               
                // coverity_url: 'COVERITY_URL',                             
                // coverity_user: 'COVERITY_USER',    
                // coverity_passphrase: 'COVERITY_PASSPHRASE',
                // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
          
                // Pull Request Comments
                // coverity_prComment_enabled: true
            
                // Mark build status if issues found
                // mark_build_status: 'UNSTABLE'

            // Uncomment to add custom logic based on return status
            // if (status == 8) { unstable 'policy violation' }
            // else if (status != 0) { error 'plugin failure' }
        }
      }
}
```

Detailed Example

```
node {
      checkout scm             
      stage("BlackDuckSecruityScan") {
         if (env.BRANCH_NAME == 'master' || env.BRANCH_NAME =~ /^PR-\d+$/) {
            def status = security_scan product: "coverity",
                // Uncomment if below parameters are not set in global configuration               
                // coverity_url: 'COVERITY_URL',                             
                // coverity_user: 'COVERITY_USER',    
                // coverity_passphrase: 'COVERITY_PASSPHRASE',
                // bitbucket_token: 'BITBUCKET_TOKEN', // Used for PR comment. Use github_token for GitHub or gitlab_token for GitLab
                // bitbucket_username:'BITBUCKET_USERNAME' // Used for bitbucket cloud pr comment if app password is set as bitbucket_token 
                // Optional for multibranch pipeline
                // coverity_stream_name: "COVERITY_STREAM_NAME", 
                // coverity_project_name: "COVERITY_PROJECT_NAME",
                // coverity_waitForScan: false,    // Used to support the async mode
                // project_directory: "PROJECT_DIRECTORY",
                // Pull Request Comments
                coverity_prComment_enabled: true,
                // coverity_prComment_impacts: 'HIGH,MEDIUM',
                // To enable the use of self-signed certificates
                // network_ssl_trustAll: true
                // network_ssl_cert_file: 'path/to/cert/cert.pem'
                // Uncomment below to add arbitrary CL parameters
                // coverity_build_command: 'mvn clean install'
                // coverity_clean_command: 'mvn clean'
                // coverity_config_path: '/USER/coverity.yml'
                // coverity_args: '--config-override capture.build.build-command=mvn install'
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

- If `coverity_url`, `coverity_user`, `coverity_passphrase`, and `bitbucket_token` are configured in Jenkins Global Configuration, then it is not necessary to pass these values as a pipeline input parameter.
- If these values are set both from Jenkins Global Configuration and as a pipeline input parameter, then the pipeline input values will take precedence.
- For GitHub and GitLab, use the appropriate parameter `github_token` or `gitlab_token` in place of the `bitbucket_token`.
