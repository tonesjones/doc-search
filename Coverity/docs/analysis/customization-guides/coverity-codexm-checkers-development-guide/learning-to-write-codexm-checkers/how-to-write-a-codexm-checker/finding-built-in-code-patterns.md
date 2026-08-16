---
title: "Finding built-in code patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/finding-built-in-code-patterns.html"
content_id: "et9mrcm72waa_sOASH5O6g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:49.900840+00:00"
---

# Finding built-in code patterns

Sometimes it might not be clear what pattern you should use to match a particular bit of your code.
To help you find the pattern (or patterns) that would match a specific part of your code, use `cov-manage-emit` to dump the specific part of your code.
(In particular, a function in which you notice the thing you're looking for.)

To do this, it helps to generate an intermediate directory that contains the desired code function.
You might want to try this on a small test case first, where a small source file contains the function
(or a relevant part of it, anyway) for which you're trying to find a pattern. Given that, invoke `cov-build` as follows:

[image: Command line follows]

```
$ cov-build --dir mycxm -- gcc -c -o test.o test.c
```

This captures the source of test.c into the mycxm/ directory.

Now, we need to see the CodeXM patterns in our test file. We do this by running `cov-manage-emit`. The general form is:

[image: Command line follows]

```
$ cov-manage-emit --dir mycxm find function-regex --print-codexm
```

So for our example, let's say you've created a little function called `example()`
(that you put into test.c, above) containing the code of interest. Use the following command syntax:

[image: Command line follows]

```
$ cov-manage-emit --dir mycxm find ".*example.*" --print-codexm
```

After running `cov-manage-emit`, the output for any function, class, enum, or global variable is presented in the following form:

[image: Command output follows]

```
{
    pattern : "functionDefinitionCode",
    record : {
        body : {
            record : {
                containedStatements : [
                    {
                        pattern : "simpleStatement",
                        record : {
                            expression : {
                            pattern : "assignmentOperator",
        ...
        functionSymbol : {
            record : {
                "identifier?" : "example",
        ...
```

By reading this JSON code, you can identify all the patterns present in your function, including the part that you're interested in matching.

Note:
As you can see in the sample output, the JSON pattern descriptions also use the *<typeName>***?** convention to show nullable types.
