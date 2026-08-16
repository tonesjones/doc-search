---
title: "Writing your first CodeXM checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/writing-your-first-codexm-checker.html"
content_id: "VRdoH2RO8r~zCJeTCXZb1g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:35.303675+00:00"
---

# Writing your first CodeXM checker

Let's jump right in.
Specifically, let's look at creating a checker that detects `goto` statements.

**Use case:**
:   Remove `goto` statements from the target code base.

    `goto` statements lead to spaghetti code: hard to read, hard to debug.

## Name the checker

The first thing to do is to give your checker an appropriate name.

At its simplest, a CodeXM checker has the parts shown in the code sample that follows.
Open a text editor or development environment of your choice (not a word processor, though),
and then type the following code, or copy it and paste it:

  
 [image: CXM code follows]   

```
checker {
    name = "NO_GOTO";
    reports = for x in y: {     // ... logic to describe what you're looking for ...
        events = [
            {
                // ... messages to describe what you found ...
            }
        ];
    };
};
```

Note:
In these first samples, we use the CodeXM `/* comment */` notation to represent parts of the checker you will
later replace with more detailed code.
(CodeXM comments have two forms.
You can use the `/* slash-asterisk-multi-line comments */` form.
You can also use the single-line form: `// slash-slash single-line comment`.)

Remember:
In most cases, CodeXM disregards white space such as indentation or line breaks.
The "Style Guide" section at the end of this guide describes a consistent style for CodeXM source
that we find useful and readable. The code samples in this guide follow that style.
For guidelines to white space, in particular, see the entries Braces and
Spacing and line length.

We have begin to define a checker named `NO_GOTO`, as declared in the checker's `name` field.
Next, we put the checker implementation itself (such as code patterns you're looking for and how to report defects)
into the `reports` statement.

## Add specifics

The next thing to do is to specify where to look and what to look for.

Since we want the checker to look for `goto` statements in each function of C/C++ source code,
the logic to find what we're looking for would look like this:

[image: CXM code follows]

```
include `C/C++`;

checker {
    name = "NO_GOTO";
    reports =
        for c in globalset allFunctionCode where c matches gotoStatement : {
            events = [
                {
                    // ... Messages to describe what you found
                }
            ];
        };
};
```

Here we have added a simple expression that looks at all the code in our project (that's what the `for` loop does),
and uses the `gotoStatement` pattern to match all instances of `goto` in the source code under examination.

The `include` statement above the checker includes the CodeXM C/C++ Standard Library;
this provides the patterns needed for CodeXM to understand C or C++, and ensures that only C or C++ source code is analyzed by this checker.
(And yes, those are back-ticks being used to surround the language name.)

## Report events

Now that we've defined the pattern that we're looking for, we want to report findings as *events,* or *issues.*

For a simple one-event defect like this `goto` statement,
we just need to provide the `description` (what the event is supposed to say)
and the `location` (where the event should be placed relative to your source code.)

What follows is a completed checker for finding a `goto` statement:

[image: CXM code follows]

```
include `C/C++`;

checker {
    name = "NO_GOTO";
    reports =
        for c in globalset allFunctionCode where c matches gotoStatement : {
            events = [
                {
                    description = "Use of goto is not allowed";
                    location = c.location;
                }
            ];
        };
};
```

Note:
In this checker, our loop variable `c` matches a `gotoStatement` pattern that is specified
in the C/C++ standard library.
This library provides patterns that are appropriate for C/C++ source code, and that limits this checker to analyzing C/C++ source code only.
The full set of available patterns can be found in the
CodeXM C/C++ library reference.

When it runs, our checker displays the message `Use of goto is not allowed` wherever it encounters a `goto`
in the source code being scanned.
The following section shows how to run a scan.
