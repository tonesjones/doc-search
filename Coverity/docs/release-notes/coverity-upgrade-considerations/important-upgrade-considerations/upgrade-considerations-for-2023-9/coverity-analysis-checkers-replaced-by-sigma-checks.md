---
title: "Coverity Analysis checkers replaced by Sigma checks"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-checkers-replaced-by-sigma-checks.html"
content_id: "f0x1hQINov8mgDK8Oz9DWA"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:57:01.902296+00:00"
---

# Coverity Analysis checkers replaced by Sigma checks

A number of Coverity Analysis
checkers have been either completely or partially replaced by Sigma (SIGMA.*)
checks.

The following Coverity Analysis checkers have been replaced by
Sigma (SIGMA.*) checks for equivalent languages.

Table 1. Coverity Analysis checkers replaced by Sigma checks for specific
languages

| Coverity Analysis checker | Languages removed from Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- | --- |
| ``` HARDCODED_CREDENTIALS ``` | PHP | ``` SIGMA.hardcoded_secret_pattern ```  ``` SIGMA.hardcoded_secret_api ``` |
| ``` HEADER_INJECTION ``` | PHP | ``` SIGMA.header_injection_core_php ``` |
| ``` INSECURE_COMMUNICATION ``` | Java, JavaScript, TypeScript | ``` SIGMA.missing_tls_apache_http SIGMA.missing_tls_apache_telnet SIGMA.missing_tls_axios SIGMA.missing_tls_core_java_httprequest SIGMA.missing_tls_core_java_httpurlconnection SIGMA.missing_tls_electron SIGMA.missing_tls_fetch SIGMA.missing_tls_got SIGMA.missing_tls_hapi_session_mongo SIGMA.missing_tls_java_aws_sdk_cloudfront SIGMA.missing_tls_java_aws_sdk_s3_bucket SIGMA.missing_tls_java_aws_sdk_sns SIGMA.missing_tls_java_gcp_compute SIGMA.missing_tls_java_grpc SIGMA.missing_tls_java_unirest SIGMA.missing_tls_moleculer_web SIGMA.missing_tls_node_arm_postgresql SIGMA.missing_tls_node_arm_rediscache SIGMA.missing_tls_node_arm_storage SIGMA.missing_tls_node_aws_sdk SIGMA.missing_tls_node_aws_sdk_cloudfront_​originprotocolpolicy SIGMA.missing_tls_node_aws_sdk_cloudfront_​viewerprotocolpolicy SIGMA.missing_tls_node_aws_sdk_elasticache_legacy SIGMA.missing_tls_node_aws_sdk_elasticache_v3 SIGMA.missing_tls_node_aws_sdk_s3_bucket SIGMA.missing_tls_node_azure_app_service SIGMA.missing_tls_node_azure_app_service_ftp SIGMA.missing_tls_node_azure_storage_sas SIGMA.missing_tls_node_fetch SIGMA.missing_tls_node_ftp SIGMA.missing_tls_node_gcp_compute SIGMA.missing_tls_node_grpc SIGMA.missing_tls_node_http SIGMA.missing_tls_node_http_server SIGMA.missing_tls_node_rest_client SIGMA.missing_tls_node_telnet SIGMA.missing_tls_node_telnet_client SIGMA.missing_tls_react_native_blob_util SIGMA.missing_tls_reactor_netty_http_client SIGMA.missing_tls_reactor_netty_server SIGMA.missing_tls_realm SIGMA.missing_tls_sequelize SIGMA.missing_tls_socket_io_client SIGMA.missing_tls_spring_boot_web_client SIGMA.missing_tls_spring_boot_web_server SIGMA.missing_tls_spring_cas_authn_code SIGMA.missing_tls_spring_ftp SIGMA.missing_tls_spring_graphql SIGMA.missing_tls_spring_hateoas_client SIGMA.missing_tls_spring_integration_feed_code SIGMA.missing_tls_spring_integration_ftp_code SIGMA.missing_tls_spring_integration_http_code SIGMA.missing_tls_spring_integration_mail_code SIGMA.missing_tls_spring_integration_mail_dsl SIGMA.missing_tls_spring_integration_webflux_code SIGMA.missing_tls_spring_integration_ws_code SIGMA.missing_tls_spring_ldap_code SIGMA.missing_tls_spring_reactive_webclient SIGMA.missing_tls_spring_reactive_websocket SIGMA.missing_tls_spring_resttemplate SIGMA.missing_tls_spring_rsocket SIGMA.missing_tls_spring_security_ldap_code SIGMA.missing_tls_spring_security_oauth2 SIGMA.missing_tls_spring_security_servlet_code SIGMA.missing_tls_spring_security_webflux SIGMA.missing_tls_spring_websocket SIGMA.missing_tls_spring_ws_code SIGMA.missing_tls_websocket SIGMA.missing_tls_websocket_client_api SIGMA.missing_tls_ws SIGMA.missing_tls_xmlhttprequest ``` |
| ``` NOSQL_QUERY_INJECTION ``` | PHP | ``` SIGMA.nosql_query_injection_core_php ``` |
| ``` OPEN_REDIRECT ``` | PHP | ``` SIGMA.open_redirect_core_php ``` |
| ``` OS_CMD_INJECTION ``` | PHP | ``` SIGMA.os_cmd_injection_core_php ``` |
| ``` PATH_MANIPULATION ``` | PHP | ``` SIGMA.path_manipulation_core_php ``` |
| ``` SCRIPT_CODE_INJECTION ``` | PHP | ``` SIGMA.script_code_injection_core_php ``` |
| ``` SENSITIVE_DATA_LEAK ``` | PHP | ``` SIGMA.sensitive_data_leak_core_php ``` |
| ``` SQLI ``` | PHP | ``` SIGMA.sqli_core_php ``` |
| ``` UNSAFE_DESERIALIZATION ``` | PHP | ``` SIGMA.unsafe_deserialization_core_php ``` |
| ``` UNSAFE_REFLECTION ``` | PHP | ``` SIGMA.unsafe_reflection_core_php ``` |
| ``` XSS ``` | PHP | ``` SIGMA.xss_core_php ``` |

Table 2. Coverity Analysis checkers completely replaced by Sigma checks

| Coverity Analysis checker | Sigma checks replacing this Coverity checker |
| --- | --- |
| ``` CONFIG.SYMFONY_CSRF_​PROTECTION_DISABLED ``` | ``` SIGMA.csrf_protection_disabled_symfony_yaml ```  ``` SIGMA.csrf_protection_disabled_symfony_xml ``` |
| ``` SYMFONY_EL_INJECTION ``` | ``` SIGMA.el_injection_symfony ``` |
