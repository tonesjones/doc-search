---
title: "xss_sanitizer_method"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/xss_sanitizer_method.html"
content_id: "6ms~qwEv2hEYGJWmBtdAKw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:05.679156+00:00"
---

# xss_sanitizer_method

**Languages: C#, Java, Visual Basic**

The `xss_sanitizer_method` directive describes the string replacements
that the cross-site-scripting (XSS) sanitizer method performs. Use this directive to
improve the XSS checker results in cases where the checker does not correctly recognize
what a sanitizer does.

## Fields

This directive uses the following fields:

`xss_sanitizer_method`
:   A MethodSet that identifies the methods to
    which this directive applies.

`input`
:   A ParamIn value to identify the unsanitized
    input to the methods in `xss_sanitizer_method`.

`output`
:   A ParamOut value to identify the sanitized
    output from the methods in

`step1`
:   A JSON array. Each field in this array describes a string operation that
    the sanitizer method performs on the `input` in order to
    compute the `output`. In other words, the operations in
    each step array describe a series of character replacements.

`step2`, `step3`, ... and so on
:   (Optional) You can add additional `step` arrays, as
    needed. Each additional step should have the same structure as
    `step1`.

    Some sanitizers handle nested language contexts (for instance, a string
    inside JavaScript inside an HTML attribute value). These require
    multiple steps.

    For another example, a step might describe HTML entity encoding (changing
    `&` to `&amp;`, and so on) for
    an HTML attribute value, while a different step describes transforming
    newline characters to `\n` for JavaScript strings.

    The replacement operations specified in each step have the following
    requirements:

    - They do not interfere with each other.

      In other words, the order in which the replacements within a step
      are applied does not change the outcome of the step as a
      whole.
    - They apply to the same language context.

      For example, operations for escaping an HTML attribute value
      should not be mixed with operations for escaping a string value
      in a JavaScript program.

    For more information, see Step
    entries and step examples.

## Step entries and step examples

**`step1` example**

The following is an example of a step:

```
    "step1": 
      [ 
        { PREPEND_BACKSLASH : [ "\"", "'" ] },
        { JS_CHAR_CODE : [ "\n" ] },
      ],
```

This step describes how three different characters are replaced in a JavaScript
string:

- Prepend a backslash in front of any single-quote or double-quote
  character.
- Replace the newline character with an escape sequence that is
  *different* from simply placing a backslash in front of the
  character. (This distinction is important because it removes the newline
  from the string.)

The replacements in this step can be performed in any order to obtain the same
result, and they all apply to the same language context: a string in JavaScript.

**`step2` example**

If you also want the sanitizer to perform HTML entity encoding on the quote and
double-quote characters, you need to add another step to use the JavaScript string
in an HTML attribute value, as shown in the following example:

```
    "step2": 
      [ 
        { HTML_CHAR_REF : [ "\"", "'" ] },
      ],
```

The steps occur in order, taking the output of the preceding step. That is,
`step1` replaces a quote with `\'`, and
`step2` turns that into `\&quot;`.

A step value is a JSON array of values representing an unordered set of replacements
that apply to different characters.

Each array element is a JSON object that has a single field:

- The `name` describes the kind of replacement
  operation.
- The `value` describes a set of replaced characters.

The set of replaced characters can be described in two ways:

- Using an array of JSON strings that represent individual characters.

  JSON string escape sequences might be needed to express certain
  characters.

  **Example:**

  ```
      "step1": 
        [ 
          { REMOVE : [ "\"", "'", "\u2029" ] },
        ],
  ```
- Using a regular expression to match a set of characters.

  **Example:**

  ```
      "step1": 
        [ 
          { REMOVE : { regex-charset : "[^a-zA-Z0-9]" } },
        ],
  ```

Names and meanings of character-replacement operations:

- PREPEND_BACKSLASH

  Insert a `\` in front of the character. This is used in
  JavaScript and CSS strings, for certain characters, to literally mean those
  characters. Some characters (for example, `n` in JavaScript,
  or `A` in CSS) cannot be escaped this way, since the result
  will mean something different.

  Within a step, this operation can be mixed with either JS_STRING_CHAR_CODE or
  CSS_CHAR_CODE operations.

  **Example:**

  Replacing `"` with `\"`.

  ***Not* an example:**

  Replacing newline with `\n` is *not* an example of
  PREPEND_BACKSLASH.
- HTML_CHAR_REF

  Replace the character with a numeric or named HTML character reference.

  Within a step, this operation cannot be mixed with other kinds of
  operations.

  **Examples:**

  Replacing `&` with `&#38;` or
  `&#x26;` or `&amp;`
- JS_STRING_CHAR_CODE

  Replace a character in a JS string with a numeric or reserved escape sequence
  that is different from PREPEND_BACKSLASH.

  Within a step, this operation can be mixed with PREPEND_BACKSLASH
  operations.

  **Examples:**

  - `\n` for newline
  - `\u000A` for newline
- CSS_CHAR_CODE

  Replace a character in a CSS string with a numeric escape sequence.

  Within a step, this operation can be mixed with PREPEND_BACKSLASH
  operations.

  **Example:**

  `\00000A` for newline
