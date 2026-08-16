---
title: "quack-patch"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/quack-patch.html"
content_id: "T9mAvvzMixwImplZOU9DIA"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:27.379894+00:00"
---

# quack-patch

## LLM API URL

```
--detect.llm.api.endpoint
```

Specifies the base URL of the LLM Gateway that the Quack Patch tool will send requests to.

| Details |  |
| --- | --- |
| Added | 11.2.0 |
| Type | String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## LLM Gateway API key

```
--detect.llm.api.key
```

Provides the API key used to authenticate with the configured LLM Gateway.

| Details |  |
| --- | --- |
| Added | 11.2.0 |
| Type | String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## LLM Model Name

```
--detect.llm.name
```

Defines which LLM model Quack Patch should use when performing analysis.

Quack Patch has been verified with the following model names: Claude Sonnet 4, GPT-4 and Gemini 2.5 Pro. You may use other OpenAI API standard compatible models supported by your LLM Gateway.

| Details |  |
| --- | --- |
| Added | 11.2.0 |
| Type | String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Quack Patch Enabled

```
--detect.quack.patch.enabled=false
```

If set to true, Detect will invoke Quack Patch -- a tool that uses LLMs to generate code patches for vulnerable transitive components.

Only supported for Rapid and Stateless Scan modes. detect.llm.api.key, detect.llm.api.endpoint, and detect.llm.name must also be set. See [Quack Patch](https://documentation%2Eblackduck%2Ecom/bundle/detect/page/runningdetect/quack%2Dpatch%2Ehtml) for further details.

| Details |  |
| --- | --- |
| Added | 11.2.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Quack Patch Output Directory (Deprecated)

```
--detect.quack.patch.output
```

Specifies the output directory for Quack Patch results.

If not set, the Quack Patch results are placed in a 'quack-patch' subdirectory under scan output directory.

**DEPRECATED: This property is deprecated and will be renamed to 'detect.quack.patch.output.path' in Detect release 12.0. This property will be removed in 12.0.0.**

| Details |  |
| --- | --- |
| Added | 11.4.0 |
| Type | String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
