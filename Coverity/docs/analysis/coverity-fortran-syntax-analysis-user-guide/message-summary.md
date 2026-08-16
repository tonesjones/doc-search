---
title: "Message summary"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/message-summary.html"
content_id: "WFNiK1vBmJozvKDDljLt6Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:34.581756+00:00"
---

# Message summary

In this appendix, all system and analysis messages are listed. The messages which are
not self-explaining are elucidated.

1 I (MESSAGE LIMIT REACHED FOR THIS STATEMENT OR ARGUMENT LIST)

- Only the first 5 messages in a statement or argument list are displayed.

2 E (OPEN ERROR ON INCLUDE FILE)

- An include file could not be located or opened.

3 E (INCLUDE NESTING TOO DEEP)

- The nesting of include files is too deep.

4 O (NEXT SOURCE RECORD TOO LONG, REMAINDER NOT PROCESSED)

- The source input record exceeds the input buffer size.

5 O (TOO MANY (COMMENT) RECORDS IN STATEMENT, REMAINDER NOT PROCESSED)

- The number of (comment) lines in the statement is too large.

6 O (STATEMENT TOO LONG, REMAINDER NOT PROCESSED)

- The number of characters in the statement is too large.

7 O (TOO MANY STATEMENTS, REMAINDER NOT PROCESSED)

- The number of statements in the program unit is too large.

8 O (NAME TOO LONG, TRUNCATED)

- The identifier is too long.

9 O (ARRAY TOO LONG, LENGTH NOT VERIFIED)

- The length of the array is too long.

10 O (CHARACTER ENTITY TOO LONG, LENGTH NOT VERIFIED)

- The character constant or type length is too large.

11 O (NUMBER CANNOT BE CONVERTED)

- The number concerned is too large for the system being used.
- The format of the number is not available on the system being used.

12 O (NAME TABLE FULL, REMAINDER NOT PROCESSED)

- The table with identifiers is full. When using many long names the name table can become full
  before the symbol table is full.

13 O (SYMBOL TABLE FULL, REMAINDER NOT PROCESSED)

- The table with information concerning named entities is full.

14 O (CONTEXT TABLE FULL)

- The number of contexts is too large.

15 O (NESTING TOO DEEP)

- The nesting of array subscripts, function-, and subroutine argument lists is too deep.

- The nesting of implied DO loops in a DATA statement is too deep.
- The context nesting is too deep

16 O (EXPRESSION STACK OVERFLOW)

- The expression is to complex to analyze.

17 E (EXPRESSION STACK UNDERFLOW)

- Internal error, please report.

18 O (CONSTRUCT STACK OVERFLOW)

- The nesting of constructs, is too deep.

19 O (DERIVED-TYPE/STRUCTURE NESTING TOO DEEP)

- The stack for nesting of derived-types and structures is full.

20 O (TOO MANY OBJECTS IN DATA STATEMENT, REMAINDER NOT VERIFIED)

21 O (TOO MANY EQUIVALENCE LISTS, REMAINDER NOT PROCESSED)

22 O (TOO MANY ARGUMENTS, REMAINDER NOT VERIFIED)

23 O (TOO MANY ARGUMENT SHAPES, REMAINDER NOT VERIFIED)

24 W (ROOT ENTRY NOT FOUND)

25 O (TOO MANY REFERENCES, REMAINDER PRINTED IN SEPARATE SUB-TREES)

26 O (TOO MANY PROGRAM UNITS, REMAINDER NOT PROCESSED)

27 O (CROSS-REFERENCE TABLE FULL, REMAINDER NOT PRESENTED)

28 O (TOO MANY COMMON-BLOCK OBJECTS TO CROSS-REFERENCE)

29 W (LIBRARY ENTRY NOT FOUND)

30 O (TOO MANY LIBRARY ENTRIES, REMAINDER NOT PROCESSED)

31 O (ARGUMENT-KEY STACK FULL, REMAINDER NOT PROCESSED)

- The stack with argument keys is full. When using many long argument keys the
  argument key stack can overflow before the argument stack overflows.

32 O (CONDITIONAL-COMPILATION SYMBOL TABLE FULL)

33 O (CONDITIONAL-COMPILATION NESTING TOO DEEP)

34 O (INVALID NESTING OF CONDITIONAL-COMPILATION META COMMANDS)

35 O (EXPRESSION COULD NOT BE EVALUATED)

36 O (STACK OVERFLOW WHILE PROCESSING REFERENCE STRUCTURE)

37 O (SOURCE POSSIBLY IN FREE FORM. SPECIFY THE FREE-FORM OPTION)

38 O (TOO MANY MESSAGES SUPPRESSED, REMAINDER IGNORED)

39 O (NAME AND REFERENCE DO NOT FIT ON A LINE, ENLARGE PAGE WIDTH)

40 E a ’;’ must not be the first nonblank character on a line

41 E invalid line

- A non-comment, non-compiler directive line with less than 6 characters has been
  read.

42 E first line must not be a continuation line

- The line is the first line encountered in the statement and has not a zero or blank
  in column 6.

43 E invalid characters in front of continuation line

- Characters have been found in column 1-5 of a fixed form continuation line.

44 W first line after an INCLUDE line must not be a continuation line

45 W too many continuation lines

- The statement has more continuation lines than the emulated compiler can
  handle.
- The statement has more than 19 continuation lines and the Fortran 77 standard option
  has been specified.
- The statement has more than 19 continuation lines and the Fortran 90 or 95 standard
  option has been specified and the source is in fixed form.
- The statement has more than 39 continuation lines and the Fortran 90 or 95 standard
  option has been specified and the source is in free form.

46 E unrecognized characters at end of statement

- After processing the statement there were characters left in the statement
  buffer.

47 W statement field empty, CONTINUE assumed

48 E invalid characters in label field of statement

- Only a label in column 1-5, and a zero or blank in column 6 are allowed in front of
  a statement.

49 W continuation character not in Fortran character set

50 W lower case character(s) used

51 W nonstandard Fortran comment used

52 W conditional compilation or D line(s) used

53 W tab(s) used

54 W formfeed(s) used

55 W include line(s) used

56 E unbalanced delimiters

57 E invalid filename specification

58 I none of the entities, declared in the include file, is used

59 I character constant split over more than one line

- This may be non-portable.

60 W fixed source form used

61 I no statement found in program unit

- Only comment lines or non-included conditional source lines were read.

62 W continuation character missing

- In freeform input the first nonblank character of a continuation line in a
  charac­ter context should be an &.

63 I unrecognized characters after compiler directive

- the cpp preprocessor does not allow characters after directives without
  argu­ments.

64 W line too long

65 I continued character constant has more than one leading blank

66 I comment line(s) within statement

69 E unrecognized statement

- The syntax is not recognized. This may be caused by a non- standard keyword which is
  not part of the supported extensions.

70 I ambiguous statement. Type statement assumed

- A function statement must have an (empty) argument list, so this statement is
  treated as an explicit type statement.

71 W nonstandard Fortran statement

72 E statement not allowed in MAIN

73 E statement not allowed in BLOCKDATA

- In a blockdata program unit only specification statements, and no executable
  statements are allowed.

74 E statement not allowed within the specification part of a (sub)module

75 E this statement can only be used within a construct

76 E this statement can only be used within a loop construct

77 E statement not allowed within this context

78 E statement out of order

79 E type specification out of order

- The type specification must confirm the implicit type or be defined before the
  declaration statement where it is used.

80 W non-DATA specification statements must precede DATA statements

- In Fortran 77 any DATA statement should be placed after other specification
  statements.

81 E no shape specified, or statement function out of order

- An undeclared subscripted variable or function name with arguments is used at the
  left side of an assignment statement.

82 E this statement cannot have prefixes

- Only a FUNCTION or SUBROUTINE statement can have prefixes.

83 E internal or module procedure expected

- After a CONTAINS statement at least one internal or module procedure must be
  specified.

84 I no path to this statement

85 E procedure END missing

86 E program unit END missing

87 E non-matching program unit or subprogram type in END

88 E non-matching name in END

89 E missing delimiter or separator

90 E unmatched parentheses

91 E missing parenthesis

92 E ”)” expected

93 E ”/” expected

94 E syntax error

95 W nonstandard Fortran syntax

96 W obsolescent Fortran feature

- This syntax is marked as obsolescent in the effective Fortran standard.

97 I PARAMETER statement within STRUCTURE

- Defined named constants are not local to the structure, so they can better be

placed outside the structure definition.

98 W deleted Fortran feature

- This syntax is marked as deleted in the effective Fortran standard.

99 W DATA statement among executable statements

- This is marked as obsolescent in the Fortran 95 standard.

100 E statement not allowed within a pure procedure

101 E statement not allowed within an interface block

102 E statement only allowed within an interface block

103 E statement only allowed within the spec. part of a (sub)module

104 E statement only allowed in interface block or spec. part of subprog.

105 E statement not allowed within a BLOCK construct

106 E lexical token contains blank(s)

- In free form source form blanks in a name, literal constant, operator, or keyword
  are not allowed.

107 E blank required in free source form

108 I use a blank to delimit this token

- In fixed form source form of Fortran blanks are not significant but the absence of a
  delimiter between these lexical tokens might indicate a syntax error.

109 I lexical token contains non-significant blank(s)

- In fixed form source form blanks are not significant. However, a blank in a name,
  literal constant, operator, or keyword might indicate a syntax error.

110 W name or operator too long

- The name or is longer than 6 characters and the conformance to the Fortran 77
  standard option has been specified.
- The name or operator is longer than 31 characters and the conformance to the Fortran
  90 standard option has been specified.
- The name or operator is longer than the maximum name length supported by the
  emulated compiler.

111 E operator name must consist of letters only

112 W name is not unique if truncated to six characters

113 E invalid name

- The syntax of the name is in error. Invalid characters have been used in the
  identifier.

