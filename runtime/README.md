# Black Duck SCA runtime validation

The Phase 2 POC is API-first and restricted to `https://sca.field-test.blackduck.com`. Credentials and mutation opt-in live only in gitignored `.env.runtime`.

## Claims

| Validation | Eval case | Classification | State change |
|---|---|---|---|
| `sca-runtime-auth` | `sca-auth-002` | API_VALIDATABLE | None |
| `sca-runtime-project-list` | `sca-auth-003` | API_VALIDATABLE | None |
| `sca-runtime-project-media` | `sca-auth-002` | API_VALIDATABLE | None |
| `sca-runtime-isolation-name` | `sca-project-003` | API_VALIDATABLE | None |
| `sca-runtime-current-user` | `sca-role-001` | API_VALIDATABLE | None |

The project/version provisioner is setup infrastructure, not an assertion that the 2026.7 documentation matches SCA 2026.4.0.

## Safety

- exact HTTPS host allowlist;
- mutations require both project-local opt-in and `--allow-mutations`;
- exact project name `Tony RAG` only;
- version prefix `RAG-VAL-` only;
- a shared-instance safety limit of 10 Active versions in `Tony RAG`; provisioning stops before exceeding it;
- an ownership marker is required before reuse;
- exact-name/count checks prevent duplicate project creation;
- no delete, archive, LTS, account-lockout, policy, role, scan, or customer-data operations;
- authorization and token values are never emitted;
- API failures and version mismatch are `INCONCLUSIVE`, not factual `FAIL` results.

If the Active-version limit is reached, a human must explicitly select an obsolete test version for deletion or decide that an appropriate released version should be converted to LTS. LTS conversion is one-way and omits scan and project details, so the provisioner never performs either cleanup action automatically.

The five versions are retained because the user requested a persistent isolated test project. `cleanup_result: PASS` means the requested retained state was verified, not deleted.
