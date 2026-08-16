---
title: "C# and Visual Basic security primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/c-and-visual-basic-security-primitives.html"
content_id: "0BoOKbGmqiHeCpk1fB1AaQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:25:48.001891+00:00"
---

# C# and Visual Basic security primitives

These primitives deal with security issues, chiefly involving potential sources or
sinks of tainted data.

The primitive to handle sensitive-data issues is named
`Security.SensitiveSource`. There are two versions of this
primitive: One takes a single argument, and the other takes two arguments.

The other primitives described in this section handle tainted-data issues.

The tainted-data primitives that do not take an argument model a method that returns
a string-like object or a simple collection object, which the analysis treats as
tainted data.

The tainted-data primitives that take a single argument model a method that taints a
string-like object or a simple collection parameter (presumably by inserting a
tainted character sequence into it). The argument must be one of the modeled
method's parameters.

Each variant corresponds to a particular taint type that can be trusted or distrusted by using
the `cov-analyze`
`trust` or `distrust` command-line options; for
example, `--trust-http` and `--distrust-http`. These
options are enumerated under "Options: Web and mobile application security", in the
description of `cov-analyze` in the Coverity 2026.6.0 Command Reference.

## `Security.AuthzAction()`

Indicates that this method is associated with actions that often require
authentication. The MISSING_AUTHZ checker will only report defects when such methods
are called.

## `Security.CSRFCheckNeededForDBUpdate()`

Indicates that this method modifies the database and should be protected by a
cross-site request forgery check. If it is not, the CSRF checker might report a
defect.

## `Security.CSRFCheckNeededForFileModification()`

Indicates that this method modifies the filesystem and should be protected by a
cross-site request forgery check. If it is not, the CSRF checker might report a
defect.

## `Security.CSRFValidator()`

Indicates that this method checks the validity of an anti-forgery token. The checker
will consider request handlers that call this method to be safe.

## `Security.CommandArgumentsSink( System.Object o )`

Marks its parameter as flowing into a method that treats it as the arguments to an
operating system command like `System.Diagnostics.Process.Start( String
fileName, String arguments )` does. The OS_CMD_INJECTION checker reports
defects when tainted data flows into this primitive. Use this primitive to model a
sink for OS_CMD_INJECTION that takes a single string, parses it, and uses it as
arguments to a new process.

Parameters:

`o`
:   Arguments to the process to be executed

## `Security.CommandFilenameSink( System.Object o )`

Marks its parameter as flowing into a method that treats it as an application
filename and runs it as an operating system command like
`System.Diagnostics.Process.Start(String fileName)` does. The
OS_CMD_INJECTION checker reports defects when tainted data flows into this
primitive. Use this primitive to model a sink for OS_CMD_INJECTION that takes a
single string, and runs it.

Parameters:

`o`
:   The file name of the application to be executed

## `Security.ConsoleSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from the
console. Use this primitive to model a method that returns tainted data from the
console.

## `Security.ConsoleSource( System.Object o )`

Marks its parameter as containing tainted data from the console. Use this primitive
to model a method that appends tainted data from the console into one of its
parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.CookieSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from a
cookie. Use this primitive to model a method that returns tainted data from a
cookie.

## `Security.CookieSource( System.Object o )`

Marks its parameter as containing tainted data from a a cookie. Use this primitive to
model a method that appends tainted data from a cookie into one of its
parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.DatabaseObjectSource()`

Use this primitive to model a method that returns an Object that is populated with
tainted data from the database, for example using an ORM (object-relational
mapping). When the analysis sees the return value cast to a user type, all members
of that instance will be treated as tainted data. If any of the these members are
themselves user data types, the taint will be recursively applied to them.

## `Security.DatabaseObjectSource( System.Object o )`

Use this primitive to model a method that populates a parameter with tainted data
from the database, for example using an ORM (object-relational mapping). When the
analysis sees the callsite argument cast to a user type, all members of that
instance will be treated as tainted data. If any of the these members are themselves
user data types, the taint will be recursively applied to them.

Parameters:

`o`
:   The parameter to be tainted

## `Security.DatabaseSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from a
database. Use this primitive to model a method that returns tainted data from a
database.

## `Security.DatabaseSource( System.Object o )`

Marks its parameter as containing tainted data from a database. Use this primitive to
model a method that appends tainted data from a database into one of its
parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.EnvironmentSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from the
environment. Use this primitive to model a method that returns tainted data from the
environment.

## `Security.EnvironmentSource( System.Object o )`

Marks its parameter as containing tainted data from the environment. Use this
primitive to model a method that appends tainted data from the environment into one
of its parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.FileSystemSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from the
filesystem. Use this primitive to model a method that returns tainted data from the
filesystem.

