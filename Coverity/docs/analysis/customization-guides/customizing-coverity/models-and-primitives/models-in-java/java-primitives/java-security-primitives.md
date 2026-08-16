---
title: "Java security primitives"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-security-primitives.html"
content_id: "EZMCxspRWv_XroZpxDsetQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:26:02.837418+00:00"
---

# Java security primitives

Primitives that define sources of untrusted (tainted) data and methods to which tainted data must not flow (sinks)

## `enum SecurityPrimitives.TaintSourceType`

Represents various possible sources of tainted data.

The following values are defined:

| Name | Description |
| --- | --- |
| `CommandLine` | The command line |
| `Console` | A console |
| `Cookie` | A cookie |
| `Database` | A database record |
| `Environment` | An environment variable |
| `Filesystem` | A saved file |
| `Http` | A web page |
| `HttpHeader` | The header of a web page |
| `MobileOtherApp` | A mobile app other than the one currently running |
| `MobileOtherPrivilegedApp` | A privileged mobile app other than the one currently running |
| `MobileSameApp` | The mobile app that is currently running |
| `MobileUserInput` | User input from a mobile app |
| `Network` | Data obtained from a system on the network |
| `Rpc` | A remote procedure call |
| `SystemProperties` | System properties settings |

## `void android_app_conditional_sink( java.lang.Object o, java.lang.Object cond )`

Marks its parameter `o` as the sensitive data to be sent to an Android application when the parameter `cond` satisfies certain condition.

## `<T> T android_app_conditional_source( java.lang.Object obj )`

Returns an object of arbitrary type that the analysis treats as tainted data coming from an Android application.

## `void android_bind_service_sink( java.lang.Object o )`

Marks its parameter `o` as the *intent* object to be bounded/started/stopped by another activity.

## `void android_broadcast_sink( java.lang.Object o )`

Marks its parameter `o` as the *intent* object to be broadcast.

## `void android_clipboard_sink( java.lang.Object o )`

Marks its parameter `o` as having been copied to the clipboard.

## `void android_content_provider_sink( java.lang.Object o )`

Marks its parameter `o` as sensitive data that will be stored on external content providers.
The external content providers will be accessible to other applications.

## `<T> T android_mobile_id_conditional_source( java.lang.Object o )`

Returns an object of arbitrary type that the analysis will treat as sensitive mobile ID data when the argument is equal to the string literal `"android_id"`.

## `<T> T android_other_app_map_values_source()`

Returns a map whose values the analysis will treat as tainted data from an external app.

## `<T> T android_other_app_map_values_source( T obj )`

Marks all the values of its map parameter `obj` as containing tainted data from an external app.

## `<T> T android_other_app_object_source()`

Models a method that returns an object with tainted data coming from an external app.
The fields of the object will become tainted when it is cast to a more specific type.

## `<T> void android_other_app_object_source( T obj )`

Models a method that populates the parameter `obj` with tainted data coming from an external app.
The fields of the object will become tainted when it is cast to a more specific type.

## `<T> T android_other_app_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data coming from an external app.

## `<T> T android_other_app_source( T obj )`

Marks its parameter `obj` as containing tainted data coming from an external app.

## `<T> T android_other_privileged_app_map_values_source()`

Returns a map whose values the analysis will treat as tainted data from an external app that has appropriate privileges.

## `<T> void android_other_privileged_app_map_values_source( T obj )`

Marks all the values of its map parameter `obj` as containing tainted data from an external app with appropriate privileges.

## `<T> T android_other_privileged_app_object_source()`

Models a method that returns an object with tainted data coming from an external app that has appropriate privileges.
The fields of the object will become tainted when it is cast to a more specific type.

## `<T> void android_other_privileged_app_object_source( T obj )`

Models a method that populates the parameter `obj` with tainted data coming from an external app that has appropriate privileges.
The fields of the object will become tainted when it is cast to a more specific type.

## `<T> T android_other_privileged_app_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data coming from an external app that has the appropriate privileges.

## `<T> void android_other_privileged_app_source( T obj )`

Marks its parameter `obj` as containing tainted data coming from an external app that has the appropriate privileges.

## `<T> T android_password_id_conditional_source( int id )`

Returns an object of arbitrary type that the analysis will treat as password-sensitive data when the argument is a resource identifier for a password field.

