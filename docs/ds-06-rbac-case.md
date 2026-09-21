# Preserve the SCA RBAC proof of concept

Assessment date: September 19, 2026.

## Outcome

DS-06 preserves the September 18 SCA 2026.7.0 RBAC exercise as one sanitized,
machine-checked case. The case records what each identity did through the UI,
API, MCP server, and Detect. It keeps unperformed tests separate from observed
success and observed denial.

The case lives at
[`BlackDuck SCA/verification/cases/sca-2026-7-rbac-poc.json`](../BlackDuck%20SCA/verification/cases/sca-2026-7-rbac-poc.json).
The SCA verifier validates the case during its normal offline run.

## Connect your own test environment

The repository does not contain a server URL, usernames, passwords, or API
tokens. Copy `BlackDuck SCA/verification/environment.example.json` to
`BlackDuck SCA/verification/environment.local.json`. Git ignores the local
file.

Set `base_url`, `expected_version`, and the principal mappings for your server.
Keep the credential values in the environment variables named by the local
file. Do not place credential values in either JSON file.

Another user must create their own local file and environment variables. A test
server replacement creates a new environment and a new observation. It does not
change the historical case.

## Recovered configuration

The isolated demonstration used these scoped assignments:

| Principal | Role | Scope |
|---|---|---|
| Central DevOps group | Global Project Manager | Global |
| BU-A group | BOM Manager | BU-A project group |
| BU-A group | Project Code Scanner | BU-A project group |
| BU-B group | BOM Manager | BU-B project group |
| BU-C group | BOM Manager | BU-C project group |

The committed case uses generic principal and resource labels. Raw credentials,
server names, internal identifiers, and customer names remain outside the
repository.

## Preserved observations

The case records these completed checks:

- A BU-A user saw exactly the two assigned BU-A projects and did not see the
  ungrouped control project.
- A user assigned to BU-A and BU-B saw the four projects in those groups.
- A user with no access saw no projects.
- A Central DevOps user saw all seven projects.
- The BU-A user generated an SPDX 2.3 JSON SBOM from an assigned project.
- An MCP snippet request completed with zero matches. This proves request
  processing, not positive matching or project isolation.
- Detect 12 ran as the BU-A identity. The scan mapped one source file to the
  assigned project and produced one unconfirmed snippet candidate.

The case does not claim that a Confirm or Ignore mutation completed. The
original run left the candidate unconfirmed. It also does not claim that a
direct API request against an unassigned project returned a preserved denial.

## Validation rules

`BlackDuck SCA/verification/rbac_case.py` rejects a case when any of these
conditions apply:

- A secret-bearing field or private proof-of-concept hostname is present.
- A principal, evidence item, scenario, or claim references an unknown ID.
- A documentation evidence path does not exist.
- A promoted claim relies on an untested scenario.
- A claim that requires isolation evidence lacks an observed negative control.

Run the checks from the repository root:

```powershell
python -B -m unittest tests.test_rbac_case tests.test_rbac_environment tests.test_sca_verification
python -B "BlackDuck SCA/verification/verify.py"
```

## Learning boundary

Future automated work may create candidate scenarios from new questions,
version changes, or contradictions between interfaces. Candidate scenarios do
not change product guidance. Promotion requires a reviewed claim, supporting
evidence, the applicable product version, and any required negative control.

This design allows proactive discovery without allowing saved assistant answers,
customer statements, or one server observation to become trusted product facts.

## Remaining live work

Complete these checks only in an approved disposable environment:

1. Read an unassigned project directly through the API and preserve the denial.
2. Confirm or ignore one disposable snippet candidate in an assigned project.
3. Attempt the equivalent mutation outside the principal's assigned scope.
4. Save sanitized response metadata and screenshots with identity and version
   labels.

The existing historical evidence is sufficient for the project-group visibility
claim and its negative control. It is not sufficient for an end-to-end Match
Review mutation claim.