## `Security.FileSystemSource( System.Object o )`

Marks its parameter as containing tainted data from the filesystem. Use this
primitive to model a method that appends tainted data from the filesystem into one
of its parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.HardcodedConnectionStringSink( System.Object o )`

Marks its parameter as flowing into a method that consumes it as a connection string.
The HARDCODED_CREDENTIALS checker reports a defect if a constant string is used as
the password in the connection string.

Parameters:

`o`
:   The object that contains the credentials

## `Security.HardcodedCryptographicKeySink( System.Object o )`

Marks its parameter as flowing into a method that consumes it as a cryptographic key. The
HARDCODED_CREDENTIALS checker reports a defect if a
source-code-embedded constant string is passed to it.

Parameters:

`o`
:   The object that contains the credentials

## `Security.HardcodedPasswordSink( System.Object o )`

Marks its parameter as flowing into a method that consumes it as a password. The
HARDCODED_CREDENTIALS checker reports a defect if a source-code-embedded constant
string is passed to it.

Parameters:

`o`
:   The object that contains the password

## `Security.HardcodedSecurityTokenSink( System.Object o )`

Marks its parameter as flowing into a method that consumes it as a security token.
The HARDCODED_CREDENTIALS checker reports a defect if a source-code-embedded
constant string is passed to it.

Parameters:

`o`
:   The object that contains the credentials

## `Security.HttpHeaderMapValuesSource()`

Returns a map whose values the analysis treats as tainted data from HTTP headers. Use
this primitive to model a method that returns a map constructed with tainted values
from HTTP headers.

## `Security.HttpHeaderMapValuesSource( System.Object map )`

Marks all the values of its 'map' parameter as containing tainted data from HTTP
headers. Use this primitive to model a method that populates the values of a
dictionary with tainted data from HTTP headers.

Parameters:

`map`
:   The dictionary whose values are to be tainted

## `Security.HttpHeaderSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from a
HTTP header. Use this primitive to model a method that returns tainted data from a
HTTP Header

## `Security.HttpHeaderSource( System.Object o )`

Marks its parameter as containing tainted data from a a HTTP header. Use this
primitive to model a method that appends tainted data from a HTTP Header into one of
its parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.HttpMapValuesSource()`

Returns a map whose values the analysis treats as tainted data from an HTTP request.
Use this primitive to model a method that returns a map constructed with tainted
values from an HTTP request.

## `Security.HttpMapValuesSource( System.Object map )`

Marks all the values of its `map` parameter as containing tainted data
from an HTTP request. Use this primitive to model a method that populates the values
of a dictionary with tainted data from an HTTP request.

Parameters:

`map`
:   The dictionary whose values are to be tainted

## `Security.HttpRedirectSink( System.Object o )`

Marks a method parameter as being used as an HTTP address to redirect to. The
OPEN_REDIRECT checker reports a defect if an unsafe user-controllable string is
passed to this method.

## `Security.HttpSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from an
HTTP request. Use this primitive to model a method that returns tainted data from an
HTTP request.

## `Security.HttpSource( System.Object o )`

Marks its parameter as containing tainted data from an HTTP request. Use this
primitive to model a method that appends tainted HTTP request data into one of its
parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.InsecureRandomValueSource()`

Returns an object of arbitrary type that the analysis treats as an insecure random
value. Use this primitive to model a method that returns an insecure random
value.

## `Security.InsecureRandomValueSource( System.Object o )`

Marks its parameter as containing an insecure random value. Use this primitive to
model a method that appends an insecure random value into one of its parameters.

Parameters:

`o`
:   The parameter that will contain the insecure random value

## `Security.NetworkSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from the
network. Use this primitive to model a method that returns tainted data from the
network.

## `Security.NetworkSource( System.Object o )`

Marks its parameter as containing tainted data from the network. Use this primitive
to model a method that appends tainted network data into one of its parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.RpcSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from a
Remote Procedure Call. Use this primitive to model a method that returns tainted
data from a Remote Procedure call.

## `Security.RpcSource( System.Object o )`