## `<T> void android_password_type_conditional_source( T pwd, int type )`

Marks the parameter `pwd` as password-sensitive data when the `type` argument is one of the `InputType.TYPE_*_PASSWORD` input types.

## `<T> T android_same_app_map_values_source()`

Returns a map whose values the analysis will treat as tainted data from the same app.

## `<T> void android_same_app_map_values_source( T obj )`

Marks all the values of the map parameter `obj` as containing tainted data from the same Android app.

## `<T> T android_same_app_object_source()`

Models a method that returns an object with tainted data coming from the same Android app.
The fields of the object will become tainted when it is cast to a more specific type.

## `<T> voidandroid_same_app_object_source( T obj )`

Models a method that populates the parameter `obj` with tainted data coming from the same Android app.
The fields of the object will become tainted when it is cast to a more specific type.

## `<T> T android_same_app_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data coming from the same Android app.

## `<T> void android_same_app_source( T obj )`

Marks the parameter `obj` as containing tainted data coming from the same Android app.

## `void android_start_activity_sink( java.lang.Object o )`

Marks its parameter `o` as the *intent* object to be started by another activity.

## `void android_start_service_sink( java.lang.Object o )`

Marks its parameter `o` as the *intent* object to be started by another activity.
The SENSITIVE_DATA_LEAK checker reports a defect
when the intent object `o` is used without setting any class or component.
Use this primitive to model sinks for SENSITIVE_DATA_LEAK.

## `void android_stop_service_sink( java.lang.Object o )`

Marks its parameter `o` as the *intent* object to be stopped by another activity.
The SENSITIVE_DATA_LEAK checker reports a defect
when the intent object `o` is used without setting any class or component.
Use this primitive to model sinks for SENSITIVE_DATA_LEAK.

## `<T> T android_user_input_map_values_source()`

Returns a map whose values the analysis will treat as tainted data from user input.

## `<T> void android_user_input_map_values_source( T obj )`

Marks all the values of its map parameter `obj` as containing tainted data from user input.

## `<T> T android_user_input_object_source()`

Models a method that returns an object with tainted data coming from user input.
The fields of the object will become tainted when it is cast to a more specific type.

## `<T> void android_user_input_object_source( T obj )`

Models a method that populates the parameter `obj` with tainted data coming from user input.
The fields of the object will become tainted when it is cast to a more specific type.

## `<T> T android_user_input_source()`

Returns an object with tainted data coming from user input.

## `<T> void android_user_input_source( T obj )`

Marks its parameter `obj` as containing tainted data coming from user input.

## `<T> T asserted_source()`

Returns an object of arbitrary type that the analysis will treat as tainted.

## `<T> void asserted_source( T o )`

Marks its parameter `o` as tainted.

## `void authz_action()`

Indicates that the method that includes this is associated with actions that often require authentication.

## `<T> T console_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from the console.

## `<T> void console_source( T o )`

Marks its parameter `o` as containing tainted data from the console.

## `void cookie_sink( java.lang.Object o )`

Indicates that the method that includes this stores sensitive data in a cookie and should be sanitized somehow.

## `<T> T cookie_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from a cookie.

## `<T> void cookie_source( T o )`

Marks its parameter `o` as containing tainted data from a cookie.

## `void csrf_check_needed_for_db_update()`

Indicates that the method that includes this modifies the database and should be protected by a cross-site request forgery (CSRF) check.

## `void csrf_check_needed_for_file_modification()`

Indicates that the method that includes this modifies the filesystem and should be protected by a cross-site request forgery (CSRF) check.

## `void csrf_validator()`

Indicates that the method that includes this validates the cross-site request forgery (CSRF) anti-forgery token.

## `<T> Tdatabase_map_values_source()`

Returns a map whose values the analysis will treat as tainted data from a database.

## `void database_object_sink( java.lang.Object o )`

Indicates that the method that includes this stores sensitive data in a database and should be sanitized somehow.

## `<T> T database_object_source()`

Models a method that returns an object that is populated with tainted data from the database;
for example, by using an object-relational mapping (ORM).
If any of the these members are themselves user data types, the taint will be recursively applied to them.

## `<T> void database_object_source( T o )`

Models a method that populates the parameter `o` with tainted data from the database;
for example, by using an object-relational mapping (ORM).
If any of the these members are themselves user data types, the taint will be recursively applied to them.

