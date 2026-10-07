---
title: "Enum, list, record, and set literals"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/enum-list-record-and-set-literals.html"
content_id: "lV1ro_WPaDddZzKXC7zn6g"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:34:09.671375+00:00"
---

# Enum, list, record, and set literals

Don't put a trailing comma after the last element.
If the sequence requires more than one line, use a separate line for each element, and indent those lines.

## Examples of enums

[image: CXM code follows]

```
typedef stateKind = enum { `INIT`, `ELSE`, `LB` };
```

[image: CXM code follows]

```
typedef statedef = enum {
    `warm`,
    `tepid`,
    `cold`
};
```

## Examples of lists

[image: CXM code follows]

```
typedef numberList = list [ 1, 2, 3 ];
```

[image: CXM code follows]

```
typedef longList = list [
    { field1 = /* ... */; field2 = /* ... */ },
    { field1 = /* ... */; field2 = /* ... */ },
    { field1 = /* ... */; field2 = /* ... */ }
];
```

## Examples of records

[image: CXM code follows]

```
let thisRecord = { field1 = 1; field2 = 2; /* ... */ fieldN = n };
```

[image: CXM code follows]

```
let thisRecord = {
    field1 = 1;
    field2 = 2;
    /* ... */;
    fieldN = n
};
```

## Exampels of sets

[image: CXM code follows]

```
typedef fib = set [ 1, 1, 2, 3, 5 ];
```

[image: CXM code follows]

```
typedef longSet = set [
    { field1 = /* ... */; field2 = /* ... */ },
    { field1 = /* ... */; field2 = /* ... */ },
    { field1 = /* ... */; field2 = /* ... */ }
];
```
