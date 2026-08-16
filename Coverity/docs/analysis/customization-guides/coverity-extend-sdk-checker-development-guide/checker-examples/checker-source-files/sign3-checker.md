---
title: "sign3 checker"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sign3-checker.html"
content_id: "iBEQ5FeZSSIX1z8ML7vmGw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:40:08.597428+00:00"
---

# sign3 checker

```
// keep track of the sign of each expression
// Extended from sign.c: Use Extend SDK API output routines.
#include "extend-lang.hpp"     // Extend SDK API
#if 1
#  define DIAGNOSTIC(stuff) cout << stuff << endl /* user ; */
#else
#  define DIAGNOSTIC(stuff) ((void)0) /* user ; */
#endif
// -------------------- AbsValue ------------------------
// abstract value domain
enum AbsValue {
  AV_NEGATIVE,     // < 0
  AV_NEG_ZERO,     // <= 0
  AV_ZERO,         // 0
  AV_POS_ZERO,     // >= 0
  AV_POSITIVE,     // > 0
  AV_UNKNOWN,      // unknown; only for return value from abstract
                   // arithmetic, not to be put into store
  NUM_ABSVALS
};
#define FOREACH_ABSVAL(var)                          \
  for(AbsValue var = AV_NEGATIVE; var < NUM_ABSVALS; \
      var = (AbsValue)(var+1))
// confirm (bounds check) that the int is in the right range
void bcAbsValue(int i)
{
  assert((unsigned)i < AV_UNKNOWN);
}
// this one allows the AV_UNKNOWN value
void bcAbsValueU(int i)
{
  assert((unsigned)i < NUM_ABSVALS);
}
// map from integer code to AbsValue; this is necessary because the
// store stores ints, not AbsValues, as its declared type
AbsValue toAbsValue(int i)
{
  bcAbsValueU(i);
  return (AbsValue)i;
}
// map a integer value to abstract value
AbsValue abstractSingleValue(long long v)
{
  if (v < 0) {
    return AV_NEGATIVE;
  }
  else if (v == 0) {
    return AV_ZERO;
  }
  else {
    return AV_POSITIVE;
  }
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
    case AV_UNKNOWN:  return os << "AV_UNKNOWN";
  }
}
// ------------------ abstract operations --------------------
// abstract addition; assumes overflow can't happen
AbsValue abstractAdd(AbsValue a, AbsValue b)
{
  static AbsValue const map[AV_UNKNOWN][AV_UNKNOWN] = {
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
// -------------------- abstract comparison -----------------
// Record the consequences of learning that the comparison 'a' op 'b'
// is true.
struct AbstractComparisonResult {
  // if this is false, we know the comparison could *not* be true,
  // so we will abort the path
  bool consistent;
  // what is the new approximation for 'a' and 'b'?
  AbsValue newAValue;
  AbsValue newBValue;
};
// the type of a precomputed relation map; maps from the abstract
// values of its arguments to the abstract comparison result
typedef AbstractComparisonResult RelationMap[NUM_ABSVALS][NUM_ABSVALS];
// concrete relational operator
typedef bool (*ConcreteOperator)(int a, int b);
// compute best approximation of union of concrete values 
// represented by 'a' and 'b'
AbsValue greatestLowerBound(AbsValue a, AbsValue b)
{
  if (a == AV_UNKNOWN || b == AV_UNKNOWN) {
    return AV_UNKNOWN;
  }
  static AbsValue const map[AV_UNKNOWN][AV_UNKNOWN] = {
    // b:   a:  <0           <=0          0            >=0          >0
    /* <0  */ { AV_NEGATIVE, AV_NEG_ZERO, AV_NEG_ZERO, AV_UNKNOWN,  AV_UNKNOWN  },
    /* <=0 */ { AV_NEG_ZERO, AV_NEG_ZERO, AV_NEG_ZERO, AV_UNKNOWN,  AV_UNKNOWN  },
    /* 0   */ { AV_NEG_ZERO, AV_NEG_ZERO, AV_ZERO,     AV_POS_ZERO, AV_POS_ZERO },
    /* >=0 */ { AV_UNKNOWN,  AV_UNKNOWN,  AV_POS_ZERO, AV_POS_ZERO, AV_POS_ZERO },
    /* >0  */ { AV_UNKNOWN,  AV_UNKNOWN,  AV_POS_ZERO, AV_POS_ZERO, AV_POSITIVE },
  };
  bcAbsValue(a);
  bcAbsValue(b);
  return map[a][b];
}
// Test if a given concrete value is a member of the set represented
// by the given abstract value.
bool elementOf(int concrete, AbsValue abstract)
{
  switch (abstract) {
    default: assert(!"bad AbsValue");
    case AV_NEGATIVE: return concrete < 0;
    case AV_NEG_ZERO: return concrete <= 0;
    case AV_ZERO:     return concrete == 0;
    case AV_POS_ZERO: return concrete >= 0;
    case AV_POSITIVE: return concrete > 0;
    case AV_UNKNOWN:  return true;
  }
}
// Concretize 'a' and 'b', filter for pairs satisfying 'op', then
// re-abstract.
AbstractComparisonResult abstractComparison(AbsValue a, AbsValue b,
                                            ConcreteOperator op)
{
  AbstractComparisonResult ret;
  ret.consistent = false;
  ret.newAValue = AV_UNKNOWN;
  ret.newBValue = AV_UNKNOWN;
  // The algorithm here is to just compare all pairs of concrete
  // values drawn from [-2,2], since that is sufficient precision
  // to distinguish all our abstract comparisons.
  //
  // This is pretty stupid (inefficient), but it works, and we'll only
  // do it once at the beginning.
  for (int aa=-2; aa<=2; aa++) {
    if (!elementOf(aa, a)) { continue; }
    for (int bb=-2; bb<=2; bb++) {
      if (!elementOf(bb, b)) { continue; }
      // Now 'aa' is a concrete element of 'a', and 'bb' is a
      // concrete element of 'b'.
      // Filter on 'op'.
      if (!op(aa, bb)) {
        continue;
      }
      // Abstract the ('aa', 'bb') pair.
      AbsValue aaa = abstractSingleValue(aa);
      AbsValue bbb = abstractSingleValue(bb);
      // Fold this into our current approximation.
      if (!ret.consistent) {
        ret.consistent = true;
        ret.newAValue = aaa;
        ret.newBValue = bbb;
      }
      else {
        ret.newAValue = greatestLowerBound(ret.newAValue, aaa);
        ret.newBValue = greatestLowerBound(ret.newBValue, bbb);
      }
    }
  }
  
  return ret;
}
// ---------------- relational operators -------------------
// information about a single relational operator ("<", "==", etc.)
class RelationalOperator {
public:      // data
  // Code to denote it
  BinaryOp binaryOp;
  // concrete comparison function; this is used to compute 'map'
  ConcreteOperator concreteOp;
  // abstract comparison table
  RelationMap map;
public:      // funcs
  RelationalOperator(BinaryOp bop, ConcreteOperator concrete);
};
RelationalOperator::RelationalOperator(BinaryOp bop, ConcreteOperator concrete)
  : binaryOp(bop),
    concreteOp(concrete)
{
  // compute the abstract operation table
  FOREACH_ABSVAL(a) {
    FOREACH_ABSVAL(b) {
      map[a][b] = abstractComparison(a, b, concreteOp);
    }
  }
}
// concrete comparisons
bool compareLess(int a, int b)      { return a < b; }
bool compareLessEq(int a, int b)    { return a <= b; }
bool compareGreater(int a, int b)   { return a > b; }
bool compareGreaterEq(int a, int b) { return a >= b; }
bool compareEqual(int a, int b)     { return a == b; }
bool compareNotEqual(int a, int b)  { return a != b; }
enum { NUM_RELATIONAL_OPERATORS = 6 };
RelationalOperator *relationalOperators[NUM_RELATIONAL_OPERATORS];
// ------------------------ the checker ----------------------
// This store maps expressions to AbsValue; unmapped expressions
// have unknown sign.
START_EXTEND_CHECKER( sign3, int_store );
// Called at program startup.
CHECKER_INIT()
{
  relationalOperators[0] = new RelationalOperator(BIN_LESS, compareLess);
  relationalOperators[1] = new RelationalOperator(BIN_LESSEQ, compareLessEq);
  relationalOperators[2] = new RelationalOperator(BIN_GREATER, compareGreater);
  relationalOperators[3] = new RelationalOperator(BIN_GREATEREQ, compareGreaterEq);
  relationalOperators[4] = new RelationalOperator(BIN_EQUAL, compareEqual);
  relationalOperators[5] = new RelationalOperator(BIN_NOTEQUAL, compareNotEqual);
}
ANALYZE_TREE()
{
  // integer literal?
  Const_int ci;
  if (MATCH(ci)) {
    SET_STATE(CURRENT_TREE, abstractSingleValue(ci.llval()));
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
    std::ostringstream os;
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
ANALYZE_CONDITION()
{
/*
  const cond_cfg_edge_t *cond_edge = dynamic_cast<const cond_cfg_edge_t *>(edge);
  if(!cond_edge) return;
  bool cov_polarity = cond_edge->polarity;
  const Expression *cond = cond_edge->cond;
  const ASTNode* astnode = (const ASTNode*)cond;
*/
  // comparison?
  Expr a, b;
  for (int i=0; i < NUM_RELATIONAL_OPERATORS; i++) {
    RelationalOperator *relop = relationalOperators[i];
    if (MATCH_COND(Binop(relop->binaryOp, a, b))) {
      int va, vb;
      if (!GET_STATE(a, va)) { va = AV_UNKNOWN; }
      if (!GET_STATE(b, vb)) { vb = AV_UNKNOWN; }
      DIAGNOSTIC("matched conditional " <<
                 (cov_polarity? "" : "!") << CURRENT_TREE <<
                 "; " << a << " = " << toAbsValue(va) <<
                 ", " << b << " = " << toAbsValue(vb));
      // do the abstract comparison
      AbstractComparisonResult &res = relop->map[va][vb];
      if (!res.consistent) {
        DIAGNOSTIC("  backtracking due to inconsistency");
        force_backtrack();
        return;
      }
      // update store?
      if (res.newAValue != va) {
        SET_STATE(a, res.newAValue);
        ADD_EVENT(a, "conditional", "Refined via conditional " << CURRENT_TREE);
        DIAGNOSTIC("  refined " << a << " to " << res.newAValue);
      }
      if (res.newBValue != vb) {
        SET_STATE(b, res.newBValue);
        ADD_EVENT(b, "conditional", "Refined via conditional " << CURRENT_TREE);
        DIAGNOSTIC("  refined " << b << " to " << res.newBValue);
      }
    }
  }
}
END_EXTEND_CHECKER();
MAKE_MAIN( sign3 )
```
