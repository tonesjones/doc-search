# Documentation router

Load this file before answering a product question from this repository.

## Route a question

1. Match the question to a product id or alias in `products.json`.
2. Load the selected product's `SKILL.md` when that file exists.
3. Search the selected product's local Markdown before using an external source.
4. Load more than one product only when the question names a cross-product workflow.
5. Ask for the product when the question is ambiguous. Do not guess.

The root router owns product selection, source priority, and handoff. A product skill owns its vocabulary, version rules, retrieval cases, UI details, API details, and verifier. The root router must not add product-specific conditionals.

Use the local corpus first. Use the official documentation API only when the local corpus is missing, stale, or the user asks for a refresh. Label claims that come from general knowledge.

Bridge is a logical product in the root registry. Its files currently live under `BlackDuck SCA` and move to `Bridge` in DS-02. Treat Bridge behavior as cross-product integration behavior even during that transition.

## Product ids

The registry defines these logical products:

- `black-duck-sca`
- `bridge`
- `coverity`
- `polaris`
- `sigma`
- `signal`
- `srm`

Use aliases only to resolve a request to one of these ids. Keep the resolved id in the answer so the source boundary is visible.
