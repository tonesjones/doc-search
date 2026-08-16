---
title: "Path-sensitive analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/path-sensitive-analysis.html"
content_id: "1ZGh40pe5i7DsZgyZ5i_RA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:51.555704+00:00"
---

# Path-sensitive analysis

In addition to detecting individual elements of target source code (such as `goto` statements or calls to `system()`),
CodeXM provides a mechanism known as *path-sensitive analysis,* which you can use to find problems that involve a specific sequence of code elements.

As you are probably aware, the computer executes the instructions in your functions one at a time (at least conceptually; let's ignore threads and
all the pipeline optimizations modern processors do to speed up your code: in spite of all these neat tricks, it's all meant to give the illusion
that instructions are executed in discrete, ordered steps).
Any nontrivial function will likely have some control flow: perhaps a condition is tested, and two or possibly more different ways can be taken based on the outcome.
Each possible way through a given function—from the entry point to where it returns—is called a *path*.

CodeXM has the ability to evaluate the feasible paths through a function, looking for specific sequences of code along any one of them.
This is what path-sensitive analysis is all about.

Finding sequences of code along paths is not much more work than what we've already done.
We just need to introduce two syntax elements: the `sequence()` function and the `>=>` operator
(AKA the *happens before* operator).
These constructs, working together, describe sequences of code elements rather than just individual elements.

CAUTION:

If the sequence contains a function call that does not return (for example, the function throws an exceptiont), then `sequence()`
might not report a match.
For an example of CXM code that handles this situation, see The happens-before-expression.

## Random thoughts

Calling things in the wrong order is a common problem when programming.
Take, for example, forgetting to seed the pseudorandom number generator before you start to pull numbers out of it.

**Use case:**
:   Find calls to `rand()` that are not preceded by a call to `srand()`.

    Like failing to initialize a variable, failing to seed a pseudorandom number generator leads to unexpected and incorrect reults.

Here is an example of outright forgetting to call `srand()`:

[image: C++ code follows]

```
void forgotToSeed(int i) {
    int x;

    // Some logic
    x = rand();
    // Some more logic expecting x to be random
}
```

More troublesome, though—and not as easily detected by the eye—is the case where `srand()` *is* called,
but only sometimes:

[image: C++ code follows]

```
void onlySometimesSeeded(int i) {
    int r;

    // Some logic
    if(someComplicatedCondition) {
        srand(i);
    }
    // More logic
    r = rand(i);
    // Still more logic, now expecting r to be validly random (it might not be)
}
```

This second example collapses what might be a complicated bit of control flow into a single `if` statement,
but the point is that while there is a path that does call `srand()`, there is also a path where
`srand()` is not called.
The second of these paths is the one we want to find.

With the problem laid out, let's see how we attack it.
To express it in words: We are looking for a sequence where we have not called `srand()` before we call
`rand()`. Here is how we can express it in CodeXM:

[image: CXM code follows]

```
    sequence( ! callToSRand >=> callToRand )
```

These are some issues you should be aware of:

- The *happens-before* operator specifies an order between two steps.
  A sequence can contain one or more of these operators, to specify a sequence of two, three, four steps, or even more.
- Negating a step by using the NOT operator `!` means that the path *must not* have
  that step at that point in the sequence.
- While a sequence defines the order between steps, other things can appear between the steps it names explicitly:
  A sequence doesn't have to represent consecutive instructions in code.

The `sequence()` function just produces a special kind of pattern that understands paths.
In fact, we'll end up putting it into a checker that specifically walks along paths. The checker looks like this:

[image: CXM code follows]

```
checker {
    name = "UNSEEDED_RAND";
    reports =
        for f in globalset allFunctionDefinitions
            where f.paths matches sequence( ! callToSRand >=> callToRand )
                as errs : errs
};
```

So the checker itself is pretty straightforward. All we need to do now is to define what we mean by `callToSRand`
and `callToRand`. Given that CodeXM is a define-before-use language, somewhere above the preceding snippet we need to define
the two patterns that match what we are looking for. The first one is the simpler of the two and should be fairly self-evident, but it does
introduce one new concept: the *path step*. Let's examine it:

[image: CXM code follows]

```
pattern callToSRand {
    nodePathStep {
        .node == functionCall {
            .calledFunction.identifier == "srand"
        }
    } -> {
        event = null
    }
};
```

This pattern is special in that it specifically matches a path step; that is, a single, discrete bit of code that is part of a larger path object.
In order to be interesting to us, the node in question is expected to be a call to the function `srand()`.

Another curiosity is that this pattern returns an empty event list.
We can get away with this because the sequence is looking for the *absence* of a call to `srand()`
(that is, `! callToSRand`) so we have nothing meaningful to report if
`srand()` is actually called.

## Using 'event' rather than 'events'

Patterns used in path-sensitive analysis should produce records with an `event` property, instead of the usual `events`.
The CodeXM engine will generate `events` properties by gathering automatically generated path events as well as matched patterns' `event` properties.

## Completing the code

The other pattern we need finds a call to `rand()`, and report its finding.
Structurally this is similar to the previous pattern, but of course we change the name of the function we're looking for,
and in this pattern we do want to report something.
To construct the report, we need to save what was matched, in a new variable, and then construct a proper event list
that references the variable. Here is the pattern in its entirety:

[image: CXM code follows]

```
pattern callToRand {
    nodePathStep {
        .node == functionCall {
            .calledFunction.identifier == "rand"
        }
    } as randCall ->
        {
            event = {
                tag = "call_rand";
                description = "Calling "
                              + randCall.node
                              + " without previously calling "
                              + "srand()".formattedAsCode
                              + ".";
                location    = randCall.node.location
            }
        }
};
```

So what might you expect to find when you run this checker? The simple case we illustrated above is straightforward.
The following sample annotates the code with a message generated by the checker `UNSEEDED_RAND`:

[image: C++ code follows]

```
void forgotToSeed(int i) {
    int x;

    // Some logic
    x = rand();     [Issue] Event call_rand -
                    [1] Calling rand() without previously calling srand().
    // Some more logic expecting x to be random
}
```

The second example—where some paths seed the generator but others don't—is more interesting:
Not only does the checker tell you that the code forgot to call `rand()`,
it tells you which path that was taken failed to do so.

Here is the second example, with messages from Coverity Analyze added:

[image: C++ code follows]

```
void onlySometimesSeeded(int i) {
    int r;

    // Some logic
    if(someComplicstedCondition) {      [1] Event cond_false: Condition
                                        "some_complicated_condition", taking false branch.
        srand(i);
    }   [2] Event if_end: End of if statement.
    // More logic
    r = rand(i);  [Issue] Event call_rand - [3]
                  Calling rand() without previously calling srand().
    // Still more logic, now expecting r to be validly random (it might not be)
}
```

So describing sequences of steps in your code is not much more difficult than writing other kinds of checkers.
This capability opens the door to solving many problems:
For example, you can use path sensitivity to check that resources you opened are always closed,
or that you only call certain functions between two "book-end" functions.

Remember:
A sequence is limited to finding steps within a single function.
Writing an interprocedural checker that combines function properties and sequences is possible,
but we'll leave that as a proverbial exercise for the reader.
