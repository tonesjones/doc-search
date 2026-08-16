---
title: "Fortran Glossary"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/fortran-glossary.html"
content_id: "gFZ0OLITePPrLlox0SeUQg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:35.978649+00:00"
---

# Fortran Glossary

**active** DO **variable.** A DO variable within the range of a DO loop.

**actual argument.** An expression, a variable, a procedure, or an alternate return
specifier that is specified in a procedure reference.

**aggregate field.** A composite, or structured, data item, that is, a (Fortran 77
extension) record structure or a record substructure.

**alphanumeric.** A letter or a digit. As an extension the dollar sign is in some
implementations considered a letter.

**analysis message.** An information, warning, or error message concerning the syntax
or static semantics of the analyzed source program.

**ANSI.** American National Standards Institute.

**argument.** A parameter passed between a calling program unit and a procedure. It
can be an actual argument or a dummy argument.

**argument association.** The relationship between an actual argument and a dummy
argument during the execution of a procedure reference.

**argument keyword.** A dummy argument name which may be used in a procedure
reference.

**array.** A set of scalar data, all of the same type and type parameters, whose
individual elements are arranged in a rectangular pattern.

**array element.** One of the scalar data that make up an array. It is identified by
the array name followed by a subscript indicating the position in the array.

**array section.** A subobject of an array consisting of a set of array elements.
**assignment statement.** A statement of the form ’variable = expression’.

**association.** Name association, pointer association, storage association, or
inheritance association.

**assumed-shape array** A nonpointer dummy array that takes it shape from the
associated actual argument.

**assumed-size array** A dummy array whose size is assumed from the associated actual
argument. Its last upper bound is specified by an asterisk.

**attribute** A property of a data object that may be specified in a type declaration
statement.

**batch job.** A number of commands placed in a file and submitted to be processed.
**blank common.** An unnamed common block.

**block.** A sequence of executable constructs embedded in another executable
construct, bounded by statements that are particular to the construct, and treated as an
integral unit.

**block-data program unit.** A program unit that provides initial values for data
objects in named common blocks.

**bounds.** For a named array, the limits within which the values of the subscripts of
its array elements must lie.

**byte.** A storage unit, generally consisting of eight bits, which can contain a
single character.

**call tree.** See ”reference structure”.

**character.** A letter, digit, or other symbol.

**character length parameter.** The type parameter that specifies the number of
characters for an entity of type character.

**character string.** A sequence of characters.

**character storage unit.** The unit of storage for holding a scalar that is not a
pointer and is of type default character and character length one.

**class.** A set of types extended from a specific type.

**collating sequence.** An ordering of all the different characters of a particular
kind type parameter.

**command input.** The entry of commands to instruct a program to perform the required
actions.

**command file.** A file containing command input.

**command file entry.** The entry of commands through specification of a command
file.

**command line entry.** The entry of commands through typing command lines.

**common block.** A block of physical storage that may be accessed by any of the
scoping units in a program.

**common-block object.** An entity in a common block denoted by a name: a variable or
record (Fortran 77 extension).

**common-block size.** The number of bytes the common block will occupy.

**compiler.** A program that translates a program, written in a higher programming
language, into code understood by the computer.

**compiler directive.** An instruction to the compiler to assist processing of source
statements. **compile time.** The time during which the compiler processes the source
file.

**complex constant.** An ordered pair of signed or unsigned real or integer constants
separated by a comma and enclosed in parentheses. The first constant of the pair is the
real part of the complex constant, the second is the imaginary part.

**complex type.** An approximation of the value of a complex number, consisting of an
ordered pair of real data items separated by a comma and enclosed in parentheses. The
first item represents the real part of the complex number, the second represents the
imaginary part.

**component.** A constituent of a derived type.

**conditional compilation.** Source code lines can be either included in the
compilation process or be left out by applying a compiler directive and a command line
option. The simplest compiler directive to tag lines to compile conditionally is a D in
the first column of the source line.

**configuration file.** A file containing instructions to adapt a program to the
user’s requirements.

**conformable.** Two arrays are said to be conformable if they have the same shape. A
scalar is conformable with any array.

**conformance.** A program conforms to the standard if it uses only those forms and
relationships described therein, and if the program has an interpretation according to
the standard. A program unit conforms to the standard if it can be included in a program
in a manner that allows the program to be standard conforming.

