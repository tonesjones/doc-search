---
title: "Building with Visual Studio or .NET SDK (‘dotnet’)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/building-with-visual-studio-or-.net-sdk-dotnet-.html"
content_id: "lHiny8c3sqnFTOaQ4hwHiA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:31.003193+00:00"
---

# Building with Visual Studio or .NET SDK (‘dotnet’)

Visual Studio and .NET SDK (`dotnet`) use a mechanism called a *shared
compiler* for builds of C# and Visual Basic by default.

`cov-build` will not work when a shared compiler is used.

`cov-build` attempts to disable the use of a shared compiler by setting
the `UseSharedCompilation` environment variable to
`false`. However, this does not always disable the use of a shared
compiler. For example, a user can override the environment variable in an MSBuild
targets file or a project file.

If you are expecting to see C# or Visual Basic files emitted from your Visual Studio or .NET
SDK build and are not seeing them, you have the following options:

MSBuild
:   If you use MSBuild, you can use the command line to force it to not use the shared compiler
    line. This will override all environment/project-specified values. For example,
    if your original command
    is:

    ```
    > msbuild /t:rebuild myproject.sln
    ```

    Change it
    to:

    ```
    > msbuild /t:rebuild /p:UseSharedCompilation=false myproject.sln
    ```

.NET SDK (`dotnet`)
:   If you use `dotnet`, you can use the command line to force it to not use the
    shared compiler line. This will override all environment/project-specified
    values. For example, if your original command
    is:

    ```
    > dotnet build --no-incremental myproject.sln
    ```

    Change
    it
    to:

    ```
    > dotnet build --no-incremental -p:UseSharedCompilation=false myproject.sln
    ```

`devenv`
:   There is not currently a way to specify `UseSharedCompilation=false` for
    devenv-based build commands on the command line. In the case of devenv, you have
    two options:

    1. Use MSBuild instead of devenv. Then you can use the technique specified
       for MSBuild above.
    2. Modify your .csproj files to not set
       `UseSharedCompilation` to `true` when
       attempting to capture with `cov-build`. This allows
       `cov-build` to disable shared compilation using the
       environment variable mentioned above.
