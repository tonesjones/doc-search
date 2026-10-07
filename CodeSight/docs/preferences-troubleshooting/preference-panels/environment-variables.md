---
title: "Environment Variables"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/environment-variables.html"
content_id: "MwSJfquwzy0fDaa~JoAtaA"
version: "2026.9.0"
section: "Code Sight: Preferences and Troubleshooting"
scraped_at: "2026-10-06T23:39:57.412011+00:00"
---

# Environment Variables

The Code Sight extension supports configuring environment variables at multiple levels. This allows you to set variables that are automatically applied when scans run, without needing to modify shell profiles or system environment settings.

## How environment variable precedence works

When a scan runs, Code Sight merges environment variables from all levels. If the same variable name is defined at more than one level, the most specific level wins:

| Priority | Level | Scope |
| --- | --- | --- |
| 1 (highest) | Scan configuration | Applies only to that specific scan |
| 2 | Project / Workspace | Applies to all scans in the current project or workspace |
| 3 | User | Applies to all scans across all projects on your machine |
| 4 (lowest) | OS environment | Variables inherited from your operating system |

Note: On Windows, variable name matching is case-insensitive (consistent with Windows behavior). On macOS and Linux, variable names are case-sensitive.

## Configure user-level environment variables

User-level variables apply to all scans across all projects on your machine. Use this for variables that should always be present regardless of which project is open.

**Examples:** `JAVA_HOME`, `MAVEN_HOME`

1. Open **Code Sight Settings**.
2. Select **Environment Variables**.
3. In the **User Variables** section, click **Add** to create a new entry.
4. Enter the variable **Name** and **Value**.
5. Repeat for additional variables.
6. Click **Apply** to save all changes.

## Configure project/workspace-level environment variables

Project-level variables apply only to scans within the current project or workspace. Use this for variables that are specific to a particular codebase.

Note: In VS Code, the term "workspace" is used when you open a `.code-workspace` file, and "project" when you open a folder directly. Environment variables work the same way in both cases.

1. Open **Code Sight Settings**.
2. Select **Environment Variables**.
3. In the **Project Variables** section, click **Add** to create a new entry.
4. Enter the variable **Name** and **Value**.
5. Repeat for additional variables.
6. Click **Apply** to save all changes.

Project-level variables are stored in a `.env` file in the `.codesight` directory of your project, making them shareable with your team via version control.

## Configure environment variables for a single scan configuration

Scan-config-level variables apply only when that specific scan runs. Use this for variables that are unique to a single scan type or scenario (for example, different build environments for Coverity captures).

1. Open a scan configuration.
2. Expand the **Advanced** section.
3. Locate the **Environment variables** field (below the PATH field).
4. Enter environment variables as key=value pairs in separate lines:

   ```
   MY_VAR=value1
   ANOTHER_VAR=value2
   ```
5. Save the scan configuration.

## Referencing other variables

Variable values can reference other environment variables (including OS variables) using `${VAR}` syntax. References are resolved against the full merged set of variables.

| Variable | Value | Resolves to |
| --- | --- | --- |
| `MY_SDK` | `/opt/sdk` | `/opt/sdk` |
| `MY_SDK_BIN` | `${MY_SDK}/bin` | `/opt/sdk/bin` |
| `CUSTOM_PATH` | `${PATH};/my/extra/path` | OS PATH + `/my/extra/path` |

Note: If a referenced variable cannot be resolved (e.g., due to a typo or circular reference), the literal `${VAR}` text is left in place.

## PATH handling

The existing **PATH** field in scan configurations continues to work as before — it appends to your OS PATH.

You can *also* set a `PATH` variable in the environment variables field. If you do, you must construct it as a complete path value (including a reference to the existing PATH if you want to preserve it):

```
PATH=${PATH};/path/to/tool1;/path/to/tool2
```

Both approaches are supported and can coexist.

## When variables take effect

Environment variables configured in Code Sight are applied **at scan time only**. They affect the environment in which scan engines execute, but they do not modify the underlying Code Sight extension or IDE environment.

If you update User or Project-level variables, the new values take effect the next time a scan runs.

## Recommended usage by scenario

| Scenario | Recommended level | Example |
| --- | --- | --- |
| Java/Maven paths used by all projects | User | `JAVA_HOME=/usr/lib/jvm/java-17` |
| Project-specific build tool location | Project | `GRADLE_HOME=/opt/project-gradle` |
| Different build configs for one scan | Scan config | `BUILD_TYPE=release;TARGET_ARCH=arm64` |
| Adding tool paths for all scans | User | `PATH=${PATH};/usr/local/bin` |

## Best practices

- **Use the most specific level appropriate.** Don't put project-specific values at the User level — it makes switching between projects error-prone.
- **Commit project** `.env` files to version control so teammates get the same scan environment.
- **Do not store secrets** (passwords, API tokens) in environment variables. Code Sight does not encrypt these values.
- **Use** `${VAR}` references to avoid duplicating paths across levels.
- **Do not override** `BLACKDUCK_HOME` or other internal Code Sight variables — doing so may cause unexpected behavior.

## Troubleshooting

| Problem | Possible cause | Solution |
| --- | --- | --- |
| Scan can't find a tool (e.g., `java not found`) | IDE didn't inherit your shell PATH | Add the tool's path as a User or Project-level variable, or set `PATH=${PATH};/path/to/tool` |
| Variable value not taking effect | A higher-priority level overrides it | Verify both the preference view and the scan configuration view to ensure a more specific level isn't overriding your setting. |
| `${VAR}` appears literally in scan output | Referenced variable doesn't exist or has a typo | Verify the referenced variable name is defined at the same or lower level |
| Changes not reflected in scan | Stale read | Variables apply at scan time; trigger a new scan after saving |

## Frequently asked questions

1. **What is the difference between "project" and "workspace" variables?**

   They are the same setting. VS Code calls it a "workspace" when using a `.code-workspace` file, and a "project" when opening a folder directly. The behavior is identical.
2. **Can I reference a variable defined at a different level?**

   Yes. For example, a scan-config variable can reference a User-level variable using `${VAR}` syntax. Variables are merged before references are resolved.
3. **Does Code Sight log which variables were used during a scan?**

   Yes. The environment variables applied during a scan are logged in the controller log for debugging purposes.