114 E statement label too long

- A statement label must consist of 1 to 5 digits.

115 E multiple definition of statement label, this one ignored

116 E statement label already in use

117 E statement label type conflict

- A label must either be used to identify a format statement, or a non-format
  statement.

118 E invalidly referenced

119 E invalid reference

120 I referenced from outside entry block

121 E statement label invalid

122 E format statement label missing

123 E undefined statement label

- A referenced statement label has not been defined.

124 I statement label unreferenced

- A statement label has been defined but is never referenced (used).

125 I format statement unreferenced

134 E missing apostrophe or quote

- The closing apostrophe or quote of a character constant is missing.

135 E zero length character constant

- In Fortran 77 a character constant must not be of zero length.

136 E invalid binary, octal or hexadecimal constant

137 E kind type parameter of real constant not allowed for this exponent

- If the kind is specified, only E is a valid exponent letter.

138 E invalid complex constant

139 E invalid Hollerith or Radix constant

140 E missing character to escape in C-string

- The closing apostrophe or quote of the C-string is preceded by a ”“”. -A named
  constant is used in a context where a variable, or
- procedure name is expected.
- In standard Fortran no named constants are allowed to define the real or imaginary
  part of a complex constant.

142 E real or integer constant expected

143 W character length too large

- A character constant or variable is longer than the emulated compiler can
  handle.

144 E number too large

145 I implicit conversion of scalar to complex

- An integer or real value is assigned to a complex variable. The imaginary part of
  the complex becomes zero. If the real is zero this information is only presented if
  the rigorous option has been specified.

146 E unsigned nonzero integer expected

147 E unsigned integer expected

148 E positive integer expected

149 E integer too large for its kind

150 W integer larger than default

151 E invalid or unrecognized attribute

152 I PRIVATE is already the default

- PRIVATE has already been specified.

153 I PUBLIC is already the default

154 E implicit type already used; type declaration must confirm this type

155 E conflict with generic name

156 E conflict with derived-type name

157 E invalid usage of subscripts or substring

158 E already specified PUBLIC

- PUBLIC has already been specified.
- PRIVATE has been specified but PUBLIC has been specified before.

159 E name already in use

160 E invalid usage of variable

- Because of the previous context the name appeared to be a variable but is now used
  in a context where a procedure name is expected.

161 E scalar variable name expected

- An array element, array name, constant, external, structure, derived-type name or
  namelist name is not allowed in this context.

162 E named scalar expected

- No array name, array section, array element, substring, or expression is allowed in
  this context.

163 E no array allowed

- No array name or array section allowed.

164 E missing array or shape specification

165 E invalid shape specification

166 E missing array subscripts

167 E invalid usage of subscripts or bounds

- An array element is not allowed in this context.
- A scalar can not be subscripted or have bounds.

168 E invalid number of subscripts or bounds

- The number of subscripts is larger than the maximum rank.
- The number of subscripts or bounds is different from the declared rank.
- The number of lower-bound expressions or bound remappings is different from the
  declared rank.

169 E invalid shape bounds

- The first bound of a specified shape is higher than the second bound.
- Array must not be zero sized in this context.

170 E shape specification out of order

- The shape must be specified before first usage.

171 E multiple specification of shape

- The shape of the array has been declared more than once.

172 E invalid array or coarray specification

173 E invalid usage of assumed-size array specification

- Only dummy array arguments can be specified with an assumed-size.
- The function name of an array-valued function must not be declared
  assumed-size.

174 E invalid usage of assumed-size array name

- An assumed-size array name can only be used as an actual argument in a procedure
  reference for which the shape is not required.

175 E invalid usage of adjustable-array dimension

- Only dummy-array arguments can be specified with adjustable dimensions.

176 E invalidly used in adjustable or automatic array declaration

- A variable which specifies an array dimension or character length must either be a
  procedure argument (with intent(in)), in common, or a global module variable.

177 E deferred- or assumed-shape array specification not allowed

178 E deferred-shape array specification required

- A POINTER or an ALLOCATABLE array must be specified as a deferred-shape array.

179 E explicit-shape array specification required

- An array valued function result, without the POINTER or ALLOCATABLE attribute, must
  have an explicit shape.

180 E invalid usage of automatic-array specification

- An automatic array must not appear in the specification part of a (sub)module

181 E invalid usage of assumed length

- Only a dummy argument, function result, or named constant of type character can be
  specified with assumed length.
- The type length of a statement-, internal-, or module function cannot be of assumed
  length.
- The type length of a dummy statement function argument can not be of assumed length.
- A function with pointer valued result cannot be of assumed length.

182 E invalid usage of adjustable-length specification

- Only dummy arguments or automatic objects can be specified with an adjustable
  length parameter.
- Statement functions and statement function arguments cannot be specified with
  adjustable length
- If the length parameter of an elemental function is specified by an expression, it
  must be a constant expression.

183 E invalid length or kind specification, default assumed

- A kind type parameter must be a nonnegative scalar integer constant
  expression.

184 E multiple specification of attribute

185 E invalid combination of attributes

186 E attribute not allowed in this context

187 E invalid to (re)define type or attribute

188 E OPTIONAL and INTENT only allowed for dummy arguments

189 E already specified PRIVATE

- PUBLIC has been specified but PRIVATE has been specified before.
- PRIVATE has already been specified.

190 E type parameter not allowed for this type

191 E invalid specification of type parameters

192 E invalid usage of type parameters

193 I already specified in host context

194 W unsupported type length, default assumed

- A type length specification of this type is not supported by the emulated
  compiler.

195 E type length invalidly specified

- The type length cannot be specified in this context
- The emulated compiler does not support this nonstandard Fortran syntax.

196 E initialization only allowed in attributed form of type spec.

- Use ’::’ between statement keyword and list.

197 E a named constant cannot have the POINTER, TARGET, or BIND attribute

198 E constant expected

199 E missing parentheses

- In standard Fortran the list of a PARAMETER statement must be enclosed in
  parentheses. Be aware, however, that the syntax extension without parentheses
  provided by some compilers uses a different assumption of the type of named
  constant. In standard Fortran the type is the implicitly or explicitly defined type
  of the name. In the syntax extension the type becomes the type of the named
  constant.

200 E constant expression missing

- If the PARAMETER attribute has been specified, the named constant must be given a
  value.

201 E entity must have been explicitly declared previously

202 E multiple specification of type, this one ignored

- The entity has already been typed by an explicit type statement.

203 E name invalidly typed

- The name must not appear in an explicit type statement.

204 I implicit type already used, change sequence

- An explicit type specification confirms the implicit type of a variable that has
  already been used.

205 E implicit properties already used, statement out of order

206 E invalid implicit range

- The first and second character in an IMPLICIT list must in lexicographic order.

207 E multiple implicit type declaration, this one ignored

- An implicit type has been specified more than once for one or more characters in the
  list.
- IMPLICIT NONE has been specified and another IMPLICIT statement has already been
  specified.

• IMPLICIT NONE has been specified but an implicit type has already been used.

208 W name not explicitly typed, implicit type assumed

- The entity has not been explicitly typed and:
- IMPLICIT UNDEFINED has been specified for the first character of the symbol.
- The declare option has been specified.

209 W conflict with IMPLICIT NONE specification or DECLARE option

- An IMPLICIT statement has been specified while IMPLICIT NONE has been spec­ified or
  the DECLARE option is enabled.

210 E SAVE has already been specified for this entity

211 E SAVE and AUTOMATIC cannot be specified both

212 E invalid to save this entity

- Only named common blocks and variables can be saved.
- There is no need to save the blank common because the common-block values in blank
  common do not become undefined after a RETURN or END.
- Common-block objects cannot be saved.
- Automatic and static arrays and pointees cannot be saved.
- Local variables of pure procedures must not be saved.

213 E SAVE or BIND specified but entity not declared

- A variable or common block has been specified in a SAVE or BIND statement but has
  not been declared or used.

214 E not saved

- If a common block has been specified in a SAVE statement in a subprogram, it must
  be specified in a SAVE statement in every subprogram in which the common block has
  been specified.
- If an object of a type for which component initialization is specified appears in
  the specification part of a (sub)module and does not have the ALLOCATABLE or POINTER
  attribute, the object must be saved.
- An object in an initial data target must be saved.

215 E already specified automatic, static or allocatable

- An object must only be specified automatic, static or allocatable once.
- AUTOMATIC and STATIC cannot be specified both.

216 E invalidly specified automatic, static or allocatable

- A dummy variable, a common-block object and a pointee must not be specified
  automatic, static or allocatable.
- An allocatable array must not be specified automatic or static and must not be a
  pointer.
- An automatic, static or allocatable object must not be equivalenced.
- A target in a pointer initialization must not be allocatable.
- An assumed-type object must not be allocatable.

217 E conflict with program unit or ENTRY name

- The name of a constant, as defined in a PARAMETER statement must not be the same as
  a global name of the subprogram, such as the name of the program unit, or an
  entry.
- The name of a common block must not be the same as the name of a program unit or
  ENTRY.

218 E conflict with common-block name

- The name of a constant, as defined in a PARAMETER statement must not be the same as
  the name of a common block specified in the current subprogram.
- A global name, such as the name in a PROGRAM, BLOCKDATA, SUBROUTINE, FUNCTION or
  ENTRY statement, must not be the same as the name of a common block of the
  program.

219 E invalidly in COMMON, EQUIVALENCE, or NAMELIST

- A dummy procedure argument, automatic or allocatable variable and a pointee
  cannot be stored in a common block, and must not be equivalenced.
- A pointer array cannot be stored in common.
- If a compiler supports NAMELIST as a FORTRAN 77 extension, a dummy argument and
  a pointee can not be placed in a namelist.
- A dummy argument with non-constant bound, a variable with nonconstant character
  length, an automatic object, a pointer, a variable of a type that has a pointer,
  or allocatable variable, can not be placed in a namelist.
