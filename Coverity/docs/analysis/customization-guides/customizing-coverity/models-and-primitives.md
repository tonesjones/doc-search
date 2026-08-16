---
title: "Models and primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/models-and-primitives.html"
content_id: "zbkABO7ZwW8v9d4435KZGw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:25.252562+00:00"
---

# Models and primitives

When you run `cov-analyze`, Coverity derives a *model* of
each function and stores it in the intermediate directory. Models are used for
interprocedural analysis.

You can write a custom model by hand, to override a derived model and improve how the
model describes the behavior of its function. Adding custom models to the
 system has two benefits: finding more bugs, and
eliminating false positives.

Models and primitives apply to analysis of statically typed, compiled languages. They do
not apply to interpreted languages.

A custom model is written in the target language. It can call *modeling primitives,*
which are function stubs that tell Coverity Analysis how to analyze (or
refrain from analyzing) the behavior of the function you are modeling.

Although the custom model is written in the target language, it exists outside of the
project code and it does not execute. Instead, you prepare your models by using the
command `cov-make-library` with the option
`--output-file <modelfile>`. This results in a library file named
<modelfile>. Then when you invoke
`cov-analyze`, specify `--model-file
<modelfile>` so the analysis will use your custom models.

Attention:
Later versions of Coverity will not be able to run models you have created with
previous versions. For this reason, you *must* preserve the source files for the
models you write yourself, and you must store the files in your source repository. When
you upgrade Coverity, you will need to run the command
`cov-make-library` and regenerate the model files using the
sources you have saved.
