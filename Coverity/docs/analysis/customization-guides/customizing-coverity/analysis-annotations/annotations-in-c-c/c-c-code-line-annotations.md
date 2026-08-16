---
title: "C/C++ code-line annotations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c/c-code-line-annotations.html"
content_id: "bF2OsKGFe3Tn7Fp6KoihlA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:18.040600+00:00"
---

# C/C++ code-line annotations

Even if you are overriding built-in or derived models, you still might not eliminate
all false positives. However, for analysis of C and C++ code, you can also use code-line
annotations to suppress false positives on untriaged issues.

Annotations affect defects that Coverity Connect categorizes as
Unclassified or Pending. They have no effect on defects that have already been triaged
manually. (This behavior was introduced in version 7.0.)

Note:
There are no code-line annotations for parse warnings.

Code-line annotations are placed immediately before the line of code where the defect occurs.

As an example, suppose the system detects that the local variable `x` can
be `NULL` when it is dereferenced in the following code:

```
x = NULL;
...

*x = 0;
```

When Coverity analyzes this code, it reports a `FORWARD_NULL` defect. As
reported in Coverity Connect, this defect contains an event with the tag
`var_deref_op`. The message that describes the event appears in
Coverity Connect in red and is displayed on the line immediately preceding
the event: In this example, the message appears just above line 20 in the source file
bad_deref.c. If this defect is a false positive, you can
suppress it with an annotation comment that contains the text
`coverity[var_deref_op]`. The annotation should appear immediately
before the dereference, as shown in the following code:

```
x = NULL;
...
//coverity[var_deref_op]
*x = 0;
```

Tip:
Rather than use a tag value such as `var_deref_op`, your annotation can
also use the name of the checker itself; for example,
`FORWARD_NULL`.

You can optionally append a `count` field after the main annotation; for example:

```
x = NULL;
...
//coverity[var_deref_op, count:2]
*x = 0;
```

If the specified `count` value is not the same as the number of defects on the line, Analysis logs a warning
and outputs a file called annotations-warnings.txt.
If the number of defects is greater than the value specified in the `count` field, Analysis does not apply the annotation
and no logging appears in applied-annotations.csv.

When Coverity Analysis scans the code again, the
`FORWARD_NULL` defect is automatically classified as
`Intentional`, and the defect commit step automatically reads and
annotates the bug in Coverity Connect.

An analysis annotation always appears at the beginning of a C comment
(`/*coverity[...]...` ) or a C++ comment
(`//coverity[...]...`).
Code-line annotations are placed immediately before the line of code where the defect occurs.

Note:
You can apply multiple `coverity` annotations with different event tags
to the same line of code. Coverity Analysis always checks the line that
precedes the event. If it finds an annotation on that line, it checks the line above
that one for yet another annotation, and so on, looping through annotations that it
finds on the immediately preceding lines.

For example, the annotations in the
following sample will suppress events `bug1` and `bug2` from the call to
`nobug()`:

```
//coverity[baz]

//coverity[bug2]
//coverity[bug1]
/* coverity[qux] */ nobug();
```

The example *does not* exclude `baz` because there is an empty
line between `baz` and `bug2`, and it *does not*
exclude `qux` because `qux` is on the same line as
`nobug()`.

Code-line annotations result in defect events being ignored. It is possible that multiple
defects share a single event and ignoring the event will suppress more than one defect.
Because of this, you should only use analysis annotations to suppress critical, unshared
events, or events you are sure that Coverity Analysis has incorrectly
identified. You can identify a critical event through its description. For example, the
event description `[Variable "x" tracked as NULL was dereferenced]`
indicates a critical event, while the event description `[Added "x" due to
comparison "x == 0"]` is informational and indicates a shareable event. Each
defect's documentation lists the critical events you can suppress if a defect is
a false positive.
