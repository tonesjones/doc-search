---
title: "The logic of for-accumulate"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-logic-of-for-accumulate.html"
content_id: "acNTlpNUwH3UeQVE287XCA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:27:32.504144+00:00"
---

# The logic of for-accumulate

This section shows the very basic logic of a `for-accumulate-expression`.

The following pseudocode expresses this logic procedurally:

```
<type> accumulator = initial-expression

foreach ( identifier in set-expression ) {
    if ( condition-expression is true ) {
        accumulator = yielding-expression
     }
}
```

Thus, the CodeXM expression that follows:

[image: CXM code follows]

```
    for x in [1, 2, 3, 4, 5]
        accumulate sum = 0 : sum + x
```

... might be expressed by the following pseudocode:

```
int sum = 0
            
foreach x in [1,2,3,4,5] {
    // There is no 'where' clause, so all members are evaluated.
    sum = sum + x
}
```

In a similar way, but using more complex expressions, the CodeXM code that follows finds the largest odd value
(`9`, in this case) among a list of positive integers:

[image: CXM code follows]

```
    for i in [ 1, 4, 8, 3, 7, 2, 9, 5 ]
        accumulate max = 0
            where odd( i ): i > max ? i
                          : max
```

... and this might be expressed procedurally by the following pseudocode:

```
int max = 0

foreach ( i  in [ 1, 4, 8, 3, 7, 2, 9, 5 ] ) {
    if ( odd( i ) ) {
        if ( i > max )
            then {
                max = i
        } else {
                // max doesn't change
        }
    }
}
```