**constant.** A data object whose value must not change during execution of a program.
It may be a named constant or a literal constant.

**constant expression.** An expression satisfying rules that ensure that its value
does not vary during program execution.

**construct.** A sequence of statements starting with an ASSOCIATE, DO, FORALL, IF,
SELECT CASE, SELECT TYPE, or WHERE statement and ending with the corresponding terminal
statement.

**construct entity.** An entity defined by a lexical token whose scope is a construct.
**cross-reference table.** A table in which all references to certain entities
are listed.

**data entity.** An entity that has or may have a data value. It may be a data object,
the result of the evaluation of an expression, or the result of a function
reference.

**data object.** A data entity that is a constant, a variable, a record (Fortran 77
extension), or a subobject of a constant.

**data type.** See type. **debug line.** A source code line containing a character
denoting conditional compilation in its first column.

**default initialization.** If initialization is specified in a type definition, an
object of the type will be automatically initialized.

**defined.** For a data object, the property of having or being given a valid
value.

**deleted feature.** A feature in a previous Fortran standard that is considered to be
redundant and largely unused.

**derived type.** A type whose data have components, each of which is either of
intrinsic type or of another derived type.

**designator.** A name, followed by zero or more component selectors, array section
selectors, array element selectors, and substring selectors.

**digit.** One of the characters 0 to 9.

**DO loop.** A range of statements executed repeatedly by a DO statement.

**double precision.** The standard name for real data that is allocated two numeric
storage units (8 bytes).

**DO variable.** A variable, specified in a DO statement that is initialized or
increased prior to each execution of the statement or statements within the DO
range.

**dummy argument.** An entity whose name appears in the parenthesized list following
the procedure name in a FUNCTION, SUBROUTINE, ENTRY, or statement function statement
(formal argument).

**dummy array.** A dummy argument that is an array.

**dummy pointer.** A dummy argument that is a pointer.

**dummy data object.** A dummy argument that is a data object.

**dummy procedure.** A dummy argument that is a procedure.

**entity.** The term entity is used for any of the following: a program unit, a
procedure, an abstract interface, an operator, a generic interface, a common block, an
external unit, a statement function, a type, a data entity, a statement label, a
construct, or a namelist group.

**entry.** The location in the subprogram where execution of the statements starts
when the entry name is referenced.

**equivalence.** The association of names referring to the same memory location.
**equivalence list.** A list of names to be associated.

**executable statement.** An instruction to perform or control one or more
computational actions.

**exit status.** The resulting error level of the execution of a program.

**explicit interface.** For a procedure referenced in a scoping unit, the property of
being an internal procedure, a module procedure, an intrinsic procedure, an external
procedure that has an interface body, a recursive procedure reference in its own scoping
unit, or a dummy procedure that has an interface body.

**explicit type.** The type of a name when specified by a type statement.

**expression.** A sequence of operands, operators, and parentheses. It may be a
variable, a constant, a function reference, or may represent a computation.

**extension.** See Filename extension.

**extent.** The size of one dimension of an array.

**external file.** A sequence of records that exists in a medium external to the
program.

**external i/o.** I/O operations performed on an external file.

**external procedure.** A procedure that is defined by an external subprogram or by
means other than Fortran.

**external subprogram.** A subprogram that is not in a main program, module, or
another subprogram.

**field.** An atomic unit of a record (Fortran 77 extension). It corresponds to a
substructure, a variable or an array element.

**file.** An internal file or an external file.

**file access type.** The way an external file is accessed: sequential, direct, or
stream.

**file name extension.** The denotation of a file type by extending the file name with
a delimiter followed by a number of characters.

**Coverity Fortran Syntax Analysis.** A computer program to validate Fortran source
programs through static analysis.

**format type.** The way the data is stored in an external file: formatted or
unformatted. Formatted: stored as printable characters (e.g. ASCII or EBCDIC)
Unformatted: stored in internal computer representation.

**FORTRAN.** An acronym of ”Formula Translation” denoting a higher computer
language.

**FORTRAN 77.** The American National Standard Programming Language FORTRAN, as
specified by the American National Standards Institute in document X3.9-1978.

**fortran 90.** The Standard Programming Language Fortran, as specified by the
ISO-1539:1991(E) document.

