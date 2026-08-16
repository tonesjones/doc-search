---
title: "Using the Coverity CLI"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-coverity-cli.html"
content_id: "LnClGOShopLE7mzch2flaw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:48.967415+00:00"
---

# Using the Coverity CLI

After installing Coverity Analysis, you can invoke the Coverity CLI tool directly by
entering a command in your terminal using the following format:

```
coverity <command> <args>
```

For example, the following command does the initial setup, captures the source files in
your current working directory, analyzes that source, and commits the result to Coverity
Connect.

```
coverity scan
```

The figure below illustrates the two workflows you can use when you run the Coverity CLI:

Figure 1. Coverity CLI workflow
[image: image]

We recommend that you use the fast workflow at first, and then use the more detailed workflow
only if you have a custom setup or if you need to fine tune the process.

Attention: The Coverity CLI has a known issue when
reading the Coverity Connect password in the Cygwin shell using the `coverity
setup` or `coverity scan` commands. To work around this
issue, run `coverity setup` using the Windows command shell
`cmd.exe`. You can then switch back to the Cygwin shell.

The scan action includes the following commands:

1. The `coverity setup` command generates a configuration file and specifies the
   name of the directory for your source code if this is different than the current
   working directory. It also specifies the location of the Connect server where you
   want to persist your results.

   For more information about the configuration file,
   see Configuring the Coverity CLI.
2. The `coverity capture` command captures the source
3. The `coverity list` command displays the files that were captured; output
   looks like this:

   ```
   ...
   Files for project file: /Users/<username>/Projects/open-source/lunr.js/Makefile
     File family: Configuration
       File type: JSON
         Filename                          Capture Status Code Lines Notes
         .eslintrc.json                    Succeeded      74
         build/jsdoc.conf.json             Succeeded      10
         package-lock.json                 Succeeded      1636
         test/fixtures/stemming_vocab.json Succeeded      1
       File type: Markdown
         Filename        Capture Status Code Lines Notes
         CHANGELOG.md    Succeeded      158
         CONTRIBUTING.md Succeeded      12
         README.md       Succeeded      54
   ```

   Information returned includes
   the file type and name, whether the file was captured for analysis, the number
   of code lines, and notes. Capture might fail due to the following:

   - For non-compiled files (Dart, JavaScript, PHP, Python, Ruby, Scala, or configuration
     files): this means the effort to capture has failed. For help, please
     contact Black Duck Support via the [Black Duck Community site](https://community.blackduck.com/s/contactsupport).
   - For compiled files: it means that files are unsupported (e.g., C or C++ with no build
     command), however you will still get analysis results.

     For C, C++,
     Objective-C, Objective-C++, or Visual Basic with a build command, or for
     Java or C#, it means the compiler did not compile them. The most likely
     reason is that the files are excluded from being compiled by the build
     system. If the files are in fact being compiled and not being captured,
     please contact Black Duck Support via the
     [Black Duck Community site](https://community.blackduck.com/s/contactsupport).
   - Source files for languages that are not supported will be listed in the output with a
     capture status of `Ignored`.
4. The `coverity analyze` command analyzes the captured code.
5. The `coverity commit` command saves analysis results to a local directory,
   to Coverity Connect, or to both locations.

   Commit results look like this: Bolded
   elements below show diagnostic and remediation information for a suspected
   copy-paste error.

   ```
   254  	/**
   255  	 * Returns a new set containing only the elements that are present in both
   256  	 * this set and the specified set.
   257  	 *
   258  	 * @param {lunr.Set} other - set to intersect with this set.
   259  	 * @returns {lunr.Set} a new set that is the intersection of this and the specified set.
   260  	 */
   261  	
   262  	lunr.Set.prototype.intersect = function (other) {
   263  	  var a, b, elements, intersection = []
   264  	

   (2) Event copy_paste_error: 	"other" in "other === lunr.Set.complete" looks like a copy-paste error.
   (3) Event remediation: 	Should it say "this" instead?
   Also see events: 	[original]

   265  	  if (other === lunr.Set.complete) {
   266  	    return this
   267  	  }
   268  	

   (1) Event original: 	"other === lunr.Set.empty" looks like the original copy.
   Also see events: 	[copy_paste_error][remediation]

   269  	  if (other === lunr.Set.empty) {
   270  	    return other
   271  	  }
   ```

After you are satisfied that analysis is being carried out as expected, you can use the
`coverity scan` command to do everything in the detailed workflow.

In this section:

- Configuring the Coverity CLI
- Command reference
- Options reference
- Point and Scan and the CLI Support matrix
