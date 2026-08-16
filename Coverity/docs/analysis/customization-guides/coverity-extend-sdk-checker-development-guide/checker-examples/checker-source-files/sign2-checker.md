---
title: "sign2 checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sign2-checker.html"
content_id: "s25fAr_9s9pjZif956AeWA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:07.872461+00:00"
---

# sign2 checker

```
// keep track of the sign of each expression
// Extended from sign.c: Use Extend SDK API output routines.
#include "extend-lang.hpp"     // Extend SDK API
using std::ostringstream;
// -------------------- utilities ------------------------
// skip past pathname component of a file name
char const *strip_path(char const *fname)
{
  // find last slash; don't want to rely on strrchr being present
  for (char const *p = fname; *p; p++) {
    if (p[0] == '/' && p[1] != '\0') {
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
// confirm (bounds check) that the int is in the right range
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
// abstract subtraction
AbsValue abstractSub(AbsValue a, AbsValue b)
{
  // just invert the sign of 'b' and add
  bcAbsValue(b);
  return abstractAdd(a, toAbsValue(AV_POSITIVE - b));
}
// ------------------------ the checker ----------------------
// This store maps expressions to AbsValue; unmapped expressions
// have unknown sign.
START_EXTEND_CHECKER( sign2, int_store );
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
    ADD_EVENT(CURRENT_TREE, "literal", "Saw literal value: " << ci.llval());
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
      CLEAR_STATE(CURRENT_TREE);    // avoid lots of 'unsigned' events
      SET_STATE(CURRENT_TREE, AV_POS_ZERO);
      ADD_EVENT(CURRENT_TREE, "unsigned", "Variable is unsigned");
    }
  }
  // arithmetic?
  Scalar a,b;
  if (MATCH(a+b)) {
    // any prior info we might have had regarding "a+b" is irrelevant
    CLEAR_STATE(CURRENT_TREE);
    int va, vb;
    if (GET_STATE(a, va) && GET_STATE(b, vb)) {
      AbsValue v = abstractAdd(toAbsValue(va), toAbsValue(vb));
      if (v != AV_UNKNOWN) {
        // at this time, there is no way to copy the events from two
        // different sources, so just get what I can ... bug 3439
        COPY_STATE(CURRENT_TREE, a);
        SET_STATE(CURRENT_TREE, v);
        ADD_EVENT(CURRENT_TREE, "addition",
          "Addition: " << a << " (" << toAbsValue(va) <<
          ") plus " << b << " (" << toAbsValue(vb) <<
          ") yields " << v);
      }
    }
    return;
  }
  if (MATCH(a-b)) {
    CLEAR_STATE(CURRENT_TREE);
    int va, vb;
    if (GET_STATE(a, va) && GET_STATE(b, vb)) {
      AbsValue v = abstractSub(toAbsValue(va), toAbsValue(vb));
      if (v != AV_UNKNOWN) {
        COPY_STATE(CURRENT_TREE, a);
        SET_STATE(CURRENT_TREE, v);
        ADD_EVENT(CURRENT_TREE, "subtraction",
          "Subtraction: " << a << " (" << toAbsValue(va) <<
          ") minus " << b << " (" << toAbsValue(vb) <<
          ") yields " << v);
      }
    }
    return;
  }
  // assignment?
  if (MATCH(a = b)) {
    COPY_STATE(a, b);
    ADD_EVENT(a, "var_assign",
      "Assigning " << a << " to value of " << b);
    return;
  }
  // possible conversion error?
  IntegralType destType;
  Cast cast(a, destType);    // cast from expression 'a' to type 'destType'
  if (MATCH(cast) && !a.get_type()->is_unsigned() && destType.is_unsigned()) {
    int v;
    if (GET_STATE(a, v)) {
      if (v == AV_NEGATIVE) {
        COMMIT_ERROR(a, "conversion_error",
          a << " is converted to 'unsigned' but is known to be negative");
      }
      else if (v == AV_NEG_ZERO) {
        COMMIT_ERROR(a, "conversion_error",
          a << " is converted to 'unsigned' but may be negative");
      }
      else {
        // we know it is *not* negative, so the cast is safe
      }
    }
    else {
      OUTPUT_ERROR(a << " is converted to 'unsigned' but may be negative");
    }
  }
  // query for abstract value?
  if (MATCH(CallSite("whatis")(a))) {
    int val;
    if (GET_STATE(a, val)) {
      COMMIT_ERROR(a, "whatis", a << " has value " << toAbsValue(val));
    }
    else {
      // here, COMMIT_ERROR would do nothing
      OUTPUT_ERROR("whatis: " << a << " has unknown value");
    }
    return;
  }
  // print entire store?
  if (MATCH(CallSite("print_store"))) {
    ostringstream os;
    os << "print_store: ";
    int mappings = 0;
    const ASTNode* t;
    int v;
    FOREACH_IN_STORE(t, v) {
      if (mappings > 0) {
        os << ", ";
      }
      os << t << " has value " << toAbsValue(v);
      mappings++;
    }
    os << "; " << mappings << " mappings";
    OUTPUT_ERROR(os.str());
    return;
  }
}
END_EXTEND_CHECKER();
MAKE_MAIN( sign2 )
```