- An equivalence object must not have the TARGET attribute or be a pointee.
- An object, imported from a (sub)module, must not be in EQUIVALENCE or
  COM­MON.

220 E invalid initialization of entity in DATA or type statement

- In a blockdata program unit, only common-block variables can be initialized.
- A dummy procedure argument, automatic array, allocatable variable and pointee cannot
  be initialized in a DATA or type statement.
- In Fortran 90 a pointer can only be initialized with a pointer assignment, ALLO­CATE
  or NULLIFY statement. From Fortran 95 pointer initialization is supported.
- A component with the ALLOCATABLE attribute can not be initialized by default.
- A variable in a pure procedure must be initialized other than by default.

221 E more than once in BLOCKDATA

- The common block has been specified in more than one block-data program unit.

222 W mixing of character and numeric types in COMMON BLOCK

- In standard Fortran it is not allowed to store character and numeric data in the
  same common block.

223 W initialization of named COMMON should be in BLOCKDATA

- Variables in a named common block should only be initialized in a blockdata program
  unit.

224 W invalid initialization of variable in blank COMMON

- Variables in blank common should not be initialized.

225 E more than once in COMMON

226 I objects not in descending order of type size

- This order could cause alignment problems on some processors.

227 I extension of COMMON

- This COMMON statement extends a previously declared common block with the same
  name.

228 W size of common block inconsistent with first declaration

- Named common blocks must have the same length in every occurrence. The length of the
  common block in this occurrence is different from that as specified in the main
  program or as specified in the first occurrence encountered.

229 W type in COMMON inconsistent with first declaration

- Numeric and character objects must not be stored in the same common block. The type
  of the objects in this occurrence of the common block is different from that in main
  or in the first occurrence encountered.

230 W list of objects in named COMMON inconsistent with first declaration

- In this occurrence of the named common block objects with different types, type
  lengths, or array sizes have been stored than in the main program or in the first
  occurrence encountered.

231 W array bounds differ from first occurrence

232 I only specified once

- The common block has been specified in one subprogram only.

233 I common block inconsistently included from include file(s)

- The common block has been specified in an include file at one occurrence and
  specified directly in another occurrence.
- The same common block has been specified in different include files.

234 E invalid equivalence with object in COMMON

- If more than one of the objects in an equivalence list is in a common block, the
  objects cannot be equivalenced.

235 E equivalence of variable to itself

- The equivalence lists are such that you try to equivalence an object to itself.

236 E storage allocation conflict due to multiple equivalences

237 I equivalence of arrays with possibly different type lengths

- When using short integers and/or logicals, this code may be highly
  non-portable.

238 E invalid storage association of object with a pointer component

- A variable of a derived type with pointer components must not be used in EQUIVALENCE
  or COMMON.

239 E invalid extension of COMMON through EQUIVALENCE

- An object in a common block is in such a way equivalenced with an array that storage
  must be allocated before the start of the common block.

240 W extension of COMMON through EQUIVALENCE

- An object in a common block is in such a way equivalenced with an array that the
  common block has to be extended.

241 W nonstandard mixing of types in EQUIVALENCE

- Character and numeric data must not be equivalenced.
- Objects of type character must be of the same kind.
- Objects of an intrinsic, non default kind, must be of the same type and kind.
- Objects of a sequence derived type that is not a numeric sequence or character
  sequence type, must be of the same type and have the same type parameter
  values.

242 E more constants than variables

- More constants than variables have been found in this data statement list.

243 E more variables than constants

- More variable elements than constants have been found in this data statement
  list.

244 E more than once initialized in DATA or type statement

245 E no expression allowed

246 E invalid type or type length for an integer POINTER

247 W assumed-length character functions are obsolescent

- This is marked as obsolescent in the Fortran 95 standard.

248 I object already used, change statement sequence

- An explicit specification of an attribute confirms the attribute of an object that
  has already been used.

249 W list of objects in blank COMMON inconsistent with first declaration

- In this occurrence of the blank common-block objects with different types, type
  lengths, or array sizes have been stored than in main or in the first occurrence
  encountered.

250 I when referencing modules implicit typing is potentially risky

- There is an increased potential for undetected errors in a scoping unit that uses
  both implicit typing and the USE statement because module objects can be typed
  differently from the implicit type.

251 E SAVE has already been specified for each entity in this scoping unit

252 E a private object must not be placed in a public namelist group

- If a namelist-group-name has the PUBLIC attribute, no object in the
  namelist-group-object-list shall have the PRIVATE attribute or have private
  components.

253 W common-block data not retained: specify in root or save it

- The common block has not been SAVEd, has not been specified in the main program or
  in the root procedure of the referencing program units so the data become undefined
  after leaving the program unit.

254 W public module data not retained: specify in root or save it

- Not all public module data has been SAVEd, the module was not referenced in the main
  program or in the root procedure of the referencing program units so the data become
  undefined after leaving the program unit.

255 E derived type or structure undefined

- A variable of derived type is declared but the derived type has not been
  de­fined.
- A record is declared but the structure has not been defined.

- A parent type name shall be the name of a previously defined extensible type.

256 E statement invalid within derived type or structure definition

- This statement is not allowed within the definition of a derived type or
  structure.

257 E derived type or structure name missing

- The derived type name is missing in the type declaration
- The outer structure must have a name.

258 E invalid structure nesting

259 E missing END TYPE or END STRUCTURE

260 E missing END UNION

261 E missing END MAP

262 E invalid usage of record or aggregate field name

- A record must not be specified in an EQUIVALENCE, DATA, or NAMELIST statement.
- An aggregate field name is not allowed in formatted I/O.

263 E component or field name missing

- No derived type components or structure fields have been specified.
- A structure field which is a structure must have a field name.

264 E unknown component, field name, or type parameter

- A component or type parameter has been referenced which has not been declared in the
  derived type.
- A record field has been referenced which has not been declared in the
  structure.

265 E derived type must be of sequence type

266 E derived type or components must be PRIVATE

267 E no fields specified in structure definition

268 E incorrect number of component specs in structure-constructor

269 E malformed structure component

- At most one of the parts of a structure-component can be an array.
- A part-name to the right of an array must not have the POINTER attribute.

270 E derived-type component(s) or binding(s) inaccessible

- The component(s) or binding(s) of the derived-type are declared private.

271 E derived-type is inaccessible

272 E an object of a PRIVATE type cannot be PUBLIC

273 E invalid usage of structure-component or type-parameter

- A structure-component is not allowed in an EQUIVALENCE statement.
- The left side part of a structure must be of derived type.
- A type inquiry can not be defined.

274 E initialization of component or field not allowed

- In Fortran 90 initialization of derived-type components is not supported.

275 E derived-type of object must be sequence or have the BIND attribute

- The derived-type of an object in COMMON or EQUIVALENCE must be of sequence type or
  have the BIND attribute.
- The type of a dummy argument must be of sequence type or have the BIND attribute if
  the type is defined in the local context.
- The type of an actual argument of an external procedure must be of sequence type or
  have the BIND attribute

276 I derived type or structure inconsistently included from include file

- The derived type or structure has been specified in an include file at one
  occurrence and specified directly in another occurrence.
- The same derived type or structure has been specified in different include
  files.

277 E component must be allocatable

279 E invalid usage of derived-type name

280 E no type parameter, or inaccessible component

281 E unknown type-bound procedure

282 E the parent type must be extensible

283 E invalid sequence of operators

284 I not allocated

- A conditionally referenced or defined allocatable variable was not allocated.
- An INTENT(IN) argument was not allocated.

285 E scalar integer constant expression expected

286 E undefined when entered through ENTRY, specify SAVE to retain data

287 E scalar integer constant name expected

288 E scalar integer variable name expected

- An integer which is not an array element, array name, constant, external, structure,
  derived-type name or namelist name is expected.

289 E scalar integer variable expected

290 E constant or scalar integer variable expected

291 E unsigned nonzero integer expected

292 E expression expected

293 E constant expression expected

294 E integer expression expected

295 E scalar integer or real variable expected

296 E NULL() or target expected

297 E integer, logical, or character expression expected

298 E integer or character expression expected

299 E logical expression expected

300 E character constant or unsigned integer constant expected

301 E character expression expected

302 E character substring must not be zero sized in this context

303 E scalar logical expression expected

304 E scalar integer expression expected

305 E scalar integer or real expression expected

306 E array expected

307 E variable not defined

- The variable is referenced but has not been defined. No value has been as­signed to
  the variable, to the elements of the array (if the variable is an array), or to the
  components (if the variable is of derived type), or the fields of a record.

308 E no statement label assigned to this variable

- The variable has been referenced as a label but no label has been assigned to the
  variable.

309 I possibly no statement label assigned to this variable

- The variable has been referenced as a label but, if statements are executed
  sequentially, no label has been assigned to the variable. There might be, how­ever,
  a path through which the variable is assigned before referenced.

310 I label assigned to dummy argument or variable in COMMON

- It is unsafe and not functional to use a global variable to denote a label.

311 I both a numeric value and label assigned to this variable

- The variable is used both to denote a label and a numeric value. This is potentially
  unsafe.

312 E no value assigned to this variable

- The variable is referenced but no value has been assigned to the variable, an
  element of the array, a component of the structure, or a field of the record.
- The variable is a dummy output argument but no value has been assigned to it.

313 I possibly no value assigned to this variable

- The variable has been referenced in an expression but, if statements are executed
  sequentially, no value has been assigned to the variable. There might be, however, a
  path through which the variable is defined before referenced.
- A dummy argument is referenced but it is not a dummy argument in all entries through
  which this statement can be reached.

314 I possible change of initial value

- A variable has been initialized in a DATA statement or explicit type specification
  statement and a new value has been assigned to it. For a scalar of intrinsic type
  this means that the initial value has been superseded permanently. For an array or a
  variable of derived type this means that the value of one or more elements or
  components might have been superseded.

