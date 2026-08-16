---
title: "Models for function pointers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/models-for-function-pointers.html"
content_id: "ERROJXVgWBrYd9Cqg1BYRA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:33.798470+00:00"
---

# Models for function pointers

In certain cases, Coverity cannot analyze calls to function pointers. In such cases,
you can explicitly model function pointers to find more defects.

You can enable analysis of calls to function pointers by using the
`cov-analyze` option `--enable-fnptr`. This
option increases the false positive rate by approximately 10–20%. Although the
`--enable-fnptr` option analyzes most calls to function pointers, in
some cases calls to function pointers might not be analyzed. The flow of functions
through casts, for example, is not tracked by the analysis. For such function calls, you
can use explicit function-pointer models: see the instructions that follow.

To model function pointers, follow these steps:

1. Create a model that uses the following naming convention:
   - If the function pointer is a global
     variable:

     ```
     __coverity_fnptr_<variable>
     ```
   - If the function pointer is a field in a structure:

     ```
     __coverity_fnptr_<type>_<field>
     ```For example, the following pointer functions have model names that are noted in
   the comments:

   ```
   struct aStruct {
       void (*ABC)(int);
       void (*ZYX)(int);
   };
   int (*INT)(void);
   struct aStruct glStruct;
       
   void testfn(struct aStruct *s) {
       int x;
       x = INT();       // call to __coverity_fnptr_INT
       glStruct.ABC(x); // call to __coverity_fnptr_aStruct_ABC
       s->ZYX(x);       // call to __coverity_fnptr_aStruct_ZYX
   }
   ```
2. In the new model, use a primitive to specify the behavior of the function pointer.

   For example, the following C code has two function pointers:

   ```
   struct memory {
       void *(*get)(size_t);
       void (*put)(void *);
   };

   void test(struct memory *m, int l, int x) {
       int *p;

       p = m->get(l);
       if (!x)
           return;   // resource leak of p
       m->put(p);
       m->put(p);    // double free of p
       }
   ```

   By default, the analysis does not find the two defects. However, with the
   following models, both defects are reported:

   ```
   void *__coverity_fnptr_memory_get(int l) {
       return __coverity_alloc__(l);
   }

   void __coverity_fnptr_memory_put(void *p) {
       __coverity_free__(p);
   }
   ```
3. Run `cov-make-library` to generate the model.
4. Run `cov-analyze` command with the
   `--fnptr-models` option.