- URI_PERCENT

  Replace the character with a percent escape sequence used in URIs.

  Within a step, this operation *cannot* be mixed with other kinds of
  operations.

  **Example:**

  Replace `&` for `%26`
- REMOVE

  Remove the character.

  Within a step, this operation *cannot* be mixed with other kinds of
  operations.

## Configuration and Java code examples

**Configuration example:**

```
// This is a 1-step sanitizer model for HTML escaping an attribute value.
{ 
  "xss_sanitizer_method" : 
    { "named" : 
        "examples.Test_xss_sanitizer_method.escapeAttributeValue(
                java.lang.String)java.lang.String"
    },
    "input" : "arg1",
    "output" : "return",
    "step1": 
      [ 
        { HTML_CHAR_REF : [ "\"", "'", "&" ] },
      ],
},

// This is also a 1-step sanitizer model for HTML escaping an attribute value.
// This demonstrates using a regular expression for specifying the affected
// characters.
{
  "xss_sanitizer_method" :
    { "named" :
      "examples.Test_xss_sanitizer_method.escapeAttributeValue_regex_spec(
              java.lang.String)java.lang.String"
    },
    "input" : "arg1",
    "output" : "return",
    "step1":
      [
        { HTML_CHAR_REF : { regex-charset : "[\"'&]" } },
      ],
},

// This is a 1-step sanitizer model for removing dangerous characters from an attribute value.
// This also demonstrates using a regular expression to specify a character set.
{ 
  "xss_sanitizer_method" : 
    { "named" : 
        "examples.Test_xss_sanitizer_method.filterAttributeValue(
                java.lang.String)java.lang.String"
    },
    "input" : "arg1",
    "output" : "return",
    "step1": 
      [ 
        { REMOVE : { regex-charset : "[\"'&]" } },
      ],
},

// This is a 1-step sanitizer model for escaping a JavaScript string.
{ 
  "xss_sanitizer_method" : 
    { "named" : 
      "examples.Test_xss_sanitizer_method.escapeJavaScriptString(
              java.lang.String)java.lang.String"
    },
    "input" : "arg1",
    "output" : "return",
    "step1": 
      [ 
        { JS_STRING_CHAR_CODE : [ "\"", "'", "\\" ] },
      ],
},

// This is a 2-step sanitizer model:
// Step 1: escape for a JavaScript string.
// Step 2: escape for an HTML attribute value.
{ 
  "xss_sanitizer_method" : 
    { "named" : 
      "examples.Test_xss_sanitizer_method.escapeJavaScriptStringInAttributeValue(
              java.lang.String)java.lang.String"
    },
    "input" : "arg1",
    "output" : "return",
    "step1": 
      [ 
        { JS_STRING_CHAR_CODE : [ "\"", "'", "\\" ] },
      ],
    "step2": 
      [ 
        { HTML_CHAR_REF : [ "\"", "'", "&" ] },
      ],
},
```

**Java code example:**

```
package examples;

import java.util.*;
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

class Test_xss_sanitizer_method extends HttpServlet
{

// The XSS analysis will use the xss_sanitizer_method directive for
// the sanitization models, rather than these implementations.

  String escapeAttributeValue(String val) { 
    return val; 
  }
  String escapeJavaScriptString(String val) { 
    return val; 
  }
  String escapeJavaScriptStringInAttributeValue(String val) {
    return val;
  }

  public void doGet(HttpServletRequest request, HttpServletResponse resp)
    throws IOException
  {
    PrintWriter pw = resp.getWriter();
    String taint = request.getParameter("taint");

  // Demonstrate an XSS from unsanitized text in a title attribute value.
    pw.print("<p title=\"" + taint + "\">"); // XSS

  // Demonstrate text sanitized using the 1-step sanitizer model
  // for the attribute value escaper.
    String safe_text = escapeAttributeValue(taint);
    pw.print("<p title=\"" + safe_text + "\">"); // no XSS

  // The same as the previous example.
  // The difference is that the xss_sanitizer_method uses a
  // regular expression to specify the escaped characters.
    String safe_text2 = escapeAttributeValue_regex_spec(taint);
    pw.print("<p title=\"" + safe_text2 + "\">"); // no XSS

  // Demonstrate an XSS from an unsanitized string in JavaScript 
  // in an onclick attribute value.
    String unsafe_js = "alert('" + taint + "');";
    pw.print("<div onclick=\"" + unsafe_js + "\">"); // XSS

  // Demonstrate sanitizing the string-in-JavaScript-in-attribute using
  // two escapers with 1-step sanitizer models.
    String safe_js = escapeJavaScriptString(taint);
    String safe_attrval = "alert('" + escapeAttributeValue(safe_js) + "');";
    pw.print("<div onclick=\"" + safe_attrval + "\">"); // no XSS

  // Demonstrate sanitizing the string-in-JavaScript-in-attribute using
  // an escaper with a 2-step sanitizer model.
    String safe_js_attrval = 
      "alert('" +
      escapeJavaScriptStringInAttributeValue(taint) +
      "');";
    pw.print("<div onclick=\"" + safe_js_attrval + "\">"); // no XSS
    
  }
}
```
