---
title: "Configuring the SCM to Coverity Connect user map"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-the-scm-to-coverity-connect-user-map.html"
content_id: "_GN9LlSR7x2IEnTN0oN08Q"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:31.219749+00:00"
---

# Configuring the SCM to Coverity Connect user map

When owners are assigned based on SCM history, Coverity Connect maps user identities from
the SCM data to users in Coverity Connect through an imported file.

The default user map file is in JSON format. It is set globally, so it is shared by all
streams in Coverity Connect that are configured to accept owners derived from SCM
data.

Coverity Connect provides a default user map file that you can access by clicking the
Export and then saving to your preferred location. After you
finish editing the file, use the Import button to import it for
use by Coverity Connect.

The file template is as follows:

```
{
  "map" : [ {
    "scmUsername" : "(.*)",
    "cimUsername" : "$1"
  } ]
  }
```

The JSON elements for user mapping are:

"`scmUsername`"
:   Represents the SCM username expressed as a regular expression using full
    string matching. It uses Java's built-in regular expression syntax. For more
    information about the regular expression syntax, see the Javadoc at <http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html>.

    The following table describes the username mapping format for supported SCM
    tools:

    Table 1. SCM username mapping format

    | SCM tool | username format description | Example regex for Coverity Connect mapping |
    | --- | --- | --- |
    | Git | The "author-mail" (`user.email`) of the revision, in the form `user@domain`. | `(.*)@(.*)` |
    | Perforce | The "user" of the revision. | `(.*)` |
    | Plastic | The "owner" of the changeset. | `(.*)` |
    | SVN | The "username" of the revision. | `(.*)` |

    Note: For all SCM tools except for Git, you might have an informal policy for the value of the
    relevant field that Coverity Connect chooses for the username. This might
    allow for a more specific regex to be used in the Coverity Connect user
    map.

"`cimUsername`"
:   Represents the user in the Coverity Connect database to which the SCM user is
    transformed. In the example
    below, the value is represented as a reference to a captured
    [subsequence](http://docs.oracle.com/javase/7/docs/api/java/util/regex/Matcher.html#replaceFirst%28java.lang.String%29). For information about
    capturing, see the Javadoc for [Groups and Capturing](http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html#cg).

    This element can not be used in the same mapping as
    "`cimEmail`".

    Note: Values for the Coverity Connect username field are
    stored in lower case.

"`cimEmail`"
:   This optional element represents the email address of the user in the
    Coverity Connect database to which the SCM user is transformed. This is
    useful for cases where the `scmUsername` is the user's email
    address.

    This element can not be used in the same mapping as
    "`cimUsername`".

"`ldapServer`"
:   This element is optional and is only required if you have duplicate user
    names from LDAP servers or a combination of LDAP users and local users. You
    can also explicitly specify a local user with "`ldapServer`"
    : "`local`" in the case that a user exists on both the local
    Coverity Connect server and the LDAP server. When
    "`ldapServer`" is left blank, is null, or is absent, the
    entry will only match if there is exactly one Coverity Connect user with the
    expected username.

Mapping rules are processed in order until a match is found, or there are no more rules
to process. If "`scmUsername`" matches the username of the SCM user, but
the corresponding "`cimUsername`" (after variable expansion) is not a
valid Coverity Connect user, the process continues to the next
"`scmUsername`" rule.

## Example - SCM user mapping

In the following example, the mapping file attempts to match an SCM user in the
format of first_name.last_name and transform
it to a Coverity Connect user in the form of
first_letter_first_name
last_name. Otherwise, the file attempts to match
username@domain.com and transform it to
username at an LDAP server domain.com.

```
{
  "map" : [ {
    "scmUsername" : "([a-z])[a-z]*\\.([a-z]+)",
    "cimUsername" : "$1$2"
  }, {
    "scmUsername" : "(.*)@(.*)",
    "cimUsername" : "$1",   
    "ldapServer" : "$2"
  } ]
}
```

The following example demonstrates literal mappings as well (`jdoe ->
john.doe`):

```
{
  "map" : [ {
    "scmUsername" : "([a-z])[a-z]*\\.([a-z]+)",
    "cimUsername" : "$1$2"
  }, {
    "scmUsername" : "(.*)@(.*)",
    "cimUsername" : "$1",
    "ldapServer" : "$2"
  }, {
    "scmUsername" : "jdoe",
    "cimUsername" : "john.doe"
  } ]
  }
```

The following example attempts to match an SCM username and
transform it to the Coverity Connect user's email_address:

```
{
  "map" : [ {
    "scmUsername" : "(.*)",
    "cimEmail" : "$1"
  } ]
}
```

The following example shows how to map `DOMAIN\username` to
`username`.

```
{ 
  "map" : [ { 
     "scmUsername" : "(.*)\\\\(.*)", 
     "cimUsername" : "$2" 
   } ] 
}
```

In the above example, the backslash character must be escaped twice. The backslash is
escaped once to be properly interpreted by the regular expression parser:
`DOMAIN\\username`. Next, because that expression is encoded in
JSON, each backslash must be escaped again: `DOMAIN\\\\username`.

Note: All SCM to Coverity Connect user map debugging messages are registered in the
cim.log file. You can view these debug messages by enabling the
Commit option in Coverity Connect's logging configuration settings.
