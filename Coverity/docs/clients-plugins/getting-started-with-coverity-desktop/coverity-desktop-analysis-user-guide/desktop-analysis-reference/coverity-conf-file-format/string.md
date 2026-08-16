---
title: "string"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/string.html"
content_id: "2CVDXaBxJv_~6ivRPHB9wg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:30.263178+00:00"
---

# string

A string is an ordinary JSON string, except that it may contain variable substitution
placeholders that are substituted during evaluation to yield the effective configuration
value.

Variable substitutions are denoted by "`$(`", then a name, then
"`)`". For example, "`$(server_port)`" is substituted
for the value of `settings.server.port`.

The defined variables are listed in the tables below:

Table 1. Simple variables

| Simple Variable | Substitution |
| --- | --- |
| `env:VAR1:VAR2:...:VARn [=default_value]` | Environment variable lookup. First, `VAR1` is looked up, and if that is defined and not empty then it is the substituted value. Otherwise, `VAR2` is looked up, and so on. If none of the variables is defined as non-empty, then an empty string is substituted. Optionally, you can append `=`, which is a string that will be substituted if none of the environment variables are set. |
| `var:VAR1:VAR2:...:VARn [=default_value]` | Variable lookup. First, `VAR1` is looked up, and if that is defined and not empty then it is the substituted value. Otherwise, `VAR2` is looked up, and so on. If none of the variables is defined as non-empty, then an empty string is substituted. Optionally, you can append `=`, which is a string that will be substituted if none of the variables are set. |
| `dollar` | The character "$". |
| `lparen` | The character "(". |
| `rparen` | The character ")". |
| `platform` | The Coverity platform identifier string. This is one of the allowable values for  `Condition.platforms` . |
| `version` | The Coverity tools version, for example "7.5.0" or "7.5.0.3". |
| `install_dir` | Directory where the invoked tool is installed. It has a bin subdirectory, among others. |
| `num_cores` | The number of detected CPU cores on the local host machine, or "1" if that can not be determined. |

Table 2. Dependent variables

| Dependent Variable | Substitution |
| --- | --- |
| `cov_user_dir` | A directory where user-specific and application-specific settings are stored. On operating systems other than Windows, this is "`$(env:HOME)/.coverity`". On Windows it is "`$(env:APPDATA)/Coverity`". |
| `code_base_dir` | The directory containing coverity.conf for the code base, if one is found; otherwise, it is the working directory where the tool was invoked. |
| `server_host_as_fname` | The effective value of `settings.server.host`, except mapped to a string that is safe to use as a file name. |
| `server_port` | The effective value of `settings.server.port`. |

Table 3. Special variables

| Special Variable | Substitution |
| --- | --- |
| `response_file_utf8` | In `specific_files_build_cmd`, this expands to the path of a temporary text file listing files to compile, one per line with UTF-8 character encoding. |
| `response_file_platform_default` | In `specific_files_build_cmd`, this expands to the path of a temporary text file listing files to compile, one per line with platform default character encoding. |

Note: Special variables are only allowed in certain contexts.
