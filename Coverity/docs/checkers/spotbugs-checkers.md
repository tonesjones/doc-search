---
title: "SpotBugs checkers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/spotbugs-checkers.html"
content_id: "HSrh_Ivp~rJDrfWo_urUmg"
version: "2026.6"
section: "SpotBugs™ Checker Reference"
scraped_at: "2026-08-12T03:21:04.539142+00:00"
---

# SpotBugs checkers

## FB.AA_ASSERTION_OF_ARGUMENTS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | AA: Misuse of assertions for checking arguments of public methods |

Assertions must not be used to validate arguments of public methods because the validations are not performed if assertions are disabled.

## FB.AM_CREATES_EMPTY_JAR_FILE_ENTRY

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | AM: API misuse | [CWE-227](http://cwe.mitre.org/data/definitions/227.html) |

The code calls `putNextEntry()`, immediately followed by a call to
`closeEntry()`. This results in an empty JarFile entry. The
contents of the entry should be written to the JarFile between the calls to
`putNextEntry()` and `closeEntry()`.

## FB.AM_CREATES_EMPTY_ZIP_FILE_ENTRY

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | AM: API misuse | [CWE-227](http://cwe.mitre.org/data/definitions/227.html) |

The code calls `putNextEntry()`, immediately followed by a call to
`closeEntry()`. This results in an empty ZipFile entry. The
contents of the entry should be written to the ZipFile between the calls to
`putNextEntry()` and `closeEntry()`.

## FB.ASE_ASSERTION_WITH_SIDE_EFFECT

|  |  |
| --- | --- |
| SpotBugs: Security | ASE: Assertion with side effect |

Expressions used in assertions must not produce side effects.

## FB.ASE_ASSERTION_WITH_SIDE_EFFECT_METHOD

|  |  |
| --- | --- |
| SpotBugs: Security | ASE: Assertion with side effect |

Expressions used in assertions must not produce side effects.

## FB.AT_OPERATION_SEQUENCE_ON_CONCURRENT_ABSTRACTION

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | AT: Possible atomicity violation |

This code contains a sequence of calls to a
concurrent abstraction (such as a concurrent hash map). These calls will not be
executed atomically.

## FB.BAC_BAD_APPLET_CONSTRUCTOR

|  |  |
| --- | --- |
| SpotBugs: Correctness | BAC: Bad `Applet` constructor |

This constructor calls methods in the parent `Applet` that rely on the
`AppletStub`. Since the `AppletStub` isn't
initialized until the `init()` method of this applet is called, these
methods will not perform correctly.

## FB.BC_BAD_CAST_TO_ABSTRACT_COLLECTION

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | BC: Bad casts of object references |

This code casts a `Collection` to an abstract collection (such as
`List`, `Set`, or `Map`). Ensure
that you are guaranteed that the object is of the type you are casting to. If all
you need is to be able to iterate through a collection, you don't need to cast it to
a `Set` or `List`.

## FB.BC_BAD_CAST_TO_CONCRETE_COLLECTION

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | BC: Bad casts of object references |

This code casts an abstract collection (such as a `Collection`,
`List`, or `Set`) to a specific concrete
implementation (such as an `ArrayList` or `HashSet`).
This might not be correct, and it may make your code fragile, since it makes it
harder to switch to other concrete implementations at a future point. Unless you
have a particular reason to do so, just use the abstract collection class.

## FB.BC_EQUALS_METHOD_SHOULD_WORK_FOR_ALL_OBJECTS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | BC: Bad casts of object references |

The `equals(Object o)` method shouldn't make any assumptions about the
type of `o`. It should simply return `false` if
`o` is not the same type as `this`.

## FB.BC_IMPOSSIBLE_CAST

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | BC: Bad casts of object references | [CWE-570](http://cwe.mitre.org/data/definitions/570.html) |

This cast will always throw a `ClassCastException`. SpotBugs tracks
type information from `instanceof` checks, and also uses more precise
information about the types of values returned from methods and loaded from fields.
Thus, it may have more precise information that just the declared type of a
variable, and can use this to determine that a cast will always throw an exception
at runtime.

## FB.BC_IMPOSSIBLE_CAST_PRIMITIVE_ARRAY

|  |  |
| --- | --- |
| SpotBugs: Correctness | BC: Bad casts of object references |

This cast will always throw a `ClassCastException`.

## FB.BC_IMPOSSIBLE_DOWNCAST

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | BC: Bad casts of object references | [CWE-570](http://cwe.mitre.org/data/definitions/570.html) |

This cast will always throw a `ClassCastException`. The analysis
believes it knows the precise type of the value being cast, and the attempt to
downcast it to a subtype will always fail by throwing a
`ClassCastException`.

## FB.BC_IMPOSSIBLE_DOWNCAST_OF_TOARRAY

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | BC: Bad casts of object references | [CWE-570](http://cwe.mitre.org/data/definitions/570.html) |

This code is casting the result of calling `toArray()` on a collection
to a type more specific than `Object[]`, as in:

```
String[] getAsArray(Collection<String> c) {
    return (String[]) c.toArray();
}
```

This will usually fail by throwing a `ClassCastException`. The
`toArray()` of almost all collections return an
`Object[]`. They can't really do anything else, since the
`Collection` object has no reference to the declared generic type
of the collection.

The correct way to do get an array of a specific type from a collection is to use
`c.toArray(new String[]);` or `c.toArray(new
String[c.size()]);` (the latter is slightly more efficient).

There is one common/known exception to this. The `toArray()` method of
lists returned by `Arrays.asList(...)` will return a covariantly
typed array. For example,

```
Arrays.asArray(new String[] { "a" }).toArray()
```

will return a
`String []`. SpotBugs attempts to detect and suppress such cases,
but may miss some.

## FB.BC_IMPOSSIBLE_INSTANCEOF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | BC: Bad casts of object references | [CWE-570](http://cwe.mitre.org/data/definitions/570.html) |

This `instanceof` test will always return false. Although this is
safe, make sure it isn't an indication of some misunderstanding or some other logic
error.

## FB.BC_NULL_INSTANCEOF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This `instanceof` test will always return false, since the value being
checked is guaranteed to be null. Although this is safe, make sure it isn't an
indication of some misunderstanding or some other logic error.

## FB.BC_UNCONFIRMED_CAST

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | BC: Bad casts of object references |

This cast is unchecked, and not all instances of the type casted from can be cast to
the type it is being cast to. Check that your program logic ensures that this cast
will not fail.

## FB.BC_UNCONFIRMED_CAST_OF_RETURN_VALUE

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | BC: Bad casts of object references |

This code performs an unchecked cast of the return value of a method. The code might
be calling the method in such a way that the cast is guaranteed to be safe, but
SpotBugs is unable to verify that the cast is safe. Check that your program logic
ensures that this cast will not fail.

## FB.BC_VACUOUS_INSTANCEOF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | BC: Bad casts of object references | [CWE-571](http://cwe.mitre.org/data/definitions/571.html) |

This `instanceof` test will always return true (unless the value being
tested is null). Although this is safe, make sure it isn't an indication of some
misunderstanding or some other logic error. If you really want to test the value for
being null, perhaps it would be clearer to do better to do a null test rather than
an `instanceof` test.

## FB.BIT_ADD_OF_SIGNED_BYTE

|  |  |
| --- | --- |
| SpotBugs: Correctness | BIT: Suspicious bitwise logical expression |

Adds a byte value and a value which is known to have the 8 lower bits clear. Values
loaded from a byte array are sign extended to 32 bits before any bitwise operations
are performed on the value. Thus, if `b[0]` contains the value
`0xff`, and `x` is initially 0, then the code
`((x << 8) + b[0])` will sign extend `0xff`
to get `0xffffffff`, and thus give the value
`0xffffffff` as the result.

In particular, the following code for packing a byte array into an int is badly
wrong:

```
int result = 0;
for(int i = 0; i < 4; i++)
    result = ((result << 8) + b[i]);
```

The following idiom will work instead:

```
int result = 0;
for(int i = 0; i < 4; i++)
    result = ((result << 8) + (b[i] & 0xff));
```

## FB.BIT_AND

|  |  |
| --- | --- |
| SpotBugs: Correctness | BIT: Suspicious bitwise logical expression |

This method compares an expression of the form `(e & C)` to
`D`, which will always compare unequal due to the specific values
of constants `C` and `D`. This may indicate a logic
error or typo.

## FB.BIT_AND_ZZ

|  |  |
| --- | --- |
| SpotBugs: Correctness | BIT: Suspicious bitwise logical expression |

This method compares an expression of the form `(e & 0)` to
`0`, which will always compare equal. This may indicate a logic
error or typo.

## FB.BIT_IOR

|  |  |
| --- | --- |
| SpotBugs: Correctness | BIT: Suspicious bitwise logical expression |

This method compares an expression of the form `(e | C)` to
`D`, which will always compare unequal due to the specific values
of constants `C` and `D`. This may indicate a logic
error or typo.

Typically, this bug occurs because the code wants to perform a membership test in a
bit set, but uses the bitwise OR operator ("`|`") instead of bitwise
AND ("`&`").

Also such bug may appear in expressions like `(e & A | B) == C`
which is parsed like `((e & A) | B) == C` while `(e &
(A | B)) == C` was intended.

## FB.BIT_IOR_OF_SIGNED_BYTE

|  |  |
| --- | --- |
| SpotBugs: Correctness | BIT: Suspicious bitwise logical expression |

Loads a byte value (e.g., a value loaded from a byte array or returned by a method
with return type byte) and performs a bitwise OR with that value. Byte values are
sign extended to 32 bits before any bitwise operations are performed on the value.
Thus, if `b[0]` contains the value `0xff`, and
`x` is initially 0, then the code `((x << 8) |
b[0])` will sign extend `0xff` to get
`0xffffffff`, and thus give the value `0xffffffff`
as the result.

In particular, the following code for packing a byte array into an int is badly
wrong:

```
int result = 0;
for(int i = 0; i < 4; i++) {
    result = ((result << 8) | b[i]);
}
```

The following idiom will work instead:

```
int result = 0;
for(int i = 0; i < 4; i++) {
    result = ((result << 8) | (b[i] & 0xff));
}
```

## FB.BIT_SIGNED_CHECK

|  |  |
| --- | --- |
| SpotBugs: Bad practice | BIT: Suspicious bitwise logical expression |

This method compares an expression such as `((event.detail & SWT.SELECTED)
> 0)`. Using bit arithmetic and then comparing with the greater than
operator can lead to unexpected results (of course depending on the value of
`SWT.SELECTED`). If `SWT.SELECTED` is a negative
number, this is a candidate for a bug. Even when `SWT.SELECTED` is
not negative, it seems good practice to use `'!= 0'` instead of
`'> 0'`.

## FB.BIT_SIGNED_CHECK_HIGH_BIT

|  |  |
| --- | --- |
| SpotBugs: Correctness | BIT: Suspicious bitwise logical expression |

This method compares a bitwise expression such as `((val & CONSTANT) >
0)` where `CONSTANT` is the negative number. Using bit
arithmetic and then comparing with the greater than operator can lead to unexpected
results. This comparison is unlikely to work as expected. The good practice is to
use `'!= 0'` instead of `'> 0'`.

## FB.BOA_BADLY_OVERRIDDEN_ADAPTER

|  |  |
| --- | --- |
| SpotBugs: Correctness | BOA: Badly Overridden Adapter |

The declared method does not actually override a method from Adapter parent class, as
its name suggests. As a result, this method will not get called when the
corresponding event occurs.

## FB.BRSA_BAD_RESULTSET_ACCESS

|  |  |
| --- | --- |
| SpotBugs: Correctness | SQL: Potential SQL Problem |

A call to `getXXX` or `updateXXX` methods of a result
set was made where the field index is 0. As `ResultSet` fields start
at index 1, this is always a mistake.

## FB.BSHIFT_WRONG_ADD_PRIORITY

|  |  |
| --- | --- |
| SpotBugs: Correctness | BSHIFT: Bad shift |

The code performs an operation like `(x << 8 + y)`. Although
this might be correct, probably it was meant to perform `(x << 8) +
y`, but shift operation has a lower precedence, so it's actually parsed
as `x << (8 + y)`.

## FB.BX_BOXING_IMMEDIATELY_UNBOXED

|  |  |
| --- | --- |
| SpotBugs: Performance | Bx: Questionable Boxing of primitive value |

A primitive is boxed, and then immediately unboxed. This probably is due to a manual
boxing in a place where an unboxed value is required, thus forcing the compiler to
immediately undo the work of the boxing.

## FB.BX_BOXING_IMMEDIATELY_UNBOXED_TO_PERFORM_COERCION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Performance | Bx: Questionable Boxing of primitive value | [CWE-192](http://cwe.mitre.org/data/definitions/192.html) |

A primitive boxed value constructed and then immediately converted into a different
primitive type (e.g.,`new Double(d).intValue()`). Just perform direct
primitive coercion (e.g., `(int) d`).

## FB.BX_UNBOXED_AND_COERCED_FOR_TERNARY_OPERATOR

|  |  |
| --- | --- |
| SpotBugs: Performance | Bx: Questionable Boxing of primitive value |

A wrapped primitive value is unboxed and converted to another primitive type as part
of the evaluation of a conditional ternary operator (the `b ? e1 :
e2` operator). The semantics of Java mandate that if `e1`
and `e2` are wrapped numeric values, the values are unboxed and
converted/coerced to their common type (e.g, if `e1` is of type
`Integer` and `e2` is of type
`Float`, then `e1` is unboxed, converted to a
floating point value, and boxed. See *Java Language Specification* Section
15.25 on the conditional operator "`?`".

## FB.BX_UNBOXING_IMMEDIATELY_REBOXED

|  |  |
| --- | --- |
| SpotBugs: Performance | Bx: Questionable Boxing of primitive value |

A boxed value is unboxed and then immediately reboxed.

## FB.CAA_COVARIANT_ARRAY_ELEMENT_STORE

|  |  |
| --- | --- |
| SpotBugs: Correctness | CAA: Covariant array assignment |

Value is stored into the array and the value type doesn't match the array type. It's
known from the analysis that actual array type is narrower than the declared type of
its variable or field and this assignment doesn't satisfy the original array type.
This assignment may cause `ArrayStoreException` at runtime.

## FB.CAA_COVARIANT_ARRAY_FIELD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | CAA: Covariant array assignment |

Array of covariant type is assigned to a field. This is confusing and may lead to
`ArrayStoreException` at runtime if the reference of some other
type will be stored in this array later like in the following code:

```
Number[] arr = new Integer[10];
arr[0] = 1.0;
```

Consider changing the type of created array or the field type.

## FB.CAA_COVARIANT_ARRAY_LOCAL

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | CAA: Covariant array assignment |

Array of covariant type is assigned to a local variable. This is confusing and may
lead to `ArrayStoreException` at runtime if the reference of some
other type will be stored in this array later like in the following code:

```
Number[] arr = new Integer[10];
arr[0] = 1.0;
```

Consider changing the type of created array or the local variable type.

## FB.CAA_COVARIANT_ARRAY_RETURN

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | CAA: Covariant array assignment |

Array of covariant type is returned from the method. This is confusing and may lead
to `ArrayStoreException` at runtime if the calling code will try to
store the reference of some other type in the returned array.

Consider changing the type of created array or the method return type.

## FB.CD_CIRCULAR_DEPENDENCY

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | CD: Circular Dependencies |

This class has a circular dependency with other classes. This makes building these
classes difficult, as each is dependent on the other to build correctly. Consider
using interfaces to break the hard dependency.

## FB.CI_CONFUSED_INHERITANCE

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | CI: Confused Inheritance |

This class is declared to be final, but declares fields to be protected. Since the
class is final, it can not be derived from, and the use of protected is confusing.
The access modifier for the field should be changed to private or public to
represent the true use for the field.

## FB.CNT_ROUGH_CONSTANT_VALUE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | CNT: Rough value of known constant |

It's recommended to use the predefined library constant for code clarity and better
precision.

## FB.CN_IDIOM

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | CN: Bad implementation of cloneable idiom | [CWE-580](http://cwe.mitre.org/data/definitions/580.html) |

Class implements `Cloneable` but does not define or use the clone
method.

## FB.CN_IDIOM_NO_SUPER_CALL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | CN: Bad implementation of cloneable idiom | [CWE-580](http://cwe.mitre.org/data/definitions/580.html) |

This non-final class defines a `clone()` method that does not call
`super.clone()`. If this class ("*A*") is extended by a
subclass ("*B*"), and the subclass *B* calls
`super.clone()`, then it is likely that *B*'s
`clone()` method will return an object of type *A*, which
violates the standard contract for `clone()`.

If all `clone()` methods call `super.clone()`, then
they are guaranteed to use `Object.clone()`, which always returns an
object of the correct type.

## FB.CN_IMPLEMENTS_CLONE_BUT_NOT_CLONEABLE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | CN: Bad implementation of cloneable idiom | [CWE-580](http://cwe.mitre.org/data/definitions/580.html) |

This class defines a `clone()` method but the class doesn't implement
`Cloneable`. There are some situations in which this is OK (e.g.,
you want to control how subclasses can clone themselves), but just make sure that
this is what you intended.

## FB.CO_ABSTRACT_SELF

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Co: Problems with implementation of `compareTo()` |

This class defines a covariant version of `compareTo()`. To correctly
override the `compareTo()` method in the `Comparable`
interface, the parameter of `compareTo()` must have type
`java.lang.Object`.

## FB.CO_COMPARETO_INCORRECT_FLOATING

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Co: Problems with implementation of `compareTo()` |

This method compares double or float values using pattern like this: `val1
> val2 ? 1 : val1 < val2 ? -1 : 0`. This pattern works incorrectly
for `-0.0` and `NaN` values which may result in
incorrect sorting result or broken collection (if compared values are used as keys).
Consider using `Double.compare` or `Float.compare`
static methods which handle all the special cases correctly.

## FB.CO_COMPARETO_RESULTS_MIN_VALUE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Co: Problems with implementation of `compareTo()` |

In some situation, this `compareTo` or
compare method returns the constant `Integer.MIN_VALUE`, which is an
exceptionally bad practice. The only thing that matters about the return value of
`compareTo` is the sign of the result. But people will sometimes
negate the return value of `compareTo`, expecting that this will
negate the sign of the result. And it will, except in the case where the value
returned is `Integer.MIN_VALUE`. So just return `-1`
rather than `Integer.MIN_VALUE`.

## FB.CO_SELF_NO_OBJECT

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Co: Problems with implementation of `compareTo()` |

This class defines a covariant version of `compareTo()`. To correctly
override the `compareTo()` method in the `Comparable`
interface, the parameter of `compareTo()` must have type
`java.lang.Object`.

## FB.CT_CONSTRUCTOR_THROW

|  |  |
| --- | --- |
| SpotBugs: Bad practice | CT: Constructor throws |

Classes that throw exceptions in their constructors are vulnerable to Finalizer attacks.

## FB.DB_DUPLICATE_BRANCHES

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | DB: Duplicate Branches |

This method uses the same code to implement two branches of a conditional branch.
Check to ensure that this isn't a coding mistake.

## FB.DB_DUPLICATE_SWITCH_CLAUSES

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | DB: Duplicate Branches |

This method uses the same code to implement two clauses of a switch statement. This
could be a case of duplicate code, but it might also indicate a coding mistake.

## FB.DCN_NULLPOINTER_EXCEPTION

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | DCN: `NullPointerException` caught |

According to SEI Cert rule [ERR08-J](https://wiki.sei.cmu.edu/confluence/display/java/ERR08-J.+Do+not+catch+NullPointerException+or+any+of+its+ancestors),
`NullPointerException` should not be caught. Handling
`NullPointerException` is considered an inferior alternative to
`null`-checking.

This non-compliant code catches a `NullPointerException` to see if an
incoming parameter is `null`:

```
boolean hasSpace(String m) {
  try {
    String ms[] = m.split(" ");
    return names.length != 1;
  } catch (NullPointerException e) {
    return false;
  }
}
```

A compliant solution would use a `null`-check as in the following
example:

```
boolean hasSpace(String m) {
    if (m == null) return false;
    String ms[] = m.split(" ");
    return names.length != 1;
}
```

## FB.DC_DOUBLECHECK

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | DC: Double check pattern | [CWE-609](http://cwe.mitre.org/data/definitions/609.html) |

This method may contain an instance of double-checked locking. This idiom is not
correct according to the semantics of the Java memory model. For more information,
see the web page <http://www.cs.umd.edu/~pugh/java/memoryModel/DoubleCheckedLocking.html>.

## FB.DC_PARTIALLY_CONSTRUCTED

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | DC: Double check pattern | [CWE-609](http://cwe.mitre.org/data/definitions/609.html) |

Looks like this method uses lazy field initialization with double-checked locking.
While the field is correctly declared as volatile, it's possible that the internal
structure of the object is changed after the field assignment, thus another thread
may see the partially initialized object.

To fix this problem consider storing the object into the local variable first and
save it to the volatile field only after it's fully constructed.

## FB.DE_MIGHT_DROP

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | DE: Dropped or ignored exception | [CWE-391](http://cwe.mitre.org/data/definitions/391.html) |

This method might drop an exception. In general, exceptions should be handled or
reported in some way, or they should be thrown out of the method.

## FB.DE_MIGHT_IGNORE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | DE: Dropped or ignored exception | [CWE-391](http://cwe.mitre.org/data/definitions/391.html) |

This method might ignore an exception. In general, exceptions should be handled or
reported in some way, or they should be thrown out of the method.

## FB.DLS_DEAD_LOCAL_INCREMENT_IN_RETURN

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DLS: Dead local store | [CWE-563](http://cwe.mitre.org/data/definitions/563.html) |

This statement has a return such as `return x++;`. A postfix
increment/decrement does not impact the value of the expression, so this
increment/decrement has no effect. Please verify that this statement does the right
thing.

## FB.DLS_DEAD_LOCAL_STORE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | DLS: Dead local store | [CWE-563](http://cwe.mitre.org/data/definitions/563.html) |

This instruction assigns a value to a local variable, but the value is not read or
used in any subsequent instruction. Often, this indicates an error, because the
value computed is never used.

Note that Sun's javac compiler often generates dead stores for final local variables.
Because SpotBugs is a bytecode-based tool, there is no easy way to eliminate these
false positives.

## FB.DLS_DEAD_LOCAL_STORE_IN_RETURN

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | DLS: Dead local store | [CWE-563](http://cwe.mitre.org/data/definitions/563.html) |

This statement assigns to a local variable in a return statement. This assignment has
effect. Please verify that this statement does the right thing.

## FB.DLS_DEAD_LOCAL_STORE_OF_NULL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | DLS: Dead local store | [CWE-563](http://cwe.mitre.org/data/definitions/563.html) |

The code stores null into a local variable, and the stored value is not read. This
store may have been introduced to assist the garbage collector, but as of Java SE
6.0, this is no longer needed or useful.

## FB.DLS_DEAD_LOCAL_STORE_SHADOWS_FIELD

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | DLS: Dead local store | [CWE-563](http://cwe.mitre.org/data/definitions/563.html) |

This instruction assigns a value to a local variable, but the value is not read or
used in any subsequent instruction. Often, this indicates an error, because the
value computed is never used. There is a field with the same name as the local
variable. Did you mean to assign to that variable instead?

## FB.DLS_DEAD_STORE_OF_CLASS_LITERAL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DLS: Dead local store | [CWE-563](http://cwe.mitre.org/data/definitions/563.html) |

This instruction assigns a class literal to a variable and then never uses it. [The behavior of this differs in Java 1.4 and in Java 5.](http://www.oracle.com/technetwork/java/javase/compatibility-137462.html#literal)
In Java 1.4 and earlier, a reference to `Foo.class` would force the
static initializer for `Foo` to be executed, if it has not been
executed already. In Java 5 and later, it does not.

See Sun's [article on Java SE compatibility](http://www.oracle.com/technetwork/java/javase/compatibility-137462.html#literal) for more details and
examples, and suggestions on how to force class initialization in Java 5.

## FB.DLS_OVERWRITTEN_INCREMENT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DLS: Dead local store | [CWE-563](http://cwe.mitre.org/data/definitions/563.html) |

The code performs an increment operation (e.g., `i++`) and then
immediately overwrites it. For example, `i = i++` immediately
overwrites the incremented value with the original value.

## FB.DL_SYNCHRONIZATION_ON_BOOLEAN

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | DL: Unintended contention or possible deadlock due to locking on shared objects |

The code synchronizes on a boxed primitive constant, such as a Boolean.

```
private static Boolean inited = Boolean.FALSE;
...
synchronized(inited) {
    if (!inited) {
        init();
        inited = Boolean.TRUE;
    }
}
...
```

Since there normally exist only two Boolean objects, this code could be synchronizing
on the same object as other, unrelated code, leading to unresponsiveness and
possible deadlock.

See CERT [LCK01-J. Do not synchronize on objects that may be
reused](https://wiki.sei.cmu.edu/confluence/display/java/LCK01-J.+Do+not+synchronize+on+objects+that+may+be+reused) for more information.

## FB.DL_SYNCHRONIZATION_ON_BOXED_PRIMITIVE

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | DL: Unintended contention or possible deadlock due to locking on shared objects |

The code synchronizes on a boxed primitive constant, such as an Integer.

```
private static Integer count = 0;
...
synchronized(count) {
    count++;
}
...
```

Since Integer objects can be cached and shared, this code could be synchronizing on
the same object as other, unrelated code, leading to unresponsiveness and possible
deadlock.

See CERT [LCK01-J. Do not synchronize on objects that may be
reused](https://wiki.sei.cmu.edu/confluence/display/java/LCK01-J.+Do+not+synchronize+on+objects+that+may+be+reused) for more information.

## FB.DL_SYNCHRONIZATION_ON_INTERNED_STRING

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | DL: Unintended contention or possible deadlock due to locking on shared objects |

The code synchronizes on interned `String`.

## FB.DL_SYNCHRONIZATION_ON_SHARED_CONSTANT

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | DL: Unintended contention or possible deadlock due to locking on shared objects |

The code synchronizes on interned `String`.

```
private static String LOCK = "LOCK";
...
synchronized(LOCK) {
    ...
}
...
```

Constant Strings are interned and shared across all other classes loaded by the JVM.
Thus, this code is locking on something that other code might also be locking. This
could result in very strange and hard to diagnose blocking and deadlock behavior.

See CERT [LCK01-J. Do not synchronize on objects that may be
reused](https://wiki.sei.cmu.edu/confluence/display/java/LCK01-J.+Do+not+synchronize+on+objects+that+may+be+reused) for more information.

## FB.DL_SYNCHRONIZATION_ON_UNSHARED_BOXED_PRIMITIVE

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | DL: Unintended contention or possible deadlock due to locking on shared objects |

The code synchronizes on an apparently unshared boxed primitive, such as an
Integer.

```
private static final Integer fileLock = new Integer(1);
...
synchronized(fileLock) {
    .. do something ..
}
...
```

It would be much better, in this code, to redeclare `fileLock` as

```
private static final Object fileLock = new Object();
```

The existing code might be OK, but it is confusing and a future refactoring, such as
the "Remove Boxing" refactoring in IntelliJ, might replace this with the use of an
interned Integer object shared throughout the JVM, leading to very confusing
behavior and potential deadlock.

## FB.DMI_ANNOTATION_IS_NOT_VISIBLE_TO_REFLECTION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Dm: Dubious method used | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

Unless an annotation has itself been annotated with
`@Retention(RetentionPolicy.RUNTIME)`, the annotation can't be
observed using reflection (e.g., by using the `isAnnotationPresent`
method).

## FB.DMI_ARGUMENTS_WRONG_ORDER

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The arguments to this method call seem to be in the wrong order. For example, a call

```
Preconditions.checkNotNull("message", message)
```

has reserved
arguments: the value to be checked is the first argument.

## FB.DMI_BAD_MONTH

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code passes a constant month value outside the expected range of 0..11 to a
method.

## FB.DMI_BIGDECIMAL_CONSTRUCTED_FROM_DOUBLE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code creates a `BigDecimal` from a double value that doesn't
translate well to a decimal number. For example, one might assume that writing
`new BigDecimal(0.1)` in Java creates a
`BigDecimal` which is exactly equal to 0.1 (an unscaled value of
1, with a scale of 1), but it is actually equal to
0.1000000000000000055511151231257827021181583404541015625. You probably want to use
the `BigDecimal.valueOf(double d)` method, which uses the String
representation of the double to create the `BigDecimal` (e.g.,
`BigDecimal.valueOf(0.1)` gives 0.1).

## FB.DMI_BLOCKING_METHODS_ON_URL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Performance | Dm: Dubious method used | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The equals and `hashCode` method of URL perform domain name
resolution, this can result in a big performance hit. See <http://michaelscharf.blogspot.com/2006/11/javaneturlequals-and-hashcode-make.html>
for more information. Consider using `java.net.URI` instead.

## FB.DMI_CALLING_NEXT_FROM_HASNEXT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The `hasNext()` method invokes the `next()` method.
This is almost certainly wrong, since the `hasNext()` method is not
supposed to change the state of the iterator, and the next method is supposed to
change the state of the iterator.

## FB.DMI_COLLECTIONS_SHOULD_NOT_CONTAIN_THEMSELVES

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This call to a generic collection's method would only make sense if a collection
contained itself (e.g., if `s.contains(s)` were true). This is
unlikely to be true and would cause problems if it were true (such as the
computation of the hash code resulting in infinite recursion). It is likely that the
wrong value is being passed as a parameter.

## FB.DMI_COLLECTION_OF_URLS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Performance | Dm: Dubious method used | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This method or field is or uses a Map or Set of URLs. Since both the equals and
`hashCode` method of URL perform domain name resolution, this can
result in a big performance hit. See <http://michaelscharf.blogspot.com/2006/11/javaneturlequals-and-hashcode-make.html>
for more information. Consider using `java.net.URI` instead.

## FB.DMI_CONSTANT_DB_PASSWORD

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | Dm: Dubious method used | [CWE-259](http://cwe.mitre.org/data/definitions/259.html) |

This code creates a database connect using a hardcoded, constant password. Anyone
with access to either the source code or the compiled code can easily learn the
password.

## FB.DMI_DOH

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This partial method invocation doesn't make sense, for reasons that should be
apparent from inspection.

## FB.DMI_EMPTY_DB_PASSWORD

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | Dm: Dubious method used | [CWE-259](http://cwe.mitre.org/data/definitions/259.html) |

This code creates a database connect using a blank or empty password. This indicates
that the database is not protected by a password.

## FB.DMI_ENTRY_SETS_MAY_REUSE_ENTRY_OBJECTS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The `entrySet()` method is allowed to return a view of the underlying
Map in which a single Entry object is reused and returned during the iteration. As
of Java 1.6, both `IdentityHashMap` and `EnumMap` did
so. When iterating through such a Map, the Entry value is only valid until you
advance to the next iteration. If, for example, you try to pass such an
`entrySet` to an `addAll` method, things will go
badly wrong.

## FB.DMI_FUTILE_ATTEMPT_TO_CHANGE_MAXPOOL_​SIZE_​OF_​SCHEDULED_​THREAD_​POOL_​EXECUTOR

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Dm: Dubious method used | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

([Javadoc](http://docs.oracle.com/javase/6/docs/api/java/util/concurrent/ScheduledThreadPoolExecutor.html)) While
`ScheduledThreadPoolExecutor` inherits from
`ThreadPoolExecutor`, a few of the inherited tuning methods are
not useful for it. In particular, because it acts as a fixed-sized pool using
`corePoolSize` threads and an unbounded queue, adjustments to
`maximumPoolSize` have no useful effect.

## FB.DMI_HARDCODED_ABSOLUTE_FILENAME

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code constructs a File object using a hard coded to an absolute pathname (e.g.,
`new
File("/home/dannyc/workspace/j2ee/src/share/com/sun/enterprise/deployment");`

## FB.DMI_INVOKING_HASHCODE_ON_ARRAY

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The code invokes `hashCode` on an array. Calling
`hashCode` on an array returns the same value as
`System.identityHashCode`, and ignores the contents and length of
the array. If you need a `hashCode` that depends on the contents of
an array `a`, use `java.util.Arrays.hashCode(a)`.

## FB.DMI_INVOKING_TOSTRING_ON_ANONYMOUS_ARRAY

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | USELESS_STRING: Useless/non-informative string generated | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The code invokes `toString` on an (anonymous) array. Calling
`toString` on an array generates a fairly useless result such as
`[C@16f0472`. Consider using `Arrays.toString` to
convert the array into a readable `String` that gives the contents of
the array. See Programming Puzzlers, chapter 3, puzzle 12.

## FB.DMI_INVOKING_TOSTRING_ON_ARRAY

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | USELESS_STRING: Useless/non-informative string generated | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The code invokes `toString` on an array, which will generate a fairly
useless result such as `[C@16f0472`. Consider using
`Arrays.toString` to convert the array into a readable
`String` that gives the contents of the array. See Programming
Puzzlers, chapter 3, puzzle 12.

## FB.DMI_LONG_BITS_TO_DOUBLE_INVOKED_ON_INT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The `Double.longBitsToDouble` method is invoked, but a 32 bit int
value is passed as an argument. This almost certainly is not intended and is
unlikely to give the intended result.

## FB.DMI_NONSERIALIZABLE_OBJECT_WRITTEN

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code seems to be passing a non-serializable object to the
`ObjectOutput.writeObject` method. If the object is, indeed,
non-serializable, an error will result.

## FB.DMI_RANDOM_USED_ONLY_ONCE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code creates a `java.util.Random` object, uses it to generate one
random number, and then discards the Random object. This produces mediocre quality
random numbers and is inefficient. If possible, rewrite the code so that the Random
object is created once and saved, and each time a new random number is required
invoke a method on the existing Random object to obtain it.

If it is important that the generated Random numbers not be guessable, you
*must* not create a new Random for each random number; the values are too
easily guessable. You should strongly consider using a
`java.security.SecureRandom` instead (and avoid allocating a new
`SecureRandom` for each random number needed).

## FB.DMI_SCHEDULED_THREAD_POOL_EXECUTOR_WITH_​ZERO_​CORE_​THREADS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Dm: Dubious method used | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

([Javadoc](http://docs.oracle.com/javase/6/docs/api/java/util/concurrent/ScheduledThreadPoolExecutor.html#ScheduledThreadPoolExecutor%28int%29)) A `ScheduledThreadPoolExecutor`
with zero core threads will never execute anything; changes to the max pool size are
ignored.

## FB.DMI_THREAD_PASSED_WHERE_RUNNABLE_EXPECTED

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | Dm: Dubious method used | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

A Thread object is passed as a parameter to a method where a
`Runnable` is expected. This is rather unusual, and may indicate
a logic error or cause unexpected behavior.

## FB.DMI_UNSUPPORTED_METHOD

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | Dm: Dubious method used | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

All targets of this method invocation throw an
`UnsupportedOperationException`.

## FB.DMI_USELESS_SUBSTRING

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code invokes `substring(0)` on a String, which returns the
original value.

## FB.DMI_USING_REMOVEALL_TO_CLEAR_COLLECTION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

If you want to remove all elements from a collection `c`, use
`c.clear`, not `c.removeAll(c)`. Calling
`c.removeAll(c)` to clear a collection is less clear, susceptible
to errors from typos, less efficient and for some collections, might throw a
`ConcurrentModificationException`.

## FB.DMI_VACUOUS_CALL_TO_EASYMOCK_METHOD

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Dm: Dubious method used | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This call doesn't pass any objects to the `EasyMock` method, so the
call doesn't do anything.

## FB.DMI_VACUOUS_SELF_COLLECTION_CALL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | DMI: Dubious method invocation | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This call doesn't make sense. For any collection `c`, calling
`c.containsAll(c)` should always be true, and
`c.retainAll(c)` should have no effect.

## FB.DM_BOOLEAN_CTOR

|  |  |
| --- | --- |
| SpotBugs: Performance | Dm: Dubious method used |

Creating new instances of `java.lang.Boolean` wastes memory, since
`Boolean` objects are immutable and there are only two useful
values of this type. Use the `Boolean.valueOf()` method (or Java 1.5
autoboxing) to create `Boolean` objects instead.

## FB.DM_BOXED_PRIMITIVE_FOR_COMPARE

|  |  |
| --- | --- |
| SpotBugs: Performance | Bx: Questionable Boxing of primitive value |

A boxed primitive is created just to call `compareTo` method. It's
more efficient to use static compare method (for double and float since Java 1.4,
for other primitive types since Java 1.7) which works on primitives directly.

## FB.DM_BOXED_PRIMITIVE_FOR_PARSING

|  |  |
| --- | --- |
| SpotBugs: Performance | Bx: Questionable Boxing of primitive value |

A boxed primitive is created from a String, just to extract the unboxed primitive
value. It is more efficient to just call the static `parseXXX`
method.

## FB.DM_BOXED_PRIMITIVE_TOSTRING

|  |  |
| --- | --- |
| SpotBugs: Performance | Bx: Questionable Boxing of primitive value |

A boxed primitive is allocated just to call `toString()`. It is more
effective to just use the static form of `toString` which takes the
primitive value. So,

|  |  |
| --- | --- |
| Replace... | With this... |
| new Integer(1).toString() | Integer.toString(1) |
| new Long(1).toString() | Long.toString(1) |
| new Float(1.0).toString() | Float.toString(1.0) |
| new Double(1.0).toString() | Double.toString(1.0) |
| new Byte(1).toString() | Byte.toString(1) |
| new Short(1).toString() | Short.toString(1) |
| new Boolean(true).toString() | Boolean.toString(true) |

## FB.DM_CONVERT_CASE

|  |  |
| --- | --- |
| SpotBugs: Internationalization | Dm: Dubious method used |

A String is being converted to upper or lowercase, using the platform's default
encoding. This may result in improper conversions when used with international
characters. Use the

- `String.toUpperCase( Locale l )`
- `String.toLowerCase( Locale l )`

versions instead.

## FB.DM_DEFAULT_ENCODING

|  |  |
| --- | --- |
| SpotBugs: Internationalization | Dm: Dubious method used |

Found a call to a method which will perform a byte to `String` (or
`String` to `byte`) conversion, and will assume
that the default platform encoding is suitable. This will cause the application
behaviour to vary between platforms. Use an alternative API and specify a charset
name or `Charset` object explicitly.

## FB.DM_EXIT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | Dm: Dubious method used | [CWE-382](http://cwe.mitre.org/data/definitions/382.html) |

Invoking `System.exit` shuts down the entire Java virtual machine.
This should only been done when it is appropriate. Such calls make it hard or
impossible for your code to be invoked by other code. Consider throwing a
`RuntimeException` instead.

## FB.DM_FP_NUMBER_CTOR

|  |  |
| --- | --- |
| SpotBugs: Performance | Bx: Questionable Boxing of primitive value |

Using `new Double(double)` is guaranteed to always result in a new
object whereas `Double.valueOf(double)` allows caching of values to
be done by the compiler, class library, or JVM. Using of cached values avoids object
allocation and the code will be faster.

Unless the class must be compatible with JVMs predating Java 1.5, use either
autoboxing or the `valueOf()` method when creating instances of
`Double` and `Float`.

## FB.DM_GC

|  |  |
| --- | --- |
| SpotBugs: Performance | Dm: Dubious method used |

Code explicitly invokes garbage collection. Except for specific use in benchmarking,
this is very dubious.

In the past, situations where people have explicitly invoked the garbage collector in
routines such as close or finalize methods has led to huge performance black holes.
Garbage collection can be expensive. Any situation that forces hundreds or thousands
of garbage collections will bring the machine to a crawl.

## FB.DM_INVALID_MIN_MAX

|  |  |
| --- | --- |
| SpotBugs: Correctness | Dm: Dubious method used |

This code tries to limit the value bounds using the construct like
`Math.min(0, Math.max(100, value))`. However, the order of the
constants is incorrect: it should be `Math.min(100, Math.max(0,
value))`. As the result this code always produces the same result (or
`NaN` if the value is `NaN`).

## FB.DM_MONITOR_WAIT_ON_CONDITION

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | Dm: Dubious method used |

This method calls `wait()` on a
`java.util.concurrent.locks.Condition` object. Waiting for a
`Condition` should be done using one of the
`await()` methods defined by the `Condition`
interface.

## FB.DM_NEW_FOR_GETCLASS

|  |  |
| --- | --- |
| SpotBugs: Performance | Dm: Dubious method used |

This method allocates an object just to call `getClass()` on it, in
order to retrieve the Class object for it. It is simpler to just access the
`.class` property of the class.

## FB.DM_NEXTINT_VIA_NEXTDOUBLE

|  |  |
| --- | --- |
| SpotBugs: Performance | Dm: Dubious method used |

If `r` is a `java.util.Random`, you can generate a
random number from `0` to `n-1` using
`r.nextInt(n)`, rather than using `(int)(r.nextDouble() *
n)`.

The argument to `nextInt` must be positive. If, for example, you want
to generate a random value from -99 to 0, use `-r.nextInt(100)`.

## FB.DM_NUMBER_CTOR

|  |  |
| --- | --- |
| SpotBugs: Performance | Bx: Questionable Boxing of primitive value |

Using `new Integer(int)` is guaranteed to always result in a new
object whereas `Integer.valueOf(int)` allows caching of values to be
done by the compiler, class library, or JVM. Using of cached values avoids object
allocation and the code will be faster.

Values between -128 and 127 are guaranteed to have corresponding cached instances and
using `valueOf` is approximately 3.5 times faster than using
constructor. For values outside the constant range the performance of both styles is
the same.

Unless the class must be compatible with JVMs predating Java 1.5, use either
autoboxing or the `valueOf()` method when creating instances of
`Long`, `Integer`, `Short`,
`Character`, and `Byte`.

## FB.DM_RUN_FINALIZERS_ON_EXIT

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Dm: Dubious method used |

*Never call System.runFinalizersOnExit or Runtime.runFinalizersOnExit for any
reason: they are among the most dangerous methods in the Java libraries.* --
Joshua Bloch

## FB.DM_STRING_CTOR

|  |  |
| --- | --- |
| SpotBugs: Performance | Dm: Dubious method used |

Using the `java.lang.String(String)` constructor wastes memory because
the object so constructed will be functionally indistinguishable from the
`String` passed as a parameter. Just use the argument
`String` directly.

## FB.DM_STRING_TOSTRING

|  |  |
| --- | --- |
| SpotBugs: Performance | Dm: Dubious method used |

Calling `String.toString()` is just a redundant operation. Just use
the `String`.

## FB.DM_STRING_VOID_CTOR

|  |  |
| --- | --- |
| SpotBugs: Performance | Dm: Dubious method used |

Creating a new `java.lang.String` object using the no-argument
constructor wastes memory because the object so created will be functionally
indistinguishable from the empty string constant `""`. Java
guarantees that identical string constants will be represented by the same
`String` object. Therefore, you should just use the empty string
constant directly.

## FB.DM_USELESS_THREAD

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | Dm: Dubious method used |

This method creates a thread without specifying a run method either by deriving from
the `Thread` class, or by passing a `Runnable` object.
This thread, then, does nothing but waste time.

## FB.DP_CREATE_CLASSLOADER_INSIDE_DO_PRIVILEDGED

|  |  |
| --- | --- |
| SpotBugs: Bad practice | DP: Use `doPrivileged` |

This code creates a classloader, which requires a security manager. If this code will
be granted security permissions, but might be invoked by code that does not have
security permissions, then the classloader creation needs to occur inside a
`doPrivileged` block.

## FB.DP_CREATE_CLASSLOADER_INSIDE_DO_PRIVILEGED

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | DP: Use `doPrivileged` |

This code creates a classloader, which needs permission if a security manage is
installed. If this code might be invoked by code that does not have security
permissions, then the classloader creation needs to occur inside a
`doPrivileged` block.

## FB.DP_DO_INSIDE_DO_PRIVILEDGED

|  |  |
| --- | --- |
| SpotBugs: Bad practice | DP: Use `doPrivileged` |

This code invokes a method that requires a security permission check. If this code
will be granted security permissions, but might be invoked by code that does not
have security permissions, then the invocation needs to occur inside a
`doPrivileged` block.

## FB.DP_DO_INSIDE_DO_PRIVILEGED

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | DP: Use `doPrivileged` |

This code invokes a method that requires a security permission check. If this code
will be granted security permissions, but might be invoked by code that does not
have security permissions, then the invocation needs to occur inside a
`doPrivileged` block.

## FB.EC_ARRAY_AND_NONARRAY

|  |  |
| --- | --- |
| SpotBugs: Correctness | EC: Comparing incompatible types for equality |

This method invokes the `.equals(Object o)` to compare an array and a
reference that doesn't seem to be an array. If things being compared are of
different types, they are guaranteed to be unequal and the comparison is almost
certainly an error. Even if they are both arrays, the equals method on arrays only
determines of the two arrays are the same object. To compare the contents of the
arrays, use `java.util.Arrays.equals(Object[], Object[])`.

## FB.EC_BAD_ARRAY_COMPARE

|  |  |
| --- | --- |
| SpotBugs: Correctness | EC: Comparing incompatible types for equality |

This method invokes the `.equals(Object o)` method on an array. Since
arrays do not override the equals method of Object, calling equals on an array is
the same as comparing their addresses. To compare the contents of the arrays, use
`java.util.Arrays.equals(Object[], Object[])`. To compare the
addresses of the arrays, it would be less confusing to explicitly check pointer
equality using `==`.

## FB.EC_INCOMPATIBLE_ARRAY_COMPARE

|  |  |
| --- | --- |
| SpotBugs: Correctness | EC: Comparing incompatible types for equality |

This method invokes the `.equals(Object o)` to compare two arrays, but
the arrays of of incompatible types (e.g., `String[]` and
`StringBuffer[]`, or `String[]` and
`int[]`). They will never be equal. In addition, when
`equals(...)` is used to compare arrays it only checks to see if
they are the same array, and ignores the contents of the arrays.

## FB.EC_NULL_ARG

|  |  |
| --- | --- |
| SpotBugs: Correctness | EC: Comparing incompatible types for equality |

This method calls `equals(Object)`, passing a null value as the
argument. According to the contract of the `equals()` method, this
call should always return `false`.

## FB.EC_UNRELATED_CLASS_AND_INTERFACE

|  |  |
| --- | --- |
| SpotBugs: Correctness | EC: Comparing incompatible types for equality |

This method calls `equals(Object)` on two references, one of which is
a class and the other an interface, where neither the class nor any of its
non-abstract subclasses implement the interface. Therefore, the objects being
compared are unlikely to be members of the same class at runtime (unless some
application classes were not analyzed, or dynamic class loading can occur at
runtime). According to the contract of `equals()`, objects of
different classes should always compare as unequal; therefore, according to the
contract defined by `java.lang.Object.equals(Object)`, the result of
this comparison will always be false at runtime.

## FB.EC_UNRELATED_INTERFACES

|  |  |
| --- | --- |
| SpotBugs: Correctness | EC: Comparing incompatible types for equality |

This method calls `equals(Object)` on two references of unrelated
interface types, where neither is a subtype of the other, and there are no known
non-abstract classes which implement both interfaces. Therefore, the objects being
compared are unlikely to be members of the same class at runtime (unless some
application classes were not analyzed, or dynamic class loading can occur at
runtime). According to the contract of `equals()`, objects of
different classes should always compare as unequal; therefore, according to the
contract defined by `java.lang.Object.equals(Object)`, the result of
this comparison will always be false at runtime.

## FB.EC_UNRELATED_TYPES

|  |  |
| --- | --- |
| SpotBugs: Correctness | EC: Comparing incompatible types for equality |

This method calls `equals(Object)` on two references of different
class types and analysis suggests they will be to objects of different classes at
runtime. Further, examination of the equals methods that would be invoked suggest
that either this call will always return false, or else the equals method is not be
symmetric (which is a property required by the contract for equals in class
`Object`).

## FB.EC_UNRELATED_TYPES_USING_POINTER_EQUALITY

|  |  |
| --- | --- |
| SpotBugs: Correctness | EC: Comparing incompatible types for equality |

This method uses using pointer equality to compare two references that seem to be of
different types. The result of this comparison will always be false at runtime.

## FB.EI_EXPOSE_BUF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | EI: Exposes internal representation | [CWE-374](http://cwe.mitre.org/data/definitions/374.html) |

Returning a reference to a buffer (`java.nio.*Buffer`) which wraps an array
stored in one of the object's fields exposes the internal representation of the
array elements because the buffer only stores a reference to the array instead of
copying its content. Similarly, returning a shallow-copy of such a buffer (using its
`duplicate()` method) stored in one of the object's fields also
exposes the internal representation of the buffer. If instances are accessed by
untrusted code, and unchecked changes to the array would compromise security or
other important properties, you will need to do something different. Returning a
read-only buffer (using its `asReadOnly()` method) or copying the
array to a new buffer (using its `put()` method) is a better approach
in many situations.

## FB.EI_EXPOSE_BUF2

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | EI2: Storing reference to mutable object | [CWE-374](http://cwe.mitre.org/data/definitions/374.html) |

This code creates a buffer which stores a reference to an external array or the array of an
external buffer into the internal representation of the object. If instances are
accessed by untrusted code, and unchecked changes to the array would compromise
security or other important properties, you will need to do something different.
Storing a copy of the array is a better approach in many situations.

## FB.EI_EXPOSE_REP

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | EI: Exposes internal representation | [CWE-374](http://cwe.mitre.org/data/definitions/374.html) |

Returning a reference to a mutable object value stored in one of the object's fields
exposes the internal representation of the object. If instances are accessed by
untrusted code, and unchecked changes to the mutable object would compromise
security or other important properties, you will need to do something different.
Returning a new copy of the object is better approach in many situations.

## FB.EI_EXPOSE_REP2

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | EI2: Storing reference to mutable object | [CWE-374](http://cwe.mitre.org/data/definitions/374.html) |

This code stores a reference to an externally mutable object into the internal
representation of the object. If instances are accessed by untrusted code, and
unchecked changes to the mutable object would compromise security or other important
properties, you will need to do something different. Storing a copy of the object is
better approach in many situations.

## FB.EI_EXPOSE_STATIC_BUF2

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

This code creates a buffer which stores a reference to an external array or the array
of an external buffer into a static field. If unchecked changes to the array would
compromise security or other important properties, you will need to do something
different. Storing a copy of the array is a better approach in many situations.

## FB.EI_EXPOSE_STATIC_REP2

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

This code stores a reference to an externally mutable object into a static field. If
unchecked changes to the mutable object would compromise security or other important
properties, you will need to do something different. Storing a copy of the object is
better approach in many situations.

## FB.ENV_USE_PROPERTY_INSTEAD_OF_ENV

|  |  |
| --- | --- |
| SpotBugs: Bad practice | ENV: Environment variable is used instead of the corresponding Java property |

Environment variables are not portable, the variable name itself (not only the value) may be different depending on the running OS.

## FB.EOS_BAD_END_OF_STREAM_CHECK

|  |  |
| --- | --- |
| SpotBugs: Correctness | EOS: Bad End of Stream check |

The method `java.io.FileInputStream.read()` returns an
`int`. If this `int` is converted to a
`byte` then `-1` (which indicates an
`EOF`) and the byte `0xFF` become
indistinguishable, this comparing the (converted) result to `-1`
causes the read (probably in a loop) to end prematurely if the character
`0xFF` is met. Similarly, the method
`java.io.FileReader.read()` also returns an `int`.
If it is converted to a `char` then `-1` becomes
`0xFFFF` which is `Character.MAX_VALUE`. Comparing
the result to `-1` is pointless, since characters are unsigned in
Java. If the checking for `EOF` is the condition of a loop then this
loop is infinite.

See SEI CERT rule [FIO08-J. Distinguish between characters or bytes
read from a stream and -1](https://wiki.sei.cmu.edu/confluence/display/java/FIO08-J.+Distinguish+between+characters+or+bytes+read+from+a+stream+and+-1).

## FB.EQ_ABSTRACT_SELF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | Eq: Problems with implementation of equals() | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines a covariant version of `equals()`. To correctly
override the `equals()` method in `java.lang.Object`,
the parameter of `equals()` must have type
`java.lang.Object`.

## FB.EQ_ALWAYS_FALSE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines an `equals` method that always returns
`false`. This means that an object is not equal to itself, and it
is impossible to create useful `Maps` or `Sets` of
this class. More fundamentally, it means that `equals` is not
reflexive, one of the requirements of the `equals` method.

The likely intended semantics are object identity: that an object is equal to itself.
This is the behavior inherited from class `Object`. If you need to
override an equals inherited from a different superclass, you can use:

```
public boolean equals(Object o) {
    return this == o;
}
```

## FB.EQ_ALWAYS_TRUE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines an `equals` method that always returns
`true`. This is imaginative, but not very smart. Plus, it means
that the `equals` method is not symmetric.

## FB.EQ_CHECK_FOR_OPERAND_NOT_COMPATIBLE_WITH_THIS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This `equals` method is checking to see if the argument is some
incompatible type (i.e., a class that is neither a supertype nor subtype of the
class that defines the `equals` method). For example, the
`Foo` class might have an equals method that looks like:

```
public boolean equals(Object o) {
    if (o instanceof Foo)
        return name.equals(((Foo)o).name);
    else if (o instanceof String)
        return name.equals(o);
    else return false;
}
```

This is considered bad practice, as it makes it very hard to implement an
`equals` method that is symmetric and transitive. Without those
properties, very unexpected behaviors are possible.

## FB.EQ_COMPARETO_USE_OBJECT_EQUALS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines a `compareTo(...)` method but inherits its
`equals()` method from `java.lang.Object`.
Generally, the value of `compareTo` should return zero if and only if
`equals` returns `true`. If this is violated,
weird and unpredictable failures will occur in classes such as
`PriorityQueue`. In Java 5 the
`PriorityQueue.remove` method uses the `compareTo`
method, while in Java 6 it uses the `equals` method.

From the JavaDoc for the `compareTo` method in the
`Comparable` interface:

Note: It is strongly recommended, but not strictly required that
`(x.compareTo(y)==0) == (x.equals(y))`. Generally speaking, any
class that implements the `Comparable` interface and violates this
condition should clearly indicate this fact. The recommended language is "Note: this
class has a natural ordering that is inconsistent with equals."

## FB.EQ_COMPARING_CLASS_NAMES

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This method checks to see if two objects are the same class by checking to see if the
names of their classes are equal. You can have different classes with the same name
if they are loaded by different class loaders. Just check to see if the class
objects are the same.

## FB.EQ_DOESNT_OVERRIDE_EQUALS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class extends a class that defines an `equals` method and adds
fields, but doesn't define an `equals` method itself. Thus, equality
on instances of this class will ignore the identity of the subclass and the added
fields. Be sure this is what is intended, and that you don't need to override the
`equals` method. Even if you don't need to override the
`equals` method, consider overriding it anyway to document the
fact that the `equals` method for the subclass just return the result
of invoking `super.equals(o)`.

## FB.EQ_DONT_DEFINE_EQUALS_FOR_ENUM

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines an enumeration, and equality on enumerations are defined using
object identity. Defining a covariant equals method for an enumeration value is
exceptionally bad practice, since it would likely result in having two different
enumeration values that compare as equals using the covariant `enum`
method, and as not equal when compared normally. Don't do it.

## FB.EQ_GETCLASS_AND_CLASS_CONSTANT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class has an `equals` method that will be broken if it is
inherited by subclasses. It compares a class literal with the class of the argument
(e.g., in class `Foo` it might check if `Foo.class ==
o.getClass()`). It is better to check if `this.getClass() ==
o.getClass()`.

## FB.EQ_OTHER_NO_OBJECT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines an `equals()` method, that doesn't override the
normal `equals(Object)` method defined in the base
`java.lang.Object` class. Instead, it inherits an
`equals(Object)` method from a superclass. The class should
probably define a `boolean equals(Object)` method.

## FB.EQ_OTHER_USE_OBJECT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines an `equals()` method, that doesn't override the
normal `equals(Object)` method defined in the base
`java.lang.Object` class. The class should probably define a
`boolean equals(Object)` method.

## FB.EQ_OVERRIDING_EQUALS_NOT_SYMMETRIC

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines an `equals` method that overrides an
`equals` method in a superclass. Both equals methods use
`instanceof` in the determination of whether two objects are
equal. This is fraught with peril, since it is important that the
`equals` method is symmetrical (in other words,
`a.equals(b) == b.equals(a)`). If B is a subtype of A, and A's
equals method checks that the argument is an `instanceof A`, and B's
equals method checks that the argument is an `instanceof B`, it is
quite likely that the equivalence relation defined by these methods is not
symmetric.

## FB.EQ_SELF_NO_OBJECT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines a covariant version of `equals()`. To correctly
override the `equals()` method in `java.lang.Object`,
the parameter of `equals()` must have type
`java.lang.Object`.

## FB.EQ_SELF_USE_OBJECT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class defines a covariant version of the `equals()` method, but
inherits the normal `equals(Object)` method defined in the base
`java.lang.Object` class. The class should probably define a
`boolean equals(Object)` method.

## FB.EQ_UNUSUAL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | Eq: Problems with implementation of `equals()` | [CWE-595](http://cwe.mitre.org/data/definitions/595.html) |

This class doesn't do any of the patterns we recognize for checking that the type of
the argument is compatible with the type of the `this` object. There
might not be anything wrong with this code, but it is worth reviewing.

## FB.ESYNC_EMPTY_SYNC

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | ESync: Empty Synchronized blocks | [CWE-585](http://cwe.mitre.org/data/definitions/585.html) |

The code contains an empty synchronized block:

```
synchronized() {
}
```

Empty synchronized blocks are far more subtle and hard to use correctly than most
people recognize, and empty synchronized blocks are almost never a better solution
than less contrived solutions.

## FB.ES_COMPARING_PARAMETER_STRING_WITH_EQ

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | ES: Checking String equality using `==` or `!=` | [CWE-597](http://cwe.mitre.org/data/definitions/597.html) |

This code compares a `java.lang.String` parameter for reference
equality using the `==` or `!=` operators. Requiring
callers to pass only String constants or interned strings to a method is
unnecessarily fragile, and rarely leads to measurable performance gains. Consider
using the `equals(Object)` method instead.

## FB.ES_COMPARING_STRINGS_WITH_EQ

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | ES: Checking String equality using `==` or `!=` | [CWE-597](http://cwe.mitre.org/data/definitions/597.html) |

This code compares `java.lang.String` objects for reference equality
using the `==` or `!=` operators. Unless both strings
are either constants in a source file, or have been interned using the
`String.intern()` method, the same string value may be
represented by two different String objects. Consider using the
`equals(Object)` method instead.

## FB.FB_MISSING_EXPECTED_WARNING

|  |  |
| --- | --- |
| SpotBugs: Correctness | FB: SpotBugs did not produce the expected warnings on a method |

SpotBugs didn't generate generated a warning that, according to a
`@ExpectedWarning` annotated, is expected or desired.

## FB.FB_UNEXPECTED_WARNING

|  |  |
| --- | --- |
| SpotBugs: Correctness | FB: SpotBugs did not produce the expected warnings on a method |

SpotBugs generated a warning that, according to a `@NoWarning`
annotated, is unexpected or undesired.

## FB.FE_FLOATING_POINT_EQUALITY

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | FE: Test for floating point equality |

This operation compares two floating point values for equality. Because floating
point calculations may involve rounding, calculated float and double values may not
be accurate. For values that must be precise, such as monetary values, consider
using a fixed-precision type such as `BigDecimal`. For values that
need not be precise, consider comparing for equality within some range, for example:
`if ( Math.abs(x - y) < .0000001 )`. See the Java Language
Specification, section 4.2.4.

## FB.FE_TEST_IF_EQUAL_TO_NOT_A_NUMBER

|  |  |
| --- | --- |
| SpotBugs: Correctness | FE: Test for floating point equality |

This code checks to see if a floating point value is equal to the special Not A
Number value (e.g., `if (x == Double.NaN)`). However, because of the
special semantics of `NaN`, no value is equal to
`Nan`, including `NaN`. Thus, `x ==
Double.NaN` always evaluates to false. To check to see if a value
contained in `x` is the special Not A Number value, use
`Double.isNaN(x)` (or `Float.isNaN(x)` if
`x` is floating point precision).

## FB.FI_EMPTY

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | FI: Incorrect use of finalizers | [CWE-586](http://cwe.mitre.org/data/definitions/586.html) |

Empty `finalize()` methods are useless, so they should be deleted.

## FB.FI_EXPLICIT_INVOCATION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | FI: Incorrect use of finalizers | [CWE-586](http://cwe.mitre.org/data/definitions/586.html) |

This method contains an explicit invocation of the `finalize()` method
on an object. Because finalizer methods are supposed to be executed once, and only
by the VM, this is a bad idea.

If a connected set of objects beings finalizable, then the VM will invoke the
finalize method on all the finalizable object, possibly at the same time in
different threads. Thus, it is a particularly bad idea, in the finalize method for a
class X, invoke finalize on objects referenced by X, because they may already be
getting finalized in a separate thread.

## FB.FI_FINALIZER_NULLS_FIELDS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | FI: Incorrect use of finalizers | [CWE-586](http://cwe.mitre.org/data/definitions/586.html) |

This finalizer nulls out fields. This is usually an error, as it does not aid garbage
collection, and the object is going to be garbage collected anyway.

## FB.FI_FINALIZER_ONLY_NULLS_FIELDS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | FI: Incorrect use of finalizers | [CWE-586](http://cwe.mitre.org/data/definitions/586.html) |

This finalizer does nothing except null out fields. This is completely pointless, and
requires that the object be garbage collected, finalized, and then garbage collected
again. You should just remove the finalize method.

## FB.FI_MISSING_SUPER_CALL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | FI: Incorrect use of finalizers | [CWE-586](http://cwe.mitre.org/data/definitions/586.html) |

This `finalize()` method does not make a call to its superclass's
`finalize()` method. So, any finalizer actions defined for the
superclass will not be performed. Add a call to
`super.finalize()`.

## FB.FI_NULLIFY_SUPER

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | FI: Incorrect use of finalizers | [CWE-586](http://cwe.mitre.org/data/definitions/586.html) |

This empty `finalize()` method explicitly negates the effect of any
finalizer defined by its superclass. Any finalizer actions defined for the
superclass will not be performed. Unless this is intended, delete this method.

## FB.FI_PUBLIC_SHOULD_BE_PROTECTED

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | FI: Incorrect use of finalizers | [CWE-583](http://cwe.mitre.org/data/definitions/583.html) |

A class's `finalize()` method should have protected access, not
public.

## FB.FI_USELESS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | FI: Incorrect use of finalizers | [CWE-586](http://cwe.mitre.org/data/definitions/586.html) |

The only thing this `finalize()` method does is call the superclass's
`finalize()` method, making it redundant. Delete it.

## FB.FL_FLOATS_AS_LOOP_COUNTERS

|  |  |
| --- | --- |
| SpotBugs: Correctness | FL: Use of floating point precision |

Using floating-point variables should not be used as loop counters, as they are not
precise, which may result in incorrect loops. A loop counter is a variable that is
changed with each iteration and controls when the loop should terminate. It is
decreased or increased by a fixed amount each iteration.

See rule [NUM09-J](https://wiki.sei.cmu.edu/confluence/display/java/NUM09-J.+Do+not+use+floating-point+variables+as+loop+counters).

## FB.FL_MATH_USING_FLOAT_PRECISION

|  |  |
| --- | --- |
| SpotBugs: Correctness | FL: Use of floating point precision |

The method performs math operations using floating point precision. Floating point
precision is very imprecise. For example, 16777216.0f + 1.0f = 16777216.0f. Consider
using double math instead.

## FB.FS_BAD_DATE_FORMAT_FLAG_COMBO

|  |  |
| --- | --- |
| SpotBugs: Bad practice | FS: Format string problem |

This format string includes a bad combination of flags which may lead to unexpected behavior.
(*SpotBugs Experimental*)

## FB.GC_UNCHECKED_TYPE_IN_GENERIC_CALL

|  |  |
| --- | --- |
| SpotBugs: Bad practice | GC: Suspicious calls to generic collection methods |

This call to a generic collection method passes an argument while compile type
`Object` where a specific type from the generic type parameters
is expected. Thus, neither the standard Java type system nor static analysis can
provide useful information on whether the object being passed as a parameter is of
an appropriate type.

## FB.GC_UNRELATED_TYPES

|  |  |
| --- | --- |
| SpotBugs: Correctness | GC: Suspicious calls to generic collection methods |

This call to a generic collection method contains an argument with an incompatible
class from that of the collection's parameter (i.e., the type of the argument is
neither a supertype nor a subtype of the corresponding generic type argument).
Therefore, it is unlikely that the collection contains any objects that are equal to
the method argument used here. Most likely, the wrong value is being passed to the
method.

In general, instances of two unrelated classes are not equal. For example, if the
`Foo` and `Bar` classes are not related by
subtyping, then an instance of `Foo` should not be equal to an
instance of `Bar`. Among other issues, doing so will likely result in
an equals method that is not symmetrical. For example, if you define the
`Foo` class so that a `Foo` can be equal to a
`String`, your equals method isn't symmetrical since a
`String` can only be equal to a `String`.

In rare cases, people do define non-symmetrical equals methods and still manage to
make their code work. Although none of the APIs document or guarantee it, it is
typically the case that if you check if a `Collection<String>`
contains a `Foo`, the equals method of argument (e.g., the equals
method of the `Foo` class) used to perform the equality checks.

## FB.HE_EQUALS_NO_HASHCODE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | HE: Equal objects must have equal hashcodes |

This class overrides `equals(Object)`, but does not override
`hashCode()`. Therefore, the class may violate the invariant that
equal objects must have equal hashcodes.

## FB.HE_EQUALS_USE_HASHCODE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | HE: Equal objects must have equal hashcodes |

This class overrides `equals(Object)`, but does not override
`hashCode()`, and inherits the implementation of
`hashCode()` from `java.lang.Object` (which
returns the identity hash code, an arbitrary value assigned to the object by the
VM). Therefore, the class is very likely to violate the invariant that equal objects
must have equal hashcodes.

If you don't think instances of this class will ever be inserted into a
`HashMap`/`HashTable`, the recommended
`hashCode` implementation to use is:

```
public int hashCode() {
    assert false : "hashCode not designed";
    return 42; // any arbitrary constant will do
}
```

## FB.HE_HASHCODE_NO_EQUALS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | HE: Equal objects must have equal hashcodes |

This class defines a `hashCode()` method but not an
`equals()` method. Therefore, the class may violate the invariant
that equal objects must have equal hashcodes.

## FB.HE_HASHCODE_USE_OBJECT_EQUALS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | HE: Equal objects must have equal hashcodes |

This class defines a `hashCode()` method but inherits its
`equals()` method from `java.lang.Object` (which
defines equality by comparing object references). Although this will probably
satisfy the contract that equal objects must have equal hashcodes, it is probably
not what was intended by overriding the `hashCode()` method.
(Overriding `hashCode()` implies that the object's identity is based
on criteria more complicated than simple reference equality.)

If you don't think instances of this class will ever be inserted into a
`HashMap`/`HashTable`, the recommended
`hashCode()` implementation to use is:

```
public int hashCode() {
    assert false : "hashCode not designed";
    return 42; // any arbitrary constant will do
}
```

## FB.HE_INHERITS_EQUALS_USE_HASHCODE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | HE: Equal objects must have equal hashcodes |

This class inherits `equals(Object)` from an abstract superclass, and
`hashCode()` from `java.lang.Object` (which
returns the identity hash code, an arbitrary value assigned to the object by the
VM). Therefore, the class is very likely to violate the invariant that equal objects
must have equal hashcodes.

If you don't want to define a `hashCode` method, and/or don't believe
the object will ever be put into a
`HashMap`/`Hashtable`, define the
`hashCode()` method to throw
`UnsupportedOperationException`.

## FB.HE_SIGNATURE_DECLARES_HASHING_OF_UNHASHABLE_CLASS

|  |  |
| --- | --- |
| SpotBugs: Correctness | HE: Equal objects must have equal hashcodes |

A method, field or class declares a generic signature where a non-hashable class is
used in context where a hashable class is required. A class that declares an equals
method but inherits a `hashCode()` method from
`Object` is unhashable, since it doesn't fulfill the requirement
that equal objects have equal hashCodes.

## FB.HE_USE_OF_UNHASHABLE_CLASS

|  |  |
| --- | --- |
| SpotBugs: Correctness | HE: Equal objects must have equal hashcodes |

A class defines an
`equals(Object)` method but not a `hashCode()`
method, and thus doesn't fulfill the requirement that equal objects have equal
hashCodes. An instance of this class is used in a hash data structure, making the
need to fix this problem of highest importance.

## FB.HRS_REQUEST_PARAMETER_TO_COOKIE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | HRS: HTTP Response splitting vulnerability | [CWE-113](http://cwe.mitre.org/data/definitions/113.html) |

This code constructs an HTTP Cookie using an untrusted HTTP parameter. If this cookie
is added to an HTTP response, it will allow a HTTP response splitting vulnerability.
See <http://en.wikipedia.org/wiki/HTTP_response_splitting> for
more information.

SpotBugs looks only for the most blatant, obvious cases of HTTP response splitting.
If SpotBugs found *any*, you *almost certainly* have more vulnerabilities
that SpotBugs doesn't report. If you are concerned about HTTP response splitting,
you should seriously consider using a commercial static analysis or pen-testing
tool.

## FB.HRS_REQUEST_PARAMETER_TO_HTTP_HEADER

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | HRS: HTTP Response splitting vulnerability | [CWE-113](http://cwe.mitre.org/data/definitions/113.html) |

This code directly writes an HTTP parameter to an HTTP header, which allows for a
HTTP response splitting vulnerability. See <http://en.wikipedia.org/wiki/HTTP_response_splitting> for more
information.

SpotBugs looks only for the most blatant, obvious cases of HTTP response splitting.
If SpotBugs found *any*, you *almost certainly* have more vulnerabilities
that SpotBugs doesn't report. If you are concerned about HTTP response splitting,
you should seriously consider using a commercial static analysis or pen-testing
tool.

## FB.HSC_HUGE_SHARED_STRING_CONSTANT

|  |  |
| --- | --- |
| SpotBugs: Performance | HSC: Huge String constants |

A large String constant is duplicated across multiple class files. This is likely
because a final field is initialized to a String constant, and the Java language
mandates that all references to a final field from other classes be inlined into
that classfile. See [JDK bug 6447475](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6447475) for a description of an occurrence of
this bug in the JDK and how resolving it reduced the size of the JDK by 1
megabyte.

## FB.IA_AMBIGUOUS_INVOCATION_OF_INHERITED_OR_OUTER_METHOD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | IA: Ambiguous invocation |

An inner class is invoking a method that could be resolved to either a inherited
method or a method defined in an outer class. For example, you invoke
`foo(17)`, which is defined in both a superclass and in an outer
method. By the Java semantics, it will be resolved to invoke the inherited method,
but this may not be what you intend.

If you really intend to invoke the inherited method, invoke it by invoking the method
on super (e.g., invoke `super.foo(17)`), and thus it will be clear to
other readers of your code and to SpotBugs that you want to invoke the inherited
method, not the method in the outer class.

If you call `this.foo(17)`, then the inherited method will be invoked.
However, since SpotBugs only looks at class files, it can't tell the difference
between an invocation of `this.foo(17)` and `foo(17)`,
it will still complain about a potential ambiguous invocation.

## FB.ICAST_BAD_SHIFT_AMOUNT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | BSHIFT: Bad shift | [CWE-192](http://cwe.mitre.org/data/definitions/192.html) |

The code performs shift of a 32 bit int by a constant amount outside the range
-31..31. The effect of this is to use the lower 5 bits of the integer value to
decide how much to shift by (e.g., shifting by 40 bits is the same as shifting by 8
bits, and shifting by 32 bits is the same as shifting by zero bits). This probably
isn't what was expected, and it is at least confusing.

## FB.ICAST_IDIV_CAST_TO_DOUBLE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | ICAST: Casting from integer values | [CWE-192](http://cwe.mitre.org/data/definitions/192.html) |

This code casts the result of an integral division (e.g., int or long division)
operation to double or float. Doing division on integers truncates the result to the
integer value closest to zero. The fact that the result was cast to double suggests
that this precision should have been retained. What was probably meant was to cast
one or both of the operands to double *before* performing the division. Here is
an example:

```
int x = 2;
int y = 5;
// Wrong: yields result 0.0
double value1 = x / y;

// Right: yields result 0.4
double value2 = x / (double) y;
```

## FB.ICAST_INTEGER_MULTIPLY_CAST_TO_LONG

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | ICAST: Casting from integer values | [CWE-192](http://cwe.mitre.org/data/definitions/192.html) |

This code performs integer multiply and then converts the result to a long, as
in:

```
long convertDaysToMilliseconds(int days) { return 1000*3600*24*days; }
```

If the multiplication is done using long arithmetic, you can avoid the possibility
that the result will overflow. For example, you could fix the above code to:

```
long convertDaysToMilliseconds(int days) { return 1000L*3600*24*days; }
```

or

```
static final long MILLISECONDS_PER_DAY = 24L*3600*1000;
long convertDaysToMilliseconds(int days) { return days * MILLISECONDS_PER_DAY; }
```

## FB.ICAST_INT_2_LONG_AS_INSTANT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | ICAST: Casting from integer values | [CWE-192](http://cwe.mitre.org/data/definitions/192.html) |

This code converts a 32-bit int value to a 64-bit long value, and then passes that
value for a method parameter that requires an absolute time value. An absolute time
value is the number of milliseconds since the standard base time known as "the
epoch", namely January 1, 1970, 00:00:00 GMT. For example, the following method,
intended to convert seconds since the epoch into a Date, is badly broken:

```
Date getDate(int seconds) { return new Date(seconds * 1000); }
```

The multiplication is done using 32-bit arithmetic, and then converted to a 64-bit
value. When a 32-bit value is converted to 64-bits and used to express an absolute
time value, only dates in December 1969 and January 1970 can be represented.

Correct implementations for the above method are:

```
// Fails for dates after 2037
Date getDate(int seconds) { return new Date(seconds * 1000L); }

// better, works for all dates
Date getDate(long seconds) { return new Date(seconds * 1000); }
```

## FB.ICAST_INT_CAST_TO_DOUBLE_PASSED_TO_CEIL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | ICAST: Casting from integer values | [CWE-192](http://cwe.mitre.org/data/definitions/192.html) |

This code converts an integral value (e.g., `int` or
`long`) to a double precision floating point number and then
passing the result to the `Math.ceil()` function, which rounds a
double to the next higher integer value. This operation should always be a no-op,
since the converting an integer to a double should give a number with no fractional
part. It is likely that the operation that generated the value to be passed to
`Math.ceil` was intended to be performed using double precision
floating point arithmetic.

## FB.ICAST_INT_CAST_TO_FLOAT_PASSED_TO_ROUND

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | ICAST: Casting from integer values | [CWE-192](http://cwe.mitre.org/data/definitions/192.html) |

This code converts an int value to a float precision floating point number and then
passing the result to the `Math.round()` function, which returns the
`int`/`long` closest to the argument. This
operation should always be a no-op, since the converting an integer to a float
should give a number with no fractional part. It is likely that the operation that
generated the value to be passed to `Math.round` was intended to be
performed using floating point arithmetic.

## FB.ICAST_QUESTIONABLE_UNSIGNED_RIGHT_SHIFT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | BSHIFT: Bad shift | [CWE-192](http://cwe.mitre.org/data/definitions/192.html) |

The code performs an unsigned right shift, whose result is then cast to a short or
byte, which discards the upper bits of the result. Since the upper bits are
discarded, there may be no difference between a signed and unsigned right shift
(depending upon the size of the shift).

## FB.IC_INIT_CIRCULARITY

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | IC: Initialization circularity |

A circularity was detected in the static initializers of the two classes referenced
by the bug instance. Many kinds of unexpected behavior may arise from such
circularity.

## FB.IC_SUPERCLASS_USES_SUBCLASS_DURING_INITIALIZATION

|  |  |
| --- | --- |
| SpotBugs: Bad practice | IC: Initialization circularity |

During the initialization of a class, the class makes an active use of a subclass.
That subclass will not yet be initialized at the time of this use. For example, in
the following code, `foo` will be null.

```
public class CircularClassInitialization {
    static class InnerClassSingleton extends CircularClassInitialization {
        static InnerClassSingleton singleton = new InnerClassSingleton();
    }

    static CircularClassInitialization foo = InnerClassSingleton.singleton;
}
```

## FB.IIL_ELEMENTS_GET_LENGTH_IN_LOOP

|  |  |
| --- | --- |
| SpotBugs: Performance | IIL: Inefficient code which can be moved outside of the loop |

The method calls `NodeList.getLength()` inside the loop and
`NodeList` was produced by `getElementsByTagName`
call. This `NodeList` doesn't store its length, but computes it every
time in not very optimal way. Consider storing the length to the variable before the
loop.

## FB.IIL_PATTERN_COMPILE_IN_LOOP

|  |  |
| --- | --- |
| SpotBugs: Performance | IIL: Inefficient code which can be moved outside of the loop |

The method calls `Pattern.compile` inside the loop passing the
constant arguments. If the `Pattern` should be used several times
there's no reason to compile it for each loop iteration. Move this call outside of
the loop or even into static final field.

## FB.IIL_PATTERN_COMPILE_IN_LOOP_INDIRECT

|  |  |
| --- | --- |
| SpotBugs: Performance | IIL: Inefficient code which can be moved outside of the loop |

The method creates the same regular expression inside the loop, so it will be
compiled every iteration. It would be more optimal to pre-compile this regular
expression using `Pattern.compile` outside of the loop.

## FB.IIL_PREPARE_STATEMENT_IN_LOOP

|  |  |
| --- | --- |
| SpotBugs: Performance | IIL: Inefficient code which can be moved outside of the loop |

The method calls `Connection.prepareStatement` inside the loop passing
the constant arguments. If the `PreparedStatement` should be executed
several times there's no reason to recreate it for each loop iteration. Move this
call outside of the loop.

## FB.IIO_INEFFICIENT_INDEX_OF

|  |  |
| --- | --- |
| SpotBugs: Performance | IIO: Inefficient use of `String.indexOf(String)` or `String.lastIndexOf(String)` |

This code passes a constant string of length 1 to `String.indexOf()`.
It is more efficient to use the integer implementations of
`String.indexOf()`. f. e. call
`myString.indexOf('.')` instead of
`myString.indexOf(".")`

## FB.IIO_INEFFICIENT_LAST_INDEX_OF

|  |  |
| --- | --- |
| SpotBugs: Performance | IIO: Inefficient use of `String.indexOf(String)` or `String.lastIndexOf(String)` |

This code passes a constant string of length 1 to
`String.lastIndexOf()`. It is more efficient to use the integer
implementations of `String.lastIndexOf()`. f. e. call
`myString.lastIndexOf('.')` instead of
`myString.lastIndexOf(".")`

## FB.IJU_ASSERT_METHOD_INVOKED_FROM_RUN_METHOD

|  |  |
| --- | --- |
| SpotBugs: Correctness | IJU: Improperly implemented JUnit `TestCase` |

A JUnit assertion is performed in a run method. Failed JUnit assertions just result
in exceptions being thrown. Thus, if this exception occurs in a thread other than
the thread that invokes the test method, the exception will terminate the thread but
not result in the test failing.

## FB.IJU_BAD_SUITE_METHOD

|  |  |
| --- | --- |
| SpotBugs: Correctness | IJU: Improperly implemented JUnit `TestCase` |

Class is a JUnit `TestCase` and defines a suite() method. However, the
suite method needs to be declared as either

```
public static junit.framework.Test suite()
```

or

```
public static junit.framework.TestSuite suite()
```

## FB.IJU_NO_TESTS

|  |  |
| --- | --- |
| SpotBugs: Correctness | IJU: Improperly implemented JUnit `TestCase` |

Class is a JUnit `TestCase` but has not implemented any test
methods.

## FB.IJU_SETUP_NO_SUPER

|  |  |
| --- | --- |
| SpotBugs: Correctness | IJU: Improperly implemented JUnit `TestCase` |

Class is a JUnit `TestCase` and implements the `setUp`
method. The `setUp` method should call
`super.setUp()`, but doesn't.

## FB.IJU_SUITE_NOT_STATIC

|  |  |
| --- | --- |
| SpotBugs: Correctness | IJU: Improperly implemented JUnit `TestCase` |

Class is a JUnit `TestCase` and implements the
`suite()` method. The suite method should be declared as being
static, but isn't.

## FB.IJU_TEARDOWN_NO_SUPER

|  |  |
| --- | --- |
| SpotBugs: Correctness | IJU: Improperly implemented JUnit `TestCase` |

Class is a JUnit `TestCase` and implements the
`tearDown` method. The `tearDown` method should
call `super.tearDown()`, but doesn't.

## FB.IL_CONTAINER_ADDED_TO_ITSELF

|  |  |
| --- | --- |
| SpotBugs: Correctness | IL: Infinite Loop |

A collection is added to itself. As a result, computing the `hashCode`
of this set will throw a `StackOverflowException`.

## FB.IL_INFINITE_LOOP

|  |  |
| --- | --- |
| SpotBugs: Correctness | IL: Infinite Loop |

This loop doesn't seem to have a way to terminate (other than by perhaps throwing an
exception).

## FB.IL_INFINITE_RECURSIVE_LOOP

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | IL: Infinite Loop | [CWE-674](http://cwe.mitre.org/data/definitions/674.html) |

This method unconditionally invokes itself. This would seem to indicate an infinite
recursive loop that will result in a stack overflow.

## FB.IMA_INEFFICIENT_MEMBER_ACCESS

|  |  |
| --- | --- |
| SpotBugs: Performance | IMA: Inefficient Member Access |

This method of an inner class reads from or writes to a private member variable of
the owning class, or calls a private method of the owning class. The compiler must
generate a special method to access this private member, causing this to be less
efficient. Relaxing the protection of the member variable or method will allow the
compiler to treat this as a normal access.

## FB.IMSE_DONT_CATCH_IMSE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | IMSE: Dubious catching of `IllegalMonitorStateException` |

`IllegalMonitorStateException` is generally only thrown in case of a
design flaw in your code (calling wait or notify on an object you do not hold a lock
on).

## FB.IM_AVERAGE_COMPUTATION_COULD_OVERFLOW

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | IM: Questionable integer math |

The code computes the average of two integers using either division or signed right
shift, and then uses the result as the index of an array. If the values being
averaged are very large, this can overflow (resulting in the computation of a
negative average). Assuming that the result is intended to be non-negative, you can
use an unsigned right shift instead. In other words, rather that using
`(low+high)/2`, use `(low+high) >>> 1`.

This bug exists in many earlier implementations of binary search and merge sort.
Martin Buchholz [found and fixed it](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6412541) in the JDK libraries, and Joshua
Bloch [widely publicized the bug pattern](http://googleresearch.blogspot.com/2006/06/extra-extra-read-all-about-it-nearly.html).

## FB.IM_BAD_CHECK_FOR_ODD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | IM: Questionable integer math |

The code uses `x % 2 == 1` to check to see if a value is odd, but this
won't work for negative numbers (e.g., `(-5) % 2 == -1`). If this
code is intending to check for oddness, consider using `x & 1 ==
1`, or `x % 2 != 0`.

## FB.IM_MULTIPLYING_RESULT_OF_IREM

|  |  |
| --- | --- |
| SpotBugs: Correctness | IM: Questionable integer math |

The code multiplies the result of an integer remaining by an integer constant. Be
sure you don't have your operator precedence confused. For example `i % 60 *
1000` is `(i % 60) * 1000`, not `i % (60 *
1000)`.

## FB.INT_BAD_COMPARISON_WITH_INT_VALUE

|  |  |
| --- | --- |
| SpotBugs: Correctness | INT: Suspicious integer expression |

This code compares an int value with a long constant that is outside the range of
values that can be represented as an int value. This comparison is vacuous and
possibly to be incorrect.

## FB.INT_BAD_COMPARISON_WITH_NONNEGATIVE_VALUE

|  |  |
| --- | --- |
| SpotBugs: Correctness | INT: Suspicious integer expression |

This code compares a value that is guaranteed to be non-negative with a negative
constant or zero.

## FB.INT_BAD_COMPARISON_WITH_SIGNED_BYTE

|  |  |
| --- | --- |
| SpotBugs: Correctness | INT: Suspicious integer expression |

Signed bytes can only have a value in the range -128 to 127. Comparing a signed byte
with a value outside that range is vacuous and likely to be incorrect. To convert a
signed byte `b` to an unsigned value in the range 0..255, use
`0xff & b`.

## FB.INT_BAD_REM_BY_1

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | INT: Suspicious integer expression |

Any expression `(exp % 1)` is guaranteed to always return zero. Did
you mean `(exp & 1)` or `(exp % 2)` instead?

## FB.INT_VACUOUS_BIT_OPERATION

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | INT: Suspicious integer expression |

This is an integer bit operation (and, or, or exclusive or) that doesn't do any
useful work (e.g., `v & 0xffffffff`).

## FB.INT_VACUOUS_COMPARISON

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | INT: Suspicious integer expression |

There is an integer comparison that always returns the same value (e.g., `x
<= Integer.MAX_VALUE`).

## FB.IO_APPENDING_TO_OBJECT_OUTPUT_STREAM

|  |  |
| --- | --- |
| SpotBugs: Correctness | IO: Input/Output problem |

This code opens a file in append mode and then wraps the result in an object output
stream. This won't allow you to append to an existing object output stream stored in
a file. If you want to be able to append to an object output stream, you need to
keep the object output stream open.

The only situation in which opening a file in append mode and the writing an object
output stream could work is if on reading the file you plan to open it in random
access mode and seek to the byte offset where the append started.

## FB.IP_PARAMETER_IS_DEAD_BUT_OVERWRITTEN

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | IP: Ignored parameter | [CWE-563](http://cwe.mitre.org/data/definitions/563.html) |

The initial value of this parameter is ignored, and the parameter is overwritten
here. This often indicates a mistaken belief that the write to the parameter will be
conveyed back to the caller.

## FB.IRA_INEFFICIENT_REPLACEALL

|  |  |
| --- | --- |
| SpotBugs: Performance | IRA: Inefficient use of `String.replaceAll(String, String)` |

This method uses `replaceAll(String regex, String replacement)`
without any special regex characters.

## FB.IS2_INCONSISTENT_SYNC

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | IS: Inconsistent synchronization | [CWE-366](http://cwe.mitre.org/data/definitions/366.html) |

The fields of this class appear to be accessed inconsistently with respect to
synchronization. This bug report indicates that the bug pattern detector judged
that

- The class contains a mix of locked and unlocked accesses,
- The class is **not** annotated as
  `javax.annotation.concurrent.NotThreadSafe`,
- At least one locked access was performed by one of the class's own methods,
  and
- The number of unsynchronized field accesses (reads and writes) was no more than
  one third of all accesses, with writes being weighed twice as high as reads

A typical bug matching this bug pattern is forgetting to synchronize one of the
methods in a class that is intended to be thread-safe.

You can select the nodes labeled "Unsynchronized access" to show the code locations
where the detector believed that a field was accessed without synchronization.

Note that there are various sources of inaccuracy in this detector; for example, the
detector cannot statically detect all situations in which a lock is held. Also, even
when the detector is accurate in distinguishing locked vs. unlocked accesses, the
code in question may still be correct.

## FB.ISC_INSTANTIATE_STATIC_CLASS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | ISC: Instantiated Static Class |

This class allocates an object that is based on a class that only supplies static
methods. This object does not need to be created, just access the static methods
directly using the class name as a qualifier.

## FB.IS_FIELD_NOT_GUARDED

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | IS: Inconsistent synchronization | [CWE-366](http://cwe.mitre.org/data/definitions/366.html) |

This field is annotated with `net.jcip.annotations.GuardedBy` or
`javax.annotation.concurrent.GuardedBy`, but can be accessed in a
way that seems to violate those annotations.

## FB.IS_INCONSISTENT_SYNC

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | IS: Inconsistent synchronization | [CWE-366](http://cwe.mitre.org/data/definitions/366.html) |

The fields of this class appear to be accessed inconsistently with respect to
synchronization. This bug report indicates that the bug pattern detector judged
that

- The class contains a mix of locked and unlocked accesses,
- At least one locked access was performed by one of the class's own methods,
  and
- The number of unsynchronized field accesses (reads and writes) was no more than
  one third of all accesses, with writes being weighed twice as high as reads

A typical bug matching this bug pattern is forgetting to synchronize one of the
methods in a class that is intended to be thread-safe.

Note that there are various sources of inaccuracy in this detector; for example, the
detector cannot statically detect all situations in which a lock is held. Also, even
when the detector is accurate in distinguishing locked vs. unlocked accesses, the
code in question may still be correct.

## FB.ITA_INEFFICIENT_TO_ARRAY

|  |  |
| --- | --- |
| SpotBugs: Performance | ITA: Inefficient use of `collection.toArray(new Foo[0])` |

This method uses the `toArray()` method of a collection derived class,
and passes in a zero-length prototype array argument. It is more efficient to use
`myCollection.toArray(new Foo[myCollection.size()])`. If the
array passed in is big enough to store all of the elements of the collection, then
it is populated and returned directly. This avoids the need to create a second array
(by reflection) to return as the result.

## FB.IT_NO_SUCH_ELEMENT

|  |  |
| --- | --- |
| SpotBugs: Bad practice | It: Incorrect definition of Iterator |

This class implements the `java.util.Iterator` interface. However, its
`next()` method is not capable of throwing
`java.util.NoSuchElementException`. The `next()`
method should be changed so it throws `NoSuchElementException` if is
called when there are no more elements to return.

## FB.J2EE_STORE_OF_NON_SERIALIZABLE_OBJECT_INTO_SESSION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | J2EE: J2EE error | [CWE-579](http://cwe.mitre.org/data/definitions/579.html) |

This code seems to be storing a non-serializable object into an
`HttpSession`. If this session is passivated or migrated, an
error will result.

## FB.JCIP_FIELD_ISNT_FINAL_IN_IMMUTABLE_CLASS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | JCIP: Violation of `net.jcip` annotations |

The class is annotated with `net.jcip.annotations.Immutable` or
`javax.annotation.concurrent.Immutable`, and the rules for those
annotations require that all fields are final.

## FB.JLM_JSR166_LOCK_MONITORENTER

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | JLM: Synchronization on `java.util.concurrent` objects |

This method performs synchronization an object that implements
`java.util.concurrent.locks.Lock`. Such an object is
locked/unlocked using `acquire()`/`release()` rather
than using the `synchronized (...)` construct.

## FB.JLM_JSR166_UTILCONCURRENT_MONITORENTER

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | JLM: Synchronization on `java.util.concurrent` objects |

This method performs synchronization an object that is an instance of a class from
the `java.util.concurrent` package (or its subclasses). Instances of
these classes have their own concurrency control mechanisms that are orthogonal to
the synchronization provided by the Java keyword `synchronized`. For
example, synchronizing on an `AtomicBoolean` will not prevent other
threads from modifying the `AtomicBoolean`.

Such code may be correct, but should be carefully reviewed and documented, and may
confuse people who have to maintain the code at a later date.

## FB.JML_JSR166_CALLING_WAIT_RATHER_THAN_AWAIT

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | JLM: Synchronization on `java.util.concurrent` objects |

This method calls `wait()`, `notify()` or
`notifyAll()()` on an object that also provides an
`await()`, `signal()`,
`signalAll()` method (such as `util.concurrent`
Condition objects). This probably isn't what you want, and even if you do want it,
you should consider changing your design, as other developers will find it
exceptionally confusing.

## FB.JUA_DONT_ASSERT_INSTANCEOF_IN_TESTS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | JUA: Problems in JUnit Assertions |

Asserting type checks in tests is not recommended as a class cast exception message
could better indicate the cause of an instance of the wrong class being used than an
instanceof assertion.

When debugging tests that fail due to bad casts, it may be more useful to observe the
output of the resulting `ClassCastException` which could provide
information about the actual encountered type. Asserting the type before casting
would instead result in a less informative `"false is not true"`
message.

If JUnit is used with hamcrest, the [`IsInstanceOf`](https://junit.org/junit4/javadoc/latest/index.html?org/hamcrest/core/IsInstanceOf.html) class from
hamcrest could be used instead.

## FB.LG_LOST_LOGGER_DUE_TO_WEAK_REFERENCE

|  |  |
| --- | --- |
| SpotBugs: Experimental | LG: Logger problem |

OpenJDK introduces a potential incompatibility. In particular, the
`java.util.logging.Logger` behavior has changed. Instead of using
strong references, it now uses weak references internally. That's a reasonable
change, but unfortunately some code relies on the old behavior - when changing
logger configuration, it simply drops the logger reference. That means that the
garbage collector is free to reclaim that memory, which means that the logger
configuration is lost. For example, consider:

```
public static void initLogging() throws Exception {
    Logger logger = Logger.getLogger("edu.umd.cs");
    logger.addHandler(new FileHandler()); // call to change logger configuration
    logger.setUseParentHandlers(false); // another call to change logger configuration
}
```

The logger reference is lost at the end of the method (it doesn't escape the method),
so if you have a garbage collection cycle just after the call to
`initLogging`, the logger configuration is lost (because Logger
only keeps weak references).

```
public static void main(String[] args) throws Exception {
    initLogging(); // adds a file handler to the logger
    System.gc(); // logger configuration lost
    Logger.getLogger("edu.umd.cs").info("Some message"); // this isn't logged to the file as expected
}
```

*Ulf Ochsenfahrt and Eric Fellheimer*

## FB.LI_LAZY_INIT_INSTANCE

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | LI: Unsynchronized Lazy Initialization |

This method contains an unsynchronized lazy initialization of a non-volatile field.
Because the compiler or processor may reorder instructions, threads are not
guaranteed to see a completely initialized object, *if the method can be called by
multiple threads*. You can make the field volatile to correct the problem.
For more information, see the [Java
Memory Model web site](http://www.cs.umd.edu/~pugh/java/memoryModel/).

## FB.LI_LAZY_INIT_STATIC

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | LI: Unsynchronized Lazy Initialization | [CWE-543](http://cwe.mitre.org/data/definitions/543.html) |

This method contains an unsynchronized lazy initialization of a non-volatile static
field. Because the compiler or processor may reorder instructions, threads are not
guaranteed to see a completely initialized object, *if the method can be called by
multiple threads*. You can make the field volatile to correct the problem.
For more information, see the [Java
Memory Model web site](http://www.cs.umd.edu/~pugh/java/memoryModel/).

## FB.LI_LAZY_INIT_UPDATE_STATIC

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | LI: Unsynchronized Lazy Initialization | [CWE-543](http://cwe.mitre.org/data/definitions/543.html) |

This method contains an unsynchronized lazy initialization of a static field. After
the field is set, the object stored into that location is further updated or
accessed. The setting of the field is visible to other threads as soon as it is set.
If the further accesses in the method that set the field serve to initialize the
object, then you have a *very serious* multithreading bug, unless something
else prevents any other thread from accessing the stored object until it is fully
initialized.

Even if you feel confident that the method is never
called by multiple threads, it might be better to not set the static field until the
value you are setting it to is fully populated/initialized.

## FB.MC_OVERRIDABLE_METHOD_CALL_IN_CLONE

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | MC: Dangerous call to overridable method |

Calling overridable methods from the `clone()` method is insecure
because a subclass could override the method, affecting the behavior of
`clone()`. It can also observe or modify the clone object in a
partially initialized state. Only static, final or private methods should be invoked
from the `clone()` method.

See SEI CERT rule [MET06-J. Do not invoke overridable methods in
clone()](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=88487921).

## FB.MC_OVERRIDABLE_METHOD_CALL_IN_CONSTRUCTOR

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | MC: Dangerous call to overridable method |

Calling an overridable method during in a constructor may result in the use of
uninitialized data. It may also leak the this reference of the partially constructed
object. Only static, final or private methods should be invoked from a
constructor.

See SEI CERT rule [MET05-J. Ensure that constructors do not call
overridable methods](https://wiki.sei.cmu.edu/confluence/display/java/MET05-J.+Ensure+that+constructors+do+not+call+overridable+methods).

## FB.MC_OVERRIDABLE_METHOD_CALL_IN_READ_OBJECT

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | MC: Dangerous call to overridable method |

The `readObject()` method must not call any overridable methods.

## FB.ME_ENUM_FIELD_SETTER

|  |  |
| --- | --- |
| SpotBugs: Bad practice | ME: Mutable enum field |

This public method declared in public enum unconditionally sets enum field, thus this
field can be changed by malicious code or by accident from another package. Though
mutable enum fields may be used for lazy initialization, it's a bad practice to
expose them to the outer world. Consider removing this method or declaring it
package-private.

## FB.ME_MUTABLE_ENUM_FIELD

|  |  |
| --- | --- |
| SpotBugs: Bad practice | ME: Mutable enum field |

A mutable public field is defined inside a public enum, thus can be changed by
malicious code or by accident from another package. Though mutable enum fields may
be used for lazy initialization, it's a bad practice to expose them to the outer
world. Consider declaring this field final and/or package-private.

## FB.MF_CLASS_MASKS_FIELD

|  |  |
| --- | --- |
| SpotBugs: Correctness | MF: Masked Field |

This class defines a field with the same name as a visible instance field in a
superclass. This is confusing, and may indicate an error if methods update or access
one of the fields when they wanted the other.

## FB.MF_METHOD_MASKS_FIELD

|  |  |
| --- | --- |
| SpotBugs: Correctness | MF: Masked Field |

This method defines a local variable with the same name as a field in this class or a
superclass. This may cause the method to read an uninitialized value from the field,
leave the field uninitialized, or both.

## FB.ML_SYNC_ON_FIELD_TO_GUARD_CHANGING_THAT_FIELD

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | ML: Synchronization on updated field (Mutable Lock) |

This method synchronizes on a field in what appears to be an attempt to guard against
simultaneous updates to that field. But guarding a field gets a lock on the
referenced object, not on the field. This may not provide the mutual exclusion you
need, and other threads might be obtaining locks on the referenced objects (for
other purposes). An example of this pattern would be:

```
private Long myNtfSeqNbrCounter = new Long(0);
private Long getNotificationSequenceNumber() {
     Long result = null;
     synchronized(myNtfSeqNbrCounter) {
         result = new Long(myNtfSeqNbrCounter.longValue() + 1);
         myNtfSeqNbrCounter = new Long(result.longValue());
     }
     return result;
}
```

## FB.ML_SYNC_ON_UPDATED_FIELD

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | ML: Synchronization on updated field (Mutable Lock) |

This method synchronizes on an object referenced from a mutable field. This is
unlikely to have useful semantics, since different threads may be synchronizing on
different objects.

## FB.MSF_MUTABLE_SERVLET_FIELD

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | MSF: Mutable servlet field |

A web server generally only creates one instance of
servlet or JSP class (i.e., treats the class as a Singleton), and will have multiple
threads invoke methods on that instance to service multiple simultaneous requests.
Thus, having a mutable instance field generally creates race conditions.

## FB.MS_CANNOT_BE_FINAL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A mutable static field could be changed by malicious code or by accident from another
package. Unfortunately, the way the field is used doesn't allow any easy fix to this
problem.

## FB.MS_EXPOSE_BUF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A public static method either returns a buffer (`java.nio.*Buffer`)
which wraps an array that is part of the static state of the class by holding a
reference only to this same array or it returns a shallow-copy of a buffer that is
part of the static stat of the class which shares its reference with the original
buffer. Any code that calls this method can freely modify the underlying array. One
fix is to return a read-only buffer or a new buffer with a copy of the array.

## FB.MS_EXPOSE_REP

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A public static method returns a reference to an array that is part of the static
state of the class. Any code that calls this method can freely modify the underlying
array. One fix is to return a copy of the array.

## FB.MS_FINAL_PKGPROTECT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A mutable static field could be changed by malicious code or by accident from another
package. The field could be made package protected and/or made final to avoid this
vulnerability.

## FB.MS_MUTABLE_ARRAY

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A final static field references an array and can be accessed by malicious code or by
accident from another package. This code can freely modify the contents of the
array.

## FB.MS_MUTABLE_COLLECTION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A mutable collection instance is assigned to a final static field, thus can be
changed by malicious code or by accident from another package. Consider wrapping
this field into
`Collections.unmodifiableSet`/`List`/`Map`/etc.,
to avoid this vulnerability.

## FB.MS_MUTABLE_COLLECTION_PKGPROTECT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A mutable collection instance is assigned to a final static field, thus can be
changed by malicious code or by accident from another package. The field could be
made package protected to avoid this vulnerability. Alternatively you may wrap this
field into
`Collections.unmodifiableSet`/`List`/`Map`/etc.,
to avoid this vulnerability.

## FB.MS_MUTABLE_HASHTABLE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A final static field references a `Hashtable` and can be accessed by
malicious code or by accident from another package. This code can freely modify the
contents of the `Hashtable`.

## FB.MS_OOI_PKGPROTECT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A final static field that is defined in an interface references a mutable object such
as an array or hashtable. This mutable object could be changed by malicious code or
by accident from another package. To solve this, the field needs to be moved to a
class and made package protected to avoid this vulnerability.

## FB.MS_PKGPROTECT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A mutable static field could be changed by malicious code or by accident. The field
could be made package protected to avoid this vulnerability.

## FB.MS_SHOULD_BE_FINAL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A mutable static field could be changed by malicious code or by accident from another
package. The field could be made final to avoid this vulnerability.

## FB.MS_SHOULD_BE_REFACTORED_TO_BE_FINAL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Malicious code vulnerability | MS: Mutable static field | [CWE-218](http://cwe.mitre.org/data/definitions/218.html) |

A mutable static field could be changed by malicious code or by accident from another
package. The field could be made final to avoid this vulnerability. However, the
static initializer contains more than one write to the field, so doing so will
require some refactoring.

## FB.MTIA_SUSPECT_SERVLET_INSTANCE_FIELD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | MTIA: Multithreaded Instance Access |

This class extends from a `Servlet` class, and uses an instance member
variable. Since only one instance of a `Servlet` class is created by
the J2EE framework, and used in a multithreaded way, this paradigm is highly
discouraged and most likely problematic. Consider only using method local
variables.

## FB.MTIA_SUSPECT_STRUTS_INSTANCE_FIELD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | MTIA: Multithreaded Instance Access |

This class extends from a Struts Action class, and uses an instance member variable.
Since only one instance of a struts Action class is created by the Struts framework,
and used in a multithreaded way, this paradigm is highly discouraged and most likely
problematic. Consider only using method local variables. Only instance fields that
are written outside of a monitor are reported.

## FB.MWN_MISMATCHED_NOTIFY

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | MWN: Mismatched wait() or notify() |

This method calls `Object.notify()` or
`Object.notifyAll()` without obviously holding a lock on the
object. Calling `notify()` or `notifyAll()` without a
lock held will result in an `IllegalMonitorStateException` being
thrown.

## FB.MWN_MISMATCHED_WAIT

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | MWN: Mismatched wait() or notify() |

This method calls `Object.wait()` without obviously holding a lock on
the object. Calling `wait()` without a lock held will result in an
`IllegalMonitorStateException` being thrown.

## FB.NM_BAD_EQUAL

|  |  |
| --- | --- |
| SpotBugs: Correctness | Nm: Confusing name |

This class defines a method `equal(Object)`. This method does not
override the `equals(Object)` method in
`java.lang.Object`, which is probably what was intended.

## FB.NM_CLASS_NAMING_CONVENTION

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

Class names should be nouns, in mixed case with the first letter of each internal
word capitalized. Try to keep your class names simple and descriptive. Use whole
words-avoid acronyms and abbreviations (unless the abbreviation is much more widely
used than the long form, such as URL or HTML).

## FB.NM_CLASS_NOT_EXCEPTION

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

This class is not derived from another exception, but ends with 'Exception'. This
will be confusing to users of this class.

## FB.NM_CONFUSING

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

The referenced methods have names that differ only by capitalization.

## FB.NM_FIELD_NAMING_CONVENTION

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

Names of fields that are not final should be in mixed case with a lowercase first
letter and the first letters of subsequent words capitalized.

## FB.NM_FUTURE_KEYWORD_USED_AS_IDENTIFIER

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

The identifier is a word that is reserved as a keyword in later versions of Java, and
your code will need to be changed in order to compile it in later versions of
Java.

## FB.NM_FUTURE_KEYWORD_USED_AS_MEMBER_IDENTIFIER

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

This identifier is used as a keyword in later versions of Java. This code, and any
code that references this API, will need to be changed in order to compile it in
later versions of Java.

## FB.NM_LCASE_HASHCODE

|  |  |
| --- | --- |
| SpotBugs: Correctness | Nm: Confusing name |

This class defines a method called `hashcode()`. This method does not
override the `hashCode()` method in
`java.lang.Object`, which is probably what was intended.

## FB.NM_LCASE_TOSTRING

|  |  |
| --- | --- |
| SpotBugs: Correctness | Nm: Confusing name |

This class defines a method called `tostring()`. This method does not
override the `toString()` method in
`java.lang.Object`, which is probably what was intended.

## FB.NM_METHOD_CONSTRUCTOR_CONFUSION

|  |  |
| --- | --- |
| SpotBugs: Correctness | Nm: Confusing name |

This regular method has the same name as the class it is defined in. It is likely
that this was intended to be a constructor. If it was intended to be a constructor,
remove the declaration of a void return value. If you had accidentally defined this
method, realized the mistake, defined a proper constructor but can't get rid of this
method due to backwards compatibility, deprecate the method.

## FB.NM_METHOD_NAMING_CONVENTION

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

Methods should be verbs, in mixed case with the first letter lowercase, with the
first letter of each internal word capitalized.

## FB.NM_SAME_SIMPLE_NAME_AS_INTERFACE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

This class/interface has a simple name that is identical to that of an
implemented/extended interface, except that the interface is in a different package
(e.g., `alpha.Foo` extends `beta.Foo`). This can be
exceptionally confusing, create lots of situations in which you have to look at
import statements to resolve references and creates many opportunities to
accidentally define methods that do not override methods in their superclasses.

## FB.NM_SAME_SIMPLE_NAME_AS_SUPERCLASS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

This class has a simple name that is identical to that of its superclass, except that
its superclass is in a different package (e.g., `alpha.Foo` extends
`beta.Foo`). This can be exceptionally confusing, create lots of
situations in which you have to look at import statements to resolve references and
creates many opportunities to accidentally define methods that do not override
methods in their superclasses.

## FB.NM_VERY_CONFUSING

|  |  |
| --- | --- |
| SpotBugs: Correctness | Nm: Confusing name |

The referenced methods have names that differ only by capitalization. This is very
confusing because if the capitalization were identical then one of the methods would
override the other.

## FB.NM_VERY_CONFUSING_INTENTIONAL

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

The referenced methods have names that differ only by capitalization. This is very
confusing because if the capitalization were identical then one of the methods would
override the other. From the existence of other methods, it seems that the existence
of both of these methods is intentional, but is sure is confusing. You should try
hard to eliminate one of them, unless you are forced to have both due to frozen
APIs.

## FB.NM_WRONG_PACKAGE

|  |  |
| --- | --- |
| SpotBugs: Correctness | Nm: Confusing name |

The method in the subclass doesn't override a similar method in a superclass because
the type of a parameter doesn't exactly match the type of the corresponding
parameter in the superclass. For example, if you have:

```
import alpha.Foo;

public class A {
    public int f(Foo x) { return 17; }
}
----
import beta.Foo;

public class B extends A {
    public int f(Foo x) { return 42; }
}
```

The `f(Foo)` method defined in class `B` doesn't
override the `f(Foo)` method defined in class `A`,
because the argument types are `Foo`'s from different packages.

## FB.NM_WRONG_PACKAGE_INTENTIONAL

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Nm: Confusing name |

The method in the subclass doesn't override a similar method in a superclass because
the type of a parameter doesn't exactly match the type of the corresponding
parameter in the superclass. For example, if you have:

```
import alpha.Foo;

public class A {
    public int f(Foo x) { return 17; }
}
----
import beta.Foo;

public class B extends A {
    public int f(Foo x) { return 42; }
    public int f(alpha.Foo x) { return 27; }
}
```

The `f(Foo)` method defined in class `B` doesn't
override the `f(Foo)` method defined in class `A`,
because the argument types are `Foo`'s from different packages.

In this case, the subclass does define a method with a signature identical to the
method in the superclass, so this is presumably understood. However, such methods
are exceptionally confusing. You should strongly consider removing or deprecating
the method with the similar but not identical signature.

## FB.NN_NAKED_NOTIFY

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | NN: Naked notify |

A call to `notify()` or `notifyAll()` was made without
any (apparent) accompanying modification to mutable object state. In general,
calling a notify method on a monitor is done because some condition another thread
is waiting for has become true. However, for the condition to be meaningful, it must
involve a heap object that is visible to both threads.

This bug does not necessarily indicate an error, since the change to mutable object
state may have taken place in a method which then called the method containing the
notification.

## FB.NOISE_FIELD_REFERENCE

|  |  |
| --- | --- |
| SpotBugs: Bogus random noise | NOISE: Bogus random warning |

Bogus warning.

## FB.NOISE_METHOD_CALL

|  |  |
| --- | --- |
| SpotBugs: Bogus random noise | NOISE: Bogus random warning |

Bogus warning.

## FB.NOISE_NULL_DEREFERENCE

|  |  |
| --- | --- |
| SpotBugs: Bogus random noise | NOISE: Bogus random warning |

Bogus warning.

## FB.NOISE_OPERATION

|  |  |
| --- | --- |
| SpotBugs: Bogus random noise | NOISE: Bogus random warning |

Bogus warning.

## FB.NO_NOTIFY_NOT_NOTIFYALL

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | No: Using notify() rather than `notifyAll()` |

This method calls `notify()` rather than `notifyAll()`.
Java monitors are often used for multiple conditions. Calling
`notify()` only wakes up one thread, meaning that the thread
woken up might not be the one waiting for the condition that the caller just
satisfied.

## FB.NP_ALWAYS_NULL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A null pointer is dereferenced here. This will lead to a
`NullPointerException` when the code is executed.

## FB.NP_ALWAYS_NULL_EXCEPTION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A pointer which is null on an exception path is dereferenced here. This will lead to
a `NullPointerException` when the code is executed. Note that because
SpotBugs currently does not prune infeasible exception paths, this may be a false
warning.

Also note that SpotBugs considers the default case of a switch statement to be an
exception path, since the default case is often infeasible.

## FB.NP_ARGUMENT_MIGHT_BE_NULL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A parameter to this method has been identified as a value that should always be
checked to see whether or not it is null, but it is being dereferenced without a
preceding null check.

## FB.NP_BOOLEAN_RETURN_NULL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A method that returns either `Boolean.TRUE`,
`Boolean.FALSE` or null is an accident waiting to happen. This
method can be invoked as though it returned a value of type boolean, and the
compiler will insert automatic unboxing of the Boolean value. If a null value is
returned, this will result in a `NullPointerException`.

## FB.NP_CLONE_COULD_RETURN_NULL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This clone method seems to return null in some circumstances, but clone is never
allowed to return a `null` value. If you are convinced this path is
unreachable, throw an `AssertionError` instead.

## FB.NP_CLOSING_NULL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

`close()` is being invoked on
a value that is always null. If this statement is executed, a `null`
pointer exception will occur. But the big risk here you never close something that
should be closed.

## FB.NP_DEREFERENCE_OF_READLINE_VALUE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

The result of invoking `readLine()` is dereferenced without checking
to see if the result is `null`. If there are no more lines of text to
read, `readLine()` will return `null` and
dereferencing that will generate a null pointer exception.

## FB.NP_DOES_NOT_HANDLE_NULL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This implementation of `equals(Object)` violates the contract defined
by `java.lang.Object.equals()` because it does not check for
`null` being passed as the parameter. All
`equals()` methods should return `false` if passed
a `null` value.

## FB.NP_EQUALS_SHOULD_HANDLE_NULL_ARGUMENT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This implementation of `equals(Object)` violates the contract defined
by `java.lang.Object.equals()` because it does not check for
`null` being passed as the argument. All
`equals()` methods should return `false` if passed
a `null` value.

## FB.NP_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This is a read of a field is never initialized within any constructor, and is
therefore could be `null` after the object is initialized. This might
be a coding error, or else the class containing the field is written in a way that
depends upon methods being called in some specific order (a little bit dodgy, but
not necessarily wrong).

## FB.NP_GUARANTEED_DEREF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

There is a statement or branch that if executed guarantees that a value is
`null` at this point, and that value that is guaranteed to be
dereferenced (except on forward paths involving runtime exceptions).

Note that a check such as

```
if (x == null) throw new
            NullPointerException();
```

is treated as a dereference of
`x`.

## FB.NP_GUARANTEED_DEREF_ON_EXCEPTION_PATH

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

There is a statement or branch on an exception path that if executed guarantees that
a value is null at this point, and that value that is guaranteed to be dereferenced
(except on forward paths involving runtime exceptions).

## FB.NP_IMMEDIATE_DEREFERENCE_OF_READLINE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

The result of invoking `readLine()` is immediately dereferenced. If
there are no more lines of text to read, `readLine()` will return
`null` and dereferencing that will generate a null pointer
exception.

## FB.NP_LOAD_OF_KNOWN_NULL_VALUE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

The variable referenced at this point is known to be null due to an earlier check
against `null`. Although this is valid, it might be a mistake
(perhaps you intended to refer to a different variable, or perhaps the earlier check
to see if the variable is `null` should have been a check to see if
it was non-null).

## FB.NP_METHOD_PARAMETER_RELAXING_ANNOTATION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A method should always implement the contract of a method it overrides. Thus, if a
method takes a parameter that is marked as `@Nullable`, you shouldn't
override that method in a subclass with a method where that parameter is
`@Nonnull`. Doing so violates the contract that the method should
handle a null parameter.

## FB.NP_METHOD_PARAMETER_TIGHTENS_ANNOTATION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A method should always implement the contract of a method it overrides. Thus, if a
method takes a parameter that is marked as `@Nullable`, you shouldn't
override that method in a subclass with a method where that parameter is
`@Nonnull`. Doing so violates the contract that the method should
handle a null parameter.

## FB.NP_METHOD_RETURN_RELAXING_ANNOTATION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A method should always implement the contract of a method it overrides. Thus, if a
method takes is annotated as returning a `@Nonnull` value, you
shouldn't override that method in a subclass with a method annotated as returning a
`@Nullable` or `@CheckForNull` value. Doing so
violates the contract that the method shouldn't return null.

## FB.NP_NONNULL_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

The field is marked as non-null, but isn't written to by the constructor. The field
might be initialized elsewhere during constructor, or might always be initialized
before use.

## FB.NP_NONNULL_PARAM_VIOLATION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This method passes a null value as the parameter of a method which must be non-null.
Either this parameter has been explicitly marked as `@Nonnull`, or
analysis has determined that this parameter is always dereferenced.

## FB.NP_NONNULL_RETURN_VIOLATION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This method may return a null value, but the method (or a superclass method which it
overrides) is declared to return `@Nonnull`.

## FB.NP_NULL_INSTANCEOF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This `instanceof` test will always return false, since the value being
checked is guaranteed to be `null`. Although this is safe, make sure
it isn't an indication of some misunderstanding or some other logic error.

## FB.NP_NULL_ON_SOME_PATH

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

There is a branch of statement that, *if executed,* guarantees that a null value
will be dereferenced, which would generate a `NullPointerException`
when the code is executed. Of course, the problem might be that the branch or
statement is infeasible and that the null pointer exception can't ever be executed;
deciding that is beyond the ability of SpotBugs.

## FB.NP_NULL_ON_SOME_PATH_EXCEPTION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A reference value which is null on some exception control path is dereferenced here.
This may lead to a `NullPointerException` when the code is executed.
Note that because SpotBugs currently does not prune infeasible exception paths, this
may be a false warning.

Also note that SpotBugs considers the default case of a switch statement to be an
exception path, since the default case is often infeasible.

## FB.NP_NULL_ON_SOME_PATH_FROM_RETURN_VALUE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

The return value from a method is dereferenced without a null check, and the return
value of that method is one that should generally be checked for null. This may lead
to a `NullPointerException` when the code is executed.

## FB.NP_NULL_ON_SOME_PATH_MIGHT_BE_INFEASIBLE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

There is a branch of statement that, *if executed,* guarantees that a null value
will be dereferenced, which would generate a `NullPointerException`
when the code is executed. Of course, the problem might be that the branch or
statement is infeasible and that the null pointer exception can't ever be executed;
deciding that is beyond the ability of SpotBugs. Due to the fact that this value had
been previously tested for nullness, this is a definite possibility.

## FB.NP_NULL_PARAM_DEREF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This method call passes a null value for a non-null method parameter. Either the
parameter is annotated as a parameter that should always be non-null, or analysis
has shown that it will always be dereferenced.

## FB.NP_NULL_PARAM_DEREF_ALL_TARGETS_DANGEROUS

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A possibly-null value is passed at a call site where all known target methods require
the parameter to be non-null. Either the parameter is annotated as a parameter that
should always be non-null, or analysis has shown that it will always be
dereferenced.

## FB.NP_NULL_PARAM_DEREF_NONVIRTUAL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A possibly-null value is passed to a non-null method parameter. Either the parameter
is annotated as a parameter that should always be non-null, or analysis has shown
that it will always be dereferenced.

## FB.NP_OPTIONAL_RETURN_NULL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

The usage of Optional return type (`java.util.Optional` or
`com.google.common.base.Optional`) always means that explicit
null returns were not desired by design. Returning a null value in such case is a
contract violation and will most likely break client code.

## FB.NP_PARAMETER_MUST_BE_NONNULL_BUT_MARKED_AS_​NULLABLE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This parameter is always used in a way that requires it to be non-null, but the
parameter is explicitly annotated as being `Nullable`. Either the use
of the parameter or the annotation is wrong.

## FB.NP_STORE_INTO_NONNULL_FIELD

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A value that could be null is stored into a field that has been annotated as
`@Nonnull`.

## FB.NP_SYNC_AND_NULL_CHECK_FIELD

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | NP: Null pointer dereference | [CWE-585](http://cwe.mitre.org/data/definitions/585.html) |

Since the field is synchronized on, it seems not likely to be null. If it is null and
then synchronized on a `NullPointerException` will be thrown and the
check would be pointless. Better to synchronize on another field.

## FB.NP_TOSTRING_COULD_RETURN_NULL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This toString method seems to return null in some circumstances. A liberal reading of
the spec could be interpreted as allowing this, but it is probably a bad idea and
could cause other code to break. Return the empty string or some other appropriate
string rather than null.

## FB.NP_UNWRITTEN_FIELD

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

The program is dereferencing a field that does not seem to ever have a non-null value
written to it. Unless the field is initialized via some mechanism not seen by the
analysis, dereferencing this value will generate a null pointer exception.

## FB.NP_UNWRITTEN_PUBLIC_OR_PROTECTED_FIELD

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | NP: Null pointer dereference | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

The program is dereferencing a public or protected field that does not seem to ever
have a non-null value written to it. Unless the field is initialized via some
mechanism not seen by the analysis, dereferencing this value will generate a null
pointer exception.

## FB.NS_DANGEROUS_NON_SHORT_CIRCUIT

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | NS: Suspicious use of non-short-circuit boolean operator |

This code seems to be using non-short-circuit logic (e.g., `&` or
`|`) rather than short-circuit logic (`&&`
or `||`). In addition, it seem possible that, depending on the value
of the left hand side, you might not want to evaluate the right hand side (because
it would have side effects, could cause an exception or could be expensive.

Non-short-circuit logic causes both sides of the expression to be evaluated even when
the result can be inferred from knowing the left-hand side. This can be less
efficient and can result in errors if the left-hand side guards cases when
evaluating the right-hand side can generate an error.

See [the Java Language Specification](https://docs.oracle.com/javase/specs/jls/se7/html/jls-15.html#jls-15.22.2) for details.

## FB.NS_NON_SHORT_CIRCUIT

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | NS: Suspicious use of non-short-circuit boolean operator |

This code seems to be using non-short-circuit logic (e.g., `&` or
`|`) rather than short-circuit logic (`&&`
or `||`). Non-short-circuit logic causes both sides of the expression
to be evaluated even when the result can be inferred from knowing the left-hand
side. This can be less efficient and can result in errors if the left-hand side
guards cases when evaluating the right-hand side can generate an error.

See [the Java Language Specification](https://docs.oracle.com/javase/specs/jls/se7/html/jls-15.html#jls-15.22.2) for details.

## FB.OBL_UNSATISFIED_OBLIGATION

|  |  |
| --- | --- |
| SpotBugs: Experimental | OBL: Unsatisfied obligation to clean up stream or resource |

This method may fail to clean up (close, dispose of) a stream, database object, or
other resource requiring an explicit cleanup operation.

In general, if a method opens a stream or other resource, the method should use a
try/finally block to ensure that the stream or resource is cleaned up before the
method returns.

This bug pattern is essentially the same as the OS_OPEN_STREAM and
ODR_OPEN_DATABASE_RESOURCE bug patterns, but is based on a different (and hopefully
better) static analysis technique. We are interested is getting feedback about the
usefulness of this bug pattern. For sending feedback, check:

- <https://github.com/spotbugs/spotbugs/>
- [malinglist](https://github.com/spotbugs/discuss/issues?q=)

In particular, the false-positive suppression heuristics for this bug pattern have
not been extensively tuned, so reports about false positives are helpful to us.

See Weimer and Necula, *Finding and Preventing Run-Time Error Handling
Mistakes*, for a description of the analysis technique.

## FB.OBL_UNSATISFIED_OBLIGATION_EXCEPTION_EDGE

|  |  |
| --- | --- |
| SpotBugs: Experimental | OBL: Unsatisfied obligation to clean up stream or resource |

This method may fail to clean up (close, dispose of) a stream, database object, or
other resource requiring an explicit cleanup operation.

In general, if a method opens a stream or other resource, the method should use a
try/finally block to ensure that the stream or resource is cleaned up before the
method returns.

This bug pattern is essentially the same as the OS_OPEN_STREAM and
ODR_OPEN_DATABASE_RESOURCE bug patterns, but is based on a different (and hopefully
better) static analysis technique. We are interested is getting feedback about the
usefulness of this bug pattern. For sending feedback, check:

- [contributing guideline](https://github.com/spotbugs/spotbugs/)
- [malinglist](https://github.com/spotbugs/discuss/issues?q=)

In particular, the false-positive suppression heuristics for this bug pattern have
not been extensively tuned, so reports about false positives are helpful to us.

See Weimer and Necula, *Finding and Preventing Run-Time Error Handling
Mistakes*, for a description of the analysis technique.

## FB.ODR_OPEN_DATABASE_RESOURCE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | ODR: Database resource not closed on all paths |

The method creates a database resource (such as a database connection or row set),
does not assign it to any fields, pass it to other methods, or return it, and does
not appear to close the object on all paths out of the method. Failure to close
database resources on all paths out of a method may result in poor performance, and
could cause the application to have problems communicating with the database.

## FB.ODR_OPEN_DATABASE_RESOURCE_EXCEPTION_PATH

|  |  |
| --- | --- |
| SpotBugs: Bad practice | ODR: Database resource not closed on all paths |

The method creates a database resource (such as a database connection or row set),
does not assign it to any fields, pass it to other methods, or return it, and does
not appear to close the object on all exception paths out of the method. Failure to
close database resources on all paths out of a method may result in poor
performance, and could cause the application to have problems communicating with the
database.

## FB.OS_OPEN_STREAM

|  |  |
| --- | --- |
| SpotBugs: Bad practice | OS: Stream not closed on all paths |

The method creates an IO stream object, does not assign it to any fields, pass it to
other methods that might close it, or return it, and does not appear to close the
stream on all paths out of the method. This may result in a file descriptor leak. It
is generally a good idea to use a `finally` block to ensure that
streams are closed.

## FB.OS_OPEN_STREAM_EXCEPTION_PATH

|  |  |
| --- | --- |
| SpotBugs: Bad practice | OS: Stream not closed on all paths |

The method creates an IO stream object, does not assign it to any fields, pass it to
other methods, or return it, and does not appear to close it on all possible
exception paths out of the method. This may result in a file descriptor leak. It is
generally a good idea to use a `finally` block to ensure that streams
are closed.

## FB.OVERRIDING_METHODS_MUST_INVOKE_SUPER

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | CN: Bad implementation of cloneable idiom | [CWE-580](http://cwe.mitre.org/data/definitions/580.html) |

Super method is annotated with `@OverridingMethodsMustInvokeSuper`,
but the overriding method isn't calling the super method.

## FB.PA_PUBLIC_ARRAY_ATTRIBUTE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | PA: Public Attribute |

[SEI CERT rule OBJ01-J](https://wiki.sei.cmu.edu/confluence/display/java/OBJ01-J.+Limit+accessibility+of+fields)
requires that accessibility of fields must be limited.

## FB.PA_PUBLIC_MUTABLE_OBJECT_ATTRIBUTE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | PA: Public Attribute |

[SEI CERT rule OBJ01-J](https://wiki.sei.cmu.edu/confluence/display/java/OBJ01-J.+Limit+accessibility+of+fields)
requires that accessibility of fields must be limited.

## FB.PA_PUBLIC_PRIMITIVE_ATTRIBUTE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | PA: Public Attribute |

[SEI CERT rule OBJ01-J](https://wiki.sei.cmu.edu/confluence/display/java/OBJ01-J.+Limit+accessibility+of+fields)
requires that accessibility to fields must be limited.

## FB.PERM_SUPER_NOT_CALLED_IN_GETPERMISSIONS

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | PERM: Custom class loader does not call its superclass's `getPermissions()` |

[SEI CERT rule SEC07-J](https://wiki.sei.cmu.edu/confluence/display/java/SEC07-J.+Call+the+superclass%27s+getPermissions%28%29+method+when+writing+a+custom+class+loader) requires that custom
class loaders must always call their superclass's `getPermissions()`
method in their own `getPermissions()` method to initialize the
object they return at the end. Omitting it means that a class defined using this
custom class loader has permissions that are completely independent of those
specified in the systemwide policy file. In effect, the class's permissions override
them.

## FB.PI_DO_NOT_REUSE_PUBLIC_IDENTIFIERS_CLASS_NAMES

|  |  |
| --- | --- |
| SpotBugs: Bad practice | PI: Do not reuse public identifiers from Java Standard Library |

It is good practice to avoid reusing public identifiers from the Java Standard Library as class names in your Java code.

## FB.PI_DO_NOT_REUSE_PUBLIC_IDENTIFIERS_FIELD_NAMES

|  |  |
| --- | --- |
| SpotBugs: Bad practice | PI: Do not reuse public identifiers from Java Standard Library |

It is good practice to avoid reusing public identifiers from the Java Standard Library as field names in your Java code.

## FB.PI_DO_NOT_REUSE_PUBLIC_IDENTIFIERS_LOCAL_VARIABLE_NAMES

|  |  |
| --- | --- |
| SpotBugs: Bad practice | PI: Do not reuse public identifiers from Java Standard Library |

It is good practice to avoid reusing public identifiers from the Java Standard Library as local variables in your Java code.

## FB.PI_DO_NOT_REUSE_PUBLIC_IDENTIFIERS_METHOD_NAMES

|  |  |
| --- | --- |
| SpotBugs: Bad practice | PI: Do not reuse public identifiers from Java Standard Library |

It is good practice to avoid reusing public identifiers from the Java Standard Library as method names in your Java code.

## FB.PS_PUBLIC_SEMAPHORES

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | PS: Public Semaphores |

This class uses synchronization along with `wait()`,
`notify()` or `notifyAll()` on itself (the this
reference). Client classes that use this class, may, in addition, use an instance of
this class as a synchronizing object. Because two classes are using the same object
for synchronization, Multithread correctness is suspect. You should not synchronize
nor call semaphore methods on a public reference. Consider using a internal private
member variable to control synchronization.

## FB.PT_ABSOLUTE_PATH_TRAVERSAL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | PT: Path traversal | [CWE-36](http://cwe.mitre.org/data/definitions/36.html) |

The software uses an HTTP request parameter to construct a pathname that should be
within a restricted directory, but it does not properly neutralize absolute path
sequences such as "`/abs/path`" that can resolve to a location that
is outside of that directory. See <http://cwe.mitre.org/data/definitions/36.html> for more information.

SpotBugs looks only for the most blatant, obvious cases of absolute path traversal.
If SpotBugs found *any*, you *almost certainly* have more vulnerabilities
that SpotBugs doesn't report. If you are concerned about absolute path traversal,
you should seriously consider using a commercial static analysis or pen-testing
tool.

## FB.PT_RELATIVE_PATH_TRAVERSAL

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | PT: Path traversal | [CWE-23](http://cwe.mitre.org/data/definitions/23.html) |

The software uses an HTTP request parameter to construct a pathname that should be
within a restricted directory, but it does not properly neutralize sequences such as
"`..`" that can resolve to a location that is outside of that
directory. See <http://cwe.mitre.org/data/definitions/23.html> for more information.

SpotBugs looks only for the most blatant, obvious cases of relative path traversal.
If SpotBugs found *any*, you *almost certainly* have more vulnerabilities
that SpotBugs doesn't report. If you are concerned about relative path traversal,
you should seriously consider using a commercial static analysis or pen-testing
tool.

## FB.PZLA_PREFER_ZERO_LENGTH_ARRAYS

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | PZLA: Prefer zero length arrays to null to indicate no results |

It is often a better design to return a length zero array rather than a null
reference to indicate that there are no results (i.e., an empty list of results).
This way, no explicit check for null is needed by clients of the method.

On the other hand, using null to indicate "there is no answer to this question" is
probably appropriate. For example, `File.listFiles()` returns an
empty list if given a directory containing no files, and returns null if the file is
not a directory.

## FB.PZ_DONT_REUSE_ENTRY_OBJECTS_IN_ITERATORS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | PZ: Warning inspired by Josh Bloch's and Neal Gafter's Programming Puzzlers |

The `entrySet()` method is allowed to return a view of the underlying
Map which is both an Iterator and `Map.Entry`. This clever idea was
used in several Map implementations, but introduces the possibility of nasty coding
mistakes. If a map `m` returns such an iterator for an
`entrySet`, then `c.addAll(m.entrySet())` will go
badly wrong. All of the Map implementations in OpenJDK 1.7 have been rewritten to
avoid this, you should to.

## FB.QBA_QUESTIONABLE_BOOLEAN_ASSIGNMENT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | QBA: Questionable Boolean Assignment | [CWE-481](http://cwe.mitre.org/data/definitions/481.html) |

This method assigns a literal boolean value (`true` or
`false`) to a boolean variable inside an if or while expression.
Most probably this was supposed to be a boolean comparison using
`==`, not an assignment using `=`.

## FB.QF_QUESTIONABLE_FOR_LOOP

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | QF: Questionable for loops |

Are you sure this for loop is incrementing the correct variable? It appears that
another variable is being initialized and checked by the for loop.

## FB.RANGE_ARRAY_INDEX

|  |  |
| --- | --- |
| SpotBugs: Correctness | RANGE: Range checks |

Array operation is performed, but array index is out of bounds, which will result in
`ArrayIndexOutOfBoundsException` at runtime.

## FB.RANGE_ARRAY_LENGTH

|  |  |
| --- | --- |
| SpotBugs: Correctness | RANGE: Range checks |

Method is called with array parameter and length parameter, but the length is out of
bounds. This will result in `IndexOutOfBoundsException` at
runtime.

## FB.RANGE_ARRAY_OFFSET

|  |  |
| --- | --- |
| SpotBugs: Correctness | RANGE: Range checks |

Method is called with array parameter and offset parameter, but the offset is out of
bounds. This will result in `IndexOutOfBoundsException` at
runtime.

## FB.RANGE_STRING_INDEX

|  |  |
| --- | --- |
| SpotBugs: Correctness | RANGE: Range checks |

String method is called and specified string index is out of bounds. This will result
in `StringIndexOutOfBoundsException` at runtime.

## FB.RCN_REDUNDANT_COMPARISON_OF_NULL_AND_NONNULL_VALUE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RCN: Redundant comparison to null | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This method contains a reference known to be non-null with another reference known to
be null.

## FB.RCN_REDUNDANT_COMPARISON_TWO_NULL_VALUES

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RCN: Redundant comparison to null | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This method contains a redundant comparison of two references known to both be
definitely null.

## FB.RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RCN: Redundant comparison to null | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This method contains a redundant check of a known non-null value against the constant
null.

## FB.RCN_REDUNDANT_NULLCHECK_OF_NULL_VALUE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RCN: Redundant comparison to null | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

This method contains a redundant check of a known null value against the constant
null.

## FB.RCN_REDUNDANT_NULLCHECK_WOULD_HAVE_BEEN_A_NPE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RCN: Redundant comparison to null | [CWE-476](http://cwe.mitre.org/data/definitions/476.html) |

A value is checked here to see whether it is null, but this value can't be null
because it was previously dereferenced and if it were null a null pointer exception
would have occurred at the earlier dereference. Essentially, this code and the
previous dereference disagree as to whether this value is allowed to be null. Either
the check is redundant or the previous dereference is erroneous.

## FB.RC_REF_COMPARISON

|  |  |
| --- | --- |
| SpotBugs: Correctness | RC: Questionable use of reference equality rather than calling equals |

This method compares two reference values using the `==` or
`!=` operator, where the correct way to compare instances of this
type is generally with the `equals()` method. It is possible to
create distinct instances that are equal but do not compare as `==`
since they are different objects. Examples of classes which should generally not be
compared by reference are `java.lang.Integer`,
`java.lang.Float`, etc.

## FB.RC_REF_COMPARISON_BAD_PRACTICE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | RC: Questionable use of reference equality rather than calling equals |

This method compares a reference value to a constant using the `==` or
`!=` operator, where the correct way to compare instances of this
type is generally with the `equals()` method. It is possible to
create distinct instances that are equal but do not compare as `==`
since they are different objects. Examples of classes which should generally not be
compared by reference are `java.lang.Integer`,
`java.lang.Float`, etc.

## FB.RC_REF_COMPARISON_BAD_PRACTICE_BOOLEAN

|  |  |
| --- | --- |
| SpotBugs: Bad practice | RC: Questionable use of reference equality rather than calling equals |

This method compares two Boolean values using the`==` or
`!=` operator. Normally, there are only two Boolean values
(`Boolean.TRUE` and `Boolean.FALSE`), but it is
possible to create other `Boolean` objects using the `new
Boolean(b)` constructor. It is best to avoid such objects, but if they
do exist, then checking `Boolean` objects for equality using
`==` or `!=` will give results than are different
than you would get using `.equals(...)`.

## FB.REC_CATCH_EXCEPTION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | REC: `RuntimeException` capture | [CWE-396](http://cwe.mitre.org/data/definitions/396.html) |

This catch block for Exception also catches any `RuntimeException`,
which could mask programming errors. This code could have been made to compile using
a number of catch blocks for various subtypes of `Exception`, not
including `RuntimeException`, suggesting the programmer did not
intend this catch block to handle `RuntimeExceptions` but used the
single catch block for convenience. There are other reasons to consider such a catch
block dangerous (see [CWE-396](http://cwe.mitre.org/data/definitions/396.html)), but a simple code change that allows
`RuntimeExceptions` to propagate up the call stack is to insert

```
catch (RuntimeException re) {
            throw re; }
```

before `catch (Exception
...`.

## FB.REFLC_REFLECTION_MAY_INCREASE_ACCESSIBILITY_OF_CLASS

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | REFLC: Reflection increasing accessibility of classes |

[SEI CERT SEC05-J](https://wiki.sei.cmu.edu/confluence/display/java/SEC05-J.+Do+not+use+reflection+to+increase+accessibility+of+classes%2C+methods%2C+or+fields) rule forbids the use of
reflection to increase accessibility of classes, methods or fields. If a class in a
package provides a public method which takes an instance of
`java.lang.Class` as its parameter and calls its
`newInstance()` method then it increases accessibility of classes
in the same package without public constructors. An attacker code may call this
method and pass such class to create an instance of it. This should be avoided by
either making the method non-public or by checking for package access permission on
the package. A third possibility is to use the
`java.beans.Beans.instantiate()` method instead of
`java.lang.Class.newInstance()` which checks whether the Class
object being received has any public constructors.

## FB.REFLF_REFLECTION_MAY_INCREASE_ACCESSIBILITY_OF_FIELD

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | REFLF: Reflection increasing accessibility of fields |

[SEI CERT SEC05-J](https://wiki.sei.cmu.edu/confluence/display/java/SEC05-J.+Do+not+use+reflection+to+increase+accessibility+of+classes%2C+methods%2C+or+fields) rule forbids the use of
reflection to increase accessibility of classes, methods or fields. If a class in a
package provides a public method which takes an instance of
`java.lang.reflect.Field` as its parameter and calls a setter (or
`setAccessible())` method then it increases accessibility of
fields in the same package which are private, protected or package private. An
attacker code may call this method and pass such field to change it. This should be
avoided by either making the method non-public or by checking for package access
permission on the package.

## FB.RE_BAD_SYNTAX_FOR_REGULAR_EXPRESSION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RE: Regular expressions | [CWE-185](http://cwe.mitre.org/data/definitions/185.html) |

The code here uses a regular expression that is invalid according to the syntax for
regular expressions. This statement will throw a
`PatternSyntaxException` when executed.

## FB.RE_CANT_USE_FILE_SEPARATOR_AS_REGULAR_EXPRESSION

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RE: Regular expressions | [CWE-185](http://cwe.mitre.org/data/definitions/185.html) |

The code here uses `File.separator` where a regular expression is
required. This will fail on Windows platforms, where the
`File.separator` is a backslash, which is interpreted in a
regular expression as an escape character. Among other options, you can just use

```
File.separatorChar=='\\' ?
            "\\\\" : File.separator
```

instead of
`File.separator`

## FB.RE_POSSIBLE_UNINTENDED_PATTERN

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RE: Regular expressions | [CWE-185](http://cwe.mitre.org/data/definitions/185.html) |

A String function is being invoked and "`.`" or "`|`"
is being passed to a parameter that takes a regular expression as an argument. Is
this what you intended? For example

- `s.replaceAll(".", "/")` will return a `String` in
  which *every* character has been replaced by a '`/`'
  character
- `s.split(".")`
  *always* returns a zero length array of `String`
- `"ab|cd".replaceAll("|", "/")` will return
  "`/a/b/|/c/d/`"
- `"ab|cd".split("|")` will return array with six (!) elements:
  `[, a, b, |, c, d]`

## FB.RI_REDUNDANT_INTERFACES

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | RI: Redundant Interfaces |

This class declares that it implements an interface that is also implemented by a
superclass. This is redundant because once a superclass implements an interface, all
subclasses by default also implement this interface. It may point out that the
inheritance hierarchy has changed since this class was created, and consideration
should be given to the ownership of the interface's implementation.

## FB.RPC_REPEATED_CONDITIONAL_TEST

|  |  |
| --- | --- |
| SpotBugs: Correctness | RpC: Repeated conditional test |

The code contains a conditional test is performed twice, one right after the other
(e.g., `x == 0 || x == 0`). Perhaps the second occurrence is intended
to be something else (e.g., `x == 0 || y == 0`).

## FB.RR_NOT_CHECKED

|  |  |
| --- | --- |
| SpotBugs: Bad practice | RR: Method ignores results of `InputStream.read()` |

This method ignores the return value of one of the variants of
`java.io.InputStream.read()` which can return multiple bytes. If
the return value is not checked, the caller will not be able to correctly handle the
case where fewer bytes were read than the caller requested. This is a particularly
insidious kind of bug, because in many programs, reads from input streams usually do
read the full amount of data requested, causing the program to fail only
sporadically.

## FB.RS_READOBJECT_SYNC

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | RS: Class's `readObject()` method is synchronized |

This serializable class defines a `readObject()` which is
synchronized. By definition, an object created by deserialization is only reachable
by one thread, and thus there is no need for `readObject()` to be
synchronized. If the `readObject()` method itself is causing the
object to become visible to another thread, that is an example of very dubious
coding style.

## FB.RU_INVOKE_RUN

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | Ru: Method invokes run() | [CWE-572](http://cwe.mitre.org/data/definitions/572.html) |

This method explicitly invokes `run()` on an object. In general,
classes implement the `Runnable` interface because they are going to
have their `run()` method invoked in a new thread, in which case
`Thread.start()` is the right method to call.

## FB.RV_01_TO_INT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

A random value from 0 to 1 is being coerced to the integer value 0. You probably want
to multiply the random value by something else before coercing it to an integer, or
use the `Random.nextInt(n)` method.

## FB.RV_ABSOLUTE_VALUE_OF_HASHCODE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code generates a hashcode and then computes the absolute value of that hashcode.
If the hashcode is `Integer.MIN_VALUE`, then the result will be
negative as well (since `Math.abs(Integer.MIN_VALUE) ==
Integer.MIN_VALUE`).

One out of 2^32 strings have a hashCode of `Integer.MIN_VALUE`,
including "`polygenelubricants`" "`GydZG_`" and
"`"DESIGNING WORKHOUSES`".

## FB.RV_ABSOLUTE_VALUE_OF_RANDOM_INT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code generates a random signed integer and then computes the absolute value of
that random integer. If the number returned by the random number generator is
`Integer.MIN_VALUE`, then the result will be negative as well
(since `Math.abs(Integer.MIN_VALUE) == Integer.MIN_VALUE`). (Same
problem arises for long values as well).

## FB.RV_CHECK_COMPARETO_FOR_SPECIFIC_RETURN_VALUE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code invoked a `compareTo`
or compare method, and checks to see if the return value is a specific value, such
as 1 or -1. When invoking these methods, you should only check the sign of the
result, not for any specific non-zero value. While many or most
`compareTo` and compare methods only return -1, 0 or 1, some of
them will return other values.

## FB.RV_CHECK_FOR_POSITIVE_INDEXOF

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The method invokes `String.indexOf` and checks to see if the result is
positive or non-positive. It is much more typical to check to see if the result is
negative or non-negative. It is positive only if the substring checked for occurs at
some place other than at the beginning of the String.

## FB.RV_DONT_JUST_NULL_CHECK_READLINE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The value returned by `readLine` is discarded after checking to see if
the return value is non-null. In almost all situations, if the result is non-null,
you will want to use that non-null value. Calling `readLine` again
will give you a different line.

## FB.RV_EXCEPTION_NOT_THROWN

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code creates an exception (or error) object, but doesn't do anything with it.
For example, something like

```
if (x < 0) {
    new IllegalArgumentException("x must be nonnegative");
}
```

It was probably the intent of the programmer to throw the created exception:

```
if (x < 0) {
    throw new IllegalArgumentException("x must be nonnegative");
}
```

## FB.RV_NEGATING_RESULT_OF_COMPARETO

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code negatives the return value of a `compareTo` or compare
method. This is a questionable or bad programming practice, since if the return
value is `Integer.MIN_VALUE`, negating the return value won't negate
the sign of the result. You can achieve the same intended result by reversing the
order of the operands rather than by negating the results.

## FB.RV_REM_OF_HASHCODE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code computes a `hashCode`, and then computes the remainder of
that value modulo another value. Since the `hashCode` can be
negative, the result of the remainder operation can also be negative.

Assuming you want to ensure that the result of your computation is non-negative, you
may need to change your code. If you know the divisor is a power of 2, you can use a
bitwise and operator instead (i.e., instead of using
`x.hashCode()%n`, use `x.hashCode()&(n-1)`). This
is probably faster than computing the remainder as well. If you don't know that the
divisor is a power of 2, take the absolute value of the result of the remainder
operation (i.e., use `Math.abs(x.hashCode()%n)`).

## FB.RV_REM_OF_RANDOM_INT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code generates a random signed integer and then computes the remainder of that
value modulo another value. Since the random number can be negative, the result of
the remainder operation can also be negative. Be sure this is intended, and strongly
consider using the `Random.nextInt(int)` method instead.

## FB.RV_RETURN_VALUE_IGNORED

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The return value of this method should be checked. One common cause of this warning
is to invoke a method on an immutable object, thinking that it updates the object.
For example, in the following code fragment,

```
String dateString = getHeaderField(name);
dateString.trim();
```

the programmer seems to be thinking that the `trim()` method will
update the `String` referenced by `dateString`. But
since `String`s are immutable, the `trim()` function
returns a new `String` value, which is being ignored here. The code
should be corrected to:

```
String dateString = getHeaderField(name);
dateString = dateString.trim();
```

## FB.RV_RETURN_VALUE_IGNORED2

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The return value of this method should be checked. One common cause of this warning
is to invoke a method on an immutable object, thinking that it updates the object.
For example, in the following code fragment,

```
String dateString = getHeaderField(name);
dateString.trim();
```

the programmer seems to be thinking that the `trim()` method will
update the String referenced by `dateString`. But since
`String`s are immutable, the `trim()` function
returns a new `String` value, which is being ignored here. The code
should be corrected to:

```
String dateString = getHeaderField(name);
dateString = dateString.trim();
```

## FB.RV_RETURN_VALUE_IGNORED_BAD_PRACTICE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Bad practice | RV: Bad use of return value | [CWE-253](http://cwe.mitre.org/data/definitions/253.html) |

This method returns a value that is not checked. The return value should be checked
since it can indicate an unusual or unexpected function execution. For example, the
`File.delete()` method returns `false` if the file
could not be successfully deleted (rather than throwing an
`Exception`). If you don't check the result, you won't notice if
the method invocation signals unexpected behavior by returning an atypical return
value.

## FB.RV_RETURN_VALUE_IGNORED_INFERRED

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code calls a method and ignores the return value. The return value is the same
type as the type the method is invoked on, and from our analysis it looks like the
return value might be important (e.g., like ignoring the return value of
`String.toLowerCase()`).

We are guessing that ignoring the return value might be a bad idea just from a simple
analysis of the body of the method. You can use a `@CheckReturnValue`
annotation to instruct SpotBugs as to whether ignoring the return value of this
method is important or acceptable.

Please investigate this closely to decide whether it is OK to ignore the return
value.

## FB.RV_RETURN_VALUE_IGNORED_NO_SIDE_EFFECT

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

This code calls a method and ignores the return value. However our analysis shows
that the method (including its implementations in subclasses if any) does not
produce any effect other than return value. Thus this call can be removed.

We are trying to reduce the false positives as much as possible, but in some cases
this warning might be wrong. Common false-positive cases include:

- The method is designed to be overridden and produce a side effect in other
  projects which are out of the scope of the analysis.
- The method is called to trigger the class loading which may have a side
  effect.
- The method is called just to get some exception.

If you feel that our assumption is incorrect, you can use a
`@CheckReturnValue` annotation to instruct SpotBugs that ignoring
the return value of this method is acceptable.

## FB.RV_RETURN_VALUE_OF_PUTIFABSENT_IGNORED

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | RV: Bad use of return value | [CWE-440](http://cwe.mitre.org/data/definitions/440.html) |

The `putIfAbsent` method is typically used to ensure that a single
value is associated with a given key (the first value for which put if absent
succeeds). If you ignore the return value and retain a reference to the value passed
in, you run the risk of retaining a value that is not the one that is associated
with the key in the map. If it matters which one you use and you use the one that
isn't stored in the map, your program will behave incorrectly.

## FB.SA_FIELD_DOUBLE_ASSIGNMENT

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | SA: Useless self-operation |

This method contains a double assignment of a field; e.g.

```
int x,y;
public void foo() {
    x = x = 17;
}
```

Assigning to a field twice is useless, and may indicate a logic error or typo.

## FB.SA_FIELD_SELF_ASSIGNMENT

|  |  |
| --- | --- |
| SpotBugs: Correctness | SA: Useless self-operation |

This method contains a self assignment of a field; e.g.

```
int x;
public void foo() {
    x = x;
}
```

Such assignments are useless, and may indicate a logic error or typo.

## FB.SA_FIELD_SELF_COMPARISON

|  |  |
| --- | --- |
| SpotBugs: Correctness | SA: Useless self-operation |

This method compares a field with itself, and may indicate a typo or a logic error.
Make sure that you are comparing the right things.

## FB.SA_FIELD_SELF_COMPUTATION

|  |  |
| --- | --- |
| SpotBugs: Correctness | SA: Useless self-operation |

This method performs a nonsensical computation of a field with another reference to
the same field (e.g., `x&x` or `x-x`). Because of
the nature of the computation, this operation doesn't seem to make sense, and may
indicate a typo or a logic error. Double check the computation.

## FB.SA_LOCAL_DOUBLE_ASSIGNMENT

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | SA: Useless self-operation |

This method contains a double assignment of a local variable; e.g.

```
public void foo() {
    int x,y;
    x = x = 17;
}
```

Assigning the same value to a variable twice is useless, and may indicate a logic
error or typo.

## FB.SA_LOCAL_SELF_ASSIGNMENT

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | SA: Useless self-operation |

This method contains a self assignment of a local variable; e.g.

```
public void foo() {
    int x = 3;
    x = x;
}
```

Such assignments are useless, and may indicate a logic error or typo.

## FB.SA_LOCAL_SELF_ASSIGNMENT_INSTEAD_OF_FIELD

|  |  |
| --- | --- |
| SpotBugs: Correctness | SA: Useless self-operation |

This method contains a self assignment of a local variable, and there is a field with
an identical name. assignment appears to have been ; e.g.

```
int foo;
    public void setFoo(int foo) {
        foo = foo;
    }
```

The assignment is useless. Did you mean to assign to the field instead?

## FB.SA_LOCAL_SELF_COMPARISON

|  |  |
| --- | --- |
| SpotBugs: Correctness | SA: Useless self-operation |

This method compares a local variable with itself, and may indicate a typo or a logic
error. Make sure that you are comparing the right things.

## FB.SA_LOCAL_SELF_COMPUTATION

|  |  |
| --- | --- |
| SpotBugs: Correctness | SA: Useless self-operation |

This method performs a nonsensical computation of a local variable with another
reference to the same variable (e.g., `x&x` or
`x-x`). Because of the nature of the computation, this operation
doesn't seem to make sense, and may indicate a typo or a logic error. Double check
the computation.

## FB.SBSC_USE_STRINGBUFFER_CONCATENATION

|  |  |
| --- | --- |
| SpotBugs: Performance | SBSC: String concatenation in loop using + operator |

The method seems to be building a String using concatenation in a loop. In each
iteration, the `String` is converted to a
`StringBuffer`/ `StringBuilder`, appended to, and
converted back to a `String`. This can lead to a cost quadratic in
the number of iterations, as the growing string is recopied in each iteration.

Better performance can be obtained by using a `StringBuffer` (or
`StringBuilder` in Java 1.5) explicitly.

For example:

```
// This is bad
String s = "";
for (int i = 0; i < field.length; ++i) {
    s = s + field[i];
}

// This is better
StringBuffer buf = new StringBuffer();
for (int i = 0; i < field.length; ++i) {
    buf.append(field[i]);
}
String s = buf.toString();
```

## FB.SC_START_IN_CTOR

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | SC: Constructor invokes `Thread.start()` |

The constructor starts a thread. This is likely to be wrong if the class is ever
extended/ subclassed, since the thread will be started before the subclass
constructor is started.

## FB.SE_BAD_FIELD

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

This `Serializable` class defines a non-primitive instance field which
is neither transient, `Serializable`, or
`java.lang.Object`, and does not appear to implement the
`Externalizable` interface or the `readObject()`
and `writeObject()` methods. Objects of this class will not be
deserialized correctly if a non-serializable object is stored in this field.

## FB.SE_BAD_FIELD_INNER_CLASS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

This `Serializable` class is an inner class of a non-serializable
class. Thus, attempts to serialize it will also attempt to associate instance of the
outer class with which it is associated, leading to a runtime error.

If possible, making the inner class a static inner class
should solve the problem. Making the outer class serializable might also work, but
that would mean serializing an instance of the inner class would always also
serialize the instance of the outer class, which it often not what you really want.

## FB.SE_BAD_FIELD_STORE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

A non-serializable value is stored into a non-transient field of a serializable
class.

## FB.SE_COMPARATOR_SHOULD_BE_SERIALIZABLE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

Because this class implements the `Comparator` interface, you should
consider whether or not it should also implement the `Serializable`
interface. If a comparator is used to construct an ordered collection such as a
`TreeMap`, then the `TreeMap` will be serializable
only if the comparator is also serializable. As most comparators have little or no
state, making them serializable is generally easy and good defensive
programming.

## FB.SE_INNER_CLASS

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

This `Serializable` class is an
inner class. Any attempt to serialize it will also serialize the associated outer
instance. The outer instance is serializable, so this won't fail, but it might
serialize a lot more data than intended. If possible, making the inner class a
static inner class (also known as a nested class) should solve the problem.

## FB.SE_METHOD_MUST_BE_PRIVATE

|  |  |
| --- | --- |
| SpotBugs: Correctness | Se: Incorrect definition of `Serializable` class |

This class implements the `Serializable` interface, and defines a
method for custom serialization/ deserialization. But since that method isn't
declared private, it will be silently ignored by the serialization/ deserialization
API.

## FB.SE_NONFINAL_SERIALVERSIONID

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

This class defines a `serialVersionUID` field that is not final. The
field should be made final if it is intended to specify the version UID for purposes
of serialization.

## FB.SE_NONLONG_SERIALVERSIONID

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

This class defines a `serialVersionUID` field that is not long. The
field should be made long if it is intended to specify the version UID for purposes
of serialization.

## FB.SE_NONSTATIC_SERIALVERSIONID

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

This class defines a `serialVersionUID` field that is not static. The
field should be made static if it is intended to specify the version UID for
purposes of serialization.

## FB.SE_NO_SERIALVERSIONID

|  |  |
| --- | --- |
| SpotBugs: Bad practice | SnVI: `Serializable` class with no Version ID |

This class implements the `Serializable` interface, but does not
define a `serialVersionUID` field. A change as simple as adding a
reference to a `.class` object will add synthetic fields to the
class, which will unfortunately change the implicit
`serialVersionUID` (e.g., adding a reference to
`String.class` will generate a static field
`class$java$lang$String`). Also, different source code to
bytecode compilers may use different naming conventions for synthetic variables
generated for references to class objects or inner classes. To ensure
interoperability of `Serializable` across versions, consider adding
an explicit `serialVersionUID`.

## FB.SE_NO_SUITABLE_CONSTRUCTOR

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

This class implements the `Serializable` interface and its superclass
does not. When such an object is deserialized, the fields of the superclass need to
be initialized by invoking the void constructor of the superclass. Since the
superclass does not have one, serialization and deserialization will fail at
runtime.

## FB.SE_NO_SUITABLE_CONSTRUCTOR_FOR_EXTERNALIZATION

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

This class implements the `Externalizable` interface, but does not
define a void constructor. When `Externalizable` objects are
deserialized, they first need to be constructed by invoking the void constructor.
Since this class does not have one, serialization and deserialization will fail at
runtime.

## FB.SE_PREVENT_EXT_OBJ_OVERWRITE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of Serializable class |

The `readExternal()` method must be declared as public and is not protected from malicious callers,
so the code permits any caller to reset the value of the object at any time.

## FB.SE_PRIVATE_READ_RESOLVE_NOT_INHERITED

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | Se: Incorrect definition of `Serializable` class |

This class defines a private `readResolve` method. Since it is
private, it won't be inherited by subclasses. This might be intentional and OK, but
should be reviewed to ensure it is what is intended.

## FB.SE_READ_RESOLVE_IS_STATIC

|  |  |
| --- | --- |
| SpotBugs: Correctness | Se: Incorrect definition of `Serializable` class |

In order for the `readResolve` method to be recognized by the
serialization mechanism, it must not be declared as a static method.

## FB.SE_READ_RESOLVE_MUST_RETURN_OBJECT

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

In order for the readResolve method to be recognized by the serialization mechanism,
it must be declared to have a return type of Object.

## FB.SE_TRANSIENT_FIELD_NOT_RESTORED

|  |  |
| --- | --- |
| SpotBugs: Bad practice | Se: Incorrect definition of `Serializable` class |

This class contains a field that is updated at multiple places in the class, thus it
seems to be part of the state of the class. However, since the field is marked as
transient and not set in `readObject` or
`readResolve`, it will contain the default value in any deserialized
instance of the class.

## FB.SE_TRANSIENT_FIELD_OF_NONSERIALIZABLE_CLASS

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | Se: Incorrect definition of `Serializable` class |

The field is marked as transient, but the class isn't `Serializable`,
so marking it as transient has absolutely no effect. This may be leftover marking
from a previous version of the code in which the class was transient, or it may
indicate a misunderstanding of how serialization works.

## FB.SF_DEAD_STORE_DUE_TO_SWITCH_FALLTHROUGH

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | SF: Switch case falls through | [CWE-484](http://cwe.mitre.org/data/definitions/484.html) |

A value stored in the previous switch case is overwritten here due to a switch fall
through. It is likely that you forgot to put a break or return at the end of the
previous case.

## FB.SF_DEAD_STORE_DUE_TO_SWITCH_FALLTHROUGH_TO_THROW

|  |  |  |
| --- | --- | --- |
| SpotBugs: Correctness | SF: Switch case falls through | [CWE-484](http://cwe.mitre.org/data/definitions/484.html) |

A value stored in the previous switch case is ignored here due to a switch fall
through to a place where an exception is thrown. It is likely that you forgot to put
a break or return at the end of the previous case.

## FB.SF_SWITCH_FALLTHROUGH

|  |  |  |
| --- | --- | --- |
| SpotBugs: Dodgy code | SF: Switch case falls through | [CWE-484](http://cwe.mitre.org/data/definitions/484.html) |

This method contains a switch statement where one case branch will fall through to
the next case. Usually you need to end this case with a break or return.

## FB.SF_SWITCH_NO_DEFAULT

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | SF: Switch case falls through |

This method contains a switch statement where default case is missing. Usually you
need to provide a default case.

Because the analysis only looks at the generated
bytecode, this warning can be incorrect triggered if the default case is at the end
of the switch statement and the switch statement doesn't contain break statements
for other cases.

## FB.SIC_INNER_SHOULD_BE_STATIC

|  |  |
| --- | --- |
| SpotBugs: Performance | SIC: Inner class could be made static |

This class is an inner class, but does not use its embedded reference to the object
which created it. This reference makes the instances of the class larger, and may
keep the reference to the creator object alive longer than necessary. If possible,
the class should be made static. *Coverity note:* Android code is particularly
susceptible to resource leaks and performance degradation based on this pattern.

## FB.SIC_INNER_SHOULD_BE_STATIC_ANON

|  |  |
| --- | --- |
| SpotBugs: Performance | SIC: Inner class could be made static |

This class is an inner class, but does not use its embedded reference to the object
which created it. This reference makes the instances of the class larger, and may
keep the reference to the creator object alive longer than necessary. If possible,
the class should be made into a *static* inner class. Since anonymous inner
classes cannot be marked as static, doing this will require refactoring the inner
class so that it is a named inner class.

## FB.SIC_INNER_SHOULD_BE_STATIC_NEEDS_THIS

|  |  |
| --- | --- |
| SpotBugs: Performance | SIC: Inner class could be made static |

This class is an inner class, but does not use its embedded reference to the object
which created it except during construction of the inner object. This reference
makes the instances of the class larger, and may keep the reference to the creator
object alive longer than necessary. If possible, the class should be made into a
*static* inner class. Since the reference to the outer object is required
during construction of the inner instance, the inner class will need to be
refactored so as to pass a reference to the outer instance to the constructor for
the inner class.

## FB.SIC_THREADLOCAL_DEADLY_EMBRACE

|  |  |
| --- | --- |
| SpotBugs: Correctness | SIC: Inner class could be made static |

This class is an inner class, but should probably be a static inner class. As it is,
there is a serious danger of a deadly embrace between the inner class and the thread
local in the outer class. Because the inner class isn't static, it retains a
reference to the outer class. If the thread local contains a reference to an
instance of the inner class, the inner and outer instance will both be reachable and
not eligible for garbage collection.

## FB.SING_SINGLETON_GETTER_NOT_SYNCHRONIZED

|  |  |
| --- | --- |
| SpotBugs: Correctness | SING: Singleton problems |

Instance-getter method of class using singleton design pattern is not synchronized.

## FB.SING_SINGLETON_HAS_NONPRIVATE_CONSTRUCTOR

|  |  |
| --- | --- |
| SpotBugs: Correctness | SING: Singleton problems |

This class is using singleton design pattern and has non-private constructor (please note that a default constructor might exist which is not private).

## FB.SING_SINGLETON_IMPLEMENTS_CLONEABLE

|  |  |
| --- | --- |
| SpotBugs: Correctness | SING: Singleton problems |

If a class using singleton design pattern directly implements the `Cloneable`
interface, it is possible to create a copy of the object, thus violating the
singleton pattern. Therefore, implementing the `Cloneable` interface
should be avoided. For more information, see: [SEI CERT MSC07-J](https://wiki.sei.cmu.edu/confluence/display/java/MSC07-J.+Prevent+multiple+instantiations+of+singleton+objects).

## FB.SING_SINGLETON_IMPLEMENTS_CLONE_METHOD

|  |  |
| --- | --- |
| SpotBugs: Correctness | SING: Singleton problems |

This class is using singleton design pattern and does not implement the
`Cloneable` interface, but implements the
`clone()` method without being an unconditional
`CloneNotSupportedException`-thrower.

## FB.SING_SINGLETON_IMPLEMENTS_SERIALIZABLE

|  |  |
| --- | --- |
| SpotBugs: Correctness | SING: Singleton problems |

This class (using singleton design pattern) directly or indirectly implements the
`Serializable` interface, which allows the class to be
serialized. Deserialization makes multiple instantiation of a singleton class
possible, and therefore should be avoided. For more information, see: [SEI CERT MSC07-J](https://wiki.sei.cmu.edu/confluence/display/java/MSC07-J.+Prevent+multiple+instantiations+of+singleton+objects).

## FB.SING_SINGLETON_INDIRECTLY_IMPLEMENTS_CLONEABLE

|  |  |
| --- | --- |
| SpotBugs: Correctness | SING: Singleton problems |

If a class using singleton design pattern indirectly implements the `Cloneable`
interface, it is possible to create a copy of the object, thus violating the
singleton pattern. Therefore, implementing the `Cloneable` interface
should be avoided.

## FB.SIO_SUPERFLUOUS_INSTANCEOF

|  |  |
| --- | --- |
| SpotBugs: Correctness | SIO: Superfluous `instanceof` |

Type check performed using the `instanceof` operator where it can be
statically determined whether the object is of the type requested.

## FB.SI_INSTANCE_BEFORE_FINALS_ASSIGNED

|  |  |
| --- | --- |
| SpotBugs: Bad practice | SI: Suspicious static initializer |

The class's static initializer creates an instance of the class before all of the
static fields are assigned.

## FB.SKIPPED_CLASS_TOO_BIG

|  |  |
| --- | --- |
| SpotBugs: Experimental | SKIPPED: Analysis skipped |

This class is bigger than can be effectively handled, and was not fully analyzed for
errors.

## FB.SP_SPIN_ON_FIELD

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | SP: Method spins on field |

This method spins in a loop which reads a field. The compiler may legally hoist the
read out of the loop, turning the code into an infinite loop. The class should be
changed so it uses proper synchronization (including `wait` and
`notify` calls).

## FB.SQL_BAD_PREPARED_STATEMENT_ACCESS

|  |  |
| --- | --- |
| SpotBugs: Correctness | SQL: Potential SQL Problem |

A call to a `setXXX` method of a prepared statement was made where the
parameter index is 0. As parameter indexes start at index 1, this is always a
mistake.

## FB.SQL_BAD_RESULTSET_ACCESS

|  |  |
| --- | --- |
| SpotBugs: Correctness | SQL: Potential SQL Problem |

A call to `getXXX` or `updateXXX` methods of a result
set was made where the field index is 0. As `ResultSet` fields start
at index 1, this is always a mistake.

## FB.SQL_NONCONSTANT_STRING_PASSED_TO_EXECUTE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | SQL: Potential SQL Problem | [CWE-89](http://cwe.mitre.org/data/definitions/89.html) |

The method invokes the `execute` or `addBatch` method
on an SQL statement with a `String` that seems to be dynamically
generated. Consider using a prepared statement instead. It is more efficient and
less vulnerable to SQL injection attacks.

## FB.SQL_PREPARED_STATEMENT_GENERATED_​FROM_​NONCONSTANT_​STRING

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | SQL: Potential SQL Problem | [CWE-89](http://cwe.mitre.org/data/definitions/89.html) |

The code creates an SQL prepared statement from a non-constant
`String`. If unchecked, tainted data from a user is used in
building this String, SQL injection could be used to make the prepared statement do
something unexpected and undesirable.

## FB.SR_NOT_CHECKED

|  |  |
| --- | --- |
| SpotBugs: Bad practice | RR: Method ignores results of `InputStream.read()` |

This method ignores the return value of `java.io.InputStream.skip()`
which can skip multiple bytes. If the return value is not checked, the caller will
not be able to correctly handle the case where fewer bytes were skipped than the
caller requested. This is a particularly insidious kind of bug, because in many
programs, skips from input streams usually do skip the full amount of data
requested, causing the program to fail only sporadically. With Buffered streams,
however, `skip()` will only skip data in the buffer, and will
routinely fail to skip the requested number of bytes.

## FB.SSD_DO_NOT_USE_INSTANCE_LOCK_ON_SHARED_STATIC_DATA

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | SSD: Do not use an instance lock to protect shared static data |

If the lock or the synchronized method is not static, that modifies the static field,
that could leave the shared static data unprotected against concurrent access. This
could occur in two ways, if a synchronization method uses a non-static lock object,
or a synchronized method is declared as non-static. Both ways are ineffective. Best
solution is to use a private static final lock object to secure the shared static
data.

See SEI CERT rule  [LCK06-J. Do not use an instance lock to protect
shared static data](https://wiki.sei.cmu.edu/confluence/display/java/LCK06-J.+Do+not+use+an+instance+lock+to+protect+shared+static+data).

## FB.SS_SHOULD_BE_STATIC

|  |  |
| --- | --- |
| SpotBugs: Performance | SS: Unread field should be static |

This class contains an instance final field that is initialized to a compile-time
static value. Consider making the field static.

## FB.STCAL_INVOKE_ON_STATIC_CALENDAR_INSTANCE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | STCAL: Static use of type `Calendar` or `DateFormat` | [CWE-366](http://cwe.mitre.org/data/definitions/366.html) |

Even though the JavaDoc does not contain a hint about it, Calendars are inherently
unsafe for multithreaded use. The detector has found a call to an instance of
`Calendar` that has been obtained via a static field. This looks
suspicious.

For more information on this see [JDK Bug #6231579](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6231579) and [JDK Bug #6178997](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6178997).

## FB.STCAL_INVOKE_ON_STATIC_DATE_FORMAT_INSTANCE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | STCAL: Static use of type `Calendar` or `DateFormat` | [CWE-366](http://cwe.mitre.org/data/definitions/366.html) |

As the JavaDoc states, DateFormats are inherently unsafe for multithreaded use. The
detector has found a call to an instance of `DateFormat` that has
been obtained via a static field. This looks suspicious.

For more information on this see [JDK Bug #6231579](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6231579) and [JDK Bug #6178997](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6178997).

## FB.STCAL_STATIC_CALENDAR_INSTANCE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | STCAL: Static use of type `Calendar` or `DateFormat` | [CWE-366](http://cwe.mitre.org/data/definitions/366.html) |

Even though the JavaDoc does not contain a hint about it, Calendars are inherently
unsafe for multithreaded use. Sharing a single instance across thread boundaries
without proper synchronization will result in erratic behavior of the application.
Under 1.4 problems seem to surface less often than under Java 5 where you will
probably see random `ArrayIndexOutOfBoundsExceptions` or
`IndexOutOfBoundsExceptions` in
`sun.util.calendar.BaseCalendar.getCalendarDateFromFixedDate()`.

You may also experience serialization problems.

Using an instance field is recommended.

For more information on this see [JDK Bug #6231579](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6231579) and [JDK Bug #6178997](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6178997).

## FB.STCAL_STATIC_SIMPLE_DATE_FORMAT_INSTANCE

|  |  |  |
| --- | --- | --- |
| SpotBugs: Multithreaded correctness | STCAL: Static use of type `Calendar` or `DateFormat` | [CWE-366](http://cwe.mitre.org/data/definitions/366.html) |

As the JavaDoc states, DateFormats are inherently unsafe for multithreaded use.
Sharing a single instance across thread boundaries without proper synchronization
will result in erratic behavior of the application.

You may also experience serialization problems.

Using an instance field is recommended.

For more information on this see [JDK Bug #6231579](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6231579) and [JDK Bug #6178997](http://bugs.java.com/bugdatabase/view_bug.do?bug_id=6178997).

## FB.STI_INTERRUPTED_ON_CURRENTTHREAD

|  |  |
| --- | --- |
| SpotBugs: Correctness | STI: Suspicious `Thread` Interrupted |

This method invokes the `Thread.currentThread()` call, just to call
the `interrupted()` method. As `interrupted()` is a
static method, is more simple and clear to use
`Thread.interrupted()`.

## FB.STI_INTERRUPTED_ON_UNKNOWNTHREAD

|  |  |
| --- | --- |
| SpotBugs: Correctness | STI: Suspicious `Thread` Interrupted |

This method invokes the `Thread.interrupted()` method on a
`Thread` object that appears to be a `Thread`
object that is not the current thread. As the `interrupted()` method
is static, the `interrupted` method will be called on a different
object than the one the author intended.

## FB.ST_WRITE_TO_STATIC_FROM_INSTANCE_METHOD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | ST: Misuse of static fields |

This instance method writes to a static field. This is tricky to get correct if
multiple instances are being manipulated, and generally bad practice.

## FB.SWL_SLEEP_WITH_LOCK_HELD

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | SWL: Sleep with lock held |

This method calls `Thread.sleep()` with a lock held. This may result
in very poor performance and scalability, or a deadlock, since other threads may be
waiting to acquire the lock. It is a much better idea to call
`wait()` on the lock, which releases the lock and allows other
threads to run.

## FB.SW_SWING_METHODS_INVOKED_IN_SWING_THREAD

|  |  |
| --- | --- |
| SpotBugs: Bad practice | SW: Swing coding rules |

([From JDC Tech Tip](http://web.archive.org/web/20090526170426/http://java.sun.com/developer/JDCTechTips/2003/tt1208.html)): The `Swing` methods
`show()`, `setVisible()`, and
`pack()` will create the associated peer for the frame. With the
creation of the peer, the system creates the event dispatch thread. This makes
things problematic because the event dispatch thread could be notifying listeners
while pack and validate are still processing. This situation could result in two
threads going through the `Swing` component-based GUI -- it's a
serious flaw that could result in deadlocks or other related threading issues. A
pack call causes components to be realized. As they are being realized (that is, not
necessarily visible), they could trigger listener notification on the event dispatch
thread.

## FB.TESTING

|  |  |
| --- | --- |
| SpotBugs: Experimental | TEST: Testing prototype and incomplete bug pattern |

This bug pattern is only generated by new, incompletely implemented bug
detectors.

## FB.TESTING1

|  |  |
| --- | --- |
| SpotBugs: Experimental | TEST: Testing prototype and incomplete bug pattern |

This bug pattern is only generated by new, incompletely implemented bug
detectors.

## FB.TESTING2

|  |  |
| --- | --- |
| SpotBugs: Experimental | TEST: Testing prototype and incomplete bug pattern |

This bug pattern is only generated by new, incompletely implemented bug
detectors.

## FB.TESTING3

|  |  |
| --- | --- |
| SpotBugs: Experimental | TEST: Testing prototype and incomplete bug pattern |

This bug pattern is only generated by new, incompletely implemented bug
detectors.

## FB.THROWS_METHOD_THROWS_CLAUSE_BASIC_EXCEPTION

|  |  |
| --- | --- |
| SpotBugs: Bad practice | THROWS: Exception throwing related problems |

Method lists `Exception` in its `throws` clause. When
declaring a method, the types of exceptions in the `throws` clause
should be the most specific. Therefore, using `Exception` in the
`throws` clause would force the caller to either use it in its
own `throws` clause, or use it in a
`try`-`catch` block (when it does not necessarily
contain any meaningful information about the thrown exception). For more
information, see the [SEI CERT ERR07-J rule](https://wiki.sei.cmu.edu/confluence/display/java/ERR07-J.+Do+not+throw+RuntimeException%2C+Exception%2C+or+Throwable).

## FB.THROWS_METHOD_THROWS_CLAUSE_THROWABLE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | THROWS: Exception throwing related problems |

Method lists `Throwable` in its `throws` clause. When
declaring a method, the types of exceptions in the `throws` clause
should be the most specific. Therefore, using `Throwable` in the
throws clause would force the caller to either use it in its own
`throws` clause, or use it in a
`try`-`catch` block (when it does not necessarily
contain any meaningful information about the thrown exception). Furthermore, using
`Throwable` like that is semantically a bad practice, considered
that Throwables include Errors as well, but by definition they occur in
unrecoverable scenarios. For more information, see the [SEI CERT ERR07-J rule](https://wiki.sei.cmu.edu/confluence/display/java/ERR07-J.+Do+not+throw+RuntimeException%2C+Exception%2C+or+Throwable).

## FB.THROWS_METHOD_THROWS_RUNTIMEEXCEPTION

|  |  |
| --- | --- |
| SpotBugs: Bad practice | THROWS: Exception throwing related problems |

Method intentionally throws `RuntimeException`. According to the [SEI CERT ERR07-J rule](https://wiki.sei.cmu.edu/confluence/display/java/ERR07-J.+Do+not+throw+RuntimeException%2C+Exception%2C+or+Throwable), throwing a
`RuntimeException` may cause errors, like the caller not being
able to examine the exception and therefore cannot properly recover from it.
Moreover, throwing a `RuntimeException` would force the caller to
catch `RuntimeException` and therefore violate the [SEI CERT ERR08-J rule](https://wiki.sei.cmu.edu/confluence/display/java/ERR08-J.+Do+not+catch+NullPointerException+or+any+of+its+ancestors). Please note that
you can derive from `Exception` or `RuntimeException`
and may throw a new instance of that exception.

## FB.TLW_TWO_LOCK_NOTIFY

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | TLW: Wait with two locks held |

The code calls `notify()` or `notifyAll()` while two
locks are held. If this notification is intended to wake up a
`wait()` that is holding the same locks, it may deadlock, since
the wait will only give up one lock and the notify will be unable to get both locks,
and thus the notify will not succeed. If there is also a warning about a two lock
wait, the probably of a bug is quite high.

## FB.TLW_TWO_LOCK_WAIT

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | TLW: Wait with two locks held |

Waiting on a monitor while two locks are held may cause deadlock. Performing a wait
only releases the lock on the object being waited on, not any other locks. This not
necessarily a bug, but is worth examining closely.

## FB.TQ_ALWAYS_VALUE_USED_WHERE_NEVER_REQUIRED

|  |  |
| --- | --- |
| SpotBugs: Correctness | TQ: Inconsistent use of type qualifier annotations |

A value specified as carrying a type qualifier annotation is consumed in a location
or locations requiring that the value not carry that annotation.

More precisely, a value annotated with a type qualifier specifying
`when=ALWAYS` is guaranteed to reach a use or uses where the same
type qualifier specifies `when=NEVER`.

For example, say that `@NonNegative` is a nickname for the type
qualifier annotation `@Negative(when=When.NEVER)`. The following code
will generate this warning because the return statement requires a
`@NonNegative` value, but receives one that is marked as
`@Negative`.

```
public @NonNegative Integer example(@Negative Integer value) {
    return value;
}
```

## FB.TQ_COMPARING_VALUES_WITH_INCOMPATIBLE_TYPE_QUALIFIERS

|  |  |
| --- | --- |
| SpotBugs: Correctness | TQ: Inconsistent use of type qualifier annotations |

A value specified as carrying a type qualifier annotation is compared with a value
that doesn't ever carry that qualifier.

More precisely, a value annotated with a type qualifier specifying
`when=ALWAYS` is compared with a value that where the same type
qualifier specifies `when=NEVER`.

For example, say that `@NonNegative` is a nickname for the type
qualifier annotation @`Negative(when=When.NEVER)`. The following code
will generate this warning because the return statement requires a
`@NonNegative` value, but receives one that is marked as
`@Negative`.

```
public boolean example(@Negative Integer value1, @NonNegative Integer value2) {
    return value1.equals(value2);
}
```

## FB.TQ_EXPLICIT_UNKNOWN_SOURCE_VALUE_REACHES_ALWAYS_SINK

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | TQ: Inconsistent use of type qualifier annotations |

A value is used in a way that requires it to be always be a value denoted by a type
qualifier, but there is an explicit annotation stating that it is not known where
the value is required to have that type qualifier. Either the usage or the
annotation is incorrect.

## FB.TQ_EXPLICIT_UNKNOWN_SOURCE_VALUE_REACHES_NEVER_SINK

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | TQ: Inconsistent use of type qualifier annotations |

A value is used in a way that requires it to be never be a value denoted by a type
qualifier, but there is an explicit annotation stating that it is not known where
the value is prohibited from having that type qualifier. Either the usage or the
annotation is incorrect.

## FB.TQ_MAYBE_SOURCE_VALUE_REACHES_ALWAYS_SINK

|  |  |
| --- | --- |
| SpotBugs: Correctness | TQ: Inconsistent use of type qualifier annotations |

A value that is annotated as possibility not being an instance of the values denoted
by the type qualifier, and the value is guaranteed to be used in a way that requires
values denoted by that type qualifier.

## FB.TQ_MAYBE_SOURCE_VALUE_REACHES_NEVER_SINK

|  |  |
| --- | --- |
| SpotBugs: Correctness | TQ: Inconsistent use of type qualifier annotations |

A value that is annotated as possibility being an instance of the values denoted by
the type qualifier, and the value is guaranteed to be used in a way that prohibits
values denoted by that type qualifier.

## FB.TQ_NEVER_VALUE_USED_WHERE_ALWAYS_REQUIRED

|  |  |
| --- | --- |
| SpotBugs: Correctness | TQ: Inconsistent use of type qualifier annotations |

A value specified as not carrying a type qualifier annotation is guaranteed to be
consumed in a location or locations requiring that the value does carry that
annotation.

More precisely, a value annotated with a type qualifier specifying
`when=NEVER` is guaranteed to reach a use or uses where the same
type qualifier specifies `when=ALWAYS`.

## FB.TQ_UNKNOWN_VALUE_USED_WHERE_ALWAYS_STRICTLY_REQUIRED

|  |  |
| --- | --- |
| SpotBugs: Correctness | TQ: Inconsistent use of type qualifier annotations |

A value is being used in a way that requires the value be annotation with a type
qualifier. The type qualifier is strict, so the tool rejects any values that do not
have the appropriate annotation.

To coerce a value to have a strict annotation, define an identity function where the
return value is annotated with the strict annotation. This is the only way to turn a
non-annotated value into a value with a strict type qualifier annotation.

## FB.UCF_USELESS_CONTROL_FLOW

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UCF: Useless control flow |

This method contains a useless control flow statement, where control flow continues
onto the same place regardless of whether or not the branch is taken. For example,
this is caused by having an empty statement block for an `if`
statement:

```
if (argv.length == 0) {
    // TODO: handle this case
}
```

## FB.UCF_USELESS_CONTROL_FLOW_NEXT_LINE

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UCF: Useless control flow |

This method contains a useless control flow statement in which control flow follows
to the same or following line regardless of whether or not the branch is taken.
Often, this is caused by inadvertently using an empty statement as the body of an
`if` statement, e.g.:

```
if (argv.length == 1);
    System.out.println("Hello, " + argv[0]);
```

## FB.UC_USELESS_CONDITION

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UC: Useless code |

This condition always produces the same result as the value of the involved variable
that was narrowed before. Probably something else was meant or the condition can be
removed.

## FB.UC_USELESS_CONDITION_TYPE

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UC: Useless code |

This condition always produces the same result due to the type range of the involved
variable. Probably something else was meant or the condition can be removed.

## FB.UC_USELESS_OBJECT

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UC: Useless code |

Our analysis shows that this object is useless. It's created and modified, but its
value never go outside of the method or produce any side-effect. Either there is a
mistake and object was intended to be used or it can be removed.

This analysis rarely produces false-positives. Common false-positive cases
include:

- This object used to implicitly throw some obscure exception.
- This object used as a stub to generalize the code.
- This object used to hold strong references to weak/soft-referenced
  objects.

## FB.UC_USELESS_OBJECT_STACK

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UC: Useless code |

This object is created just to perform some modifications which don't have any
side-effect. Probably something else was meant or the object can be removed.

## FB.UC_USELESS_VOID_METHOD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UC: Useless code |

Our analysis shows that this non-empty void method does not actually perform any
useful work. Please check it: probably there's a mistake in its code or its body can
be fully removed.

We are trying to reduce the false positives as much as possible, but in some cases
this warning might be wrong. Common false-positive cases include:

- The method is intended to trigger loading of some class which may have a side
  effect.
- The method is intended to implicitly throw some obscure exception.

## FB.UG_SYNC_SET_UNSYNC_GET

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | UG: Unsynchronized get method, synchronized set method |

This class contains similarly-named get and set methods where the set method is
synchronized and the get method is not. This may result in incorrect behavior at
runtime, as callers of the get method will not necessarily see a consistent state
for the object. The get method should be made synchronized.

## FB.UI_INHERITANCE_UNSAFE_GETRESOURCE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | UI: Unsafe inheritance |

Calling `this.getClass().getResource(...)` could give results other
than expected if this class is extended by a class in another package.

## FB.UL_UNRELEASED_LOCK

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | UL: Lock not released on all paths |

This method acquires a JSR-166 (`java.util.concurrent`) lock, but does
not release it on all paths out of the method. In general, the correct idiom for
using a JSR-166 lock is:

```
Lock l = ...;
l.lock();
try {
    // do something
} finally {
    l.unlock();
}
```

## FB.UL_UNRELEASED_LOCK_EXCEPTION_PATH

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | UL: Lock not released on all paths |

This method acquires a JSR-166 (`java.util.concurrent`) lock, but does
not release it on all exception paths out of the method. In general, the correct
idiom for using a JSR-166 lock is:

```
Lock l = ...;
l.lock();
try {
    // do something
} finally {
    l.unlock();
}
```

## FB.UMAC_UNCALLABLE_METHOD_OF_ANONYMOUS_CLASS

|  |  |
| --- | --- |
| SpotBugs: Correctness | UMAC: Uncallable method of anonymous class |

This anonymous class defined a method that is not directly invoked and does not
override a method in a superclass. Since methods in other classes cannot directly
invoke methods declared in an anonymous class, it seems that this method is
uncallable. The method might simply be dead code, but it is also possible that the
method is intended to override a method declared in a superclass, and due to an typo
or other error the method does not, in fact, override the method it is intended
to.

## FB.UM_UNNECESSARY_MATH

|  |  |
| --- | --- |
| SpotBugs: Performance | UM: Unnecessary Math on constants |

This method uses a static method from `java.lang.Math` on a constant
value. This method's result in this case, can be determined statically, and is
faster and sometimes more accurate to just use the constant. Methods detected
are:

|  |  |
| --- | --- |
| Method | Parameter |
| abs | -any- |
| acos | 0.0 or 1.0 |
| asin | 0.0 or 1.0 |
| atan | 0.0 or 1.0 |
| atan2 | 0.0 |
| cbrt | 0.0 or 1.0 |
| ceil | -any- |
| cos | 0.0 |
| cosh | 0.0 |
| exp | 0.0 or 1.0 |
| expm1 | 0.0 |
| floor | -any- |
| log | 0.0 or 1.0 |
| log10 | 0.0 or 1.0 |
| rint | -any- |
| round | -any- |
| sin | 0.0 |
| sinh | 0.0 |
| sqrt | 0.0 or 1.0 |
| tan | 0.0 |
| tanh | 0.0 |
| toDegrees | 0.0 or 1.0 |
| toRadians | 0.0 |

## FB.UNKNOWN

|  |  |
| --- | --- |
| SpotBugs: Experimental | TEST: Testing prototype and incomplete bug pattern |

A warning was recorded, but SpotBugs can't find the description of this bug pattern
and so can't describe it. This should occur only in cases of a bug in SpotBugs or
its configuration, or perhaps if an analysis was generated using a plugin, but that
plugin is not currently loaded.

## FB.UOE_USE_OBJECT_EQUALS

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UOE: Use Object Equals |

This method invokes the `.equals(Object o)` method on a final class
that doesn't override the equals method in the Object class, effectively making the
equals method test for sameness, like `==`. It is good to use the
`.equals` method, but you should consider adding an
`.equals` method in this class.

## FB.UPM_UNCALLED_PRIVATE_METHOD

|  |  |
| --- | --- |
| SpotBugs: Performance | UPM: Private method is never called |

This private method is never called. Although it is possible that the method will be
invoked through reflection, it is more likely that the method is never used, and
should be removed.

## FB.URF_UNREAD_FIELD

|  |  |
| --- | --- |
| SpotBugs: Performance | UrF: Unread field |

This field is never read. Consider removing it from the class.

## FB.URF_UNREAD_PUBLIC_OR_PROTECTED_FIELD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UrF: Unread field |

This field is never read. The field is public or protected, so perhaps it is intended
to be used with classes not seen as part of the analysis. If not, consider removing
it from the class.

## FB.UR_UNINIT_READ

|  |  |
| --- | --- |
| SpotBugs: Correctness | UR: Uninitialized read of field in constructor |

This constructor reads a field which has not yet been assigned a value. This is often
caused when the programmer mistakenly uses the field instead of one of the
constructor's parameters.

## FB.UR_UNINIT_READ_CALLED_FROM_SUPER_CONSTRUCTOR

|  |  |
| --- | --- |
| SpotBugs: Correctness | UR: Uninitialized read of field in constructor |

This method is invoked in the constructor of the superclass. At this point, the
fields of the class have not yet initialized.

To make this more concrete, consider the following classes:

```
abstract class A {
    int hashCode;
    abstract Object getValue();

    A() {
        hashCode = getValue().hashCode();
    }
}

class B extends A {
    Object value;

    B(Object v) {
        this.value = v;
    }

    Object getValue() {
        return value;
    }
}
```

When a `B` is constructed, the constructor for the `A`
class is invoked *before* the constructor for `B` sets
`value`. Thus, when the constructor for `A`
invokes `getValue`, an uninitialized value is read for
`value`.

## FB.USC_POTENTIAL_SECURITY_CHECK_BASED_ON_​UNTRUSTED_​SOURCE

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | USC: Potential security check based on untrusted source |

A public method of a public class may be called from outside the package which means
that untrusted data may be passed to it. Calling a method before the
`doPrivileged` to check its return value and then calling the
same method inside the class is dangerous if the method or its enclosing class is
not final. An attacker may pass an instance of a malicious descendant of the class
instead of an instance of the expected one where this method is overridden in a way
that it returns different values upon different invocations. For example, a method
returning a file path may return a harmless path to check before entering the
`doPrivileged` block and then a sensitive file upon the call
inside the `doPrivileged` block. To avoid such scenario defensively
copy the object received in the parameter, e.g. by using the copy constructor of the
class used as the type of the formal parameter. This ensures that the method behaves
exactly as expected.

See SEI CERT rule [SEC02-J. Do not base security checks on untrusted
sources](https://wiki.sei.cmu.edu/confluence/display/java/SEC02-J.+Do+not+base+security+checks+on+untrusted+sources).

## FB.USM_USELESS_ABSTRACT_METHOD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | USM: Useless method |

This abstract method is already defined in an interface that is implemented by this
abstract class. This method can be removed, as it provides no additional value.

## FB.USM_USELESS_SUBCLASS_METHOD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | USM: Useless method |

This derived method merely calls the same superclass method passing in the exact
parameters received. This method can be removed, as it provides no additional
value.

## FB.UUF_UNUSED_FIELD

|  |  |
| --- | --- |
| SpotBugs: Performance | UuF: Unused field |

This field is never used. Consider removing it from the class.

## FB.UUF_UNUSED_PUBLIC_OR_PROTECTED_FIELD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UuF: Unused field |

This field is never used. The field is public or protected, so perhaps it is intended
to be used with classes not seen as part of the analysis. If not, consider removing
it from the class.

## FB.UWF_FIELD_NOT_INITIALIZED_IN_CONSTRUCTOR

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UwF: Unwritten field |

This field is never initialized within any constructor, and is therefore could be
null after the object is constructed. Elsewhere, it is loaded and dereferenced
without a null check. This could be a either an error or a questionable design,
since it means a null pointer exception will be generated if that field is
dereferenced before being initialized.

## FB.UWF_NULL_FIELD

|  |  |
| --- | --- |
| SpotBugs: Correctness | UwF: Unwritten field |

All writes to this field are of the constant value null, and thus all reads of the
field will return null. Check for errors, or remove it if it is useless.

## FB.UWF_UNWRITTEN_FIELD

|  |  |
| --- | --- |
| SpotBugs: Correctness | UwF: Unwritten field |

This field is never written. All reads of it will return the default value. Check for
errors (should it have been initialized?), or remove it if it is useless.

## FB.UWF_UNWRITTEN_PUBLIC_OR_PROTECTED_FIELD

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | UwF: Unwritten field |

No writes were seen to this public/protected field. All reads of it will return the
default value. Check for errors (should it have been initialized?), or remove it if
it is useless.

## FB.UW_UNCOND_WAIT

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | UW: Unconditional wait |

This method contains a call to `java.lang.Object.wait()` which is not
guarded by conditional control flow. The code should verify that condition it
intends to wait for is not already satisfied before calling wait; any previous
notifications will be ignored.

## FB.VA_FORMAT_STRING_ARG_MISMATCH

|  |  |
| --- | --- |
| SpotBugs: Correctness | FS: Format string problem |

A format-string method with a variable number of arguments is called, but the number
of arguments passed does not match with the number of % placeholders in the format
string. This is probably not what the author intended.

## FB.VA_FORMAT_STRING_BAD_ARGUMENT

|  |  |
| --- | --- |
| SpotBugs: Correctness | FS: Format string problem |

The format string placeholder is incompatible with the corresponding argument. For
example, `System.out.println("%d\n", "hello");`

The `%d` placeholder requires a numeric argument, but a string value
is passed instead. A runtime exception will occur when this statement is
executed.

## FB.VA_FORMAT_STRING_BAD_CONVERSION

|  |  |
| --- | --- |
| SpotBugs: Correctness | FS: Format string problem |

One of the arguments is incompatible with the corresponding format string specifier.
As a result, this will generate a runtime exception when executed. For example,
`String.format("%d", "1")` will generate an exception, since the
String `"1"` is incompatible with the format specifier
`%d`.

## FB.VA_FORMAT_STRING_BAD_CONVERSION_FROM_ARRAY

|  |  |
| --- | --- |
| SpotBugs: Correctness | USELESS_STRING: Useless/non-informative string generated |

One of the arguments being formatted with a format string is an array. This will be
formatted using a fairly useless format, such as `[I@304282`, which
doesn't actually show the contents of the array. Consider wrapping the array using
`Arrays.asList(...)` before handling it off to a formatted.

## FB.VA_FORMAT_STRING_BAD_CONVERSION_TO_BOOLEAN

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | FS: Format string problem |

An argument not of type `Boolean` is being formatted with a
`%b` format specifier. This won't throw an exception; instead, it
will print `true` for any non-null value, and `false`
for `null`. This feature of format strings is strange, and may not be
what you intended.

## FB.VA_FORMAT_STRING_EXPECTED_MESSAGE_FORMAT_SUPPLIED

|  |  |
| --- | --- |
| SpotBugs: Correctness | FS: Format string problem |

A method is called that expects a Java `printf` format string and a
list of arguments. However, the format string doesn't contain any format specifiers
(e.g., `%s`) but does contain message format elements (e.g.,
`{0}`). It is likely that the code is supplying a
`MessageFormat` string when a `printf`-style
format string is required. At runtime, all of the arguments will be ignored and the
format string will be returned exactly as provided without any formatting.

## FB.VA_FORMAT_STRING_EXTRA_ARGUMENTS_PASSED

|  |  |
| --- | --- |
| SpotBugs: Correctness | FS: Format string problem |

A format-string method with a variable number of arguments is called, but more
arguments are passed than are actually used by the format string. This won't cause a
runtime exception, but the code may be silently omitting information that was
intended to be included in the formatted string.

## FB.VA_FORMAT_STRING_ILLEGAL

|  |  |
| --- | --- |
| SpotBugs: Correctness | FS: Format string problem |

The format string is syntactically invalid, and a runtime exception will occur when
this statement is executed.

## FB.VA_FORMAT_STRING_MISSING_ARGUMENT

|  |  |
| --- | --- |
| SpotBugs: Correctness | FS: Format string problem |

Not enough arguments are passed to satisfy a placeholder in the format string. A
runtime exception will occur when this statement is executed.

## FB.VA_FORMAT_STRING_NO_PREVIOUS_ARGUMENT

|  |  |
| --- | --- |
| SpotBugs: Correctness | FS: Format string problem |

The format string specifies a relative index to request that the argument for the
previous format specifier be reused. However, there is no previous argument. For
example,

`formatter.format("%<s %s", "a", "b")`

would throw a `MissingFormatArgumentException` when executed.

## FB.VA_FORMAT_STRING_USES_NEWLINE

|  |  |
| --- | --- |
| SpotBugs: Bad practice | FS: Format string problem |

This format string includes a newline character (`\n`). In format
strings, it is generally preferable to use `%n`, which will produce
the platform-specific line separator.

## FB.VA_PRIMITIVE_ARRAY_PASSED_TO_OBJECT_VARARG

|  |  |
| --- | --- |
| SpotBugs: Correctness | VA: Var arg problems |

This code passes a primitive array to a function that takes a variable number of
object arguments. This creates an array of length one to hold the primitive array
and passes it to the function.

## FB.VO_VOLATILE_INCREMENT

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | VO: Use of `volatile` |

This code increments a `volatile` field. Increments of volatile fields
aren't atomic. If more than one thread is incrementing the field at the same time,
increments could be lost.

## FB.VO_VOLATILE_REFERENCE_TO_ARRAY

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | VO: Use of `volatile` |

This declares a `volatile` reference to an array, which might not be
what you want. With a volatile reference to an array, reads and writes of the
reference to the array are treated as volatile, but the array elements are
non-volatile. To get volatile array elements, you will need to use one of the atomic
array classes in `java.util.concurrent` (provided in Java 5.0).

## FB.VR_UNRESOLVABLE_REFERENCE

|  |  |
| --- | --- |
| SpotBugs: Correctness | VR: Version compatibility issue |

This class makes a reference to a class or method that can not be resolved using
against the libraries it is being analyzed with.

## FB.VSC_VULNERABLE_SECURITY_CHECK_METHODS

|  |  |
| --- | --- |
| SpotBugs: Malicious code vulnerability | VSC: Vulnerable security check performing methods |

Methods that perform security checks should be prevented from being overridden, so they must be declared as private or final.

## FB.WA_AWAIT_NOT_IN_LOOP

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | Wa: Wait not in loop |

This method contains a call to `java.util.concurrent.await()` (or
variants) which is not in a loop. If the object is used for multiple conditions, the
condition the caller intended to wait for might not be the one that actually
occurred.

## FB.WA_NOT_IN_LOOP

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | Wa: Wait not in loop |

This method contains a call to `java.lang.Object.wait()` which is not
in a loop. If the monitor is used for multiple conditions, the condition the caller
intended to wait for might not be the one that actually occurred.

## FB.WL_USING_GETCLASS_RATHER_THAN_CLASS_LITERAL

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | WL: Possible locking on wrong object |

This instance method synchronizes on `this.getClass()`. If this class
is subclassed, subclasses will synchronize on the class object for the subclass,
which isn't likely what was intended. For example, consider this code from
`java.awt.Label`:

```
private static final String base = "label";
private static int nameCounter = 0;

String constructComponentName() {
    synchronized (getClass()) {
        return base + nameCounter++;
    }
}
```

Subclasses of `Label` won't synchronize on the same subclass, giving
rise to a datarace. Instead, this code should be synchronizing on
`Label.class`

```
private static final String base = "label";
private static int nameCounter = 0;

String constructComponentName() {
    synchronized (Label.class) {
        return base + nameCounter++;
    }
}
```

## FB.WMI_WRONG_MAP_ITERATOR

|  |  |
| --- | --- |
| SpotBugs: Performance | WMI: Inefficient Map Iterator |

This method accesses the value of a `Map` entry, using a key that was
retrieved from a `keySet` iterator. It is more efficient to use an
iterator on the `entrySet` of the map, to avoid the
`Map.get(key)` lookup.

## FB.WS_WRITEOBJECT_SYNC

|  |  |
| --- | --- |
| SpotBugs: Multithreaded correctness | WS: Class's `writeObject()` method is synchronized but nothing else is |

This class has a `writeObject()` method which is synchronized;
however, no other method of the class is synchronized.

## FB.XFB_XML_FACTORY_BYPASS

|  |  |
| --- | --- |
| SpotBugs: Dodgy code | XFB: XML Factory Bypass |

This method allocates a specific implementation of an xml interface. It is preferable
to use the supplied factory classes to create these objects so that the
implementation can be changed at runtime. See

- `javax.xml.parsers.DocumentBuilderFactory`
- `javax.xml.parsers.SAXParserFactory`
- `javax.xml.transform.TransformerFactory`
- o`rg.w3c.dom.Document.createXXXX`

for details.

## FB.XSS_REQUEST_PARAMETER_TO_JSP_WRITER

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | XSS: Cross site scripting vulnerability | [CWE-79](http://cwe.mitre.org/data/definitions/79.html) |

This code directly writes an `HTTP` parameter to `JSP`
output, which allows for a cross site scripting vulnerability. See <http://en.wikipedia.org/wiki/Cross-site_scripting> for
more information.

SpotBugs looks only for the most blatant, obvious cases of cross site scripting. If
SpotBugs found *any*, you *almost certainly* have more cross site
scripting vulnerabilities that SpotBugs doesn't report. If you are concerned about
cross site scripting, you should seriously consider using a commercial static
analysis or pen-testing tool.

## FB.XSS_REQUEST_PARAMETER_TO_SEND_ERROR

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | XSS: Cross site scripting vulnerability | [CWE-81](http://cwe.mitre.org/data/definitions/81.html) |

This code directly writes an HTTP parameter to a `Server` error page
(using `HttpServletResponse.sendError`). Echoing this untrusted input
allows for a reflected cross site scripting vulnerability. See <http://en.wikipedia.org/wiki/Cross-site_scripting> for more
information.

SpotBugs looks only for the most blatant, obvious cases of cross site scripting. If
SpotBugs found *any*, you *almost certainly* have more cross site
scripting vulnerabilities that SpotBugs doesn't report. If you are concerned about
cross site scripting, you should seriously consider using a commercial static
analysis or pen-testing tool.

## FB.XSS_REQUEST_PARAMETER_TO_SERVLET_WRITER

|  |  |  |
| --- | --- | --- |
| SpotBugs: Security | XSS: Cross site scripting vulnerability | [CWE-79](http://cwe.mitre.org/data/definitions/79.html) |

This code directly writes an HTTP parameter to `Servlet` output, which
allows for a reflected cross site scripting vulnerability. See <http://en.wikipedia.org/wiki/Cross-site_scripting> for more
information.

SpotBugs looks only for the most blatant, obvious cases of cross site scripting. If
SpotBugs found *any*, you *almost certainly* have more cross site
scripting vulnerabilities that SpotBugs doesn't report. If you are concerned about
cross site scripting, you should seriously consider using a commercial static
analysis or pen-testing tool.