**fortran 90.** The Standard Programming Language Fortran, as specified by the
ISO-1539­1:1997(E) document.

**fortran-supplied procedure.** See ”intrinsic function”.

**function.** A procedure that is invoked in an expression.

**function result.** The data object that returns the value of a function.

**function subprogram.** A sequence of statements beginning with a FUNCTION statement
that is not an interface block and ending with the corresponding END statement.

**generic identifier.** A name that appears in an INTERFACE statement and is
associated with all the procedures in the interface block or that appears in a GENERIC
statement and is associated with the specific type-bound procedures.

**global entity.** An entity identified with an identifier whose scope is a
program.

**global information.** All information on global entities that is relevant to other
program units of the program.

**global Program Analysis.** The analysis across program unit boundaries to verify the
global entities.

**hexadecimal constant.** A literal constant that is represented by a sequence of
digits and the letters A through F (base-16 notation).

**hollerith constant.** A string of any characters preceded by wH, where w is the
number of characters in the string.

**host.** Host scoping unit.

**host association.** The process by which a contained scoping unit accesses entities
of its host.

**host scoping unit.** A scoping unit that immediately surrounds another scoping unit.
**identifier.** See ”Name”.

**implicit interface.** A procedure referenced in a scoping unit other than its own is
said to have an implicit interface if the procedure does not have an explicit interface
there.

**implicit Type.** The default type of a name when no type has been specified by a
type specification statement.

**implied** DO**.** An indexing specification (similar to a DO statement, but
without specifying the word DO) with a list of data elements, rather than a set of
statements, as its range.

**include file.** A file with statements that have to be included in the source code
of the program at the place of the include statement which references the include
file.

**include path.** A file directory at which the system tries to locate include
files.

**input record.** A record of the input source file.

**input file.** A sequence of input records.

**inquiry function.** An function that is either intrinsic or is defined in an
intrinsic module and whose result depends on properties of one or more of its arguments
instead of their values.

**intent.** An attribute of a dummy data object that indicates whether it is used to
transfer data into the procedure, out of the procedure, or both.

**interface block.** A sequence of statements from an INTERFACE statement to the
corresponding END INTERFACE statement.

**inter-subprogram information.** All information on subprograms which is relevant to
other program units of the program (global information).

**interactive entry.** Specification of program commands and options through a query.
**interface of a procedure.** See ”procedure interface”.

**internal file.** A character variable that is used to transfer and convert data from
internal storage to internal storage.

**internal i/o.** I/O operations performed on an internal file.

**internal procedure.** A procedure that is defined by an internal subprogram.

**internal subprogram.** A subprogram in a main program or another subprogram.

**intrinsic.** An adjective applied to types, operations, assignment statements,
procedures, and modules that are defined in the standard and may be used in any scoping
unit with­out further definition or specification.

**i/o.** Pertaining to either input or output, or both.

**i/o list.** A list of items in an input or output statement specifying which data is
to be read or to be written.

**i/o operation code.** A symbol denoting the category of input/output operation
performed.

**keyword.** An argument keyword or a word with a special, predefined, meaning for the
compiler.

**kind type parameter.** A parameter whose values label the available kinds of an
intrinsic type, or a derived-type parameter that is declared to have the KIND
attribute.

**label.** See ”Statement label”.

**label type.** The syntactic construct in which the statement label is used
determines its type: end of a `DO` loop, identification of a
`FORMAT` statement, or other.

**labeled common.** See ”Named common”.

**length.** Array length, character string length, type length, or record length.

**length specification.** The specification of the type length.

**lexical token.** A sequence of one or more characters with a specified
interpretation.

**library file.** An external file consisting of an index and the global information
on program units.

**line.** A sequence of characters containing (part of) Fortran statements, a comment,
or an `INCLUDE` line.

**list file.** A sequential formatted file in which the numbered statements are
presented with other information concerning the source code.

**listing.** See ”List file”.

**literal constant.** A constant without a name.

**local entity.** An entity identified by a lexical token whose scope is a scoping
unit.

**logical constant.** A constant that can have one of two values: true or false.

**logical expression.** A combination of logical primaries and logical operators. The
result is the value true or false.

**logical operator.** Any of the set of operators `.NOT.`,
`.AND.`, `.OR.`, `.EQV.`,
`.NEQV.`, `.XOR.` **logical primary.** A primary
that can have the value true or false. See also ”primary”.

