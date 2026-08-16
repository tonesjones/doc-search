---
title: "Examples of using base class properties"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples-of-using-base-class-properties.html"
content_id: "MJN55PbMZYMwft2apYYEtw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:34:13.258900+00:00"
---

# Examples of using base class properties

Here are some examples of using a base class.

This first example uses `findBaseClass`.
If `findBaseClass` can locate a class whose identifier (`base.identifier`)
is `"A"`, it returns the object for that class.
Otherwise, the return value is `null`:

  
 [image: CXM code follows]   

```
checker {
    name = "DERIVES_FROM_A_findBaseClass";
    reports = for c in globalset allClasses
        where c.findBaseClass(
            function ( base: typeof( classType ).producedType ) ->
                base.identifier == "A" ? base : null )
                    matches NonNull as baseA :
                        {
                            events = [
                                {
                                    tag = "base";
                                    description = baseA
                                                  + " is here";
                                    location = baseA.location;
                                },
                                {
                                    tag = "child";
                                    description = "Class "
                                                  + c.declaredType
                                                  + " derives from A";
                                    location = c.location;
                                }
                            ];
                        };
};
```

The second example uses `findMatchingBaseClass`:

  
 [image: CXM code follows]   

```
checker {
    name = "DERIVES_FROM_A_findMatchingBaseClass";
    reports = for c in globalset allClasses
        where c.findMatchingBaseClass(
            classType { .identifier == "A"} )
                matches NonNull as baseA :
                    {
                        events = [
                            {
                                tag = "base";
                                description = baseA
                                              + " is here";
                                location = baseA.location;
                            },
                            {
                                tag = "child";
                                description = "Class "
                                              + c.declaredType
                                              + " derives from A";
                                location = c.location;
                            }
                        ];
                    };
};
```
