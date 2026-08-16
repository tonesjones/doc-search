---
title: "poetry"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/poetry.html"
content_id: "C4PUgMcOjuXgAV4NM5Ez_g"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:43.946216+00:00"
---

# poetry

## Poetry dependency groups

```
--detect.poetry.dependency.groups.excluded
```

Set this value to indicate which Poetry dependency groups Detect should exclude from the BOM.

When specified, presence of both `poetry.lock` and `pyproject.toml` files is required for this detector to run successfully. Components and related dependencies that belong to excluded groups will not be in the BOM unless the component also belongs to a non-excluded group. For example, to recursively exclude all components under the `tool.poetry.group.dev.dependencies` and `tool.poetry.group.test.dependencies` sections of `pyproject.toml`: `detect.poetry.dependency.groups.excluded='dev,test'`. For Poetry pre-1.2.x style of specifying dev depenenicies (`tool.poetry.dev-dependencies` section), use `dev` as the group name.

| Details |  |
| --- | --- |
| Added | 9.7.0 |
| Type | String List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | Yes |
| Acceptable Values | Any |
| Strict | No |
