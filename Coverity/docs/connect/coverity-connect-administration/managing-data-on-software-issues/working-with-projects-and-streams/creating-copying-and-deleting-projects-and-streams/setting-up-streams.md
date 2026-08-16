---
title: "Setting up streams"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-streams.html"
content_id: "oct8bid2R7FJfZrD_WvhSQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:00.185235+00:00"
---

# Setting up streams

The process of creating a stream is similar to creating a project. When you create a
stream, you give it a name and description. In addition, you must associate the stream
with a Triage Store. You can also select a
component map, an issue category map (if more than
one is set up), and one or more groups with permission to the stream. For more
information about roles and the permissions that are associated with those roles, see
Roles and role-based access control.

Note: See Important preconditions for using streams in a production
environment.

**To create a stream:**

1. Select Configuration > Projects & Streams.
2. Decide where to create the stream:

   - If you select a project before creating a stream, Coverity Connect will
     automatically associate the stream with the selected project. Creating a
     stream under a project also makes the project the primary project for
     the stream (see Primary projects and stream links for
     more information).
   - To create an unassociated stream, you need to select Other
     Streams and click the +Stream
     button. You can then associate the new stream with any existing
     project.

   Note that you can always associate a stream with another project (but not
   Other Streams) after creating it.
3. Click +Stream.

   Coverity Connect displays a dialog with a name similar to New
   Stream 280. You can either use the default name or create a new
   name.

   Important: Stream names are case-sensitive and
   must be 1 - 256 characters. Stream names can NOT contain the following special
   characters:
   - `:` (colon)
   - `*` (asterisk)
   - `/` (forward slash)
   - `\` (back slash)
   - `` ` `` (backtick)
   - `'` (single quote)
   - `"` (double quote)
4. Select a programming language for the stream:

   - Any
   - C/C++
   - C#
   - Java
   - Dynamic Analysis
   - Other

   These settings determine the programming language's analysis results that you can
   commit to the stream. The default for a newly created stream is
   Any, indicating that the stream can accept commits
   from any of the supported languages. Furthermore, you can commit multiple
   analyses of mixed languages to the same Any stream.
   Coverity highly recommends that you choose Any for each
   new stream that you create.

   The other languages are provided for backward compatibility for previously
   released Coverity Connect versions (in implicitly designated languages were
   required for streams). Coverity recommends that you only select a specific
   language when you want to commit to the stream using pre-7.0 clients. If you
   define a specific language to a stream, Coverity Connect prohibits you from
   committing results from a different language.

   After a stream has been defined and an initial commit has been executed, it is
   possible to change the language for the stream and then commit the newly defined
   language analysis results to it. Use extreme caution if you plan to switch
   languages because the stream will not necessarily indicate any information about
   the stream's past commits from another language.
5. Optionally, select a component map for the stream.

   This setting associates the source stream with an existing component map. For
   information about component maps, see 1.
6. Optionally, select an Issue Categorization. If one or more
   issue categorization maps have been set up in Coverity Connect (see Configuring custom issue categories), you can apply one to the
   stream. Issues found in future commits to the stream will use those issue
   categories.
7. Select a Triage Store for the stream.

   Each stream must be associated with a single Triage Store. For information about
   Triage Stores, see Managing triage stores.
8. Optionally designate the stream as Outdated.

   When you select this option, the stream and its data are effectively hidden from
   Coverity Connect user-oriented operations such as metric calculation, issue
   reporting, views displays, and so forth. Certain marked non-issue views
   (Functions, Files) will continue to include outdated issues in their aggregate
   counts, though following the link can bring the user to a view that excludes the
   specific outdated issues.

   Note: A user can still commit to an outdated stream.
9. Click Create to save your changes and exit. If you need to
   change any of the information, click Edit in
   Stream Details.

   Note: Once you create the stream, it will include a Snapshots
   tab. For details, see Managing snapshots of streams.
