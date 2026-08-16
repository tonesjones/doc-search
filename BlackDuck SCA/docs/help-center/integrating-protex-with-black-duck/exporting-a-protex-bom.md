---
title: "Exporting a Protex BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/exporting-a-protex-bom.html"
content_id: "EgB_juqY3JpJUEiAebiF9Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:32:27.180379+00:00"
---

# Exporting a Protex BOM

The Protex BOM tool provides several different ways by which you can
import a Protex BOM into Black Duck.

For example, you can use the tool to:

- Export the Protex BOM from the Protex server and import it into Black Duck using the tool.
- Export the Protex BOM from the Protex server to a file and manually import it through
  Black Duck UI.
- Import a Protex BOM file into Black Duck using the tool.

The tool does not require any specific role in Black Duck or in Protex to use the tool.

By default, the tool outputs component/version data only; use the -**-include-files**
parameter to include file data.

The Protex BOM tool has these parameters:

| Parameter | Description |
| --- | --- |
| **-?**, **--help** | Shows help for this tool. |
| **-A**, -**--dest** <*host: port*> | Specifies Black Duck host name and port. |
| **-P**, **--hub-project** <*name*> | Specifies the name of the Black Duck project to which you want to map this Protex BOM. If the project does not exist, the tool creates the project and maps the BOM to the project. |
| **-R**, **--hub-release** <*name*> | Specifies the name of the Black Duck project version to which you want to map this BOM. If the version does not exist, the tool creates the version and maps the BOM to this version of the project. If you specify **hub-project**, **hub-release** is optional. If you do not specify **hub-release**, the version defaults to the value of the **release** parameter. |
| **-S**, **--secure-dest** | Uses HTTPS to connect to the server hosting Black Duck. If you do not include this parameter, HTTP is used. |
| **-U**, **--dest-user** <*user*> | Specifies the username to log in to the Black Duck server. |
| **-W**, **--dest-password** | Forces the tool to prompt you for a password for the Black Duck server. When the tool runs, a prompt appears requesting the password for the specified user. For non-interactive use, set the BD_HUB_PASSWORD environment variable with the password for the Black Duck server. If you set this variable, the **dest-password** parameter is optional: the tool prompts the user for the password; it does not check the password against the variable. |
| **-a**, -**--address** <*host:port*> | Specifies the Protex host name and port. |
| **-r** **--release**<*name*> | Specifies a value to use to identify the current state of the Protex BOM. You can use any value for <*name*>.  Use this parameter to enable viewing multiple "versions" of a Protex BOM in Black Duck. Click here or more information. |
| **--list-projects** <*SearchQuery*> | Lists all Protex project identifiers for all projects to which you have access, one per line, on the console. <*SearchQuery*> is optional.  To export multiple Protex projects, use the output from this parameter to write a script which iterates over multiple project identifiers. |
| **--data** <*path*> | Specifies the path to the Protex BOM file. |
| **--output** <*path*> | Writes the BOM out to a file or directory with the project name. |
| **-p**, **--project** <*id or name*> | Specifies the Protex project identifier or project name. |
| **-s**, **--secure** | Uses HTTPS to connect to the server hosting Protex. If you do not specify this parameter, HTTP is used. |
| **-u**. **--user** <*user*> | Specifies the username to log in to the Protex server. |
| **-w**, **--password** | Forces the tool to prompt you for a password. When the tool runs, a prompt appears requesting the Protex server password for the specified user. For non-interactive use, set the BD_PROTEX_PASSWORD environment variable with the password for the Protex server. If you set this variable, the **password** parameter is optional. |
| **-V**, **--version** | Shows the version information of this tool. |
| **-v**, **--verbose** | Sets the logging level to verbose. |
| **--dryRunWriteDir** <*dryRunWriteDir*> | Specifies the directory to which the Protex BOM Tool outputs a JSON file with the original file metadata used for scanning. |
| **--debug** | Shows debug output. |
| **--include-files** Hub-10228 | Includes the Protex code tree and match details. |

By default, the tool generates the Protex BOM to standard out, if you
don't specify an output (file) or use the tool to import the BOM to Black Duck.

## Exit Statuses

The possible exit statuses are:

- **0**: SUCCESS. The export completed successfully.
- **1**: FAILURE. Generic failure.
- **64**: USAGE. The command to run the tool was used incorrectly, for
  example, with the wrong number of arguments or a bad syntax.
