---
title: "Quoting and escaping shell script arguments"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/quoting-and-escaping-shell-script-arguments.html"
content_id: "UN1pCVybdfBRgvZ7nWWvWA"
version: "11.5.1"
section: "Configuring Detect"
scraped_at: "2026-08-08T23:44:24.481384+00:00"
---

# Quoting and escaping shell script arguments

Tip: Escaping characters via the command line can be complicated, to simplify any escaping requirements we recommend you consider using either environment variable or configuration files.

## Running the Bash script (detect11.sh) on Linux or Mac

The recommended environment ("parent shell") for running detect11.sh on Linux is Bash, and Bash or Zsh on Mac.

Note: Exact requirements for escaping characters will depend on the set of properties and arguments provided. The following section provides general guidance.

When an argument contains a space or other non double quote special character, you can wrap the argument in single quotes, or escape the special character with a backslash (\). The quotes can surround either the value or the entire argument.

For example:

```
# name: Project Test
bash <(curl -s -L https://detect.blackduck.com/detect11.sh) --detect.project.name='Project Test'

# name: Project Test
bash <(curl -s -L https://detect.blackduck.com/detect11.sh) --detect.project.name=Project\ Test

# name: Project!Test
bash <(curl -s -L https://detect.blackduck.com/detect11.sh) --detect.project.name=Project\!Test
```

You can include a double quote by single quoting the string, and escaping the double quotes with backslashes:

```
# license: BSD 3-clause "New" or "Revised" License
bash <(curl -s -L https://detect.blackduck.com/detect11.sh) --detect.project.version.license='BSD 3-clause \"New\" or \"Revised\" License'
```

## Running in Command Prompt (cmd) on Windows (detect11.ps1)

On Windows, you can run detect11.ps1 in either a [Windows Command Prompt](https://en.wikipedia.org/wiki/Cmd.exe)
session, or a PowerShell session.
This section describes running
detect11.ps1 in a [Windows Command Prompt](https://en.wikipedia.org/wiki/Cmd.exe)
session.

Note: Exact requirements for escaping characters will depend on the set of properties and arguments provided. The following section provides general guidance.

When an argument contains a space or other non quote special character, you can wrap the argument in single quotes, or escape the special character with a backtick (`). The quotes can surround either the value or the entire argument.

For example:

```
# name: Project Test
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect" --detect.project.name='Project Test'

# name: Project Test
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect" '--detect.project.name=Project Test'

# name: Project Test
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect" --detect.project.name=Project` Test
```

When an argument contains a comma, you can wrap the argument in single quotes, and escape the special character with a backtick (`). In the case of a name with a comma and a space, you would use a backtick in front of both the comma and space.

For example:

```
# name: Project,Test   
Powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm  https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect --blackduck.url=<url> --detect.project.name='Project,Test'"   

# name: Project,Test   
Powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm  https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect --blackduck.url=<url> '--detect.project.name=Project,Test'"   

# name: Project, Test   
Powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm  https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect --blackduck.url=<url> --detect.project.name=Project`,` Test"
```

You can include a single quote by doubling it:

```
# name: singlequote'
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect" --detect.project.name='singlequote'''
```

You can include a double quote using this sequence: double quote, 2 backslashes, 2 double quotes:

```
# license: BSD 3-clause "New" or "Revised" License
powershell "[Net.ServicePointManager]::SecurityProtocol = 'tls12'; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect" --detect.project.version.license='BSD 3-clause "\\""New"\\"" or "\\""Revised"\\"" License'
```

## Running in PowerShell on Windows (detect11.ps1)

An alternative environment for running detect11.ps1 on Windows is to run it from inside a PowerShell session.

This invocation has an important distinction from the Command Prompt invocation in that the script does NOT EXIT the session. This is desirable when running the script from a terminal session but not from within a CI/CD environment.

Tip: When running from within a CI/CD environment either omit the passthrough flag or use the command prompt invocation as the job may not set the proper exit code if the session does not exit.

Note: Exact requirements for escaping characters will depend on the set of properties and arguments provided. The following section provides general guidance.

When an argument contains a space or other non-quote special character, you can wrap the argument in single quotes, or escape the special character with a backtick. The quotes can surround either the value or the entire argument.

For example:

```
# name: Project Test
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect --detect.project.name='Project Test'

# name: Project Test
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect "--detect.project.name=Project Test"
```

When an argument contains a comma, you must escape the special character with a backtick (`). In the case of a name with a comma and a space, you would use a backtick in front of both the comma and space.

For example:

```
# name: Project,Test
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https:/
/detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect --detect.project.name=Project`,Test

# name: Project, Test
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https:/
/detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect --detect.project.name=Project`,` Test
```

You can include a double quote using this sequence: backslash, backtick, double quote:

```
# license: BSD 3-clause "New" or "Revised" License
[Net.ServicePointManager]::SecurityProtocol = 'tls12'; $Env:DETECT_EXIT_CODE_PASSTHRU=1; irm https://detect.blackduck.com/detect11.ps1?$(Get-Random) | iex; detect --detect.project.version.license="BSD 3-clause \`"New\`" or \`"Revised\`" License"
```
