---
title: "Passing Arguments using a JSON file"
source_url: "https://docs.blackduck.com/r/bridge/latest/bridge-cli-guide/passing-arguments-using-a-json-file.html"
content_id: "u~RnWn2KcypS~G90P0S3Kw"
version: "latest"
section: "Bridge CLI"
scraped_at: "2026-08-08T23:46:51.144570+00:00"
---

# Passing Arguments using a JSON file

Passing arguments using a JSON file greatly simplifies the command line and promotes
reuse. Here are the steps:

1. Create an access token in the web interface of the Black Duck security product you
   are integrating with.
2. Use environment variable(s) to pass sensitive information such as password or access token
   to Bridge CLI (recommended for security purposes). Bridge CLI
   automatically picks up values passed through these variables.
   - Example: `export
     BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>`.
3. Pass the JSON file to Bridge CLI using the `--input` command
   line option.
4. Pass the Black Duck security product you are integrating with using the
   `--stage` option.

Here are the example
commands:

```
export BRIDGE_POLARIS_ACCESSTOKEN=<POLARIS_ACCESSTOKEN>
bridge-cli --stage polaris --input input.json
```

Note: Depending on your OS, you will need to use appropriate mechanism to set
environment variables.

Here is the `input.json` file:

```
{
	"data": {
		"polaris": {
			"application": {
				"name": "<APPLICATION_NAME>"
			},
			"project": {
				"name": "<PROJECT_NAME>"
			},
			"branch": {
				"name": "<BRANCH_NAME>"
			},	
			"assessment": {
				"types":  ["SAST", "SCA"]

			},
			"serverurl": "<SERVER_URL>"
		}
	}
}
```

Note: It is recommended that you save the JSON file at
the root of the project directory being scanned. The JSON file can have any name as
long as it has a `.json` extension.

Note: You can use different JSON files for different use cases.

For a complete list of environment variables and command line arguments, see Complete list of Bridge arguments.

For tool specific information and examples, see:

- Using Bridge CLI with Polaris
- Using Bridge CLI with Black Duck SCA
- Using Bridge CLI with Coverity
- Using Bridge CLI with Software Risk Manager (SRM)
