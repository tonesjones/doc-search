# Draft answer for snippet scans with Detect

Status: user approved this answer and the single-case documentation export on 2026-09-27. A GPT-6 Luna replay at commit `e791f6c` produced a measured trace that failed. The user then reviewed the failed expectations on 2026-09-27 (decisions below) and removed `--detect.tools=SIGNATURE_SCAN` from this reference answer so Detect runs its default applicable tools. The case is not promoted. Promotion still requires a fresh passing replay, inspection of the full answer, and a dry-run preview before any `--apply`.

Set `BLACKDUCK_API_TOKEN` in your environment before you run Detect. Keep the token out of the command line. Confirm that your Black Duck registration includes the Snippets feature.

From Windows PowerShell, run:

```powershell
$Env:DETECT_JAR_PATH = Join-Path $HOME 'detect\download'
$Env:DETECT_EXIT_CODE_PASSTHRU = '1'
[Net.ServicePointManager]::SecurityProtocol = 'tls12'
irm "https://detect.blackduck.com/detect.ps1?$(Get-Random)" | iex
detect --blackduck.url=https://YOUR_BLACK_DUCK_SERVER --detect.source.path='C:\path\to\source' --detect.project.name=YOUR_PROJECT --detect.project.version.name=YOUR_VERSION --detect.blackduck.signature.scanner.snippet.matching=SNIPPET_MATCHING
```

From Linux Bash, run:

```bash
bash <(curl -s -L https://detect.blackduck.com/detect.sh) --blackduck.url=https://YOUR_BLACK_DUCK_SERVER --detect.source.path=/path/to/source --detect.project.name=YOUR_PROJECT --detect.project.version.name=YOUR_VERSION --detect.blackduck.signature.scanner.snippet.matching=SNIPPET_MATCHING
```

These generic scripts fetch the latest Detect release. For repeatable production runs, use a version-specific script and pin the Detect version. Keep the Detect download cache outside the source path. Do not set `SNIPPET_MATCHING_ONLY` for a first scan; it requires a prior successful full scan.

Detect runs signature scanning by default, and `SNIPPET_MATCHING` adds snippet matching to it. When the scan finishes and the server processes it, open the named project version in Black Duck. On its Components tab, select the Unconfirmed snippets link at the right of the risk graphs to open the Source tab (Source view) filtered to unconfirmed snippet matches. Confirm a match if you want it included as a confirmed snippet component. Detect's normal intelligent mode persists scan data, so no scan-mode flag is needed unless your configuration overrides the default with RAPID or STATELESS.

Sources: `BlackDuck SCA/docs/detect-12.0.0/planning-and-running-detect/running-the-detect-script.md`, `BlackDuck SCA/docs/detect-12.0.0/configuring-detect/providing-sensitive-values-such-as-credentials.md`, `BlackDuck SCA/docs/detect-12.0.0/configuring-detect/shell-script-configuration-and-environment-variables.md`, `BlackDuck SCA/docs/detect-12.0.0/detect-properties/detect-configuration-property-details/{blackduck-server,paths,project,signature-scanner}.md`, `BlackDuck SCA/docs/help-center/scanning-your-code/about-signature-scanning/about-snippet-matching.md`, `BlackDuck SCA/docs/help-center/about-project-version-boms/editing-a-project-version-bom/reviewing-snippet-matches/viewing-snippet-matches-in-the-source-tab.md`, and `BlackDuck SCA/docs/help-center/about-project-version-boms/understanding-the-information-in-a-project-versions-bom/unconfirmed-snippets-and-unmatched-components.md`.

## Review of the failed replay (2026-09-27)

The `e791f6c` Luna replay failed on required facts `detect.ps1`, `detect.sh`, `SIGNATURE_SCAN`, and `Source tab`, on the required Source-tab page, and on the abstention check. The user decided:

- **UI destination.** Either 2026.7 page is accepted (`must_retrieve_any`), and `Source tab` or `Source view` is accepted. The Source-tab page says the BOM badge opens the **Source** tab; the unconfirmed-snippets page says the link beside the Risk graphs goes to Source view. Confirming a match only applies when unconfirmed snippets exist, so the case does not require confirmation steps.
- **Signature scan.** The literal `SIGNATURE_SCAN` is not required; the answer must still say a signature scan runs. Detect 12.0.0 `paths.md` (Detect Tools Included) runs applicable tools when `detect.tools` is unset, and `--detect.tools=SIGNATURE_SCAN` would disable package-manager detection. A first-scan command with `SNIPPET_MATCHING_ONLY` is forbidden.
- **Detect scripts.** Generic `detect.ps1`/`detect.sh` and version-specific scripts such as `detect12.ps1`/`detect12.sh` are accepted; `running-the-detect-script.md` recommends version-specific scripts for production. Setting `DETECT_LATEST_RELEASE_VERSION` to `12.0.0` is forbidden because 12.0.0 is the documentation snapshot, not a runtime requirement. That page's PowerShell "latest" example uses `detect12.ps1`, an inconsistency in the source documentation.
- **Version caveat.** The adapter prompt said to report an unavailable requested version without saying which product it named, so the answer stated that the checkout does not establish a Detect 2026.7 client. That phrase also triggers the abstention check. The prompt now says the requested version is the selected product's version and companion tools use their documented default. The abstention regex was not changed.

Accepted alternatives are recorded as verified entries in `evaluation/scoring/sca-human-equivalents.jsonl`.

## Live UI observation (separate from documentation evidence)

The user supplied a screenshot of a Black Duck project version's Components tab (Bill of Materials view) showing a **Snippets** section with an **Unconfirmed** count link at the far right of the risk graphs, and a **Source** tab in the project-version navigation. The server version, the scan that produced that version, and the account were not recorded, and the screenshot shows 0 unconfirmed snippets and an empty BOM. It corroborates the UI location only; it does not validate snippet-scan results. No live Detect scan was run for this case.
