---
title: "Frequently asked questions"
source_url: "https://docs.blackduck.com/r/blackduck-tools/latest/black-duck-tools/frequently-asked-questions.html"
content_id: "PTZp6Ld~U~dRqLEHGmQVTw"
version: "latest"
section: "Black Duck C/CPP Tool"
scraped_at: "2026-08-13T16:16:58.949855+00:00"
---

# Frequently asked questions

1. **Why is the BOM missing expected components?**

   Analyze each section of the tool separately. There may be errors in the log that
   could lead to the cause of the missing components. For example, if the BOM is
   missing binary information, check the results of the binary scan in the
   `blackduck_c_cpp.log` file.

   If the scans look succesful, make sure the Coverity build was run correctly. Run all
   clean commands and configure commands before running the Black Duck C/CPP tool with
   build command.

   If everything above was succesful, verify that the component is published and
   findable in the KnowledgeBase.

   Also, if you are using custom compilers, you have to configure it as follows:
   `--cov_configure_args: {"gcc.cx.a.b-ac.mips64-linux":"gcc"}`
   where `gcc.cx.a.b-ac.mips64-linux` is compiler and "gcc" is compiler
   type. you can also set `matchConfidenceThreshold` to 0 in
   `additional_sig_scan_args`.
2. **Where is the blackduck-c-cpp.log found on the system?**

   All output files will be in
   `user_home/.blackduck/blackduck-c-cpp/output/project_name` by
   default if `--output_dir` is not given. Else, All output files
   will be in `output_dir`.
3. **How do I run a snippet scan?**

   Pass the following command in your yaml file:
   `additional_sig_scan_args:'--snippet-matching'`.

   To run it from command line, example:

   `blackduck-c-cpp -bc "make" -d "/apps/cpuminer-2.5.1/" -s False -v True -proj
   "cpuminer-cmd" -vers 1.0 -bd "https:&lt;bd_url>" -a "&lt;api_token" -as
   ="--snippet-matching --copyright-search" -i False`
4. **How do I run Black Duck C/CPP?**

   Run with config file where are arguments are set or through command line. Example:
   `blackduck-c-cpp -c /apps/../../cpuminer-config.yaml`.

   To run it from command line:

   `blackduck-c-cpp -bc "make" -d "/apps/cpuminer-2.5.1/" -s False -proj
   "cpuminer-cmd" -vers 1.0 -bd "https:<bd_url>" -a "<api_token" -i
   False`
5. **Do I need to be licensed for BDBA? What happens if I don't have a BDBA
   license?**

   If you don't have a BDBA license, running the command will output the following
   error:

   ```
   BDBA is not licensed for use with the current Black Duck instance -- will not be used
   ```

   The tool will then continue to next matching type.
