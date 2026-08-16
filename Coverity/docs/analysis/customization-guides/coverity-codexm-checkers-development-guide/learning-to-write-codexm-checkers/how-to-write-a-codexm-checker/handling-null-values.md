---
title: "Handling null values"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/handling-null-values.html"
content_id: "n9ygdynnnLxHzQpEKLVQtg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:43.343978+00:00"
---

# Handling null values

In the previous pattern for loops (Returning objects from patterns),
you might have noticed that the `after` property and `condition` property can be `null`,
depending on the type of loop that is matched. In fact, we say that these properties are *nullable*.

In CodeXM documentation, a nullable value is indicated by the potential type followed by a question mark;
for example, `string?`.

Accessing a `null` value is not a fatal run-time error in CodeXM, as it is in many other languages.
A nullable property is one that might not return an actual value: This does require additional CodeXM code to account for that possibility.

You can handle a nullable type in one of the following ways:

- Check that the value is not `null` by matching it against the built-in pattern `NonNull`.
  As in all pattern matching, you can use the `as` clause to extract the matched value.
  You can also match against `null` itself, then if the match is true, execute code that doesn't depend on the
  property having a value.

  Use the matching method when you want to act only on non-`null` values and ignore `null` values altogether.
- Use the *null-coalescing operator* `??` to provide a default value that stands in for a `null` property.

  Use the coalescing (default value) method when you want to act on all possible values, including `null`.

The following code sample uses the method of matching `NonNull`:

[image: CXM code follows]

```
    for loop in globalset allFunctionCode % allLoops
        where loop.after matches NonNull as aft
        && // Use aft here, knowing now that it isn't null.
```

The following code sample uses the converse method of checking that a property value *is* `null`:

[image: CXM code follows]

```
    for loop in globalset allFunctionCode % allLoops
        where loop.after == null
        && ( /* The loop.after property is now confirmed to be null,
                so don't attempt to use its value here! */ )
```

The null-coalescing operator simply specifies a default value to use when a property is `null`.
The following code fragment shows how to use it in code:

[image: CXM code follows]

```
    myNullableString ?? "default value"
```

... After this expression, the CodeXM code can now access `myNullableString` just as it accesses any non-nullable property.
If the property has a value, that is what CodeXM inspects. If the property is `null`, CodeXM uses the value
`"default value"` instead.

Note:
Some language libraries have a pattern to match all loop types. The C/C++ library and the Python library do not.