315 I redefined before referenced

- A new value was assigned to the variable before it was referenced.
- The dummy argument is apparently an output variable while the last operation on the
  actual argument was an assignment.

316 W not locally defined, specify SAVE in the module to retain data

- The variable is not defined in this program unit or in the module where it is
  declared. It could have been defined by another program unit using the module. In
  that case you must save the data in the module to preserve the data. From Fortran
  2008 on module data are saved by default.

317 E entity imported from more than one module: do not use

318 E not allocated

- An allocatable variable must be allocated before being defined or referenced.

319 W not locally allocated, specify SAVE in the module to retain data

- An allocatable variable must be allocated before being defined or referenced. The
  variable is not allocated in this program unit. It is use associated but not saved.
  From Fortran 2008 on module data are saved by default.

320 E pointer not associated

321 I pointer not associated

322 I target not associated with a pointer

323 I variable unreferenced

- A variable has been defined but is not referenced.

324 I variable unreferenced as statement label

- A label has been assigned to this variable but the variable has not been referenced
  as a label.

325 I input variable unreferenced

- A variable which is defined by a READ, INPUT, or DECODE statement is not
  referenced.

326 I entity, declared in include file, not used

- An external, namelist, or local variable has been declared in an include file but is
  not used in the current subprogram.

327 E subscript out of range

328 I array, array extent, or character variable is zero sized

- The array extent is zero.
- The first bound of a specified shape is higher than the second bound.
- The first substring value is higher than the second.

329 E substring expression out of range

330 E invalid substring

331 E invalid usage of substring

332 W referenced character elements defined

- In Fortran 77 none of the character positions defined may be referenced in the same
  statement.

333 E division by zero

334 E invalid power execution

- It is invalid to raise a negative number to a real exponent.

335 E types do not conform

336 W typeless data used in invalid context

- Octal, hexadecimal and Hollerith data should only be used in DATA or PARAMETER
  statements

337 I implicit conversion to shorter type

- The type length of the variable is shorter than the resulting type length of the
  expression.

338 I character variable padded with blanks

339 E integer overflow in expression

340 I equality or inequality comparison of floating point data

- Because of limited precision and different implementations of real and complex
  numbers the result of this comparison may be unpredictable.

341 I eq. or ineq. comparison of floating point data with integer

- Because of limited precision and different implementations of real and complex
  numbers the result of this comparison may be unpredictable.

342 I eq.or ineq. comparison of floating point data with zero constant

- Because of limited precision and different implementations of real and complex
  numbers the result of this comparison may be unpredictable.

343 I implicit conversion of complex to scalar

- An integer or real is assigned to a complex variable.

344 I implicit conversion of constant (expression) to higher accuracy

- In an assignment statement precision is lost if the variable is of a more accurate
  type than the constant or constant expression.
- In a complex constant precision is lost if one of the components is of a less
  accurate type than the other.
- In an expression precision is lost if a constant is specified in a less accurate
  type than the resulting expression.

345 I implicit conversion to less accurate type

- Precision is lost due to conversion of real to real of less precision.

346 I implicit conversion of integer to real

347 I non-optimal explicit type conversion

- If the target of an expression is of type double precision real, best is to convert
  the expression primaries to double precision real explicitly, e.g. by specifying the
  kind type parameter.
- If the target of an expression is of type double precision complex, best is to
  convert the expression primaries to double precision complex explicitly, e.g. by
  specifying the kind type parameter.

348 E invalid usage of logical operator

349 E invalid usage of relational operator

350 E invalid mixed mode expression

351 E invalid usage of operator

352 W nonstandard operator

353 E undefined operator

354 E invalid concatenation with character variable of assumed length

- In Fortran 77 concatenation with a character variable of assumed length is only
  allowed in a character assignment statement.

355 E array-section specification invalid for assumed-shape array

- The second subscript of a subscript triplet of an array section must not be omit­ted
  for an assumed-shape array.

356 E array section specified incorrectly

357 E no array section allowed in this context

358 E invalid stride

359 E array has invalid rank

360 E each element in an array constructor must be of the same decl. type

361 E each element in an array constructor must have the same type length

362 E vector-valued subscript not allowed in this context

363 E array does not conform to expression, other arguments or target

- The rank or shape of the argument differs from that of the other arguments of the
  intrinsic procedure reference.
- The rank or shape of the expression differs from that of the left-hand side of an
  assignment statement.

364 E arrays do not conform

- The rank or shape of the operands in an expression differ.

365 E only nonproc.pointers and allocatable variables can be (de)allocated

366 E defined assignment not allowed in this context

367 E pointer assignment expected

368 E invalid usage of pointer assignment

369 E invalid assignment to pointer

370 E invalid target for a data pointer

- the Object must have the POINTER or TARGET attribute to be assigned to a data
  pointer

371 E only pointers can be nullified

372 E target must have the same rank as the pointer

373 E shape of variable differs from the shape of the mask expression

374 E assignment of array expression to scalar

375 E integer overflow in assignment

- The right-site expression yields a value which does not fit in the left-site
  target.

376 W scalar integer variable name expected

- An integer which is not an array element, array name, constant, external, structure,
  derived-type name or namelist name is expected.

377 W scalar integer expression expected

378 W pointer not locally associated, specify SAVE in the module

- A pointer must be associated before being referenced. The pointer is not associated
  in this program unit. It is use associated but not saved. From Fortran 2008 on
  module data are saved by default.

379 E invalid operation on a non-local variable in a pure procedure

- A global variable must not be modified in a pure procedure.
- Allocation, deallocation of global variables is not allowed in a pure
  procedure.
- pointer operations on global variables are not allowed in a pure procedure.

380 E shape of mask expression differs from shape of outer WHERE construct

- If a WHERE construct contains a WHERE statement, a masked ELSEWHERE statement, or
  another WHERE construct then each mask expression shall have the same shape.

381 E none of the equivalenced variables of the same type is defined

- The variable is referenced but the variable and none of the equivalenced variables
  with the same type are defined.

382 I none of the equivalenced variables of the same type referenced

- The variable is defined but the variable and none of the equivalenced objects with
  the same type are referenced.

383 I truncation of character constant (expression)

- The type length of the variable is shorter than the resulting type length of the
  expression.

384 I truncation of character variable (expression)

- The type length of the variable is shorter than the resulting type length of the
  expression.

385 E invalid usage of construct name

386 E construct name expected

387 E non-matching construct name

- The construct name does not match the name of a construct.

388 E invalid construct nesting

389 E invalid statement in logical IF

- A statement in a logical IF must be executable, but no IF, ELSEIF, ELSE, DO, or
  END.

390 E statement not allowed within a construct

391 E too many ENDIF’s

392 E ELSE must be between IF and ENDIF

393 E missing ENDIF(’s)

394 E THEN missing

395 E invalid sequence of ELSEIF and ELSE

397 E more than one ELSE at this IF level

398 E invalid DO-loop incrementation parameter

- The incrementation parameter of an (implied) DO loop is too small.

399 E invalid implied-DO specification

400 E invalid DO-loop specification

401 E terminal statement of loop at invalid IF level

402 E invalid terminal statement of DO construct

- A DO construct must end with an executable statement, but no IF, ELSEIF, ELSE,
  ELSEIF, DO, STOP, RETURN, or END.

403 E invalid transfer of control into construct

- A branch is detected which transfers control into a DO, an IF, CASE, WHERE, or
  FORALL construct

404 E referenced from outside construct

405 E redefinition of DO variable or construct index within construct •A DO variable of
an active DO loop is modified.

- An index name of a FORALL statement is modified in the forall statement or active
  FORALL construct.
- An index name of a DO CONCURRENT construct is modified in the active DO CONCURRENT
  construct.

406 I no action statements in previous construct or construct block

407 E terminal statement of DO construct out of order

408 E missing terminal statement of DO construct

- No definition of the label of the terminal statement of the DO loop has been
  found.
- END DO missing

409 E missing END LOOP or UNTIL

410 E missing END WHILE or UNTIL

411 E too many END DO’s, END LOOP’s, or END WHILE’s

412 E terminal statement of DO construct at invalid CASE level

413 W shared DO termination

- This syntax is marked as obsolescent in Fortran 90 and up

414 E Incorrect usage of RANK(*)

415 E too many END BLOCKS

416 E missing END BLOCK (’s)

418 E type inconsistent with SELECT CASE expression type

419 E kind inconsistent with SELECT CASE expression kind

420 E invalid range of values specified

- A range of values of type logical cannot be specified

421 E overlapping CASE range

422 E CASE statement expected after a SELECT CASE statement

423 E a CASE statement must be within a CASE construct

424 E too many END SELECT’s

425 E missing END SELECT (’s)

426 E only one CASE DEFAULT statement allowed in a CASE construct

427 E statement at invalid DO level

428 E statement at invalid IF level

429 E statement at invalid CASE level

430 E invalid statement after WHERE

431 E rank out of range

432 E too many END WHERE’s

433 E an ELSEWHERE must be within a WHERE construct

434 E missing END WHERE(’s)

435 E too many END FORALL’s

436 E missing END FORALL(’s)

437 E reference of construct index in a concurrent control triplet

438 W obsolescent terminal statement of DO loop

- In Fortran 90 and up a terminal statement of a DO loop must be an END DO or a
  CONTINUE statement

439 E type already selected

440 E too many END ASSOCIATES’s

441 E statement not allowed within SELECT TYPE construct

442 E rank already selected

443 E RANK, or RANK DEFAULT at invalid SELECT RANK level

444 E only one RANK DEFAULT statement allowed in a SELECT RANK construct

445 E only one CLASS DEFAULT statement allowed in a SELECT TYPE construct

446 E missing output item list

447 E invalid input/output list