**main program.** A program unit that is not a module, external subprogram, or block
data program unit.

**module.** A program unit that contains or accesses definitions to be accessed by
other program units.

**module procedure.** A procedure that is defined by a module subprogram.

**module subprogram.** A subprogram that is in a module but is not an internal
subprogram.

**name.** A lexical token consisting of a letter followed by up to 62 alphanumeric
characters (letters, digits, and underscores). Note that in Fortran 77 this was called a
symbolic name.

**named.** Having a name.

**named constant.** A constant that has a name. Note that in Fortran 77 this was
called a symbolic constant.

**nonexecutable statement.** A statement that describes the characteristics of the
program unit, of data, of editing information, or of statement functions, but does not
cause an action to be taken by the program.

**nonstandard syntax.** Syntax which does not conform to the Fortran standard.

**numeric constant.** A constant that expresses an integer, real, double precision, or
complex number.

**numeric type.** Integer, real, or complex type.

**obsolescent feature.** A feature that is considered to have become redundant but
that is still in frequent use.

**operation code.** A symbol denoting the kind of operation performed on a data
object.

**operational message.** A message presented to signal a problem in the operation of
the program.

**operand.** An expression that precedes or succeeds an operator.

**operation.** A computation involving one or two operands.

**operator.** A lexical token that specifies an operation.

**option.** A sub-command to select program features.

**output file.** A sequential formatted file in which all information requested is
stored.

**parameter.** See ”argument”.

**path.** A full file specification.

**pointer.** An entity that has the POINTER attribute.

**pointer assignment.** The pointer association of a pointer with a target by the
execution of a pointer assignment statement or the execution of an assignment statement
for a data object of derived type having the pointer as a subobject.

**pointer associated.** The relationship between a pointer and a target following a
pointer assignment or a valid execution of an ALLOCATE statement.

**pointer association.** The process by which a pointer becomes pointer associated
with a target.

**primary.** An irreducible unit of data; a constant, variable, function reference, or
expression enclosed in parentheses.

**procedure.** A computation that may be invoked during program execution. It may be a
function or a subroutine. It may be an intrinsic procedure, an internal procedure, an
external procedure, a module procedure, a dummy procedure, or a statement function.

**procedure interface.** The characteristics of a procedure, the name of the
procedure, the name of each dummy argument, and the generic identifiers (if any) by
which it may be referenced.

**program.** A set of program units that includes exactly one main program.

**program interface.** The way to instruct the program to perform the required
actions.

**program unit.** The fundamental component of a program. A sequence of statements,
comments and INCLUDE lines. It may be a main program, a module, an external subprogram,
or a block data program unit.

**qualifier.** See ”option”.

**rank.** The number of dimensions of an array. Zero for a scalar.

**real type.** An arithmetic type, capable of approximating the value of a real
number.

**record.** 1) A sequence of values that is treated as a whole within a file. 2) A
named data entity, consisting of one or more fields, contained in the program (Fortran
77 extension).

**record length.** 1) The number of bytes or storage units that make up an entity in a
file. 2) The number of bytes a record (Fortran 77 extension) occupies.

**recursive reference.** A subprogram is recursively referenced when the subprogram is
invoked from within that same subprogram, either directly or via other subprograms.

**reference structure.** The hierarchical call tree in which all references of
subprograms are presented graphically.

**reference.** The appearance of an object designator in a context requiring the value
at that point during execution, the appearance of a procedure designator, its operator
symbol, or a defined assignment statement in a context requiring execution of the
procedure at that point, or the appearance of a module name in a USE statement.

**relational expression.** An expression that consists of an arithmetic expression,
followed by a relational operator, followed by another arithmetic expression or a
character expression, followed by a relational operator, followed by another character
expression. The result is a value that is true or false.

**relational operator.** Any of the set of operators: `.GT.`,
`.GE.`, `.LT.`, `.LE.`,
`.EQ.`, `.NE.`

**saved.** Variables, records (Fortran 77 extension) and named common blocks can be
saved by specifying them in a `SAVE` statement to prevent them from
becoming undefined after exit of a subprogram.

**scalar.** A single datum that is not an array and is not a record (Fortran 77
extension) or aggregate field (Fortran 77 extension).

