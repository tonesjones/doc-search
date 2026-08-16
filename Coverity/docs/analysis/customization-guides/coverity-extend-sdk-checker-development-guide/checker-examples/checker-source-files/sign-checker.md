---
title: "sign checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sign-checker.html"
content_id: "Tyw~LqSLsh5C2JqXEgZ7Gw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:07.055400+00:00"
---

# sign checker

```
// keep track of the sign of each expression
#include "extend-lang.hpp"     // Extend SDK API
// -------------------- utilities ------------------------
// skip past pathname component of a file name
char const *strip_path(char const *fname)
{
  // find last slash; don't want to rely on strrchr being present
  for (char const *p = fname; *p; p++) {
    if (*p == '/') {
      fname = p+1;    // go one past this (maybe last) slash
    }
  }
  return fname;
}
// print out the current file/line (stripping the path of the file),
// and return an ostream for additional printing
ostream &cout_loc()
{
  return cout << strip_path(current_file_get_name()) << ":"
              << current_file_lineno() << ": ";
}
// -------------------- AbsValue ------------------------
// abstract value domain
enum AbsValue {
  AV_NEGATIVE,     // < 0
  AV_NEG_ZERO,     // <= 0
  AV_ZERO,         // 0
  AV_POS_ZERO,     // >= 0
  AV_POSITIVE,     // > 0
  AV_UNKNOWN       // unknown; only for return value from abstract 
                   // arithmetic, not to be put into store
};
// confirm the int is in the right range for an AbsValue
void bcAbsValue(int i)
{
  assert((unsigned)i < AV_UNKNOWN);
}
// map from int to AbsValue; this is necessary because the store
// stores ints, not AbsValues, as its declared type
AbsValue toAbsValue(int i)
{
  bcAbsValue(i);
  return (AbsValue)i;
}
// print an abstract value
ostream& operator<< (ostream &os, AbsValue v)
{
  switch (v) {
    default: assert(!"bad AbsValue code");
    case AV_NEGATIVE: return os << "AV_NEGATIVE";
    case AV_NEG_ZERO: return os << "AV_NEG_ZERO";
    case AV_ZERO:     return os << "AV_ZERO";
    case AV_POS_ZERO: return os << "AV_POS_ZERO";
    case AV_POSITIVE: return os << "AV_POSITIVE";
  }
}
// ------------------ abstract operations --------------------
// abstract addition; assumes overflow can't happen
AbsValue abstractAdd(AbsValue a, AbsValue b)
{
  static AbsValue const map[5][5] = {
    // b:   a:  <0           <=0          0            >=0          >0
    /* <0  */ { AV_NEGATIVE, AV_NEGATIVE, AV_NEGATIVE, AV_UNKNOWN,  AV_UNKNOWN  },
    /* <=0 */ { AV_NEGATIVE, AV_NEG_ZERO, AV_NEG_ZERO, AV_UNKNOWN,  AV_UNKNOWN  },
    /* 0   */ { AV_NEGATIVE, AV_NEG_ZERO, AV_ZERO,     AV_POS_ZERO, AV_POSITIVE },
    /* >=0 */ { AV_UNKNOWN,  AV_UNKNOWN,  AV_POS_ZERO, AV_POS_ZERO, AV_POSITIVE },
    /* >0  */ { AV_UNKNOWN,  AV_UNKNOWN,  AV_POSITIVE, AV_POSITIVE, AV_POSITIVE },
  };
  bcAbsValue(a);
  bcAbsValue(b);
  return map[a][b];
}
AbsValue abstractSub(AbsValue a, AbsValue b)
{
  // just invert the sign of 'b' and add
  bcAbsValue(b);
  return abstractAdd(a, toAbsValue(AV_POSITIVE - b));
}
// ------------------------ the checker ----------------------
// This store maps expressions to AbsValue; unmapped expressions
// have unknown sign.
START_EXTEND_CHECKER( sign, int_store );
ANALYZE_TREE()
{
  // integer literal?
  Const_int ci;
  if (MATCH(ci)) {
    if (ci.llval() < 0) {
      SET_STATE(CURRENT_TREE, AV_NEGATIVE);
    }
    else if (ci.llval() == 0) {
      SET_STATE(CURRENT_TREE, AV_ZERO);
    }
    else {
      SET_STATE(CURRENT_TREE, AV_POSITIVE);
    }
    return;
  }
  // unsigned variable?
  Scalar scal;
  Var var;
  if (MATCH(var) && MATCH(scal) && scal.get_type()->is_unsigned()) {
    int v;
    if (GET_STATE(CURRENT_TREE, v) && v == AV_POSITIVE) {
      // 'var' is already known to be positive, so leave it alone
    }
    else {
      // set it to >= 0
      SET_STATE(CURRENT_TREE, AV_POS_ZERO);
    }
  }
  // arithmetic?
  Expr a,b;
  if (MATCH(a+b)) {
    int va, vb;
    if (GET_STATE(a, va) && GET_STATE(b, vb)) {
      AbsValue v = abstractAdd(toAbsValue(va), toAbsValue(vb));
      if (v != AV_UNKNOWN) {
        SET_STATE(CURRENT_TREE, v);
      }
    }
    return;
  }
  if (MATCH(a-b)) {
    int va, vb;
    if (GET_STATE(a, va) && GET_STATE(b, vb)) {
      AbsValue v = abstractSub(toAbsValue(va), toAbsValue(vb));
      if (v != AV_UNKNOWN) {
        SET_STATE(CURRENT_TREE, v);
      }
    }
    return;
  }
  // assignment?
  if (MATCH(a = b)) {
    COPY_STATE(a, b);
    return;
  }
  // query for abstract value?
  if (MATCH(CallSite("whatis")(a))) {
    int val;
    if (GET_STATE(a, val)) {
      cout_loc() << a << " has value " << toAbsValue(val) << endl;
    }
    else {
      cout_loc() << a << " has unknown value" << endl;
    }
    return;
  }
  // print entire store?
  if (MATCH(CallSite("print_store"))) {
    cout_loc() << "print_store:\n";
    int mappings = 0;
    const ASTNode* t;
    int v;
    FOREACH_IN_STORE(t, v) {
      cout << "  " << t << " has value " << toAbsValue(v) << endl;
      mappings++;
    }
    cout << "  " << mappings << " mappings" << endl;
    return;
  }
}
END_EXTEND_CHECKER();
MAKE_MAIN( sign )
```
