---
title: "Creating custom patterns"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-custom-patterns.html"
content_id: "Dqurfw~7zkYk~5ybxfeRMw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:41.151845+00:00"
---

# Creating custom patterns

You have now used patterns from the C/C++ library, such as `functionCall` and `gotoStatement`.
In CodeXM, you can also define your own patterns.

A custom pattern can be useful if you find yourself matching the same thing many times,
or if you just want to assign a descriptive name to what you are trying to match: It is important to write readable code.

Let's assume that you want to find any use of the comma operator in your source code.

**Use case:**
:   Find uses of the C/C++ comma operator.

    The comma operator is problematic because it is error-prone. The expression to the left of the comma is evaluated, but this result is not saved
    (presumably, the evaluation generates some side effect). Not only is this confusing, it is easy to overlook when reviewing code.

Since the comma operator is a binary operator, we can find it by using the C/C++ library pattern `binaryOperator`.

This fragment shows the structure for using `binaryOperator`:

[image: CXM code follows]

```
    for code in globalset allFunctionCode
        where code matches binaryOperator // ...
```

But there are many kinds of binary operators. We need to be more specific. The `binaryOperator` pattern has a property,
`.operator`, that tells us which kind of operator it has matched. So the following code fragment shows how to detect instances of using the comma operator:

[image: CXM code follows]

```
    for code in globalset allFunctionCode
        where code matches binaryOperator {
            .operator == `,`
    }
```

Note:
The various C-language binary operators are represented by literal values—they are members of an `enum`—so in CodeXM code
you need to surround them with backticks.
For example, the addition operator is indicated by using `` `+` `` and the multiplication operator is indicated by using `` `*` ``.

Now, let's suppose we are writing a complex checker that requires finding the C-language comma operator several times.
In order to prevent repeating the previous code over and over again, we can declare a reusable custom pattern.
We can call the new pattern, `theCommaOperator`.

Here is a piece of code that does just that:

[image: CXM code follows]

```
pattern theCommaOperator {
    binaryOperator { .operator == `,` }
};
```

(Always end a pattern declaration with a semicolon, as you do for any other kind of declaration.)

That's it! This new pattern finds any use of the comma operator.

Remember:
Not all commas are instances of the comma operator: a comma can also be a separator in a list, a separator between parameters in a function declaration
or a call to that function, and so forth.
The comma operator is defined as evaluating its left-hand operand, throwing it away, then evaluating its right-hand operand,
whose result then becomes the result of the whole expression.

Tip:
To use a custom pattern as often as you'd like, put the pattern declaration above the `checker` keyword.
That is, make it global to the individual checkers in your code.

Now that you have defined `theCommaOperator`, you can use it anywhere a library pattern would be valid;
for example, as an argument to the `matches` operator
or to the `%` operator.
The following code fragments show this usage:

[image: CXM code follows]

```
    for code in globalset allFunctionCode
        where code matches theCommaOperator as comma
    
    // ... alternatively ...
    
    for comma in globalset allFunctionCode % theCommaOperator
```
