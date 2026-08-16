---
title: "Synopsis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synopsis.html"
content_id: "wyKK~968KYmrUAn6ELSqNA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:40:11.235454+00:00"
---

# Synopsis

```
cov-commit-defects
	--dataport <port_number> | --port <port_number> | --https-port <port_number>  
	--dir <intermediate_directory>
	--host <host_server_name>
	--stream <stream_name> 
	[--authenticate-ssl]
	[--auth-key-file <keyfile>]
	[--description "description"] 
	[--encryption <requirement_level>]
	[--extra-output <path>]
	[--output-tag <name>]
	[--on-new-cert <trust | distrust>]    
	[--password <password>] 
	[--preview-report <filename> | --preview-report-v2 <filename> | --preview-report-v3 <filename>]  
	[--scm <scm_type>]             
	[--scm-tool <scm_tool_path>]
	[--scm-project-root <scm_root_path>]
	[--scm-tool-arg <scm_tool_arg>]
	[--scm-command-arg <scm_command_arg>]
	[--snapshot-id-file <filename>]
	[--strip-path <path>] 
	[--target <platform>] 
	[--ticker-mode <mode>]
	[--url <path>]
	[--user <user_name>]               
	[--version <version>]
	[SHARED_OPTIONS]
```

**[SHARED_OPTIONS]**:

```
    [--config <coverity_config.xml>]
    [--debug]
    [--ident]
    [--info]
    [--tmpdir <tmp>]
    [--verbose <level>]
```
