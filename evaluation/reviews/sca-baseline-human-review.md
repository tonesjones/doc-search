# SCA baseline human-review packet

Generated: `2026-08-24T18:30:11.961836+00:00`  
Cases: **30** · machine pass: **12** · machine fail: **18** · human reviewed: **2/30**

This packet is derived from the preserved SCA baseline, its production traces, and its machine report. It does not modify the baseline. The machine-readable human decisions belong in `sca-baseline-adjudications.jsonl`.

## Review method

1. Complete **Pass A** from the customer-visible question and answer before opening the evidence details.
2. Judge correctness, requested scope, clarity, and whether the answer abstained when it should have.
3. Open **Pass B** and compare the answer with the version-matched evidence, citations, retrieval, and machine scoring.
4. Record exactly one verdict in the companion JSONL: `TRUE_PASS`, `FALSE_PASS`, `TRUE_FAILURE`, `SCORING_FALSE_NEGATIVE`, `BENCHMARK_NEEDS_REVISION`, or `NEEDS_PRODUCT_EXPERT`.
5. Set `review_status` to `REVIEWED`, add the reviewer and review time, and explain every verdict except an obvious `TRUE_PASS`.

Do not change expected facts during review. If the benchmark is wrong or overly literal, use `BENCHMARK_NEEDS_REVISION` or `SCORING_FALSE_NEGATIVE`; preserve the original case until that decision is reviewed separately.

## Machine summary

| Result | Count |
|---|---:|
| PASS | 12 |
| FAIL | 18 |

| Failure class | Count |
|---|---:|
| ABSTENTION_FAILURE | 1 |
| CITATION_FAILURE | 5 |
| RETRIEVAL_FAILURE | 3 |
| SYNTHESIS_FAILURE | 17 |
| UNSUPPORTED_CLAIM | 1 |
| VERSION_FAILURE | 1 |

## Review queue

