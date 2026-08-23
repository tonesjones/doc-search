# Current documentation-answering architecture

Baseline: `bd-docs-9485d952-20260823` (`9485d952e1a15f65fafecd6eb2c92b1ec435357b`)

## Actual path

```text
Official Black Duck Fluid Topics TOC/content APIs
        ↓
Per-product scrape scripts
        ↓
One Markdown file per TOC topic + YAML metadata
        ↓
Per-product JSON manifest + generated Markdown indexes
        ↓
Question routed by the external `bd` skill
        ↓
Catalog search, then recursive text search (`rg`) when needed
        ↓
Selected Markdown passages read by the assistant
        ↓
Assistant-generated answer + local Markdown citations
```

## Components found

| Concern | Current implementation |
|---|---|
| Product organization | Separate roots for Black Duck SCA/Detect/Alert/Bridge/C/CPP, Coverity, Polaris, Sigma, and Signal. |
| Ingestion | Each product root has `scripts/build-index.py`, `scripts/scrape-pending.py`, and a product registry. Official Fluid Topics TOC/content APIs are used. |
| Documents | Markdown, normally one official TOC topic per file, with YAML front matter. |
| Version metadata | Product registries and manifests pin explicit versions or deliberately use `latest`; topic front matter is not completely uniform across corpora. |
| Chunking | File/topic granularity plus ad hoc passage selection by the assistant. No programmatic chunker is checked in. |
| Embeddings/vector store | None checked in. |
| Retrieval | The external `bd` skill routes by product, searches `index*.md`, then uses recursive text search and opens selected files. There is no checked-in callable retrieval API or stable scoring/ranking function. |
| Ranking/scoring | Search-tool output and assistant judgment; no numeric retrieval score. |
| Context construction | The assistant opens selected topic files/passages. No checked-in context assembler or token policy. |
| Prompt/generation | Governed outside this repository by the installed `bd` skill and Codex host. The baseline adapter invokes that same installed path through Codex CLI 0.147.0; no alternative prompt or retriever was introduced. |
| Citations | The guidance requires local Markdown-path citations. Phase 1 now captures and deterministically checks cited paths against consulted files. |
| Skill structure | The installed `bd` skill lives outside this repository. Product-specific `AGENTS.md` files provide corpus rules. No repository `SKILL.md` exists. |
| Tests | Corpus validators and retrieval smoke scripts exist for several product roots. Smoke scripts assert file/needle presence, not end-to-end answer quality. |
| Logging/tracing | No answer-level tracing existed at baseline. The added wrapper records answer IDs, ranked consulted files, citations, revisions, model settings, and latency without changing answer prompts. |
| Configuration | Product registries contain map IDs, versions, paths, and source URLs. |
| CI/feedback | No checked-in CI or answer-feedback workflow existed at baseline. |
| Runtime testing | Phase 2 adds a common validator contract and one API-first Black Duck SCA adapter. It is exact-host allowlisted and isolates mutations to the ownership-marked `Tony RAG` project. |

## Evaluation and runtime boundaries

The evaluator calls the actual installed `bd` answer path through `codex exec`. It sends only `question`, `product`, and `product_version`; expected facts, expected behavior, eval IDs, and evidence stay inside the evaluator. Tool events are wrapped into reconstructable traces after generation. Fixture traces are used only for deterministic infrastructure tests.

Runtime evidence remains separate from documentation/RAG evidence. The SCA adapter authenticates with the gitignored project-local token, checks the observed environment, and returns `PASS`, `FAIL`, or `INCONCLUSIVE`. The combined report retains retrieval, answer, corpus, and runtime signals as separate fields.
