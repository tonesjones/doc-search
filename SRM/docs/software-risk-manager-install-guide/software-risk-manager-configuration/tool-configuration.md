---
title: "Tool Configuration"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/tool-configuration.html"
content_id: "qIYD2tRMLGIEmQDOkhyzCQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:31.856871+00:00"
content_hash: "bd9772f390aea6849ce363d0f6e6d509c95b95a7c620683e91fb09457ff5815f"
---

# Tool Configuration

## Props Settings

Software Risk Manager has tool-specific settings for some tools, which control how
Software Risk Manager will behave in response to data from those tools.

### Veracode

When accessing Veracode via a Tool Connector, it is possible to load "Callstack"
information for each Veracode Flaw. (Veracode Callstack information is
interpreted as Software Risk Manager Data Flow information for the corresponding
results.) Doing so will improve the decision-making process of agentless hybrid
correlation, but this comes at a steep performance cost (roughly 1-2 seconds per
flaw).

- `veracode.callstack-load-enabled` enables loading of the
  optional "Callstack" information when set to `true`. Defaults
  to `false`.

### NowSecure

NowSecure uses `lab-api` as the default subdomain for the lab api
and `app` as the default subdomain for the user interface.
Software Risk Manager allows user-defined values for these subdomains in the
props file.

- `nowsecure.lab-api-subdomain` defines the subdomain for the
  lab api. Defaults to `lab-api`.
- `nowsecure.lab-ui-subdomain` defines the subdomain for the
  lab user interface. Defaults to `app`.

### Black Duck

When automatically importing projects with parent mapping from Black Duck,
Software Risk Manager omits the top-level Black Duck project group.

- `blackduck.project-enumeration.include-top-level-group`
  enables including the top-level Black Duck project group in SRM parent project
  mapping when set to `true`. Defaults to `false`.

### Clang-Tidy

By default, the Clang-Tidy reader parses a certain portion of the input file for format
detection. The relevant properties can be changed according to preferences
in the props file:

- `clang-tidy.format-detection.max-line-length` sets the maximum
  number of characters to read per line of the input file. Defaults to
  `8192` characters.
- `clang-tidy.format-detection.num-lines` sets the number of
  lines to read from the input file. Defaults to `1500` lines.
- `clang-tidy.format-detection.patience` sets the number of lines
  to scan before running into a relevant line for format detection. Defaults to
  `15` lines.

### Clippy

Clippy is a tool for linting Rust code, typically through the Cargo package
manager. Software Risk Manager can run Clippy on Rust code, if available.

When Software Risk Manager is properly configured to use Clippy, it will be
offered as a bundled tool when analyzing a ZIP containing at least one
`Cargo.toml` file. During analysis, Clippy will be invoked
for each `Cargo.toml` file discovered in the ZIP.

In order for Software Risk Manager to run Clippy:

- The [standard Rustup installer](https://www.rust-lang.org/tools/install) must be used and
  installed in a manner accessible to Software Risk Manager.
- Clippy must be installed as a Cargo component. Clippy is typically installed
  as part of Rustup installation, but it can also be [installed manually](https://github.com/rust-lang/rust-clippy#step-2-install-clippy), if
  needed.
- Software Risk Manager must be able to discover the installation paths.
- Any additional dependencies needed for building your Rust projects must be
  pre-installed on the Software Risk Manager machine.

The procedure varies by platform as described in the sections below.

#### Clippy on Linux

*These steps should be followed only after Software Risk Manager has been
installed.*

**Note:** Rustup must be installed for the user which runs Software Risk
Manager.

- *For non-root installations,* this will be the user that was logged
  in when Software Risk Manager was installed. The Rustup installer can be
  run by that user and installed as usual.
- *For root installations,* this will be the `tomcat`
  user created automatically by the Software Risk Manager installer. The
  Rustup installer must be run through a `tomcat` user
  session. For example, on Ubuntu, this may be done with `sudo -u
  tomcat bash` to start a new shell as the
  `tomcat` user, followed by the Rustup install
  command.

This should provide a `.cargo` folder in the user's home
directory that contains the `bin/cargo` executable required
by Software Risk Manager.

Restart Software Risk Manager and Clippy should be offered as a bundled tool
during analysis of relevant ZIP files.

#### Clippy on Windows

*These steps can be followed before or after Software Risk Manager has been
installed.*

On Windows, Software Risk Manager runs through the `Local
Service` user, which does not have a home directory. Instead,
these steps will be followed:

- Install Rustup for at least one user on the Software Risk Manager
  machine.
- Give the `Local Service` user permission to read, write,
  and execute content in the `.cargo` and
  `.rustup` folders in the user's home directory.
- Update `codedx.props` to provide the path to the
  `.cargo` and `.rustup` folders.

Log in to the Software Risk Manager machine and run the standard Rustup
installer as that user. Once installation has completed, navigate to the
user's home directory (Win+R, type `%USERPROFILE%`, press
enter) and find the `.cargo` and `.rustup`
folders.

For each folder, do the following:

1. Right-click and select Properties.
2. Go to the Security tab.
3. Click the "Edit" button.
4. Click the "Add" button.
5. In the textbox at the bottom, enter the text "Local Service."
6. Click "OK" to close the "Select User or Groups" modal. The "Local
   Service" user should now appear in the list of users.
7. Select the user and enable all permissions except "Full control" and
   "Special permissions."
8. Click "OK" to close the "Permissions for Folder" window.
9. Click "OK" to close the "Folder Properties" window.

With these changes, Software Risk Manager will have access to the
`.cargo` and `.rustup` folders.

Next, open the Software Risk Manager Properties file and add these entries:

```
cargo.path = C:/Users/<username>/.cargo
rustup.path = C:/Users/<username>/.rustup
```

... where `<username>` will be replaced with the name of
the user that installed Rustup.

Restart Software Risk Manager, and Clippy should be offered as a bundled tool
during analysis of relevant ZIP files.

### Coverity

By default, a finding’s severity in Software Risk Manager is based on the Coverity
issue's severity. "Dismissed" and "Absent Dismissed" issues are also excluded by
default from the findings.
The relevant properties can be changed according to preferences in the props file:

- `coverity.finding-severity-from-cvss-score` determines whether
  to use the CVSS Score to configure the finding severity. Defaults to
  `false`.
- `coverity.include-dismissed-issues` determines whether
  to include Coverity issues with "Dismissed" status in the list of findings.
  Defaults to `false`.
- `coverity.include-absent-dismissed-issues` determines whether
  to include Coverity issues with "Absent Dismissed" status in the list of findings.
  Defaults to `false`.

When automatically importing Coverity projects and versions from the integrations page,
SRM will attempt to parse the branch name from the stream name. Coverity stream names
must be globally unique, and so a common pattern is to use the project name, followed
by a separator and the branch name. For example, a project `WebGoat` with
branch `main` might have a stream named `WebGoat-main`.
By default, SRM will attempt to determine the branch from the stream name by checking
for the project name, followed by a separator of either `-`,
`_`, or a space. Additional stream name parsing behavior can be defined
with the following props setting:

- `coverity.stream-name-regexes.#` defines additional regular
  expressions to be used for Coverity stream name parsing. `#` must be
  replaced with 0 for the first regex pattern to be defined. If additional regex
  patterns are required, each additional one must increment `#` by one.

The first regular expression to match the stream name in ascending order of their
indexes will be used to determine the branch name. The branch name will be extracted
from the first capture group of the matching regex. If other groups are required, they
must be defined as non-capturing groups. Additionally, if the stream name format
includes the project name, `{{projectName}}` may be used in place of the
project name. When evaluating the regular expressions, SRM will replace any instances
of `{{projectName}}` with each project name's literal.

For example, consider a project `WebGoat` with streams `WebGoat - main`
and `Webgoat (develop)`, where `main` and `develop`
are the respective branches. The first stream's format may be defined with the regex
`{{projectName}} - (.+)`. The second stream's format may be defined with the regex
`{{projectName}} \((.+)\)`. Both regexes may be defined in the props file by
assigning one to the property `coverity.stream-name-regexes.0`, and the other to
`coverity.stream-name-regexes.1`.

### Dynatrace

When ingesting Dynatrace data into Software Risk Manager using the tool connector,
it limits the number of entities and related attacks that are included in each result,
since these lists can get overwhelmingly large. By default, the tool connector
also specifies a port for ActiveGate environments, and a page size for the number
of vulnerabilities or attack results to include per page.
The relevant properties can be changed according to preferences in the props file:

- `dynatrace.active-gate-environment.port` sets the default port
  number to use for ActiveGate type Dynatrace environments. Defaults to
  `9999`.
- `dynatrace.vulnerabilities.page-size` sets the number of
  vulnerability results to include per page. Should be between 1 and 500.
  Defaults to `100`.
- `dynatrace.max-num-entities` sets the maximum number of
  entities that are included in vulnerability results. Defaults to
  `10`.
- `dynatrace.max-num-attacks` sets the maximum number of
  related attacks that are included in vulnerability results. Defaults to
  `10`.
- `dynatrace.attacks.page-size` sets the number of attack results
  to include per page. Should be between 1 and 500. Defaults to
  `100`.

### SD Elements

Regulations Sections data from SD Elements can be pulled in by SRM based on a
configuration setting defined in `codedx.props`. To pull in this
data, set the property `sdelements.fetch-regulation-sections` to
`true`. (The default setting is `false`.)

Note: The default is set to `false` due
to a known issue with SD Elements that requesting Regulations Sections data
causes errors.

## Configuration Files

For some of the bundled tools, Software Risk Manager provides the ability to define a
configuration file, either system-wide or on a per-project basis. Within the
Software Risk Manager appdata directory, locate
the `tool-data` directory (or create it if it isn't present). To
define a configuration file for a tool, create a directory with that tool's name (as
specified below). A system-wide configuration should be placed in that directory,
or, for a per-project config, create a sub-directory named with the given project's
ID, and then place the configuration file in that sub-directory.

### Scalastyle

Software Risk Manager supports user-defined `config.xml`
scalastyle config files. Place the file within the
`tool-data/scalastyle` directory or within a project-specific
subdirectory. Files should follow the [format](http://www.scalastyle.org/configuration.html) defined by scalastyle.

Software Risk Manager also supports a user-defined
`scalastyle.props` config file for configuring the JVM
environment in which the scalastyle tool runs. Currently, the only supported
property is `file.encoding`, which will be passed to the JVM via
the `-Dfile.encoding` environment variable. This allows you to
run scalastyle on projects that don't use the standard encoding.

### Checkstyle

Software Risk Manager supports user-defined `config.xml`
Checkstyle configuration files. Place the file within the
`tool-data/checkstyle` directory or within a project-specific
subdirectory. Files should follow the [format](https://checkstyle.sourceforge.io/config.html) defined by Checkstyle.

### Cppcheck

Software Risk Manager supports a user-defined `cppcheck.conf`
config file. Create the file in the `tool-data/cppcheck`
directory or within a project-specific subdirectory. Within that file, you can
define a value for the `useThreads` property (e.g.,
`useThreads=4` to request that Cppcheck use four threads).
Also, Cppcheck will run with the `--inline-suppr` option enabled
by default, allowing you to suppress errors from within your source code. This
behavior can be disabled by setting `inlineSuppression=false`.
See the [Cppcheck Manual](http://cppcheck.sourceforge.net/manual.pdf) for more details on these
settings.

You can also choose to define the `platform` property. This
affects Cppcheck's configuration for platform-specific types and sizes. By
default, Cppcheck will choose the platform your Software Risk Manager server is
running on. Available platform options are as follows:

- `unix32` 32 bit Unix variant
- `unix64` 64 bit Unix variant
- `win32A` 32 bit Windows ASCII character encoding
- `win32W` 32 bit Windows UNICODE character encoding
- `win64` 64 bit Windows
- `avr8` 8 bit AVR microcontrollers
- `native` Type sizes of host system are assumed, but no
  further assumptions
- `unspecified` Unknown type sizes

You can also use the `libraries` property to specify a list of
library configurations for Cppcheck to use. For example, setting
`libraries = [gtk, posix, qt]` will enable Cppcheck's library
configurations for gtk, posix, and qt. The available configurations are avr,
bento4, boost, bsd, cairo, cppcheck-lib, cppunit, daca, dpdk, embedded_sql,
emscripten, ginac, gnu, googletest, gtk, icu, kde, libcerror, libcurl,
libsigc++, lua, mfc, microsoft_atl, microsoft_sal, microsoft_unittest, motif,
nspr, ntl, opencv2, opengl, openmp, openssl, pcre, posix, python, qt, ruby, sdl,
sfml, sqlite3, tinyxml2, vcl, windows, wxsqlite3, wxsvg, wxwidgets, and
zlib.

### JSHint

Software Risk Manager supports a user-defined `jshint.conf` config
file. Create the file in the `tool-data/jshint` directory or
within a project-specific subdirectory. Within that file, you can define a value
for the `scan-html` property, which tells JSHint to additionally
scan `.htm` and `.html` files. This property is
enabled by default (i.e., `scan-html=true`).

You can also define a value for the `extract` property, which sets
the value for the `--extract` flag from JSHint. This flag
controls how JSHint extracts HTML from files. Available extract options are as
follows:

- `auto` JSHint will attempt to extract javascript only if the
  file looks like it is an HTML file. This is the default value (i.e.,
  `extract=auto`).
- `always` JSHint will always attempt to extract javascript.
  Note that if this value is set, JSHint will scan all files as HTML. This
  means that javascript source files will not be scanned normally. Instead,
  JSHint will search them for HTML to extract and anything else in the file
  will be ignored.
- `never` JSHint will never attempt to extract javascript. Note
  that if this value is set, JSHint will not be able to scan HTML.
  `scan-html` must be set to `false`,
  otherwise JSHint will try to scan HTML files as javascript source and will
  report an error for each one.

### PHPMD

Software Risk Manager supports user-defined `config.xml` PHPMD
ruleset files. Place the file within the `tool-data/phpmd`
directory or within a project-specific subdirectory. Files should follow the
[format](https://phpmd.org/rules/index.html) defined by PHPMD.

### PHP_CodeSniffer

Software Risk Manager supports user-defined `config.xml`
PHP_CodeSniffer ruleset files. Place the file within the
`tool-data/phpcodesniffer` directory or within a
project-specific subdirectory. Files should follow the [format](https://github.com/squizlabs/PHP_CodeSniffer/wiki/) defined by PHP_CodeSniffer.

### PMD

In Software Risk Manager's config
file in the `tool-data/pmd` directory or within a
project-specific subdirectory, you can define a value for the
`debug-logging` property (e.g.,
`debug-logging=true` to enable verbose PMD logs). You can
also define a value for the `encoding` property (e.g.,
`encoding=UTF-8` to set the character encoding PMD expects
source to be in. Acceptable values are any standard
`java.nio.charset.Charset` character set). By default, these
are `debug-logging=false` and
`encoding=UTF-8`.

### ESLint

By default, Software Risk Manager will pass `--ignore-pattern
**/node_modules/*`.

**Configuration**

Software Risk Manager supports user-defined `.eslintrc` and
`.eslintignore` ESLint config files. Place the file(s) within
the `tool-data/eslint` directory or within a project-specific
subdirectory. Files should follow the [format](https://eslint.org/docs/user-guide/configuring) defined by ESLint. You can use the
`js`, `yml`, `json`, or
`eslintrc` formats.

In the event that there are multiple config files present in different formats,
Software Risk Manager will follow the same [priority](https://eslint.org/docs/user-guide/configuring#configuration-file-formats) that ESLint uses. ESLint will
also use any `.eslintrc` config files uploaded in the project as
defined by the rules explained [here](https://eslint.org/docs/user-guide/configuring#configuration-cascading-and-hierarchy).

Additionally, Software Risk Manager will search for an
`.eslintignore` file in the root directory of the uploaded
zip file. The `.eslintignore` file in the zip will take
precedence over the `.eslintignore` file in the
`tool-data/eslint` or project-specific directories. If you
use a custom config, be sure to adjust your tool configuration. By default, only
the recommended ESLint rules are enabled.

Software Risk Manager also supports user-defined "appdata-dir.dita"he default
`eslintrc.json` file. For users wanting to add minor
adjustments to the default configuration, a
`eslint-config-extra.js` can be placed within the
`tool-data/eslint` directory or within a project-specific
subdirectory (a directory whose name is the numeric `id` of the
Software Risk Manager project), as with the custom `.eslintrc`
and `.eslintignore` files mentioned above. When running ESLint,
SRM will search for this "extra" config file and, if present, will include it as
an extension of its default ESLint config file.

The contents of the `eslint-config-extra.js` file should be in the
form `module.exports = { ... }`, where the `...`
is replaced by your custom configuration as defined in [the ESLint configuration guide](https://eslint.org/docs/user-guide/configuring).

**Important notes about using a custom `.eslintignore`
file**

- If an `.eslintignore` file is neither found in the
  uploaded zip file nor provided in the `tool-data/eslint`
  directory, Software Risk Manager will pass `--ignore-pattern
  **/node_modules/*` as a command-line argument to
  ESLint.
- If you want to provide an `.eslintignore` file, it is a
  good idea to include the `**/node_modules/*` pattern in
  that file; linting the contents of your third-party dependencies is not
  recommended, due to the fact that in some cases this can cause ESLint to
  fail.

Several ESLint plugins are made available when running as a bundled tool in
Software Risk Manager:

- [eslint-plugin-security](https://www.npmjs.com/package/eslint-plugin-security): enabled by
  default
- [eslint-plugin-scanjs-rules](https://www.npmjs.com/package/eslint-plugin-scanjs-rules):
  disabled by default
- [eslint-plugin-no-unsanitized](https://www.npmjs.com/package/eslint-plugin-no-unsanitized):
  enabled by default
- [eslint-plugin-xss](https://www.npmjs.com/package/eslint-plugin-xss): enabled by default
- [eslint-plugin-html](https://www.npmjs.com/package/eslint-plugin-html): enabled by default
- [eslint-plugin-react](https://www.npmjs.com/package/eslint-plugin-react): enabled by default
- [eslint-plugin-react-hooks](https://www.npmjs.com/package/eslint-plugin-react-hooks): enabled
  by default
- [eslint-plugin-n](https://www.npmjs.com/package/eslint-plugin-n): enabled by default; replaces
  eslint-plugin-node
- [eslint-plugin-node](https://www.npmjs.com/package/eslint-plugin-node): disabled by default
- [eslint-plugin-import](https://www.npmjs.com/package/eslint-plugin-import): enabled by
  default
- [eslint-plugin-flowtype](https://www.npmjs.com/package/eslint-plugin-flowtype): enabled by
  default
- [eslint-plugin-jsx-a11y](https://www.npmjs.com/package/eslint-plugin-jsx-a11y): disabled
  by default in Software Risk Manager Tool Configuration
- [@stylistic/eslint-plugin-js](https://www.npmjs.com/package/@stylistic/eslint-plugin-js):
  disabled by default
- [@babel/eslint-parser](https://www.npmjs.com/package/@babel/eslint-parser): default
  Software Risk Manager parser

Any of these plugins can be used in or excluded from your user-defined configs.
All plugins use their default or recommended rules and settings, except for
[no-location-href-assign](https://github.com/Rantanen/eslint-plugin-xss/blob/master/docs/rules/no-location-href-assign.md) from
`eslint-plugin-xss`. For this rule, Software Risk Manager
uses `encodeURIComponent` for the `escapeFunc`
option instead of the default `escape` function, which has been
deprecated. More information about how to configure these plugins can be found
on their respective npmjs or GitHub pages.

By default, Software Risk Manager will run ESLint on `.js`,
`.html`, and `.htm` files. If you want to
change this behavior, you can specify a comma-separated list of file extensions
with the `eslint.extensions` setting in your
`codedx.props` file. You do not need to include the
`.` with each file extension (`eslint.extensions =
js,html,htm`). Note that if you decide not to use the html plugin in
your custom configs, you must use this setting to specify that you want ESLint
to only run on `.js` files. Otherwise, it will try to scan any
`.html` and `.htm` files it finds as
javascript, which will cause ESLint parsing errors.

**Custom Plugins and ESLint Installations**

Software Risk Manager allows you to install third-party ESLint plugins, shareable
configs, and parsers. To do so, first make sure you have `npm`
installed and accessible from the command line by installing [Node.js](https://nodejs.org/en/).
Then, open a command line and navigate to the `tool-data/eslint`
directory or a project-specific subdirectory. From there, you can install any
plugins, shareable configs, and parsers you wish to use by running the command
`npm install ... --save`. You do not need to install any of
the plugins that are included with Software Risk Manager by default.

If you want to use your own ESLint environment, you can specify the path to it in
your `codedx.props` file with the `eslint.path`
setting. Software Risk Manager expects that the provided directory will point to
the folder containing ESLint's `bin` folder. Software Risk
Manager will also try to find any of the supported ESLint config files in this
directory. Note that if you use the global or project config files as described
above, they will take precedence over the ones in this folder. Also, when using
an external installation, Software Risk Manager will ignore any custom plugin
folders in the `tool-data/eslint` directory.

### ZPA

Software Risk Manager supports user-defined `forms-metadata.json`
ZPA Oracle Forms metadata files. Place the file within the
`tool-data/zpa` directory or within a project-specific
subdirectory. Files should follow the [format](https://github.com/felipebz/zpa/wiki/Oracle-Forms-support) defined by ZPA.

### STIG

By default, the STIG reader only ingests vulnerabilities with `Open`
and `Not Reviewed` status. The following properties can be configured
in the props file to also ingest other statuses if required:

- `stig.status.include-not-a-finding` determines whether to ingest
  vulnerabilities with `Not A Finding` status. Defaults to
  `false`.
- `stig.status.include-not-applicable` determines whether to ingest
  vulnerabilities with `Not Applicable` status. Defaults to
  `false`.

### IriusRisk

When ingesting IriusRisk data into Software Risk Manager using the tool connector,
either based on Threats or Countermeasures, it ingests custom fields data and puts it
into the result contextual description. The tool connector specifies a page size which
can be used to configure the number of custom fields that are included per page of the
API response:

- `iriusrisk.custom-fields-page-size` sets the number of custom
  fields to include per page. Defaults to `20`.

Also, when ingesting IriusRisk data based on Countermeasures specifically, the tool
connector includes the `Implementations` tab data in the contextual
description. This data is represented in Base 64 encoded form in the API response,
which is then decoded by SRM to get the raw data to put into the result contextual
description. The relevant properties to set the decoding scheme and charset used for
this can be changed according to preferences in the props file:

- `iriusrisk.countermeasure-implementation-decoder` sets the
  specific decoding scheme to use for the implementations data decoding process.
  Acceptable values include `Default`, `URL` and
  `MIME`. Defaults to using all three schemes until decoding is
  successful - using `Default`, `URL` and
  `MIME`, in that order.
- `iriusrisk.countermeasure-implementation-charset` sets the
  specific charset to use for the implementations data decoding process.
  Any canonical name or alias of a charset is an acceptable value. Defaults to using
  `UTF-8`.
