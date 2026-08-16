---
title: "Custom API models"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/custom-api-models.html"
content_id: "LCYZ2KKnzKozGp9mH8Z9bw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:11.360870+00:00"
---

# Custom API models

You can write your own model of a function, in order to override the model generated
by Coverity and to better describe the function's behavior. Custom models can be
useful both for finding more bugs, and for eliminating false positives.

When Coverity scans the code for a statically typed, compiled language—such as C, C++,
C#, Go, Java, or Visual Basic—for each function in the source, it generates a model. The
model is an abstraction of the function's behavior at execution time, and the
models that Coverity generates are used for interprocedural analysis.

A custom model is written in the target language. It can call modeling primitives, which
are function stubs that tell Coverity Analysis how to analyze (or
refrain from analyzing) the behavior of the function you are modeling.

Although the model is written in the target language, it exists outside of the project
code and it does not execute. Instead, you prepare your models by using the command
`cov-make-library` with the option `--output-file
<modelfile>`. This results in an XML file named
<modelfile>. Then, when you invoke
`cov-analyze`, specify `--model-file
<modelfile>` so the analysis will use your custom models.

**Use case:** For the SQLI checker, write a custom model to trap SQL strings that have
been constructed from untrusted sources.

For example, the custom database API method `MyDb.execute(String sql)`
should never be passed SQL strings that are constructed from untrusted substrings,
because this can enable SQL injection attacks. The following custom model reports such
an error to the SQLI checker, at the point where `sql_sink()` is
called:

```
import static com.coverity.primitives.SecurityPrimitives.*;
            
            
public final class MyDb
{
    public void execute(String x)
    {
        sql_sink(x);                // Report SQLI if 'x' is untrusted
    }
}
```

**Limitations and alternatives:** The opportunity to write a custom model depends on
the particular checker involved and which language the source code is written in. So
using custom models involves more research and planning than simply enabling or
disabling checker options does.

- API modeling is available only for statically typed languages such as C++, Java, C#,
  and so on. In a statically typed language, the fully qualified signature of a method
  is sufficient to precisely identify which method is being modeled in the universe of
  code.
- For dynamically typed languages, the method definition lacks type names (often it
  lacks argument information entirely) and is therefore less precise. To model a
  dynamically typed function, Coverity relies instead on security analysis directives
  to define a naming system that can trace the origin of an object on which a call is
  made.
- Each API model describes a single method (and its overriders). To describe a
  collection or pattern of methods; for example, by using regular expression matching
  or the presence of an in-code annotation, you need to use security directives.

For more about using directives, see the Coverity 2026.6.0 Security Directives Reference.

**Learn more:** In the chapter "Coverity Analysis checkers" of the Coverity 2026.6.0 Checker Reference, the checker descriptions tell whether the checker
can use models. If it can, the checker description lists the modeling primitives that
are available to such models. For an overall description of using models, see Models and primitives. This chapter also includes details about the
modeling primitives, organized by language.
