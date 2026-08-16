---
title: "bool COMMIT_ERROR(tree t, char const *tag, desc)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/bool-commit_error-tree-t-char-const-tag-desc-.html"
content_id: "vxm~SChWQF5xvo6tdoscAw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:41.007362+00:00"
---

# bool COMMIT_ERROR(tree t, char const *tag, desc)

If there is no mapping for `t`, or `t` has no events, returns
`false`.

If `tag` is neither NULL nor the empty string (`""`), outputs the
event sequence associated with `t`, *plus* one more event,
constructed from `tag` and `event` as described in `ADD_EVENT`.

Note: Due to these rules, you *must* create a mapping for a tree before you can add or output
events. Further, you need to add at least one event (by using
`ADD_EVENT`) before calling `COMMIT_ERROR`. In some
circumstances, you need to invent a dummy value and/or event for this purpose.
