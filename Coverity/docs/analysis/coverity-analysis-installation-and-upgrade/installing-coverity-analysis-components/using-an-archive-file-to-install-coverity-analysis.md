---
title: "Using an archive file to install Coverity Analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-an-archive-file-to-install-coverity-analysis.html"
content_id: "wXIv4_ysbPRsc5QkYuSXkQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:44:57.643393+00:00"
---

# Using an archive file to install Coverity Analysis

Coverity recommends using the executable installers (.sh,
.exe files described in Installing Coverity Analysis) instead of the archive installers
(.tar.gz and .zip files, for example,
cov-analysis-aix-2026.6.0.tar.gz)
because the executables set up user preferences that you will need, while the archive
files do not. Archive installers are provided only for the very rare cases in which
there is a problem with the executables. If you need a command line mechanism for
automating the installation when using executables, see Coverity Analysis silent installer.

**To install Coverity Analysis components using an archive file:**

1. Verify that your operating system and compiler versions are supported.

   For
   details, see Supported platforms for Coverity Analysis.
2. Verify that the archive installer has the MD5 checksum described in the [Black Duck Community site](https://community.blackduck.com/s/contactsupport) (requires login).

   You need to use the
   md5sum utility to calculate the MD5 hash.
3. On the machine where you intend to perform builds and analyses, decompress the
   contents of the archive into an installation directory that is *not* the root
   directory and that *does not* have a space character (" ") in the directory
   name.

   This directory is your
   <install_dir>.
4. Set up licensing for Coverity Analysis.

   For details, see Coverity Analysis license options.
5. Add the <install_dir>/bin/ directory to your PATH
   environment variable.

   Once your PATH is set correctly, running command such as
   `cov-help --help` should display the help page for the
   command.