- **65**: DATA_ERROR. The input data was incorrect.
- **66**: NO INPUT. An input file (not a system file) did not exist or was
  not readable.
- **67**: NO_USER. The specified user does not exist.
- **68**: NO_HOST. The specified host does not exist.
- **69**: UNAVAILABLE. A service is unavailable.
- **70**: SOFTWARE. An internal software error has been detected.
- **71**: OS_ERROR. An operating system error has been detected.
- **72**: OS_FILE. A system file does not exist, cannot be opened, or has
  some sort of error, for example a syntax error.
- **73**: CANNOT_CREATE. An output file cannot be created.
- **74**: IO_ERROR. An error occurred while doing input/output on a
  file.
- **75**: TEMPORARY FAILURE. Temporary failure,
- **76**: PROTOCOL. The remote system returned something that was "not
  possible" during a protocol exchange.
- **77**: NO_PERMISSION. You did not have sufficient permission to perform
  the operation.
- **78**: CONFIGURATION. Something was found in an unconfigured or
  misconfigured state.
- **79**: NO_REGISTRATION. Registration to Black Duck or
  Protex was not valid.

## Viewing multiple versions of a Protex BOM in Black Duck

When you import a Protex BOM, Black Duck creates a
file (labeled a BOM File in Black Duck UI) that is associated with
that BOM. In Black Duck, a BOM File can only be mapped to a single
project and version – if you import the Protex BOM again, the new
file is added to the existing BOM File.

You may want to view multiple versions, or snapshots, of a Protex BOM
in Black Duck. Although Protex does not have project
versions, you can use the **release** parameter in the Protex BOM
tool to denote a snapshot of your Protex BOM. When you use the **release**
parameter, Black Duck creates a new BOM file for that snapshot. You
can then map that BOM file to a different project or to a different version of a
project. This gives you the flexibility to create multiple snapshots of a single Protex BOM and view them at the same time in Black Duck.

Note that if you specify a value for **release** that has already been used for
that Protex BOM, a new BOM File is not created. Instead, the new file
will be added to the existing BOM File.

## Examples

The following are examples of using the Protex BOM tool:

- Exporting the Protex BOM and
  importing it into Black Duck using the export
  tool
- Exporting the Protex BOM to a
  file
- Importing a Protex BOM from a
  file

Note that the examples show the required parameters.

### Using the Protex BOM tool to map the Protex BOM

In these examples, you have the option of using these parameters to specify the
Black Duck project and version that this BOM should be
mapped to:

- **hub-project** <*name*>
- **hub-release** <*name*>

If you specify a value for the **release** parameter and wish to use the tool
to map the Protex BOM, the **hub-release** parameter is
optional: if you do not specify a value for **hub-release**, Black Duck project version defaults to the value of
**release**.

If you do not specify **hub-project** and **release** or
**hub-release**, you must map
the Protex BOM using the Black Duck
UI.

### Exporting the Protex BOM and importing it into Black Duck using the export tool

This example exports the Protex BOM from the Protex
server and imports it into Black Duck using the tool.

1. Open a command prompt.
2. Go to the directory where the tool is installed and run the following
   command:

   **Linux example**

   ```
   ./scan.protex.cli.sh --address <host:port> --user <user> --password --project <id>  --output <path> --dest-address <host:port>  --dest-user <user> --dest-password
   ```

   **Windows example**

   ```
   scan.protex.cli.bat --address <host:port> --user <user> --password --project <id>  --output <path> --dest-address <host:port>  --dest-user <user> --dest-password
   ```

### Exporting the Protex BOM to a file

This example exports the Protex BOM from the Protex
server to a JSON file. You then need to use the Black Duck UI
to manually
import the file.

1. Open a command prompt.
2. Go to the directory where the tool is installed and run the following
   command:

   **Linux example**

   ```
   ./scan.protex.cli.sh --address <host:port> --user <user> --password --project <id>  --output <path>
   ```

   **Windows example**

   ```
   scan.protex.cli.bat --address <host:port> --user <user> --password --project <id>  --output <path>
   ```

### Importing a Protex BOM from a file

This example imports a Protex BOM file into Black Duck using the tool.

1. Open a command prompt.
2. Go to the directory where the tool is installed and run the following
   command:

   **Linux example**

   ```
   ./scan.protex.cli.sh --data <path> --dest-address <host:port>  --dest-user <user> --dest-password
   ```

   **Windows example**

   ```
   scan.protex.cli.bat --data <path> --dest-address <host:port>  --dest-user <user> --dest-password
   ```
