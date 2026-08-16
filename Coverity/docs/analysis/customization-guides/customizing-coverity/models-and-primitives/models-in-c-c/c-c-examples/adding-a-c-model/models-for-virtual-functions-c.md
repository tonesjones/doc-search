---
title: "Models for virtual functions (C++)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/models-for-virtual-functions-c-.html"
content_id: "hCReFSDwMz2nP3HAZVxeJw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:38.415488+00:00"
---

# Models for virtual functions (C++)

When you make a call to a virtual or pure virtual function that you have modeled, the
analysis will always use that model. As a consequence, you do not need to set the
`cov-analyze` option `--enable-virtual` for
this purpose.

The following example shows how `a->color()` makes the analysis resolve to
the model:

```
/* Abstract base class Fruit */                
class Fruit {
    virtual int color() = 0; 
};
    
/* Derived class Lemon */
class Lemon: public Fruit {
    int color(); 
};
    
/* Derived class Apple */
class Apple: public Fruit {
    int color(); 
}
    
/* In a model file, a model based on derived class Apple */
class Apple {
    int color() { what_color_should_do(); }
};

/* Testing the analysis with and without setting --enable-virtual. */
void test(Fruit *f, Apple *a) {
    // Without --enable-virtual set: 
    //     Call to f->color() is unimplemented.
    // With --enable-virtual set: 
    //     Call to f->color() resolves to the model and to Lemon::color.
    f->color(); 
    
    // Call to a->color() always resolves to the model 
    // regardless of whether you set --enable-virtual.
    a->color();
}
```

1. An abstract class, `Fruit`, is the basis for two derived classes,
   `Lemon` and `Apple`. Each of these declare a
   virtual function named `color()`.
2. A model file defines a model based on the `Apple` class. In the
   model, `Apple` contains code to describe what
   `color()` would do.
3. Test code specifies parameters of type `Fruit` and
   `Apple`. Analysis behavior is as follows:
   - For the parameter `Fruit *f`, if the option
     `--enable-virtual` is not set, the call to
     `f->color()` is undefined (unimplemented). If
     `--enable-virtual` is set, the call to
     `f->color()` resolves to
     `Lemon::color`.
   - For the parameter `Apple *a`, the call to
     `a->color()` resolves to the model *regardless of
     whether* the option `--enable-virtual` is set or
     not.

For more information about the `--enable-virtual` option, see the
description of `cov-analyze`
in the Coverity 2026.6.0 Command Reference.