**scale factor.** A specification in a `FORMAT` statement, which
changes the location of the decimal point in a real number.

**scope.** That part of a program within which a lexical token has a single
interpretation. It may be a program, a scoping unit, a construct, a single statement, or
a part of a statement.

**scoping unit.** One of the following:

- A program unit or subprogram, excluding any scoping units in it,
- a derived-type definition, or an interface body, excluding any scoping units in
  it.

**scratch file.** An external file in which temporary information is stored.

**size.** The size of an array, record (Fortran extension), derived type, or common
block is the total number of bytes that make up the entity.

**source code.** The original text which forms FORTRAN statements.

**source code listing.** See ”list file”.

**source file.** A file containing the original text of a program.

**source program.** The original text which forms a FORTRAN program.

**specific function.** An Fortran supplied (intrinsic) function which can be
referenced directly or by referencing a generic function which invokes the specific
function depending on the type of the actual arguments.

**specification statement.** One of the set of statements that provides the compiler
with information about the data used in the source program. It supplies the information
required to allocate data storage.

**standard conforming.** See ”conformance”.

**statement.** A sequence of lexical tokens. It may consist of a single line, but can
be continued using a continuation character, or can be limited to occupy part of a line
by a separation character.

**statement entity.** An entity identified by a lexical token whose scope is a single
statement or part of a statement.

**statement function.** A procedure specified by a single statement.

**statement label.** A lexical token consisting of up to five digits that precedes a
statement and may be used to refer to the statement.

**static analysis.** The analysis of the source code without execution of the program.
**static analyzer.** A tool to perform static analysis.

**static semantics.** The meaning of the code as far as it can be directly inferred
from the code without knowing the algorithm.

**storage association.** The relationship between two storage sequences if a storage
unit of one is the same as a storage unit of the other.

**string.** A character literal constant.

**stride.** The increment specified in a subscript triplet.

**structure.** A scalar data object of derived type (Fortran 90, or 95), or a group of
statements that define the form of a record (Fortran 77 extension).

**structure component.** The part of an object of derived-type.

**subobject.** A portion of a data object that may be referenced or defined
independently of other portions.

**subprogram.** A function subprogram or a subroutine subprogram. Note that in Fortran
77 a block data program unit was called a subprogram.

**subroutine.** A procedure that is invoked by a CALL statement or by a defined
assignment statement.

**subroutine subprogram.** A sequence of statements beginning with a SUBROUTINE
statement that is not in an interface block and ending with the corresponding END
statement.

**subscript.** One of the list of scalar integer expressions in an array element
selector. Note that in Fortran 77 the whole list was called the subscript.

**subscript triplet.** An item in the list of an array section selector that contains
a colon and specifies a regular sequence of integer values.

**substring.** A contiguous portion of a scalar character string.

**suffix.** See File name extension.

**symbolic constant.** See ”Named constant”.

**symbolic name.** See ”Name”.

**syntax.** The lexical structure of the language.

**system Message.** A message presented to inform the user of a problem during
execution of the program.

**target.** A data entity that has the TARGET attribute, or an entity that is
associated with a pointer.

**truncation.** The implicit conversion of a type to another type which occupies less
storage, or conversion of a representation of a real number to an integer.

**type.** A named category of data that is characterized by a set of values, together
with a way to denote these values and a collection of operators that interpret and
manipulate the values. The set of data values depends on the values of the type
parameters.

**type declaration.** The specification of the type for the name of a constant,
variable, or function by use of an explicit type specification statement.

**type length.** The number of bytes an object of a specific type occupies.

**type parameter.** A parameter of a data type.

**type statement.** A statement to specify the type of a name.

**unassigned.** See ”Undefined”.

**undefined.** The property of a data object of not having a determinate value.

**unit identifier.** A means of referring to a file in order to use input/output
statements.

**unreferenced.** The condition of a data object that no reference is made to that
object.

**use association.** The association of names in different scoping units specified by
a USE statement.

**variable.** A data object whose value can be defined and redefined during the
execution of a program. It may be a named data object, an array element, an array
section, a structure component, or a substring. Note that in Fortran 77 a variable was
always scalar and named.

**vector subscript.** A section subscript that is an integer expression of rank
one.

**whole array.** A named array, or an array component of a structure with no subscript
list.