## `void database_sink( java.lang.Object o )`

Indicates that the method that includes it stores sensitive data in a database and should be sanitized somehow.

## `<T> T database_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from a database.

## `<T> void database_source( T o )`

Marks its parameter `o` as containing tainted data from a database.

## `void encryption_sink( java.lang.Object o )`

Marks its parameter `o` as flowing into a method that encrypts it.
The UNENCRYPTED_SENSITIVE_DATA checker reports a defect if unencrypted (tainted) data flows into this primitive.

## `<T> T environment_map_values_source()`

s

Returns a map whose values the analysis will treat as tainted data from the system environment.

## `<T> T environment_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from the environment.

## `<T> void environment_source( T o )`

Marks its parameter `o` as containing tainted data from the environment.

## `void filesystem_object_sink( java.lang.Object o )`

Indicates that the method that includes this stores sensitive data in a filesystem and should be sanitized somehow.

## `<T> T filesystem_object_source()`

Models a method that returns an object that is populated with tainted data from the filesystem.
When the analysis sees the return value cast to a user type, all members of that instance will be treated as tainted data.
If any of the these members are themselves user data types, the taint will be recursively applied to them.

## `<T> void filesystem_object_source( T obj )`

Models a method that populates the parameter `o` with tainted data from filesystem.
The fields of the object will become tainted when it is cast to a more specific type.

## `void filesystem_sink( java.lang.Object o )`

Indicates that the method that includes this stores sensitive data in a filesystem and should be sanitized somehow.

## `<T> T filesystem_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from the filesystem.

## `<T> void filesystem_source( T o )`

Marks the parameter `o` as containing tainted data from the filesystem.

## `void hardcoded_credential_connection_string_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that consumes it as a connection string.

## `void hardcoded_credential_crypto_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that consumes it as a cryptographic key.

## `void hardcoded_credential_passwd_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that consumes it as a password.

## `void hardcoded_credential_token_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that consumes it as a security token.

## `void http_header_sink( java.lang.Object o )`

Marks the parameter `o` as being used as an HTTP header.

## `<T> T http_header_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from an HTTP header.

## `<T> void http_header_source( T o )`

Marks the parameter `o` as containing tainted data from an HTTP header.

## `void http_redirect_sink( java.lang.Object o )`

Marks the parameter `o` as being used as an HTTP address to redirect to.

## `<T> T http_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from an HTTP request.

## `void insecure_communication_sink( java.lang.Object url )`

Indicates that its parameter `url` is being used as a URL for
communication. This can be used to model code such as
`connect("http://www.blackduck.com")`.

## `void insecure_communication_sink( java.lang.Object url, int port )`

Indicates that its parameters `url` and `port` are being used as the URL and port values for communication.
This can be used to model code such as `connect("http://www.myupload.org", 21)`.

## `void insecure_random_sink( java.lang.Object o )`

Indicates that the parameter `o` should not be an insecure random value.

## `<T> T insecure_random_value_source()`

Returns an object of arbitrary type that the analysis will treat as an insecure random value.

## `<T> void insecure_random_value_source( T o )`

Marks the parameter `o` as containing an insecure random value.

## `void logging_sink( java.lang.Object o )`

Indicates that the method that includes this stores sensitive data to a log and should be sanitized somehow.

## `<T> T network_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from the network.

## `<T> void network_source( T o )`

Marks the parameter `o` as containing tainted data from the network.

## `void os_cmd_array_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that treats the elements as arguments to an operating-system command
in the way `java.lang.Runtime.exec( String[] cmdarray )` does.

## `void os_cmd_one_string_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that parses it and runs it as an operating-system command
the way `java.lang.Runtime.exec(String cmd)` does.

## `void registry_sink( java.lang.Object o )`

Indicates that the method that includes it stores sensitive data in a registry and should be sanitized somehow.

## `<T> T rpc_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from a Remote Procedure Call (RPC).

## `<T> void rpc_source( T o )`

Marks the parameter `o` as containing tainted data from a Remote Procedure Call (RPC).

## `void secure_random_seed_sink( java.lang.Object o )`

Indicates that the parameter `o` is being used as a secure random seed.

## `<T> T sensitive_source( SensitivePrimitives.SensitiveDataType type )`

Returns an object of arbitrary type that the analysis will treat as sensitive data.

