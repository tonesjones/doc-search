---
title: "The output of 'cov-build': The 'build-log.txt' log file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/the-output-of-cov-build-the-build-log.txt-log-file.html"
content_id: "A4hs2s2FQ7_ywtvD12Vfsg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:59.640698+00:00"
---

# The output of 'cov-build': The 'build-log.txt' log file

The `cov-build` command generates the log file in
<intermediate_directory>/build-log.txt that contains a
line for every command executed by the build process. The contents of
build-log.txt are similar to:

```
EXECUTING 'make all '
EXECUTING '/bin/sh -c cd qmake && make '
EXECUTING 'make '
CWD = /export/home/acc/test-packages/qt-x11-free-3.3.2/qmake
COMPILING '/export/home/acc/prevent/bin/cov-translate g++ -c -o property.o \
-I. -Igenerators -Igenerators/unix \
-Igenerators/win32 -Igenerators/mac -I/export/home/acc/test-packages/qt-x11 \  
-free-3.3.2/include/qmake \
-I/export/home/acc/test-packages/qt-x11-free-3.3.2/include \
-I/export/home/acc/test-packages/qt-x11-free-3.3.2/include \
-DQT_NO_TEXTCODEC -DQT_NO_UNICODETABLES -DQT_NO_COMPONENT \
-DQT_NO_STL -DQT_NO_COMPRESS \
-I/export/home/acc/test-packages/qt-x11-free-3.3.2/mkspecs/solaris-g++ \
-DHAVE_QCONFIG_CPP property.cpp ' \
 /export/home/acc/prevent/bin/cov-emit --g++ -I. \
-Igenerators -Igenerators/unix \
 -Igenerators/win32 -Igenerators/mac \
-I/export/home/acc/test-packages/qt-x11-free-3.3.2/include/qmake \
-I/export/home/acc/test-packages/qt-x11 \
-free-3.3.2/include -I/export/home/acc/test-packages/qt-x11-free-3.3.2/ \
include \
-DQT_NO_TEXTCODEC -DQT_NO_UNICODETABLES -DQT_NO_COMPONENT \
-DQT_NO_STL -DQT_NO_COMPRESS \
-I/export/home/acc/test-packages/qt-x11-free-3.3.2/mkspecs/solaris-g++ \
-DHAVE_QCONFIG_CPP \
--emit=/export/home/acc/prevent/emit -w \
--preinclude /export/home/acc/prevent/config/nodefs.h \
--preinclude /export/home/acc/prevent/config/solaris-x86/nodefs-g++.h \
--sys_include /usr/local/include/c++/3.3.2 \
--sys_include /usr/local/include/c++/3.3.2/i386-pc-solaris2.9 \
--sys_include /usr/local/include/c++/3.3.2/backward \
--sys_include /usr/local/include \
--sys_include /usr/local/lib/gcc-lib/i386-pc-solaris2.9/3.3.2/include \
--sys_include /usr/include property.cpp \
Emit for file '/export/home/acc/test-packages/qt-x11 \
-free-3.3.2/qmake/property.cpp' complete.
Emit for file '/export/home/acc/test-packages/qt-x11-free-3.3.2 \
/src/tools/qsettings.h' complete.
EXECUTING '/usr/local/lib/gcc-lib/i386-pc-solaris2.9/3.3.2/cc1 \
plus -quiet -I. \
-Igenerators -Igenerators/unix \
-Igenerators/win32 -Igenerators/mac \
-I/export/home/acc/test-packages/qt-x11-free-3.3.2/include/qmake \
-I/export/home/acc/test-packages/qt-x11-free-3.3.2/include \
-I/export/home/acc/ \
test-packages/qt-x11 \
-free-3.3.2/include -I/export/home/acc/test-packages/qt-x11-free-3.3.2/ \
mkspecs/solaris-g++ \
-D__GNUC__=3 -D__GNUC_MINOR__=3 -D__GNUC_PATCHLEVEL__=2 \
-DQT_NO_TEXTCODEC \
-DQT_NO_UNICODETABLES -DQT_NO_COMPONENT \
-DQT_NO_STL -DQT_NO_COMPRESS \
-DHAVE_QCONFIG_CPP \
property.cpp -D__GNUG__=3 -quiet -dumpbase property.cpp \
-auxbase-strip property.o \
-o /var/tmp//cc2Wo7sG.s '
EXECUTING '/usr/ccs/bin/as -Qy -s -o property.o /var/tmp//cc2Wo7sG.s '
```

The lines beginning with EXECUTING are commands that are executed by your build system
but do not have any relation to compiling source code. For example, the commands
executed by the build system to recursively descend into subdirectories in the source
tree should show up as EXECUTING. When a compile line is encountered, three lines are
printed. The first line begins with CWD, and shows the current working directory for the
subsequent compile lines. The subsequent lines beginning with COMPILING are lines that
are recognized as compiler invocations. The `cov-translate` program is
called with the compiler command line arguments. The `cov-translate`
command reads .xml and transforms the command line into the
following line, which invokes the Coverity front-end program
(`cov-emit`) to parse and emit the source file. The command line
arguments to `cov-emit` are described in Configuring compilers for Coverity Analysis.

For each source file that contains at least one function, the Coverity compiler prints a
message "`Emit for file '/path/to/file.c' complete.`" The
presence of this message confirms that the file exists in the intermediate directory and
will be analyzed in the analysis step. The compiler can decide to skip emitting a file
if it decides that it cannot have changed since the last emit. This will only happen if
the timestamp for the file and all of the files included by it are the same as the
previous emit.

If `cov-emit` produces error messages, it might be because of a
misconfiguration or parsing compatibility issue. For more information on how to resolve
compilation issues, see Configuring compilers for Coverity Analysis.
After `cov-emit` completes the emit, the compiler for the native build
runs. This results in additional EXECUTING lines for the compiler proper
(`cc1plus` in the example) and the assembler (`as`
in the example).