448 W ”,” not allowed

- After a command-info list, no comma must be used.
- In an explicit type statement a comma may only be used in a CHARACTER statement
  after the length specification.

449 W invalid usage of parentheses

- Redundant parentheses are not allowed in an I/O list.

450 E invalid reference of standard unit

- OPEN, CLOSE, ENCODE, DECODE, BACKSPACE, REWIND is not possible on the standard
  unit.

451 W list directed I/O not allowed

- List directed I/O is only allowed for sequential I/O, and not on internal
  files.

452 E sequential formatted access expected

- Only sequential formatted I/O is allowed for internal I/O and I/O on the standard
  unit.

453 E invalid reference of internal file

- Only read and write operations can be performed on an internal file.
- The unit identifier must be a character variable, but not a constant or
  expression.

454 I possible recursive I/O attempt

- A function in which I/O may occur is referenced in an I/O statement.

455 W unrecognized or unsupported specifier

- An unsupported, nonstandard Fortran specifier has been detected.
- The specifier is not supported for this statement.

456 W nonstandard Fortran specifier

- One of the standard options is specified and the specifier is not in the Fortran
  standard.
- The specifier is an old, obsolescent, synonym for a standard specifier.

457 E more than once specified

- The specifier has already been specified in the list.

458 E invalid usage of specifier

- POS= only allowed for an external unit that is not specified by an asterix.
- ID= only allowed in combination with PENDING=
- If NEWUNIT= specified, FILE= or STATUS= must be present.

459 E no unit specified

460 E no unit or filename specified

461 E unit and filename specified

462 E invalid or missing io-unit identifier

- A unit identifier must be an asterix (standard unit), a positive integer expression,
  or a character variable.

463 E missing or invalid format specifier

- A format specifier must be: a label of a format statement, an integer variable to
  which a label of a format statement is assigned, a character expression containing
  the format specification, a non-character array name (language extension).
- In Fortran 90 a namelist group name must be specified with the NML= specifier.

464 W missing delimiter in format specification

465 E statement label expected

466 E more than once in OPEN, CLOSE, or INQUIRE list

- A variable or array element, or any associated entity, must not be both referenced
  and defined, or defined more than once in an OPEN, CLOSE or INQUIRE statement.

467 E ”FMT=” or ”NML=” expected

- When in a control-info list a keyword has been used, all specifiers from there on
  must be specified using keywords.

468 E ”END=” only allowed in a sequential READ or WAIT statement

469 W ”FILE=” not allowed for a scratch file

470 W ”RECL=” only allowed for a direct access file

471 E ”BLANK=” only allowed for a formatted file

472 E ”ADVANCE=” only allowed for external formatted sequential i/o

- The ADVANCE= specifier may be present only in a formatted sequential input/output
  statement with explicit format specification and with no internal file unit
  specifier.

473 E ”EOR=” only allowed in READ with ”ADVANCE=NO” or WAIT

- The EOR= specifier is only allowed in an input statement that contains the ADVANCE=
  specifier with the value NO, or in a WAIT statement.

474 W no record size specified

475 E ”SIZE=” only allowed in READ with ”ADVANCE=NO”

- The SIZE= specifiers is only allowed in an input statement that contains the
  ADVANCE= specifier with the value NO.

476 E must be declared EXTERNAL

- The procedure name specified in ”USEROPEN=” must have been declared EXTERNAL

477 E invalid combination of specifiers

- For namelist I/O no format must be specified.
- POS= and REC= must not be specified both.

478 E invalid usage of namelist name

- A namelist specifier is only allowed in sequential read and write statements on an
  external file.

479 E namelist name expected

480 E namelist i/o only allowed on an external file

481 I extension of previously defined namelist

- This NAMELIST statement extends a previously declared namelist with the same
  name.

482 E invalid type

483 W unrecognized value

- An unsupported, nonstandard Fortran value has been detected.

484 E invalid usage of value

485 W nonstandard Fortran value

486 E invalid repeat

- A nonzero, unsigned, integer constant is required.

487 E missing repeat

- A nonzero, unsigned, integer constant is required.

488 E invalid usage of repeat

489 E invalid usage of scale factor

- A scalefactor is only allowed for floating point edit descriptors.

490 W nonstandard edit descriptor

491 E missing or invalid width

- A nonzero, unsigned, integer constant is required.

492 E invalid edit descriptor

- No valid edit descriptor was detected.

493 E external i/o not allowed in a pure procedure

494 I namelist unreferenced

- A namelist has been specified but is never referenced (used).

495 I more than once in namelist group

496 E namelist group undefined

- A namelist group is referenced but it has not been specified.

497 E stream and async i/o only allowed on ext. files and not on * units

498 E namelist i/o only allowed for sequential i/o

499 E accompanying subprogram statement missing or incorrect

500 E no main program unit

- The complete option was specified but no main program is present.

501 I recursive reference

502 I possible recursive reference

503 E more than one main program unit

- A main program is a program unit of which the first statement is not a BLOCK-DATA,
  SUBROUTINE, or FUNCTION statement. Therefor, besides of a program unit beginning
  with a PROGRAM statement, a main program will also be detected when e.g. two
  consecutive END statements have been specified.

504 E more than one unnamed BLOCKDATA

- Only one unnamed blockdata program unit is allowed.

505 E multiple declaration of BLOCKDATA

- The name of the blockdata program unit has already been declared as the name of a
  blockdata program unit.

506 E multiple declaration of program unit or entry

- The name has been defined already before as a PROGRAM, SUBROUTINE, FUNCTION or ENTRY
  name.
- The name of a program, subroutine, function, or entry name has already been
  used.

507 E multiple declaration of statement function

508 I entries are not disjoint

- There could be transfer of control to the current or other entry blocks.

509 E no name specified

- A procedure, (sub)module or type name is expected.

510 E multiple declaration of interface, this one ignored

511 E explicit interface required

512 E invalid subroutine or function reference

- A procedure reference is not allowed in this context.
- The function needs an explicit interface and must not be referenced in this
  con­text.

513 E invalid usage of procedure name

- The name of the current subprogram or entry cannot be used as an actual
  argument.
- An internal procedure name cannot be used as an actual argument.
- A procedure name must not be specified in a type-declaration-statement with a
  language-binding.

514 E subroutine/function conflict

- The procedure is referenced as a subroutine but has been referenced or de­fined as a
  function before.
- The procedure is referenced as a function but has been referenced or defined as a
  subroutine before.

515 E invalid subprogram type

516 E invalid usage of EXTERNAL

- A procedure name, as specified in an EXTERNAL statement, cannot be used at the left
  side of an assignment statement or as a statement function.

517 E procedure actual argument must be declared EXTERNAL or INTRINSIC

- A procedure name, used as an actual argument, must be declared EXTERNAL or
  INTRINSIC.

518 W referenced procedure not declared EXTERNAL

519 I name of external procedure is same as module procedure name

520 E referenced procedure not declared EXTERNAL

521 E invalid usage of generic name

- The generic name of a procedure cannot be used as an actual argument. Use the
  appropriate specific name.

522 E an interface with (module) procedure statements must be generic

523 E procedure already in list of specific procedures of this interface

524 W mixing of subroutines and functions in generic interface not allowed

- The Fortran standard does not allow to combine specific functions and subroutines in
  a generic procedure. Some compilers allow this as a syntax extension.

525 E defined operator procedure must be a function

526 E defined assignment procedure must be a subroutine

527 E no matching intrinsic or specific procedure found

528 I no procedure interfaces specified in interface block

529 E recursive reference

- A function is referenced recursively while recursive functions are not supported in
  the Fortran language level specified.
- A function is referenced recursively while it is not specified to be recursive.
- A module is referenced circularly.

530 W possible recursive reference

- A path has been detected through which the procedure may reference itself.

531 I function is impure

- An argument and/or common-block object is being modified in this procedure.
- A local variable is saved.

- A non-local variable is modified in this procedure.
- A variable is initialized in a type or data statement.

532 E type conflict with type of function

- All entries within a character function must be of type character.
- The type specified when referencing the function differs from the specification of
  the function.

533 E type length conflict with type length of function

- All entries within function must have the same type length.
- The type length while referencing the function differs from the specification of the
  function.

534 E type of function inconsistent with first occurrence

- The type of the function differs from that at the first reference encountered.

535 E function type length inconsistent with first occurrence

- The type length of the function differs from that at the first reference
  encountered.

536 I function type length inconsistent with first occurrence

- The type length of the dummy function differs from that at the first reference
  encountered.

537 E shape of function reference differs from shape at first reference

538 E shape of function reference differs from shape of function result

539 E procedure must have private accessibility

- If one or more of the dummy arguments or the function result is of private type the
  procedure must be private.

540 E multiple specification of prefix specification

541 E invalid combination of prefix specifications

- A procedure cannot be specified elemental and recursive.
- PURE and IMPURE cannot be specified both.

542 E procedure must be pure

- Any procedure referenced in a pure subprogram, a forall statement, FORALL construct,
  or DO CONCURRENT construct shall be pure.

543 E invalid usage of prefix specification

544 E dummy argument of elemental procedure must be scalar

545 E dummy arg. of elemental proc. must not be a pointer or allocatable

546 E elemental procedure must be scalar

547 E elemental procedure must not be a pointer or allocatable

548 E dummy procedure argument not allowed in elemental procedure

549 W referenced intrinsic procedure not declared INTRINSIC

550 E invalid usage of alternate return

- An alternate return is only allowed in a subroutine which is not elemental.

551 E invalid dummy argument list

552 E invalid usage of arguments

- In an EXTERNAL or INTRINSIC specification a single procedure name without arguments
  is required.
- In a dummy argument list a dummy procedure must not have arguments.
- In the reference of an external procedure in USEROPEN no arguments are
  al­lowed.

553 E invalid usage of dummy argument