## `<T> void sensitive_source( T o, SensitivePrimitives.SensitiveDataType type )`

Marks the parameter `o`, of type `type`, as containing sensitive data.

## `<T> T servlet_map_values_source()`

Returns a map whose values the analysis will treat as tainted data from a servlet request.

## `<T> void servlet_map_values_source( T o )`

Marks all the values of its map parameter `o` as containing tainted data from a servlet request.

## `<T> T servlet_source()`

Returns an object of arbitrary type that the analysis will treat as tainted data from a servlet request.

## `<T> void servlet_source( T o )`

Marks the parameter `o` as containing tainted data from a servlet request.

## `void sql_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that runs it as an SQL, HQL, or JPQL query.

## `void ssl_socket_create_insecure()`

Indicates that the method that includes it returns a Socket or SSLEngine that does not automatically do hostname verification.

## `void ssl_socket_use( java.lang.Object o )`

Indicates that the parameter `o` is being used for communication.

## `void ssl_socket_verify( java.lang.Object o )`

Indicates that the hostname of the parameter `o` is being verified.

## `<T> T system_properties_source()`

Returns an object of arbitrary type that the analysis will treats as tainted data from the system properties.

## `<T> void system_properties_source( T o )`

Marks the parameter `o` as containing tainted data from the system properties.

## `<T> T taint_map_keys( SecurityPrimitives.TaintSourceType t )`

Returns a map whose keys the analysis treats as tainted data of type `t`.

## `<T> void taint_map_keys( T obj, SecurityPrimitives.TaintSourceType t )`

Marks all the keys of its map parameter `obj` as containing tainted
data of type `t`.

## `<T> T taint_map_values( SecurityPrimitives.TaintSourceType t )`

Returns an object of arbitrary type that the analysis treats as tainted data of type `t`.

## `<T> void taint_map_values( T obj, SecurityPrimitives.TaintSourceType t )`

Marks all the values of its map parameter `obj` as containing tainted
data of type `t`.

## `<T> T taint_source( SecurityPrimitives.TaintSourceType t )`

Marks all the values of its map parameter `obj` as containing tainted
data of type `t`.

## `<T> void taint_source( T obj, SecurityPrimitives.TaintSourceType t )`

Returns a map whose keys the analysis treats as tainted data of type `t`.

## `void transit_object_sink( java.lang.Object o )`

Indicates that the method that includes it sends sensitive data somewhere else and should be sanitized or secured somehow.

## `void transit_sink( java.lang.Object o )`

Indicates that the method that includes it sends sensitive data somewhere else and should be sanitized or secured somehow.

## `void ui_object_sink( java.lang.Object o )`

Indicates that the method that includes it reflects sensitive data back to the user and should be sanitized somehow.

## `void ui_sink( java.lang.Object o )`

Indicates that the method that includes it reflects sensitive data back to the user and should be sanitized somehow.

## `void unencrypted_crypto_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that consumes it as a cryptographic key.

## `void unencrypted_passwd_map_sink( java.lang.Object o )`

Marks its parameter as flowing into a method that consumes it as a password.
The UNENCRYPTED_SENSITIVE_DATA checker might report a defect if unencrypted (tainted)
data flows into this primitive.

## `void unencrypted_passwd_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that consumes it as a password.

## `<T> T unencrypted_socket_source()`

Returns an object of arbitrary type that the analysis will treat as an unencrypted (non-SSL) socket.

Marks the parameter `o` as being an unencrypted (non-SSL) socket.

## `void unencrypted_token_sink( java.lang.Object o )`

Marks the parameter `o` as flowing into a method that consumes it as a security token.

## `<T> T unencrypted_url_connection_source()`

Returns an object of arbitrary type that the analysis will treat as an unencrypted URL connection.

## `<T> void unencrypted_url_connection_source( T o )`

Marks the parameter `o` as being an unencrypted URL connection.

## `<T> T unrestricted_access_source()`

Returns an object of arbitrary type that represents a path to external storage and therefore does not have any access control.

## `void unrestricted_database_access_sink( java.lang.Object path )`

Marks the parameter `path` as flowing into a method that creates a database at the specified location.

## `void unrestricted_file_access_sink( java.lang.Object path )`

Marks the parameter `path` as flowing into a method that creates a file at the specified location.