6. **Why is Black Duck C/CPP throwing import errors?**

   Check if you installed Black Duck C/CPP from testpypi. If so, please uninstall
   and install from pypi for dependencies to be automatically installed. If you
   still see import errors, There may be some issues with multiple installations.
   Try to create a virtual environment with Python versions 3.7 through 3.12.
   Uninstall Black Duck C/CPP outside virtual environment and install Black Duck
   C/CPP inside virtual env. Otherwise, it may be looking at wrong installation
   path (can be seen in stacktrace).

   In linux environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   pip3 install blackduck-c-cpp
   ```
7. **Where do I download the Coverity mini package?**

   If `coverity_root` is not specified, Black Duck C/CPP
   automatically downloads latest mini-coverity package from GCP for authorized
   Black Duck SCA users for Black Duck SCA versions >= 2021.10. For downloading
   Coverity package using GCP, you need to open connection toward
   `*.googleapis.com:443`. If you don't have Coverity package
   and your Black Duck SCA version is < 2021.10, please contact Black Duck
   Support to get latest version of Coverity package.
8. **What do I do if BDBA upload throws a Remote end closed connection without
   response error?**

   ```
   raise RemoteDisconnected("Remote end closed connection without"
   http.client.RemoteDisconnected: Remote end closed connection without response
   .......
   requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
   ```

   Check your requests-toolbelt library version `-pip show
   requests-toolbelt`. If you have older version than 0.9.1, install
   0.9.1 version and try again.
9. **What do I do if the Black Duck C/CPP process is stuck during a phase on
   Windows?**

   Try giving a keyboard input by pressing enter/any other key if you still have the
   command prompt open where stuck. We noticed in Windows that programs sometimes get
   stuck when we click into the console and enter the "selection" mode to
   highlight/copy text from it.
10. **What do I do if I get a KeyError error message?**

    ```
    headers.pop('Accept')
    KeyError: 'Accept'
    ```

    Run `pip show blackduck`. If you have version < 1.0.4, install 1.0.4
    version and try again.
11. **What do I do if I get a memory error on Windows?**

    Make sure you have the correct installation of Python (64 bit vs 32 bit) for your
    operating system.
12. **Can I have spaces in the paths to Coverity Analysis?**

    `/apps/.../cov\ 2021\ <vers>/bin/cov-build` Coverity needs to be
    located in a directory that doesn't have a space in it.
13. **Signature scan is performed on ZIP. Adding other signature scan arguments are
    not working. What to do?**

    Set `expand_sig_files: True`.
14. **How to uninstall Black Duck C/CPP?**

    Run the following command:

    `pip uninstall blackduck-c-cpp`
15. **I already have a Coverity build for my project. Can I use the tool?**

    Yes, you can set `--cov_output_dir` to the path where your
    Coverity output files reside. (build-log.txt and emit directory), then set
    `skip_build: True`.
16. **How to see more logging information for troubleshooting?**

    You can see the `blackduck-c-cpp.log` file in
    `output_dir` (OR) set `verbose: True` to see
    if it reveals any issues in `stdout`.
17. **What do I do if I have custom compilers?**

    If you are using custom compilers, you have to configure it as follows:
    `cov_configure_args: {"gcc.cx.a.b-ac.mips64-linux":"gcc"}`
    where "`gcc.cx.a.b-ac.mips64-linux`" is compiler and
    "`gcc`" is compiler type.
18. **What is debug mode?**

    Setting `debug: True` sends all the files we found to all matching
    types. By default, it will only send files not detected by package manager to
    BDBA and Signature matching.
19. **How to run a specific matching type?**

    You can select modes: `sig`, `bdba`,
    `pkg_mgr` in the configuration file to run specific ones.
20. **I already have run Black Duck C/CPP once. I ran in offline mode. I want to run
    in online mode. Do I need to do the full build again?**

    No, you can set `use_offline_files: True` and `skip_build:
    True` to use already stored files and just upload it to Black Duck
    SCA.
21. **I already have run Black Duck C/CPP once. I got a few errors after build is
    finished which are fixed now. I want to run again. Do I need to do the full
    build again?**

    No, you can set `skip_build: True` to skip build process.
22. **How do I exclude a full directory with the signature scan method?**

    Create a `excludes.txt` file and add the directories to be
    excluded. Then, in your configuration yaml file, add the following command:

    ```
    additional_sig_scan_args: '--snippet-matching --exclude-from <location of your excludes.txt file>'
    ```
23. Is `--individualFileMatching=BINARY` needed to use "Binary" value
    for individualFileMatching?

    The individualFileMatching parameter is already enabled by default in
    blackduck-c-cpp tool and cannot be disabled.
24. **The BDIO splitter fails to split one part when uploading to hub. How to fix
    it?**

    The BDIO splitter operates on the node numbers, not size, so when a dataset
    contains large archives, it performs suboptimally. The following parameter
    modify this behavior:

    - `bdio_split_max_file_entries`

      The `bdio_split_max_file_entries` parameter has a default
      value of `100000`.
    - `bdio_split_max_chunk_nodes`

      the `bdio_split_max_chunk_nodes` has a defaut value of
      `3000`.

    If the default values don't work, try reducing
    `bdio_split_max_file_entries` to about 80000 and see if the
    file size drops closer to 5GB.
