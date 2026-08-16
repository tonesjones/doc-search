---
title: "Configuring LLM API keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-llm-api-keys.html"
content_id: "ByR~sY7RiNmr2DwXXP_7Lg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:32.639469+00:00"
---

# Configuring LLM API keys

Use the Coverity Cloud REST API to register LLM API keys at the project or global
scope for AI-assisted triage. Keys are ECIES-encrypted and stored immediately and are never
logged or echoed in the response.

You can configure LLM API keys at two scopes:

- **Project-level**: Assigns a dedicated key to one or more individual
  projects.
- **Global**: Sets a single key that applies to all projects that do not have a
  project-level key. Global keys always take precedence over the project-level
  key.

When a triage request is triggered, Coverity Cloud resolves which key to use based on
the `useGlobalKey` flag:

- When `useGlobalKey` is `true`, Coverity Cloud
  sends the global key without a `project_id`.
- When `useGlobalKey` is `false`, Coverity Cloud
  looks up the project-specific key and sends it with the
  `project_id`. If no project key exists, the request
  fails.

To check whether the `useGlobalKey` flag is set, query the
`system_preference` table in the database.

In both cases, the key is ECIES-encrypted with the triage service's public key before
being sent via `POST /auth`. The triage service decrypts and uses the
key, then deletes it after processing.

For information about the `triage-suggestion-service.llmKeyEncryption`
Helm values, see Generating a key pair.

1. **Optional:** 
   Configure a project-level LLM key using `PUT
   /config/projects/llmKey`.

   Requires Manage Project permission (minimum).

   1. Build a JSON array where each element contains a
      `projectName` and an `llmKey`:

      ```
      [
        {"projectName": "my-project", "llmKey": "sk-abc123..."},
        {"projectName": "my-project-2", "llmKey": "sk-def456..."}
      ]
      ```
   2. Send the request:

      ```
      PUT /config/projects/llmKey
      Content-Type: application/json
      ```
   3. Confirm you receive a `200 OK`.

      A `400 Bad Request` indicates a malformed payload.

   To update an existing project key, send the same `projectName`
   with a new `llmKey` value. It overwrites the previous
   key.

   To remove a project key, send the `projectName` with an empty
   string for `llmKey`:

   ```
   [{"projectName": "my-project", "llmKey": ""}]
   ```
2. **Optional:** 
   Configure the global LLM key using `PUT
   /config/system/ai/globalLlmKey`.

   Requires System Admin permission.

   1. Build a JSON object with a `globalKey` string and a
      `useGlobalKey` boolean:

      ```
      {
        "globalKey": "sk-xyz789...",
        "useGlobalKey": true
      }
      ```
   2. Send the request:

      ```
      PUT /config/system/ai/globalLlmKey
      Content-Type: application/json
      ```
   3. Confirm you receive a `200 OK`.

   To update the global key, send a new `globalKey` value.

   To disable the global key and require per-project keys instead, set
   `useGlobalKey` to `false`:

   ```
   {
     "globalKey": "sk-xyz789...",
     "useGlobalKey": false
   }
   ```
