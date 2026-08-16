---
title: "switch_default.cpp"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/switch_default.cpp.html"
content_id: "WmnYsIL2Te9MJ8rM2c~4Lw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:09.896039+00:00"
---

# switch_default.cpp

```
// find switch/case statements with no "default"
#include "extend-lang.hpp"     // Extend API
START_EXTEND_CHECKER( switch_default, simple );
ANALYZE_TREE()
{
    SwitchPat sw;
    
    if (MATCH(sw)) {
        const S_switch *s = sw.last_stmt();
        vector<const Statement *> cases;
        // getTargets gets all the "S_case" and the "S_default", if
        // any, for the switch.
        // See cc.ast
        s->getTargets(cases);
        bool hasDefault = false;
        foreach(i, cases) {
            const Statement *stmt = *i;
            // as<class>() -> downcast with assert, similar to
            // dynamic_cast<class &>
            // as<class>C() -> same, pointer to const
            // if<class>() -> downcast, NULL on failure, similar do
            // dynamic_cast<class *>
            const S_default *def = stmt->ifS_defaultC();
            if(def) {
                hasDefault = true;
                break;
            } else {
                // Only possibilities = S_default and S_case, so this
                // must be an S_case.
                const S_case *case_stmt =
                    stmt->asS_caseC();
                // You can obtain the value of the "case"
                const E_intLit *case_expr = case_stmt->expr;
                
                long long case_value = case_expr->i;
                // This is not relevant for this checker, but is only
                // included as an example
            }
        }
        if(!hasDefault) {
            OUTPUT_ERROR("switch statement doesn't have a \"default\"");
        }
    }
}
END_EXTEND_CHECKER();
MAKE_MAIN( switch_default )
```