- The name of a dummy procedure argument has been used as the name of a statement
  function.
- A pointee cannot be a dummy argument.

554 E invalid dummy argument

- A dummy procedure argument cannot be a constant or expression.

555 E more than once in argument list

- A dummy argument is specified more than once in the dummy argument list.
- An argument keyword is specified more than once in the actual argument list.

556 I argument unreferenced in statement function

- A dummy argument of a statement function is not referenced in the statement
  function.

557 I dummy argument not used

558 E missing argument list

- In an expression or in an output statement a function must have an actual argument
  list. This argument list can be empty.
- In a FUNCTION statement an argument list is required. This list can be empty.

559 E argument missing, or no corresponding actual argument found

- A null argument is nonstandard Fortran.
- A non-optional actual argument is missing.
- No actual argument with the dummy argument keyword is found.

560 E incorrect number of arguments

561 E incorrect argument type

562 E incorrect argument attributes

563 E number of arguments inconsistent with first occurrence

- The number of actual arguments differs from that at the first reference
  encountered.

564 I number of arguments inconsistent with first occurrence

- The number of arguments of the dummy procedure differs from that at the first
  reference encountered.

565 E number of arguments inconsistent with specification

- The number of actual arguments differs from that in the specification of the
  procedure.

566 E argument keyword missing in actual argument list

- When in an argument list a keyword has been used, all subsequent arguments must be
  specified using keywords.

567 E argument keyword does not match a dummy argument

568 E argument class inconsistent with first occurrence

- The actual argument is a function, subroutine, external name, record, or label, but
  at the first reference encountered, the argument is of a different class.

569 I type inconsistent with first occurrence

- The actual argument of the dummy procedure is a function, subroutine, external name,
  record, or label, but at the first reference encountered, the argument is of a
  different class.
- The type of an actual argument of the dummy procedure differs from that at the first
  reference encountered.

570 E argument class inconsistent with specification

- The actual argument is a function, subroutine, external name, or label, but in the
  specification of the procedure the argument is of a different class.

571 E argument type inconsistent with first occurrence

- The type of an actual argument differs from that at the first reference
  encountered.

572 W type inconsistent with first occurrence

- The type of a common-block object differs from that in the first list
  encountered.

573 E argument type inconsistent with specification

- The type of an actual argument differs from that in the specification of the
  procedure.

574 E argument type inconsistent with first occurrence (int/log)

- The type of an actual argument differs from that at the first reference encountered.
  (Mixing of integer and logical types of equal lengths.)

575 W argument type inconsistent with first occurrence (int/log)

- The type of an actual argument of the dummy procedure differs from that at the first
  reference encountered. (Mixing of integer and logical types of equal lengths.)

576 E argument type inconsistent with specification (int/log)

- The type of an actual argument differs from that in the specification of the
  procedure. (Mixing of integer and logical types of equal lengths.)

577 E argument type inconsistent with first occurrence (int/real)

- The type of an actual argument differs from that at the first reference encountered.
  (Mixing of integer and real types of equal lengths.)

578 I argument type inconsistent with first occurrence (int/real)

- The type of an actual argument of the dummy procedure differs from that at the first
  reference encountered. (Mixing of integer and real types of equal lengths.)

579 E argument type inconsistent with specification (int/real)

- The type of an actual argument differs from that in the specification of the
  procedure. (Mixing of integer and real types of equal lengths.)

580 E argument type length inconsistent with first occurrence

- The type length of an actual argument differs from that at the first reference
  encountered.

581 I type length inconsistent with first occurrence

- The type length of an argument of a dummy procedure differs from that at the first
  reference encountered.
- The type length of a common-block object differs from that in the first list
  en­countered.
- The type length is explicit in one instance and implicit in another.

582 E argument type length inconsistent with specification

- The type length of an actual argument differs from that in the specification of the
  procedure.

583 E type of function argument inconsistent with first occurrence

- The type of a function actual argument differs from that at the first reference
  encountered.

584 I type of function argument inconsistent with first occurrence

- The type of a function actual argument of the dummy procedure differs from that at
  the first reference encountered.

585 E argument type kind inconsistent with first occurrence

- The type kind of an actual argument differs from that at the first reference
  en­countered.

586 I type kind inconsistent with first occurrence

- The type kind of an argument of a dummy procedure differs from that at the first
  reference encountered.
- The type kind of a common-block object differs from that in the first list
  encountered.
- The type kind is explicit in one instance and implicit in another.
- The type kind has been specified in one instance, the type length in the other.

587 E type of function argument inconsistent with specification

- The type of a function actual argument differs from that in the specification of
  the procedure.

588 E argument type kind inconsistent with specification

- The type kind of an actual argument differs from that in the specification of the
  procedure.

589 E shape of this argument must be supplied as argument

- Adjustable shapes must be specified in each entry in which the array occurs.

590 E array versus scalar conflict

- An actual argument is an array name while at a previous reference the argument is a
  scalar, or vice versa.
- An actual argument is an array name while the dummy argument is a scalar, or vice
  versa.
- An actual argument is an array element of an assumed-shape or pointer array while
  the dummy argument is an array.

591 I array versus scalar conflict

- The argument of a dummy procedure is an array name, while at a previous reference
  the argument was a scalar, or vice versa.

592 I arg. is an array element while it was an array in the previous ref.

593 I arg. is an array while it was an array element in the previous ref.

594 I the actual argument is an array element while the dummy is an array

595 I shape of argument differs from first occurrence

596 E shape of argument differs from specification

597 I shape of argument differs from specification

598 E actual array or character variable shorter than dummy

- The array or character datum as specified in the procedure is longer than the size
  specified the referencing program unit.

599 W array or character length differs form first occurrence

600 E attributes of argument inconsistent with first occurrence

601 E attributes of actual argument inconsistent with specification

602 E invalid modification: actual argument is constant or expression

- The dummy procedure argument is an output or input/output argument but cannot modify
  the actual argument.

604 E invalid modification: the actual argument is an active DO variable

- The dummy procedure argument is an output or input/output argument and will modify
  the actual argument which is an active DO variable.

605 I possible invalid modification: act.arg. is constant or expression

- The procedure might modify this argument.

607 I possible invalid modification: actual argument is active DO variable

- The actual argument is an active DO variable and might be modified during the
  procedure reference.

608 I no INTENT specified, specify INTENT(IN) in the referenced subprogram

609 E dummy argument must not be OPTIONAL

610 E optional dummy argument unconditionally used

- An optional dummy argument may only be referenced, defined, allocated, or
  deallocated if it is present in the actual argument list of the referencing program
  unit, unless as an actual argument of a procedure reference if the corresponding
  dummy argument is also optional and not a pointer.

611 E actual argument is an optional dummy argument, the dummy argument not

- The procedure is unconditionally referenced while the actual argument is an
  optional dummy argument of the referencing procedure which may not be present.

612 E optional dummy argument expected

613 E INTENT not allowed for pointer arguments

614 E INTENT(IN) or VALUE attribute required for this dummy argument

- The arguments of a defined operator function must be declared INTENT(IN) or have the
  VALUE attribute.
- The second argument of a defined assignment subroutine must be declared INTENT(IN)
  or have the value attribute.
- The arguments of a pure or elemental function must be declared INTENT(IN) or have
  the VALUE attribute.

615 E INTENT(OUT) or INTENT(INOUT) required for this dummy argument

- The first argument of a defined assignment subroutine must be declared IN-TENT(OUT)
  or INTENT(INOUT).

616 E referenced input or input/output argument is not defined

- The argument was not defined when the procedure was referenced and not defined
  in the procedure before it was unconditionally referenced.

617 I conditionally referenced argument is not defined

- The argument was not unconditionally defined when the procedure was referenced and
  it was not defined in the procedure before it was conditionally referenced.

618 I possibly ref. input or input/output argument is possibly not defined

- The argument was not unconditionally defined when the procedure was referenced and
  not defined in the procedure before it was referenced.
- The argument was not defined when the procedure was referenced and was possibly not
  defined in the procedure before it was referenced.

622 E dummy function must be specified as entry argument

- A dummy function must be specified in the argument list of each ENTRY statement from
  where the function is referenced.

623 I intrinsic procedure is specific

- By referencing the generic intrinsic procedure instead, the code will be better
  readable, portable and easier to adapt to different type parameters.

624 E conflict with intrinsic-procedure name

- A generic procedure has been referenced while the name of the generated specific
  procedure is already in use as a user defined, dummy, or statement function.
- The name of a common block must not be the name of an intrinsic procedure.

625 W nonstandard Fortran intrinsic procedure

626 E no intrinsic procedure

- A non-intrinsic procedure has been specified in an INTRINSIC statement.

627 E this intrinsic function is not allowed as actual argument

- The intrinsic functions to determine the minimum and maximum and the type conversion
  functions must not be passed as an argument.

628 E type conflict with intrinsic function of the same name

- An intrinsic function has been generated or referenced while an intrinsic function
  with the same name and different data type has already been declared or used.

629 E invalid number of arguments for intrinsic procedure

630 E invalid argument type for intrinsic procedure

- The type of the argument of a specific procedure is incorrect.
- No specific procedure could be generated of which the argument type matches the
  actual argument type.

- A specific procedure has been generated with an argument type which matches the
  argument type of the first argument, but the type of (one of) the other arguments
  does not match.

631 E invalid argument type length for intrinsic procedure

- The type length of the argument of a specific procedure is incorrect.
- No specific procedure could be generated of which the argument type length matches
  the actual argument type length.
- A specific procedure has been generated with an argument type length which matches
  the argument type length of the first argument, but the type length of (one of) the
  other arguments does not match.

632 I intrinsic function is explicitly typed

- Intrinsic functions are implicitly typed and need not to appear in a type
  statement.

633 E invalid usage of built-in function

- This built-in function can only be used in an actual argument list.

634 E invalid modification, variable more than once in statement

