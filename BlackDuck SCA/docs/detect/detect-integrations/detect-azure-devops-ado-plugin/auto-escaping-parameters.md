---
title: "Auto-escaping Parameters"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/auto-escaping-parameters.html"
content_id: "Ncznf5~m_PeHMrH6Rc~2rQ"
version: "11.5.1"
section: "Detect Integrations"
scraped_at: "2026-08-08T23:46:09.126655+00:00"
---

# Auto-escaping Parameters

In Azure integrations for Black Duck® Detect, several special parameters are automatically escaped.
The workflows pertaining to quotation marks and spaces are as follows.

- Detect properties must be separated by spaces or carriage returns/line feeds.
- Values containing spaces must be surrounded by either single or double quotation marks ('single' or "double") for Linux and Mac agents while for Windows you must use single quotes ('single').
- Values containing single quotes must be surrounded with double quotation marks.
- Values containing double quotes must be surrounded with single quotation marks.
