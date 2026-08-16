---
title: "callsite_with_static_target"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/callsite_with_static_target.html"
content_id: "GPXXvvTb0QUmfuUDZJ~Vow"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:10.881175+00:00"
---

# callsite_with_static_target

**Languages: C#, Java, Visual Basic**

A `callsite_with_static_target CallsiteSet` matches call sites whose
static call target (that is, the function to which the call resolves before considering
virtual call resolution) is in a specified MethodSet.

## Fields

`callsite_with_static_target`
:   Specifies a MethodSet.
    Function call sites that call a function in this set are included in the
    `CallsiteSet`.

## Examples

**Java Example:**

```
{
    callsite_with_static_target : {
        "named" : "battle.robot.api.RobotService.run(java.lang.String, int)void"
    }
},
```

The `CallsiteSet` above matches the call site in this Java code:

```
void doRotate(battle.robot.api.RobotService robot) {
    robot.run("rotate", 180);
}
```