- If a variable occurs more than once in a statement it must not be modified during
  evaluation of the statement (Fortran 77). The dummy procedure argument is an output,
  or inout argument and will modify the actual argument.

635 I possible invalid modification:variable more than once in statement

- The variable occurs more than once in the statement in which the procedure is
  referenced and might be modified during the reference (Fortran 77).

636 E INTENT must be specified for this dummy argument

- The intent of the arguments of a pure subprogram must be specified.
- The intent of the arguments of an elemental subprogram that do not have the VALUE
  attribute must be specified.

637 E specific procedure has no unique argument list

638 E invalid redefinition of intrinsic operation or assignment

639 I type is not the type of the generic intrinsic function

- Specifying a type for a generic intrinsic function does not, in itself, remove the
  generic property from that function.

640 E generic procedure reference could not uniquely be solved

641 E argument must be an allocatable variable

642 E argument must have the POINTER attribute

643 E argument must have the POINTER or TARGET attribute

644 I none of the entities, imported from the module, is used

645 E module must not reference itself directly or indirectly

646 E (MODULE OR SUBMODULE NOT FOUND)

- The (sub)module information is not found.
- The library entry found is not a module.

647 E multiple specification of (sub)module

- A (sub)module with the same name has already been analyzed.

648 E conflict between (sub)module and program unit or entry name

649 I module already referenced without only or rename list

650 E invalid rename clause

- No generic name, operator, or assignment expected.
- local name=¿module name expected.

651 I entity already imported from host or same module

- The entity is in an ONLY list and has already been imported from the same module in
  the same or host scoping unit.
- The entity is already imported from the host scoping unit

652 I entity imported from more than one module: do not reference

653 E entity is not a public entity of the imported module

654 I (sub)module unused

- The complete option has been specified and the module is not imported in any of the
  analysed program units, or a submodule is not used.

665 I eq. or ineq. comparison of floating point data with constant

- Because of limited precision and different implementations of real and complex
  numbers the result of this comparison may be unpredictable.

666 E undefined operation

667 E undefined: dummy argument not in entry argument list

- The variable has been referenced but when entered through the previous EN­TRY
  statement no value has been assigned to the variable.

668 I possibly undefined: dummy argument not in entry argument list

- The variable has been conditionally referenced but when entered through the previous
  ENTRY statement no value has been assigned to the variable.

669 I not locally associated, specify SAVE in the module to retain data

- A target must be associated with a pointer before being defined or referenced. The
  variable is not associated in this program unit and is use associated but not saved.
  From Fortran 2008 on module data are saved by default.

670 E actual argument must be a variable

- The dummy procedure argument is an output or input/output argument and could modify
  the actual argument.

671 E variable more than once in actual argument list

- The dummy procedure argument is an output or input/output argument and could modify
  the actual argument.

672 E active DO variable invalid for this actual argument

- The dummy procedure argument is an output or input/output argument and could modify
  the actual argument.

673 I not locally referenced

- The variable is not referenced in this subprogram. It could have been referenced by
  another subprogram using the module.

674 I procedure, program unit, or entry not referenced

- A procedure or program unit (entry) has been explicitly specified but is not
  referenced.

675 I named constant not used

- A named constant has been defined but is never referenced.

676 I none of the objects of the common block is used

677 I none of the objects of the common block is referenced

678 I none of the entities stored in the library file is used

679 I common-block object not used

680 I common-block object unreferenced

681 I not used

- An entity has been declared and possibly allocated, initialized or assigned, but is
  never used.

682 E procedure not defined

- The specified module procedure is not defined in the module.

683 E common-block object not defined before referenced

684 I common-block object possibly not defined before referenced

- The common-block object was conditionally defined.

685 I generic name was not needed to generate a specific procedure

686 E conflict with constant name

- The name of a common block must not be the same as the name of a constant.

687 E type length must be specified by a constant expression

- The type length of this object must be known at compile time.

688 E implicit characteristics are inconsistent with those in host context

- The type of the entity has been declared in the host scoping unit however, in the
  current scoping unit it appears to be a statement function. You must declare this
  entity locally.
- The type of the object has been declared in the host scoping unit however, in the
  current scoping unit it appears to be an EXTERNAL or INTRINSIC procedure. You must
  declare the entity in the host scoping unit as EXTERNAL or INTRINSIC.

689 I type length inconsistent with type length of function

- All entries within a function must have the same type length. One has the de­fault
  length, the other has an explicitly specified type length.
- The type length while referencing the function is inconsistently specified com­pared
  to the specification of the function. One has the default length, the other has an
  explicitly specified type length.

690 I type length inconsistent with type length at first reference

- The type length while referencing the function is inconsistently specified com­pared
  to the first reference. One has the default length, the other has an explicitly
  specified type length.
- The type length of an actual argument is inconsistently specified compared to the
  first reference encountered. One has the default length, the other has an explicitly
  specified type length.
- The type length of a common-block object is inconsistently specified compared to the
  first reference encountered. One has the default length, the other has an explicitly
  specified type length.

691 I type length inconsistent with specification

- type length of an actual argument is inconsistently specified compared to the
  specification of the procedure. One has the default type length, the other has an
  explicitly specified type length.

692 E result of procedure must be scalar

693 E storage association conflict with object with the TARGET attribute

- An object with the TARGET attribute may become storage associated only with another
  object that has the TARGET attribute and the same type and type parameters.

694 E explicitness of dummy proc. argument inconsistent with first occurr.

- If the interface of a dummy procedure argument is explicit in one instance it must
  be explicit in each instance.

695 E no defined assignment supplied for this type

- If a defined assignment for one or more of the derived type components is present,
  you must supply a defined assignment for the type.

696 E entity is not an accessible entity in the host scoping unit

697 E name not explicitly typed, implicit type assumed

- The object has not been explicitly typed and:
- IMPLICIT NONE has been specified.

698 I implicit conversion to more accurate type

699 I implicit conversion of real or complex to integer

- Precision is lost due to conversion to integer.

700 E object undeclared

- An attribute is specified for an object which has not been specified.

701 I type length of element inconsistent with first element

- The type length of this array element is inconsistently specified compared to that
  of the first element. One has the default length, the other has an explicitly
  specified type length.

702 E scalar default character expression expected

703 E a procedure cannot have the POINTER or TARGET attribute

704 E more than once in derived-type parameter list

705 E the VALUE attribute cannot be specified for this object

706 E a protected object must not be modified outside its module

707 I module procedure not referenced from outside its module

- The module procedure can be declared private.

708 E END INTERFACE statement missing

709 E source expression not allowed for a typed allocation

- type-spec and a source expression cannot be specified both.

710 E only one source expression allowed in a sourced allocation

- SOURCE= and MOLD= cannot be specified both.

711 I declared RECURSIVE but not recursively referenced

712 E ancestor or parent (sub)module name missing

713 E interface name missing

714 I abstract interface not referenced

- An abstract procedure interface has been specified but it is not used.

715 E type-bound procedures not allowed in sequence or interoperable type

716 E a component cannot have the name of a type parameter

- KIND or LEN must be specified for a derived-type parameter declaration.
- Only KIND and LEN are valid derived-type parameter attributes.

717 E derived-type parameter not specified

- Each derived-type parameter must be declared with the KIND or LEN attribute.

718 E a CLASS component must be allocatable or a pointer

719 E a procedure component must be a pointer

720 E no components specified in derived-type definition

721 E no type-bound procedures specified

722 E external or module procedure expected

723 E type-bound procedure undefined

724 E DEFERRED attribute required

725 E DEFERRED attribute not allowed

726 E component keyword missing in structure-constructor

- When in a structure-constructor a keyword has been used, all subsequent components
  must be specified using keywords.

727 E keyword missing in type-param-spec-list

- When in a parameter list a keyword has been used, all subsequent parameters must be
  specified using keywords.

728 E incorrect, or missing language-binding-spec: BIND(C) expected

- the language-binding-spec must be BIND(C)

729 E no enumerators in enumeration

730 E END ENUM missing

731 E interface name not allowed in this context

732 E procedure attributes not allowed in this context

733 E delimiter not allowed in this context

734 E statement only allowed in a (non separate) interface body

735 E explicit or abstract interface required

736 E this intrinsic function not allowed as interface name

737 E TYPE IS, CLASS IS, or CLASS DEFAULT expected after SELECT TYPE

738 E associate name expected

739 E association list missing

740 E selector missing

741 E invalid assignment

742 E the selector must be polymorphic

743 E passed-object dummy argument not found

744 E incorrect number of derived-type parameters

745 E invalid argument kind type parameter for intrinsic procedure

- The kind type parameter of the argument of a specific procedure is incorrect.
- No specific procedure could be generated of which the argument kind type parameter
  matches the actual argument type kind.
- A specific procedure has been generated with an argument kind type parameter which
  matches the argument type kind of the first argument, but the type kind of (one of)
  the other arguments do not match.

746 I type kind or length inconsistently specified

- The type kind or length of the argument is explicit, the type kind or length of
  others is default, or specified as DOUBLE PRECISION.
- The type kind or length of this object in one instance of the common block is
  explicit, the type kind or length in the others is default, or specified as DOUBLE
  PRECISION.

747 E each element in an array constructor must be of the same kind

748 I element kind inconsistent with kind of first element

- The kind of this array element is inconsistently specified compared to that of the
  first element. One has the default kind, the other has an explicitly specified
  kind.

749 E mixing of protected and non-protected objects in equivalence

750 W unsupported kind type parameter, default assumed

- The kind type parameter of this type is not supported by the emulated compiler.

751 W unsupported kind, default assumed

- No supported kind can be found that matches.

752 W unsupported character set, default kind assumed

- No supported kind can be found for this character set.

753 E each element must have the same kind type parameters

754 E no objects to allocate or to deallocate

755 E unrecognized keyword