Marks its parameter as containing tainted data from a a Remote Procedure Call. Use
this primitive to model a method that appends tainted data from a Remote Procedure
call into one of its parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.SDLCookieSink( System.Object o )`

Indicates that this method stores sensitive data in a cookie and should be sanitized
somehow. If it is not, the SENSITIVE_DATA_LEAK checker might report a defect.

Parameters:

`o`
:   The object that is stored in the cookie

## `Security.SDLDatabaseSink( System.Object o )`

Indicates that this method stores sensitive data in a database and should be
sanitized somehow. If it is not, the SENSITIVE_DATA_LEAK checker might report a
defect.

Parameters:

`o`
:   The object that is written to the database

## `Security.SDLFileSystemSink( System.Object o )`

Indicates that this method stores sensitive data in a filesystem and should be
sanitized somehow. If it is not, the SENSITIVE_DATA_LEAK checker might report a
defect.

Parameters:

`o`
:   The object that is written to the filesystem

## `Security.SDLLoggingSink( System.Object o )`

Indicates that this method stores sensitive data in a log and should be sanitized
somehow. If it is not, the SENSITIVE_DATA_LEAK checker might report a defect.

Parameters:

`o`
:   The object that is stored in the log

## `Security.SDLRegistrySink( System.Object o )`

Indicates that this method stores sensitive data in a registry and should be
sanitized somehow. If it is not, the SENSITIVE_DATA_LEAK checker might report a
defect.

Parameters:

`o`
:   The object that is stored in the registry

## `Security.SDLTransitSink( System.Object o )`

Indicates that this method sends sensitive data somewhere else and should be
sanitized/secured somehow If it is not, the SENSITIVE_DATA_LEAK checker might report
a defect.

Parameters:

`o`
:   The object that is transmitted

## `Security.SDLUISink( System.Object o )`

Indicates that this method reflects sensitive data back to the user and should be
sanitized somehow. If it is not, the SENSITIVE_DATA_LEAK checker might report a
defect.

Parameters:

`o`
:   The object that is displayed

## `Security.SecureRandomSeedSink( System.Object o )`

Indicates that a method parameter is a secure random number generator seed. The
PREDICTABLE_RANDOM_SEED checker reports defects when a predictable seed is passed to
this method.

## `Security.SensitiveSource(Coverity.Primitives.SensitiveDataType type)`

Returns an object of arbitrary type that the analysis treats as sensitive data. Use
this primitive to model a method that returns sensitive data.

Parameters:

`type`
:   The specific type of sensitive data

## `Security.SensitiveSource( System.Object o, Coverity.Primitives.SensitiveDataType type )`

Marks its parameter as containing sensitive data. Use this primitive to model a
method that puts sensitive data into one of its parameters.

Parameters:

`o`
:   The object that now contains the sensitive data

`type`
:   The specific type of sensitive data

## `Security.SqlSink( System.Object o )`

Marks its parameter as flowing into a method that runs it like an SQL, HQL, or JPQL
query. The SQLI checker reports a defect when tainted data flows into this
primitive. Use this primitive to model sinks for SQLI.

Parameters:

`o`
:   The object that contains the query

## `Security.SystemPropertiesSource()`

Returns an object of arbitrary type that the analysis treats as tainted data from the
system properties. Use this primitive to model a method that returns tainted data
from the system properties.

## `Security.SystemPropertiesSource( System.Object o )`

Marks its parameter as containing tainted data from the system properties. Use this
primitive to model a method that appends tainted data from the system properties
into one of its parameters.

Parameters:

`o`
:   The parameter to be tainted

## `Security.UnencryptedCryptographicKeySink( System.Object o )`

Marks its parameter as flowing into a method that consumes it as a cryptographic key.
The UNENCRYPTED_SENSITIVE_DATA checker may report a defect if unencrypted (tainted)
data flows into this primitive.

## `Security.UnencryptedPasswordSink( System.Object o )`

Marks its parameter as flowing into a method that consumes it as a password. The
UNENCRYPTED_SENSITIVE_DATA checker might report a defect if unencrypted (tainted)
data flows into this primitive.

## `Security.UnencryptedSecurityTokenSink( System.Object o )`

Marks its parameter as flowing into a method that consumes it as a security token.
The UNENCRYPTED_SENSITIVE_DATA checker might report a defect if unencrypted
(tainted) data flows into this primitive.

## `Security.UnencryptedSocketSource()`

Returns an object of arbitrary type that the analysis treats as an unencrypted (non
SSL) socket. Use this primitive to model a method that returns an unencrypted
socket.

## `Security.UnencryptedSocketSource( System.Object o )`

Marks its parameter as being an unencrypted (non SSL) socket.

Parameters:

`o`
:   The parameter that is known to be an unencrypted socket

## `Security.UnencryptedUrlConnectionSource()`

Returns an object of arbitrary type that the analysis treats as an unencrypted URL
connection. Use this primitive to model a method that returns an unencrypted URL
connection.

## `Security.UnencryptedUrlConnectionSource( System.Object o )`

Marks its parameter as being an unencrypted URL connection.

Parameters:

`o`
:   The parameter that is known to be an unencrypted URL connection