| # | Case | Machine | Failures | Human verdict |
|---:|---|---|---|---|
| 1 | [`sca-auth-001`](#case-sca-auth-001) | FAIL | SYNTHESIS_FAILURE | SCORING_FALSE_NEGATIVE |
| 2 | [`sca-auth-002`](#case-sca-auth-002) | PASS | — | TRUE_PASS |
| 3 | [`sca-auth-003`](#case-sca-auth-003) | PASS | — | UNREVIEWED |
| 4 | [`sca-auth-004`](#case-sca-auth-004) | PASS | — | UNREVIEWED |
| 5 | [`sca-auth-005`](#case-sca-auth-005) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 6 | [`sca-auth-006`](#case-sca-auth-006) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 7 | [`sca-auth-007`](#case-sca-auth-007) | FAIL | CITATION_FAILURE, RETRIEVAL_FAILURE, SYNTHESIS_FAILURE | UNREVIEWED |
| 8 | [`sca-auth-008`](#case-sca-auth-008) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 9 | [`sca-auth-009`](#case-sca-auth-009) | PASS | — | UNREVIEWED |
| 10 | [`sca-project-001`](#case-sca-project-001) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 11 | [`sca-project-002`](#case-sca-project-002) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 12 | [`sca-project-003`](#case-sca-project-003) | FAIL | CITATION_FAILURE, RETRIEVAL_FAILURE, SYNTHESIS_FAILURE | UNREVIEWED |
| 13 | [`sca-project-004`](#case-sca-project-004) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 14 | [`sca-version-001`](#case-sca-version-001) | PASS | — | UNREVIEWED |
| 15 | [`sca-version-002`](#case-sca-version-002) | PASS | — | UNREVIEWED |
| 16 | [`sca-version-003`](#case-sca-version-003) | PASS | — | UNREVIEWED |
| 17 | [`sca-version-004`](#case-sca-version-004) | FAIL | CITATION_FAILURE, SYNTHESIS_FAILURE | UNREVIEWED |
| 18 | [`sca-version-005`](#case-sca-version-005) | FAIL | CITATION_FAILURE, SYNTHESIS_FAILURE | UNREVIEWED |
| 19 | [`sca-version-006`](#case-sca-version-006) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 20 | [`sca-version-007`](#case-sca-version-007) | PASS | — | UNREVIEWED |
| 21 | [`sca-version-008`](#case-sca-version-008) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 22 | [`sca-version-009`](#case-sca-version-009) | FAIL | CITATION_FAILURE, RETRIEVAL_FAILURE, SYNTHESIS_FAILURE | UNREVIEWED |
| 23 | [`sca-bom-001`](#case-sca-bom-001) | PASS | — | UNREVIEWED |
| 24 | [`sca-security-001`](#case-sca-security-001) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 25 | [`sca-security-002`](#case-sca-security-002) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 26 | [`sca-security-003`](#case-sca-security-003) | FAIL | SYNTHESIS_FAILURE | UNREVIEWED |
| 27 | [`sca-security-004`](#case-sca-security-004) | PASS | — | UNREVIEWED |
| 28 | [`sca-role-001`](#case-sca-role-001) | PASS | — | UNREVIEWED |
| 29 | [`sca-role-002`](#case-sca-role-002) | PASS | — | UNREVIEWED |
| 30 | [`sca-version-caveat-001`](#case-sca-version-caveat-001) | FAIL | ABSTENTION_FAILURE, UNSUPPORTED_CLAIM, VERSION_FAILURE | UNREVIEWED |

## Cases

<a id="case-sca-auth-001"></a>

### 1. `sca-auth-001` — machine FAIL

Human review: **SCORING_FALSE_NEGATIVE** · status: `REVIEWED`

#### Pass A — customer view

**Question:** What authentication mechanism does the Black Duck SCA REST API use?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-1c730432f5954cdfbb7e74059bdaa520`

**Production answer:**

~~~~text
Black Duck SCAâ€™s REST API uses **token-based authentication**:

1. Create a user API token in Black Duck.
2. Send it to `POST /api/tokens/authenticate` using:
   ```http
   Authorization: token <api-token>
   ```
3. The response contains a short-lived bearer [REDACTED] Use it for later requests:
   ```http
   Authorization: Bearer <bearer-token>
   ```

Source: [Authenticating with the API](</C:/TestCode/Product Docs/BlackDuck SCA/docs/api/authenticating-with-the-api.md>) (Black Duck SCA 2026.7).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `API tokens` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- `username and password are the REST API authentication mechanism` (EXACT_FACT, case-insensitive)

**Authoritative evidence:**

- [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>) — section `# Authenticating with the API` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/docs/api/using-the-right-media-types.md](<../../BlackDuck SCA/docs/api/using-the-right-media-types.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/api/using-the-black-duck-api-with-postman.md](<../../BlackDuck SCA/docs/api/using-the-black-duck-api-with-postman.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `API tokens` (EXACT_FACT, case-insensitive)
- `PASS` forbidden: `username and password are the REST API authentication mechanism` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-auth-002"></a>

### 2. `sca-auth-002` — machine PASS

Human review: **TRUE_PASS** · status: `REVIEWED`

#### Pass A — customer view

**Question:** Which endpoint exchanges a Black Duck SCA API token for a bearer token?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-3df1048faa694e0c80ff54e6597f1262`

**Production answer:**

~~~~text
Send an HTTP `POST` request to:

```http
/api/tokens/authenticate
```

Include the API token as:

```http
Authorization: token <your-api-token>
```

Source: [authenticating-with-the-api.md](<C:/TestCode/Product Docs/BlackDuck SCA/docs/api/authenticating-with-the-api.md:27>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `/api/tokens/authenticate` (EXACT_FACT, case-sensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>) — section `## Step 2: Exchange the token for a bearer token` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/api/using-the-black-duck-api-with-postman.md](<../../BlackDuck SCA/docs/api/using-the-black-duck-api-with-postman.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `/api/tokens/authenticate` (EXACT_FACT, case-sensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-auth-003"></a>

### 3. `sca-auth-003` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** How is the Black Duck SCA API token placed in the authentication request header?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-e9eca146451542fb910cd6f6d4d8c03a`

**Production answer:**

~~~~text
Place it in the `Authorization` request header using the `token` scheme:

```http
Authorization: token <your-api-token>
```

Example authentication request:

```bash
curl -X POST \
  https://<black-duck-server>/api/tokens/authenticate \
  -H "Accept: application/vnd.blackducksoftware.user-4+json" \
  -H "Authorization: token <your-api-token>"
```

The response contains a bearer [REDACTED] for subsequent API requests.

Source: [Authenticating with the API](<C:/TestCode/Product Docs/BlackDuck SCA/docs/api/authenticating-with-the-api.md:27>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `Authorization: token <your-api-token>` (EXACT_FACT, case-sensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>) — section `## Step 2: Exchange the token for a bearer token` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/index-detect.md](<../../BlackDuck SCA/index-detect.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/executing-the-black-duck-c-cpp-tool.md](<../../BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/executing-the-black-duck-c-cpp-tool.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/detect/release-notes/release-notes-for-older-detect-versions.md](<../../BlackDuck SCA/docs/detect/release-notes/release-notes-for-older-detect-versions.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `Authorization: token <your-api-token>` (EXACT_FACT, case-sensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-auth-004"></a>

### 4. `sca-auth-004` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What permissions does a user access token have relative to the user who created it?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-450d48ec16e04ddbb830d5e214d528a5`

**Production answer:**

~~~~text
A Black Duck user access token inherits the **same role and permissions as the user who created it**. It cannot grant greater privileges.

The token is further limited by its selected scope: **read-only** or **read/write**. If the user is inactivated, the token is invalidated.

[Black Duck SCA documentation](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md:21>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `same role` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) — section `# Managing user access tokens` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `same role` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-auth-005"></a>

### 5. `sca-auth-005` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Do Black Duck SCA user access tokens expire?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-f4f0ca4103814b6b8a140322059d4ef5`

**Production answer:**

~~~~text
No. Black Duck SCA **user access tokens do not expire**.

They can still become invalid if:

- An administrator purges them after a configured period of inactivity.
- The owning user account is inactivated.
- The token is deleted or regenerated.

The short-lived **bearer [REDACTED]** obtained by authenticating with a user access token does expire; that is a different token.

Source: [Managing user access tokens](</C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) (Black Duck SCA 2026.7).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `Access tokens do not expire` (EXACT_FACT, case-insensitive)
- `purged after a set period` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) — section `# Managing user access tokens` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/detect/detect-quickstart-guide.md](<../../BlackDuck SCA/docs/detect/detect-quickstart-guide.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/detect/detect-properties/basic-properties.md](<../../BlackDuck SCA/docs/detect/detect-properties/basic-properties.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/detect/detect-properties/all-properties.md](<../../BlackDuck SCA/docs/detect/detect-properties/all-properties.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `Access tokens do not expire` (EXACT_FACT, case-insensitive)
- `FAIL` required: `purged after a set period` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-auth-006"></a>

### 6. `sca-auth-006` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What happens to a user's Black Duck SCA access tokens when that user is inactivated?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-3fa25490a9854d65b780b74bbdcc0c3a`

**Production answer:**

~~~~text
When a Black Duck SCA user is inactivated, **all access tokens tied to that user are invalidated** and can no longer authenticate API or integration requests. The documentation says “invalidated,” not deleted.

Source: [Managing user access tokens](</C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) (Black Duck SCA 2026.7).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `tokens are invalidated` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) — section `# Managing user access tokens` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/bridge/bridge-cli-reference/complete-list-of-bridge-arguments.md](<../../BlackDuck SCA/docs/bridge/bridge-cli-reference/complete-list-of-bridge-arguments.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/bridge/jenkins-black-duck-security-scan-plugin-for-jenkins/using-the-black-duck-security-scan-plugin-with-software-risk-manager.md](<../../BlackDuck SCA/docs/bridge/jenkins-black-duck-security-scan-plugin-for-jenkins/using-the-black-duck-security-scan-plugin-with-software-risk-manager.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/administering-black-duck/viewing-jobs.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/viewing-jobs.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `tokens are invalidated` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-auth-007"></a>

### 7. `sca-auth-007` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Can one Black Duck SCA user have multiple access tokens, and what naming constraint applies?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-8547408fa62a40a1adb3117b22a5deef`

**Production answer:**

~~~~text
Yes. A Black Duck SCA user can have multiple access tokens, but **each token must have a unique name**.

Source: [Managing user access tokens](</C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md:24>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `multiple tokens` (EXACT_FACT, case-insensitive)
- `unique name` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) — section `# Managing user access tokens` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>)

**Top retrieved files:**

- None

**Machine failures:** `CITATION_FAILURE, RETRIEVAL_FAILURE, SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `None`

**Machine fact results:**

- `FAIL` required: `multiple tokens` (EXACT_FACT, case-insensitive)
- `PASS` required: `unique name` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-auth-008"></a>

### 8. `sca-auth-008` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** After creating a Black Duck SCA user access token, can its value be viewed later?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-9043d30ae3bf46d48b42661158ea8d6c`

**Production answer:**

~~~~text
No. The token value is shown only once, immediately after creation. After closing the dialog, it cannot be viewed again.

If it wasn’t saved, regenerate the token and copy the new value; the previous value will be replaced.

Source: [Managing user access tokens](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `cannot view the value` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) — section `## Generating an access token` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `cannot view the value` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-auth-009"></a>

### 9. `sca-auth-009` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Where does the current corpus say a Black Duck SCA API token is created? Surface any differing UI paths.

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-78f1552554c24085942bf9e05afaad02`

**Production answer:**

~~~~text
The corpus’s clearest current Black Duck SCA 2026.7 path is:

**Top navigation user menu → My Access Tokens → Create New Token**

This is the dedicated user-token procedure. It also says tokens can only be created by the current user. See [managing-user-access-tokens.md](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md:34>).

Differing paths also appear:

| Corpus source | Documented UI path |
|---|---|
| SCA API guide, also 2026.7 | **Top-right menu → System → Access Tokens → Create New Token** ([authenticating-with-the-api.md](<C:/TestCode/Product Docs/BlackDuck SCA/docs/api/authenticating-with-the-api.md:15>)) |
| C/CPP Tool, “latest” | **Top-right user menu → Access Tokens → + Create Token** ([api-token.md](<C:/TestCode/Product Docs/BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/api-token.md:26>)) |
| Detect Jenkins integration 11.5.1 | **Top navigation user menu → My Access Tokens → Create New Token** ([users-and-roles-for-jenkins-plugin.md](<C:/TestCode/Product Docs/BlackDuck SCA/docs/detect/detect-integrations/detect-jenkins-plugin/users-and-roles-for-jenkins-plugin.md:14>)) |
| Detect GitLab/Bitbucket integrations 11.5.1 | **User profile → User Access Token section → Generate** ([detect-gitlab-integration.md](<C:/TestCode/Product Docs/BlackDuck SCA/docs/detect/detect-integrations/detect-gitlab-integration.md:14>), [detect-bitbucket-integration.md](<C:/TestCode/Product Docs/BlackDuck SCA/docs/detect/detect-integrations/detect-bitbucket-integration.md:18>)) |

Bottom line: use **user menu → My Access Tokens → Create New Token** as the primary current path. The corpus is internally inconsistent even within the 2026.7 material—especially the API guide’s **System → Access Tokens** wording. The profile-page and **Generate** instructions appear to reflect an older UI workflow retained in companion documentation.
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `surface_conflict`

**Required facts:**

- `System` (EXACT_FACT, case-insensitive)
- `My Access Tokens` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>) — section `## Step 1: Generate an API token` — corpus `bd-docs-9485d952-20260823`
- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>) — section `## Generating an access token` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/access-tokens/managing-user-access-tokens.md>)
- [BlackDuck SCA/docs/api/authenticating-with-the-api.md](<../../BlackDuck SCA/docs/api/authenticating-with-the-api.md>)
- [BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/api-token.md](<../../BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/api-token.md>)
- [BlackDuck SCA/docs/detect/detect-integrations/detect-jenkins-plugin/users-and-roles-for-jenkins-plugin.md](<../../BlackDuck SCA/docs/detect/detect-integrations/detect-jenkins-plugin/users-and-roles-for-jenkins-plugin.md>)
- [BlackDuck SCA/docs/detect/detect-integrations/detect-gitlab-integration.md](<../../BlackDuck SCA/docs/detect/detect-integrations/detect-gitlab-integration.md>)
- [BlackDuck SCA/docs/detect/detect-integrations/detect-bitbucket-integration.md](<../../BlackDuck SCA/docs/detect/detect-integrations/detect-bitbucket-integration.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/executing-the-black-duck-c-cpp-tool.md](<../../BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/executing-the-black-duck-c-cpp-tool.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/api-token.md](<../../BlackDuck SCA/docs/c-cpp-tool/black-duck-c-cpp-tool/api-token.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/api/using-the-black-duck-api-with-postman.md](<../../BlackDuck SCA/docs/api/using-the-black-duck-api-with-postman.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `System` (EXACT_FACT, case-insensitive)
- `PASS` required: `My Access Tokens` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-project-001"></a>

### 10. `sca-project-001` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What is the base unit in Black Duck SCA?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-3eedd06ce5714e60bbb4e313469e7ead`

**Production answer:**

~~~~text
A **project** is the base unit in Black Duck SCA. It may be a standalone development project or part of a larger project.

Source: [Creating a project](C:\TestCode\Product Docs\BlackDuck SCA\docs\help-center\understanding-projects-in-black-duck\creating-a-project.md:12)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `A project is the base unit` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md>) — section `# Creating a project` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/scanning-best-practices/scanning-best-practices-2.md](<../../BlackDuck SCA/docs/scanning-best-practices/scanning-best-practices-2.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/scanning-best-practices/rapid-scan-overview.md](<../../BlackDuck SCA/docs/scanning-best-practices/rapid-scan-overview.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/release-notes/black-duck-sca-version-2026-7-0/new-and-changed-features.md](<../../BlackDuck SCA/docs/release-notes/black-duck-sca-version-2026-7-0/new-and-changed-features.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `A project is the base unit` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-project-002"></a>

### 11. `sca-project-002` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What Managed Code base limit does the Black Duck SCA project documentation state?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-b66540a0c43046aca71516a785366002`

**Production answer:**

~~~~text
Black Duck SCA documentation states a **10 GB Managed Code base limit per project or application**.

Source: [Creating a project](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md:18>) (version 2026.7).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `10GB` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md>) — section `# Creating a project` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/architecture-hosted/architecture-overview/communication-between-the-scan-client-black-duck-and-black-duck-services.md](<../../BlackDuck SCA/docs/architecture-hosted/architecture-overview/communication-between-the-scan-client-black-duck-and-black-duck-services.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `1.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `10GB` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-project-003"></a>

### 12. `sca-project-003` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Must a Black Duck SCA project name be unique?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-0e22bbd37a2342dc986c28c5ce169182`

**Production answer:**

~~~~text
Yes. A Black Duck SCA project name must be unique among all projects in that Black Duck instance. It may, however, match a project name in the Black Duck KnowledgeBase.

Source: [Creating a project](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md:28>). Detect also returns duplicate-project exit code 21 when creation conflicts.
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `must be unique among projects` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md>) — section `To create a project:` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project.md>)

**Top retrieved files:**

- None

**Machine failures:** `CITATION_FAILURE, RETRIEVAL_FAILURE, SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `None`

**Machine fact results:**

- `FAIL` required: `must be unique among projects` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-project-004"></a>

### 13. `sca-project-004` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** How many versions does a Black Duck SCA project have when first created?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-f0b42d4e7de74d838b9b0535db7495b3`

**Production answer:**

~~~~text
A newly created Black Duck SCA project has **one version**. Additional versions can be added later.

Source: [Creating a new version of a project](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md:12>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `it has one version` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>) — section `# Creating a new version of a project` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project/creating-a-scm-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/creating-a-project/creating-a-scm-project.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/cloning-projects.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/cloning-projects.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `it has one version` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-001"></a>

### 14. `sca-version-001` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What is the default phase for a new Black Duck SCA project version?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-3966651161134d24adeb90a0402ba15c`

**Production answer:**

~~~~text
The default phase for a new Black Duck SCA project version is **In Planning**.

Source: [About project version phases](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md:35>) (Black Duck SCA 2026.7).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `In Planning` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- `In Development is the default` (EXACT_FACT, case-insensitive)

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>) — section `In Planning (Default)` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/scanning-best-practices/scanning-best-practices-2.md](<../../BlackDuck SCA/docs/scanning-best-practices/scanning-best-practices-2.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2020-12-x/new-and-changed-features-in-version-2020-12-0.md](<../../BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2020-12-x/new-and-changed-features-in-version-2020-12-0.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2022-2-x/new-and-changed-features-in-version-2022-2-0/api-enhancements.md](<../../BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2022-2-x/new-and-changed-features-in-version-2022-2-0/api-enhancements.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `In Planning` (EXACT_FACT, case-insensitive)
- `PASS` forbidden: `In Development is the default` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-002"></a>

### 15. `sca-version-002` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Which project version phases are documented by Black Duck SCA?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-7a052ea938ae4bfdae7ec5603a5d96b5`

**Production answer:**

~~~~text
Black Duck SCA 2026.7 documents six project-version phases:

- **In Planning** — default
- **In Development**
- **Pre-release**
- **Released**
- **Deprecated**
- **Archived**

The first five are treated alike and included in project risk calculations. **Archived** versions are treated differently and excluded from those calculations.

Source: [About project version phases](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `In Planning` (EXACT_FACT, case-insensitive)
- `In Development` (EXACT_FACT, case-insensitive)
- `Pre-release` (EXACT_FACT, case-insensitive)
- `Released` (EXACT_FACT, case-insensitive)
- `Deprecated` (EXACT_FACT, case-insensitive)
- `Archived` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md>) — section `# About project version phases` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `1.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `In Planning` (EXACT_FACT, case-insensitive)
- `PASS` required: `In Development` (EXACT_FACT, case-insensitive)
- `PASS` required: `Pre-release` (EXACT_FACT, case-insensitive)
- `PASS` required: `Released` (EXACT_FACT, case-insensitive)
- `PASS` required: `Deprecated` (EXACT_FACT, case-insensitive)
- `PASS` required: `Archived` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-003"></a>

### 16. `sca-version-003` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What is the default distribution for a new Black Duck SCA project version?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-e6904409bcc94cc7b98e240d30d8113d`

**Production answer:**

~~~~text
The default distribution for a new Black Duck SCA project version is **External**.

Source: [Creating a new version of a project](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `External` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- `Internal is the default` (EXACT_FACT, case-insensitive)

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>) — section `External (Default)` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2026-1-x/black-duck-sca-2026-1-0/announcements.md](<../../BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2026-1-x/black-duck-sca-2026-1-0/announcements.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `External` (EXACT_FACT, case-insensitive)
- `PASS` forbidden: `Internal is the default` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-004"></a>

### 17. `sca-version-004` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Are internally distributed project versions included in Black Duck SCA project risk calculations?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-190bdeb34a4f408798148b3c24b9b5ca`

**Production answer:**

~~~~text
No. Black Duck SCA excludes project versions whose **Distribution** is set to **Internal** from the project’s aggregate risk calculations.

This does not mean the version’s own BOM risks disappear; it means they do not contribute to the project-level calculation. Archived versions are likewise excluded.

Source: [Creating a new version of a project](C:/TestCode/Product%20Docs/BlackDuck%20SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md) (Black Duck SCA 2026.7).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `not included in the risk calculations` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>) — section `Distribution` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- None

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/help-center/viewing-your-dashboards/about-saved-searches-dashboards.md](<../../BlackDuck SCA/docs/help-center/viewing-your-dashboards/about-saved-searches-dashboards.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/viewing-risk-in-black-duck.md](<../../BlackDuck SCA/docs/help-center/viewing-risk-in-black-duck.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/viewing-risk-in-black-duck/viewing-overall-risk.md](<../../BlackDuck SCA/docs/help-center/viewing-risk-in-black-duck/viewing-overall-risk.md>) — version `2026.7`

**Machine failures:** `CITATION_FAILURE, SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `not included in the risk calculations` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-005"></a>

### 18. `sca-version-005` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Are archived Black Duck SCA project versions included in project risk calculations?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-514a8559d1e3458495537acef66653d8`

**Production answer:**

~~~~text
No. Black Duck SCA excludes project versions whose phase is **Archived** from project-level risk calculations.

Source: [Understanding projects in Black Duck](/C:/TestCode/Product%20Docs/BlackDuck%20SCA/docs/help-center/understanding-projects-in-black-duck.md:42) (SCA 2026.7 documentation).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `excluded from project risk calculations` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md>) — section `## About archived project versions` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- None

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/help-center/about-security-risk/remediating-security-vulnerabilities.md](<../../BlackDuck SCA/docs/help-center/about-security-risk/remediating-security-vulnerabilities.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/hosted-vs-air-gapped-knowledgebase.md](<../../BlackDuck SCA/docs/help-center/hosted-vs-air-gapped-knowledgebase.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/administering-black-duck/viewing-jobs.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/viewing-jobs.md>) — version `2026.7`

**Machine failures:** `CITATION_FAILURE, SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `excluded from project risk calculations` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-006"></a>

### 19. `sca-version-006` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Are new and updated policy rules evaluated for archived Black Duck SCA project versions?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-c217b0dba70548d9a04f93b9f20e6406`

**Production answer:**

~~~~text
No. For archived Black Duck SCA project versions:

- New policy rules are not evaluated.
- Changes to existing policy-rule expressions are not evaluated.
- However, violations from disabled or deleted policy rules are removed.

Source: [About project version phases](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md:73>) (Black Duck SCA 2026.7 documentation).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `not evaluated in archived project versions` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md>) — section `## About archived project versions` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/about-project-version-phases.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/release-notes/black-duck-sca-version-2026-7-0/announcements.md](<../../BlackDuck SCA/docs/release-notes/black-duck-sca-version-2026-7-0/announcements.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `not evaluated in archived project versions` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-007"></a>

### 20. `sca-version-007` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What phase does a cloned Black Duck SCA project version default to?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-dfdba38a0a5349aaa82d970c642cd0e3`

**Production answer:**

~~~~text
A cloned Black Duck SCA project version defaults to **In Development** when the source version is **Archived**; the Archived phase is not retained.

[Cloning project versions](</C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md:71>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `In Development` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- `In Planning is the cloned version default` (EXACT_FACT, case-insensitive)

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md>) — section `The cloned version will default` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/detect/release-notes/release-notes-for-previous-detect-versions.md](<../../BlackDuck SCA/docs/detect/release-notes/release-notes-for-previous-detect-versions.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/detect/detect-properties/basic-properties.md](<../../BlackDuck SCA/docs/detect/detect-properties/basic-properties.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `In Development` (EXACT_FACT, case-insensitive)
- `PASS` forbidden: `In Planning is the cloned version default` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-008"></a>

### 21. `sca-version-008` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Can Black Duck SCA clone individual component or remediation values?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-1c5ae718ad484e09b0787c922754dd14`

**Production answer:**

~~~~text
No. Black Duck SCA can clone categories such as **Component Edits** or **Remediation Details**, but it cannot clone selected individual component or remediation values.

Cloned data applies only to matching components present in the newly scanned version, plus manually added components. See [Cloning project versions](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md:77>) (SCA 2026.7).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `cannot clone individual component or remediation values` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md>) — section `cannot clone individual component` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/cloning-project-versions.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/getting-started/viewing-your-bill-of-materials-bom.md](<../../BlackDuck SCA/docs/getting-started/viewing-your-bill-of-materials-bom.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/detect/detect-quickstart-guide.md](<../../BlackDuck SCA/docs/detect/detect-quickstart-guide.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/detect/detect-properties/all-properties.md](<../../BlackDuck SCA/docs/detect/detect-properties/all-properties.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `cannot clone individual component or remediation values` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-009"></a>

### 22. `sca-version-009` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Can a Black Duck SCA project version be converted back from Long-Term Support?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-c2b85e1a4dc74e0193a20582799becfc`

**Production answer:**

~~~~text
No. Converting a Black Duck SCA project version from **Active** to **Long-Term Support (LTS)** is a one-way process. It cannot currently be reverted to Active after conversion begins.

LTS conversion also removes certain project and scan data, so Black Duck recommends reviewing the limitations before converting.

Source: [Black Duck SCA 2026.7 — Converting a project version to LTS](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-long-term-support-lts-projects/converting-a-project-version-to-lts.md>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `one-way process` (EXACT_FACT, case-insensitive)
- `cannot be reverted` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-long-term-support-lts-projects.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-long-term-support-lts-projects.md>) — section `# About Long-Term support (LTS) projects` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-long-term-support-lts-projects/converting-a-project-version-to-lts.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-long-term-support-lts-projects/converting-a-project-version-to-lts.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/index-detect.md](<../../BlackDuck SCA/index-detect.md>) — version `2026.7`

**Machine failures:** `CITATION_FAILURE, RETRIEVAL_FAILURE, SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `None`

**Machine fact results:**

- `PASS` required: `one-way process` (EXACT_FACT, case-insensitive)
- `FAIL` required: `cannot be reverted` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-bom-001"></a>

### 23. `sca-bom-001` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** By default, which components and subprojects are included in a Black Duck SCA Notices File report?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-ada5093a90ec40108a1a913786173291`

**Production answer:**

~~~~text
By default, **all components and subprojects in the project-version BOM** are included in the Black Duck SCA Notices File report, unless explicitly excluded.

Source: [Black Duck SCA 2026.7 documentation](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/about-project-version-boms/generating-project-version-reports/notices-file-report/excluding-a-component-or-subproject-from-the-notices-file-report.md:12>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `all components and subprojects` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/about-project-version-boms/generating-project-version-reports/notices-file-report/excluding-a-component-or-subproject-from-the-notices-file-report.md](<../../BlackDuck SCA/docs/help-center/about-project-version-boms/generating-project-version-reports/notices-file-report/excluding-a-component-or-subproject-from-the-notices-file-report.md>) — section `# Excluding a component or subproject from the Notices File report` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/about-project-version-boms/generating-project-version-reports/notices-file-report/excluding-a-component-or-subproject-from-the-notices-file-report.md](<../../BlackDuck SCA/docs/help-center/about-project-version-boms/generating-project-version-reports/notices-file-report/excluding-a-component-or-subproject-from-the-notices-file-report.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/scanning-best-practices/rapid-scan-overview.md](<../../BlackDuck SCA/docs/scanning-best-practices/rapid-scan-overview.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/detect/planning-and-running-detect/stateless-scan.md](<../../BlackDuck SCA/docs/detect/planning-and-running-detect/stateless-scan.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/detect/planning-and-running-detect/rapid-scan.md](<../../BlackDuck SCA/docs/detect/planning-and-running-detect/rapid-scan.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `all components and subprojects` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-security-001"></a>

### 24. `sca-security-001` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** After how many failed local login attempts is a Black Duck SCA account locked, and for how long?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-7e2bdbb9c43349429739a42c76a28d11`

**Production answer:**

~~~~text
A local Black Duck SCA account is locked after **10 failed password attempts** for **10 minutes**.

There is no time window for accumulating failures; the counter resets after a successful login. This lockout does not apply to SAML or LDAP users.

Source: [Black Duck SCA 2026.7 documentation](</C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md:10>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `10 attempts` (EXACT_FACT, case-insensitive)
- `10 minutes` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md>) — section `# About locked out user accounts` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/detect/release-notes/release-notes-for-previous-detect-versions.md](<../../BlackDuck SCA/docs/detect/release-notes/release-notes-for-previous-detect-versions.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/detect/detect-components/detectors.md](<../../BlackDuck SCA/docs/detect/detect-components/detectors.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2021-10-x/new-and-changed-features-in-version-2021-10-1/fixed-issues-in-2021-10-1.md](<../../BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2021-10-x/new-and-changed-features-in-version-2021-10-1/fixed-issues-in-2021-10-1.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `10 attempts` (EXACT_FACT, case-insensitive)
- `PASS` required: `10 minutes` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-security-002"></a>

### 25. `sca-security-002` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Does Black Duck SCA's failed-password lockout apply to SAML or LDAP users?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-88491a6ab0344cbd9948c8cc24253094`

**Production answer:**

~~~~text
No. Black Duck SCA’s built-in lockout—10 failed attempts resulting in a 10-minute lockout—does **not** apply to users authenticating through SAML or LDAP.

Those users may still be subject to lockout policies enforced by their identity provider or LDAP directory.

Source: [About locked out user accounts](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md>) (Black Duck SCA 2026.7 documentation).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `does not apply to users logging in using SAML or LDAP` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md>) — section `# About locked out user accounts` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/about-locked-out-user-accounts.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/administering-black-duck/configuring-integrations/authenticating-users-with-ldap.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/configuring-integrations/authenticating-users-with-ldap.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/administering-black-duck/configuring-integrations/configuring-saml-for-single-sign-on.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/configuring-integrations/configuring-saml-for-single-sign-on.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `1.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `does not apply to users logging in using SAML or LDAP` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-security-003"></a>

### 26. `sca-security-003` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What are the default minimum password length and required character-type count for local Black Duck SCA accounts?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-f6212e691f6d4f369e41886d4cffbdaa`

**Production answer:**

~~~~text
By default, local Black Duck SCA accounts require:

- **Minimum password length:** 8 characters
- **Required character types:** 1 type

Character types include lowercase letters, uppercase letters, numbers, and special characters. These settings don’t apply to LDAP or SAML accounts.

Source: [Configuring password requirements](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md:43>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `eight characters` (EXACT_FACT, case-insensitive)
- `one character type` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md>) — section `By default, password requirements are enabled` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2020-12-x/new-and-changed-features-in-version-2020-12-0.md](<../../BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2020-12-x/new-and-changed-features-in-version-2020-12-0.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/alert/installation-references/black-duck-alert-environment-variables.md](<../../BlackDuck SCA/docs/alert/installation-references/black-duck-alert-environment-variables.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/alert/post-installation-configuration/encryption-and-proxy-configuration.md](<../../BlackDuck SCA/docs/alert/post-installation-configuration/encryption-and-proxy-configuration.md>) — version `2026.7`

**Machine failures:** `SYNTHESIS_FAILURE`

**Recall@1/3/5:** `0.0` / `1.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `FAIL` required: `eight characters` (EXACT_FACT, case-insensitive)
- `FAIL` required: `one character type` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-security-004"></a>

### 27. `sca-security-004` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What maximum password length does Black Duck SCA document for local accounts?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-9b8427d8fa4a4aad9c556c3c0e154d98`

**Production answer:**

~~~~text
Black Duck SCA documents a maximum password length of **128 characters** for local accounts.

Source: [Configuring password requirements](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md>) (SCA 2026.7).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `128 characters` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md>) — section `System Administrators can:` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/configuring-password-requirements.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `1.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `128 characters` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-role-001"></a>

### 28. `sca-role-001` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** Which global roles can create, edit, and delete Black Duck SCA projects?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-ca7a7e45288848ac91dce806faa89083`

**Production answer:**

~~~~text
The global roles that can create, edit, and delete Black Duck SCA projects are:

- **Global Project Administrator**
- **Global Project Manager**
- **Project Creator** — limited to editing or deleting projects created by that same user.

Source: [Black Duck SCA user role matrix](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md:23>) (version 2026.7).
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `Global Project Administrator` (EXACT_FACT, case-insensitive)
- `Global Project Manager` (EXACT_FACT, case-insensitive)
- `Project Creator` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md>) — section `## Global roles by task` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/global-roles-reference.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/global-roles-reference.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/administering-black-duck/viewing-heatmap-data.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/viewing-heatmap-data.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `0.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `Global Project Administrator` (EXACT_FACT, case-insensitive)
- `PASS` required: `Global Project Manager` (EXACT_FACT, case-insensitive)
- `PASS` required: `Project Creator` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-role-002"></a>

### 29. `sca-role-002` — machine PASS

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What project-version permission does the Black Duck SCA Global Release Creator role have?

**Requested product/version:** `blackduck-sca` / `2026.7`

**Answer ID:** `ans-a9fa4f72639c4e59bc3e1be6058faa70`

**Production answer:**

~~~~text
The **Global Release Creator** role has **Create permission only** for project versions. It cannot edit or delete them.

Source: [Black Duck SCA user role matrix](<C:/TestCode/Product Docs/BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md:25>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `answer`

**Required facts:**

- `Global Release Creator` (EXACT_FACT, case-insensitive)
- `Create permission only` (EXACT_FACT, case-insensitive)

**Forbidden facts:**

- None

**Authoritative evidence:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md>) — section `Manage projects versions` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2021-8-x/new-and-changed-features-in-version-2021-8-0.md](<../../BlackDuck SCA/docs/release-notes/previous-black-duck-sca-releases/black-duck-sca-2021-8-x/new-and-changed-features-in-version-2021-8-0.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/global-roles-reference.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/global-roles-reference.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md](<../../BlackDuck SCA/docs/help-center/administering-black-duck/administering-user-accounts/understanding-roles/black-duck-sca-user-role-matrix.md>) — version `2026.7`

**Machine failures:** `none`

**Recall@1/3/5:** `0.0` / `0.0` / `1.0`

**Version accuracy:** `True`

**Machine fact results:**

- `PASS` required: `Global Release Creator` (EXACT_FACT, case-insensitive)
- `PASS` required: `Create permission only` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---

<a id="case-sca-version-caveat-001"></a>

### 30. `sca-version-caveat-001` — machine FAIL

Human review: **UNREVIEWED** · status: `UNREVIEWED`

#### Pass A — customer view

**Question:** What is the default project-version distribution in Black Duck SCA 2026.4?

**Requested product/version:** `blackduck-sca` / `2026.4`

**Answer ID:** `ans-804998bd8c6f422e95bfb0887f9131b1`

**Production answer:**

~~~~text
The default project-version distribution in Black Duck SCA 2026.4 is **External** (`EXTERNAL`).

Source: [Creating a new version of a project](<C:\TestCode\Product Docs\BlackDuck SCA\docs\help-center\understanding-projects-in-black-duck\about-project-versions\creating-a-new-version-of-a-project.md:55>)
~~~~

**Pass A notes to record:** correctness, missing information, unnecessary scope, customer risk, and preferred correction.

<details>
<summary><strong>Pass B — expected behavior, evidence, and machine details</strong></summary>

**Expected behavior:** `abstain`

**Required facts:**

- None

**Forbidden facts:**

- `External` (EXACT_FACT, case-insensitive)

**Authoritative evidence:**

- [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — section `Version | **2026.7**` — corpus `bd-docs-9485d952-20260823`

**Citations emitted by the answer:**

- [BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md](<../../BlackDuck SCA/docs/help-center/understanding-projects-in-black-duck/about-project-versions/creating-a-new-version-of-a-project.md>)

**Top retrieved files:**

- rank 1: [BlackDuck SCA/AGENTS.md](<../../BlackDuck SCA/AGENTS.md>) — version `2026.7`
- rank 2: [BlackDuck SCA/index.md](<../../BlackDuck SCA/index.md>) — version `2026.7`
- rank 3: [BlackDuck SCA/docs/detect/release-notes/release-notes-for-older-detect-versions.md](<../../BlackDuck SCA/docs/detect/release-notes/release-notes-for-older-detect-versions.md>) — version `2026.7`
- rank 4: [BlackDuck SCA/docs/detect/detect-properties/detect-configuration-property-details/project.md](<../../BlackDuck SCA/docs/detect/detect-properties/detect-configuration-property-details/project.md>) — version `2026.7`
- rank 5: [BlackDuck SCA/docs/help-center/finding-data-in-black-duck/searching-for-projects.md](<../../BlackDuck SCA/docs/help-center/finding-data-in-black-duck/searching-for-projects.md>) — version `2026.7`

**Machine failures:** `ABSTENTION_FAILURE, UNSUPPORTED_CLAIM, VERSION_FAILURE`

**Recall@1/3/5:** `1.0` / `1.0` / `1.0`

**Version accuracy:** `False`

**Machine fact results:**

- `FAIL` forbidden: `External` (EXACT_FACT, case-insensitive)

**Human adjudication record:** edit the matching line in `sca-baseline-adjudications.jsonl`.

</details>

---
