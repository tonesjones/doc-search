---
title: "ADD_EVENT"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/add_event.html"
content_id: "0uAF6H8AypQX_QM5uZz~rw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:38:38.208607+00:00"
---

# ADD_EVENT

In Manipulating the store, we oversimplified things a bit. The
store actually maps an expression to a value and a set of events:

```
expression -> integer, set of events
```

An event is created by calling ADD_EVENT(t, tag, text):

- `tree t` — The associated expression tree. Among other things,
  this is used to obtain the line number to display the event.
- `string tag` — Something that identifies the general kind of
  event, for example `var_assign`. It provides a name for
  hyperlinks pointing at the event. Also, source code annotations can be used
  to suppress errors with a given event tag. Finally, the event tag affects
  CID merging; reports with different sets of event tags are never merged.
- `string text` — A string that explains the event, for example
  `"a is assigned to the value of b"`.

The set of events associated with an expression are (conventionally) a history of what
has happened to give the expression the abstract value it currently has. A good rule of
thumb is that any time you set or change an abstract value, you should add an event
explaining why.

The store operations explained in Manipulating the store
operate on events as well as values, transparently. For example,
CLEAR_STATE removes all events, and COPY_STATE
copies events.

It is not possible to associate an event with an expression (with ADD_EVENT) without
first giving that expression an abstract value (with SET_STATE). In some cases, you
might need to invent a new abstract value (for example, `unknown`) so
that you can assign a value in order to attach an event.

Also note that simply adding an event to an expression will not cause it to be output.
Rather, calling COMMIT_ERROR(t, ....) or
COMMIT_INPUTFILE_ERROR(t, ....)  will output the event that you
add this way.
