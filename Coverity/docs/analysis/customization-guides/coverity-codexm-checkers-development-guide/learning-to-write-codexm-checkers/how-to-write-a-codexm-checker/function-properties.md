---
title: "Function properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/function-properties.html"
content_id: "4gPN5j3UELRSeAlbjs2fDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:50.729137+00:00"
---

# Function properties

A *function property* is, in effect, a sub-checker that provides information about a called function.

You can think of a function property as a pattern on steroids, since it allows the main checker to match characteristics found in other functions
that the current function calls. Examples might include, *Does the function being called contain side effects?*
Or, *Does this function, or any function it calls, call `system()`?*

Function properties permit a lightweight form of interprocedural analysis.

Function properties are defined using the key-phrase `function property`,
followed by an identifier, followed by a record definition that has a single property named `models`, which should be a `pattern`.
The general form appears like this:

[image: CXM code follows]

```
    function property /* name */ {
        models = /* The pattern to look for in called functions */;
    }
```

The pattern you provide to the `models` property should have the following form:

[image: CXM code follows]

```
pattern(astnode) -> record { events : list<eventRecord> }
```

That is to say, the pattern should expect to match an `astnode` (a statement, an expression, and so on)
and return a record object with the member field `events` containing a list of `eventRecord` items (much like an ordinary checker does).
This pattern should match nodes of interest within the called function, and produce one or more events descriptive of what was matched.

The following example shows a function property that determines whether a given called function calls `system()`.

**Use case:**
:   Find function calls that contain calls to `system()`.

    This is similar to our earlier example that found calls to `system()` itself.

[image: CXM code follows]

```
function property callsSystem {
    models
        = pattern {
            /* The basic part of the pattern:
               Does this function call system() directly? */
            | functionCall { .calledFunction.identifier == "system" } as call ->
                {
                    events = [
                        {
                            description = "system".formattedAsCode
                                          + " is called directly here.";
                            location    = call.location;
                        }
                    ];
                }
            /* An optional part of the pattern:
               only necessary if the property is transitive
               (that is, if it also applies to functions within
               the function called). */
            | callsSystem as transitiveCall ->
                {
                    events = [
                        {
                            description = "system".formattedAsCode
                                          + " is called by this function"
                                          + " (or one it calls)."; 
                            location    = transitiveCall.location;   
                        }
                    ];
                }
        }
};
```

Here we see that the pattern in the function property contains two cases. The first (top) case identifies an event of interest directly:
a call of a function named `system()`.
The second (bottom) case applies the function property recursively on call sites within the called function.
(If that transitive behavior is not desired, that alternative of the pattern can be omitted.)

The function property behaves like a pattern you match against `functionCall` results.
If the property matches, the called function in question exhibits that characteristic; if the property does not match, neither does the function.

To use our new function property we could write the following, treating the function property as an expression:

[image: CXM code follows]

```
    for funCall in globalset allFunctionCode % functionCall
        where funCall matches callsSystem :
            /* Do something, such as report an issue. */
```

To be more complete, here the pattern is used to implement a complete checker. In this case, the function property is treated as a pattern:

[image: CXM code follows]

```
checker {
    name  = "CALLS_SYSTEM" ;
    reports =
        for c in globalset allFunctionCode % callsSystem :
            {
                events = [
                    {
                        description = "This function calls "
                                      + "system".formattedAsCode
                                      + ".";
                        location    = c.location;
                    }
                ];
            };
};
```

In this second example we use the function property like a pattern, making it the right-hand operand of the `%` (which-are) operator,
instead of filtering against `functionCall` and then matching against the function property. Both methods work.

If you play with using this code, you'll see that this brief checker finds all instances where a function calls `system()`, including indirectly so.
This is a more general test than the earlier checker that searched for `system()` calls, but it might generate more issues than you expect.

If `FunctionA` calls `FunctionB`, which in turn calls `FunctionC`, which finally calls `system()`,
you will get exactly what the checker was told to do: an issue report for each of `FunctionA`, `FunctionB`, and `FunctionC`,
because each of them ultimately causes a call to `system()`.

This might not be the result you want. More often you will probably want to combine the function property with another condition, specific to the current function,
so only when both conditions are met do you actually generate an issue event.
