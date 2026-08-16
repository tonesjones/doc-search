---
title: "Custom translation code"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/custom-translation-code.html"
content_id: "uDPrSr~y8MRQ09CdjtTnDA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:17.049191+00:00"
---

# Custom translation code

Custom translation code can be created and executed using the extern_trans and
intern_trans tags. The intern_trans tag can only be used by Coverity since the code gets
linked directly into `cov-translate`. The source code for these
translators is shipped with the product and can be converted to an external translator
by compiling it in combination with intern_to_extern_phase.cpp. For
example, tm_compilers.cpp can be compiled as follows (this command
is an example and should be adjusted for your compiler. If you do not have a compiler
that produces binaries for your system, you can use the Extend SDK compiler):

```
cd install_dir/config/templates/tm
```

The compilation should be executed from the 
install_dir/config/templates/compiler
 directory because the binary will be placed into the current working
directory and will be automatically retrieved by `cov-translate`
without modifying the configuration file.

The binary name produced by the compilation should match the internal translator
specified by the intern_trans tag in the 
install_dir/config/templates/compiler/compiler_config.xml
file. However, you should not modify the intern_trans tag.

Execute the compilation, for example:

```
install_dir/sdk/compiler/bin/g++ -std=c++11 -o trimedia_pre_translate -I. -I../../cit  \
-DCOMPILER_FILE=tm_compilers.cpp -DFUNCTION=trimedia_pre_translate  \
--static ../../cit/intern_to_extern_phase.cpp
```

Note: There are known issues with Cygwin gcc, so you should use statically linked binaries
and the Extend SDK compiler wherever possible.

The following example is typical for a translator. The `CompilerOptions` class
is an executable representation of the compiler switches file.

```
#include "translate_options.hpp"

void trimedia_pre_translate(const CompilerOptions &opts, arg_list_t& in)
{
    arg_list_t out;
    arg_processor mopt(in, out, opts);

    while (!in.empty()) {
        if (mopt("Xc")) {
            if (mopt.extra_arg == "ansi"
                || mopt.extra_arg == "knr"
                || mopt.extra_arg == "mixed"
               ) {
                out.push_back("-coverity_source=c,h");
	        }
            else if (mopt.extra_arg == "arm"
                     || mopt.extra_arg == "cp"
                    ) {
                out.push_back("-coverity_source=c++,hpp");
            }
        }
        else if (mopt("Xchar")) {
	        if (mopt.extra_arg == "signed") {
	            out.push_back("--signed_chars");
	        }
            else if (mopt.extra_arg == "unsigned") {
	            out.push_back("--unsigned_chars");
	        }
	    }
        //Automatically translate based on the switch table.
        //Do not remove this call.
	    else if (mopt.translate_one_arg()) { }
	    else {
	        out.push_back(in.front());
                    in.pop_front();
	    }
    }
    mopt.finalize();

    in = out;
}
```
