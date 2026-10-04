---
title: "bool ADD_EVENT(tree t, char const *tag, desc)"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/bool-add_event-tree-t-char-const-tag-desc-.html"
content_id: "Xe4a88cUNv5AEwMm5B_zYg"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:58.251681+00:00"
---

# bool ADD_EVENT(tree t, char const *tag, desc)

If there is no mapping for `t`, returns `false`.

Otherwise, appends a new event to the event sequence to which `t` is mapped, and
returns `true`.

The new event is constructed using `tag` and `desc`. The
latter is evaluated as the right-hand argument to operator
`<<(ostream&)` so you can construct complicated event
strings, for example:

```
 ADD_EVENT(t, "my_tag", "One plus " << 1 << " is " << (1+1));
```

See Adding events for more information
on tags.