756 E type-spec or source-expression required

- One or more of the allocate-objects have deferred-type parameters.
- The allocate-object is unlimited polymorphic or is of abstract type.

757 I no entities imported from module

758 E invalid target for a procedure pointer

759 E procedure already in list of final subroutines of this derived type

760 E final procedure has no unique argument list

761 E type parameter specified more than once or unknown

762 E empty parameter list

763 E deferred type parameter not allowed

764 E assumed-type parameter not allowed

765 E each length type parameter must be assumed

766 E SEQUENCE type, or BIND attribute not allowed

767 E type must be an extension of the selector

768 E NOPASS must be specified

769 E passed-object argument required.

770 E argument must be a data-object

771 E derived type i/o procedure must be a subroutine

772 E type must be abstract

773 E argument must be scalar

774 E argument must be polymorphic

775 E argument must not be polymorphic

776 E the accessibility of the generic spec must be the same as originally

777 I the accessibility is inconsistently specified

778 E types are not compatible

779 E a CLASS entity must be dummy, allocatable or a pointer

780 E entity is not accessible

781 E entity must be interoperable

782 E type kind conflict with type kind of function

- All entries within a function must have the same type kind.
- The type kind while referencing the function differs from the specification of the
  function.

783 E function type kind inconsistent with first occurrence

- The type kind of the function differs from that at the first reference
  encountered.

784 I type kind inconsistent with type kind of function

- All entries within a function must have the same type kind. One has the default
  kind, the other has an explicitly specified kind.
- The type kind while referencing the function is inconsistently specified com­pared
  to the specification of the function. One has the default kind, the other has an
  explicitly specified kind.

785 I type kind inconsistent with type kind at first reference

- The type kind while referencing the function is inconsistently specified com­pared
  to the first reference. One has the default kind, the other has an explicitly
  specified kind.
- The type kind of an actual argument is inconsistently specified compared to the
  first reference encountered. One has the default kind, the other has an explicitly
  specified kind.
- The type kind of a common-block object is inconsistently specified compared to the
  first reference encountered. One has the default kind, the other has an explicitly
  specified kind.

786 I type kind inconsistent with specification

- The type kind of an actual argument is inconsistently specified compared to the
  specification of the procedure. One has the default kind, the other has an
  explicitly specified type kind.
- The type kind has been specified in one instance, the type length in the other.

787 E invalid usage of abstract type

788 E invalid overriding of binding

789 E component name not unique

790 E component not defined

791 E the derived type must be extensible

792 E entity cannot be an explicit-shape array

793 E INTENT not allowed for nonpointer dummy procedure arguments

794 E entity cannot have the POINTER attribute

795 E entity cannot have the PROTECTED attribute

796 E dummy argument with assumed-type parameter expected

797 E dummy argument must not be an elemental procedure

798 E invalid specification of shape

799 E named language binding not allowed

800 E multiple declaration of procedure

801 E derived-type name expected

802 E list of type-bound procedures not allowed

- In Fortan 2003 a list is not supported.

803 E invalid usage of unlimited format item

804 E scalar default integer or character constant expression expected

805 O could not determine type parameter, default assumed

806 E invalid coarray specification

807 E argument must not have a polymorphic allocatable component

808 E NULL() expected

809 E NULL() or procedure name expected

810 E TYPE IS, CLASS IS, or CLASS DEFAULT at invalid SELECT TYPE level

811 E invalid argument value

812 I derived-type component not used

- None of the objects of the type uses this component.

813 I derived-type component not referenced

- None of the objects of the type references this component.

814 I derived-type component not defined

- None of the objects of the type defines this component.

815 I derived-type component not allocated

- None of the objects of the type allocates this component.

816 I derived-type component not associated

- None of the objects of the type associates this component.

817 E incorrect type for a coarray

818 E cannot extend parent type

819 E nonpointer nonallocatable scalar expected

820 E array with the POINTER attribute expected

821 E target must be contiguous

822 E missing coarray specification

823 E function result cannot be a coarray

824 E type of function result must not have a coarray ultimate component

825 E a coarray must be a dummy argument, allocatable, in main, or saved

826 E must be a dummy argument or saved

827 E deferred-coshape specification not allowed

828 E deferred-coshape specification required

829 E array pointer, assumed-shape, or assumed-rank array expected

830 E actual argument must be a contiguous array

831 E entity cannot be a coarray

832 E type not allowed for an INTENT(OUT) argument

833 E a coarray cannot have the POINTER attribute

834 E invalid usage of coindex or image selector

835 E invalid number of cosubscripts

836 E missing coshape specification

837 E SAVE without entity list invalid in a BLOCK construct

838 I input or input/output argument is not defined

- The argument was defined as an input or input/output argument and was not defined
  when the procedure was referenced.
- The argument was not or conditionally referenced before defined in the procedure and
  was not defined when the procedure was referenced.

839 E invalid usage of coindexed object

840 E target has invalid rank

841 I module object not used outside the module

- The object can be declared PRIVATE

842 E component must have the POINTER and/or ALLOCATABLE attribute

843 E statement not allowed within a CRITICAL or DO CONCURRENT construct

- A RETURN or an image control statement is not allowed within a CRITICAL or DO
  CONCURRENT construct

844 E no corresponding CRITICAL statement found

845 E missing END CRITICAL

846 E a coarray cannot not be (de)allocated within this construct

- A coarray cannot be (de)allocated within a CRITICAL or DO CONCURRENT construct

847 E invalid transfer of control out of construct

848 E invalid list of edit descriptors

849 E scalar character constant expression expected

850 E ancestor module must not be intrinsic

851 E module nature conflict

- An intrinsic module with this name is already used in this scoping unit
- A nonintrinsic module with this name is already used in this scoping unit

852 E statement not allowed within a CHANGE TEAM construct

854 E inconsistent attribute

855 E inconsistent dummy argument name

856 E inconsistent characteristics

857 I intrinsic module has the same name as a nonintrinsic module

858 I nonintrinsic module has the same name as an intrinsic module

859 I variable, used as actual argument, unreferenced

- The variable is defined by argument association in a referenced procedure but not
  referenced in the referencing program unit.

860 E scalar default character constant expression expected

861 E inconsistent BIND(C) attribute or binding label

- When a common blockor external procedure has been specified with the BIND(C)
  attribute in a certain subprogram, it must be specified with the BIND(C) attribute
  and the same binding label in every subprogram in which the common block or external
  procedure has been specified.

862 E binding label is not unique

863 E initialization expression expected

864 E an assumed-type entity must be a dummy variable

865 E an assumed-type variable name can only be used as an actual argument

866 E an assumed-rank variable name can only be used as an actual argument

867 E assumed-shape or assumed-rank argument expected

868 E assumed-rank entity must be a dummy data object

869 E invalid usage of procedure pointer result

- A function reference that returns a procedure pointer must not appear in an
  expression.

870 I dummy argument has no INTENT attribute

871 E INTENT(IN) dummy argument must not be modified

- The INTENT(IN) attribute for a non pointer dummy argument specifies that it shall
  not be modified during the execution of the procedure.

872 E INTENT(IN) dummy argument pointer must not be modified

- The INTENT(IN) attribute for a pointer dummy argument specifies that during the
  execution of the procedure its association shall not be modified.

873 I INTENT(OUT) dummy argument is not defined

874 I INTENT(OUT) dummy argument pointer is not associated or nullified

875 I INTENT(INOUT) dummy argument is not modified in this procedure

- The INTENT can be changed to INTENT(IN).

876 I INTENT(INOUT) pointer association is not modified in this procedure

- The INTENT can be changed to INTENT(IN).

877 I INTENT(INOUT) dummy argument is defined before referenced

- The INTENT can be changed to INTENT(OUT).

878 I INTENT(INOUT) dummy argument pointer is modified before referenced

- The INTENT can be changed to INTENT(OUT).

879 E an explicit RESULT variable must be declared for direct recursion.

880 E specification expression expected

881 E missing END ASSOCIATE(’s)

882 E pointer association is not defined

883 E pointer association of one or more component(s) is not defined

884 O (SOURCE POSSIBLY IN FIXED FORM. DO NOT SPECIFY THE FREE-FORM OPTION)

885 E array element or scalar structure component expected

886 E expression in CASE statement not in range of selector

887 I array unreferenced

- An array has been defined but is not referenced.

888 I array not used

- An array has been declared and possibly allocated, initialized or assigned, but is
  never used.

889 W shape differs from first occurrence

890 E inquired characteristic must be specified in a prior specification

891 E USE of ancestor module is not permitted

892 I mixing of volatile and non-volatile objects in equivalence

893 E invalid modification: actual argument has a vector subscript

- The dummy procedure argument is an output or input/output argument but cannot modify
  the actual argument.

894 E decimal range of integer must be at least that of default integer

895 E ”ADVANCE=” specifier not allowed in a DO CONCURRENT construct

896 E statement function cannot be of a parametrized derived type

897 E ancestor declares no separate module procedures

898 I variable not defined

- The variable is possibly referenced but has not been defined.

899 I none of the equivalenced variables of the same type is defined

- The variable is possibly referenced but the variable and none of the equivalenced
  variables with the same type are defined.

900 I optional dummy argument used without verifying with PRESENT

901 I IMPORT already specified

902 E assumed-rank array expected

903 E statement only allowed within derived type definition

904 E scalar default integer or character expression expected

905 E too many END TEAM’s

906 E missing END TEAM(’s)

907 E an internal procedure must not appear in an interface block

908 E multiple IMPLICIT NONE declaration

909 E conflict with previous IMPORT statement

910 E scalar expression expected

911 E scalar variable expected

912 E coarray expected

913 E variable expected

914 E variable must not be allocatable

915 E incorrect usage of optional argument

916 E incorrect usage of polymorphic entity

917 E incorrect usage of finalizable object

918 E locality not specified
