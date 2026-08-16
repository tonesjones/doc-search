---
title: "Example coverity.conf file"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-coverity.conf-file.html"
content_id: "lICRdSes7LMRzdMKSpitUg"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:47:32.867954+00:00"
---

# Example coverity.conf file

```
{
    "type": "Coverity configuration",
    "format_version": 1,
    "format_minor_version": 7,
    "settings": {
        "server": {
            "url": "https://d-linux64-03.sf.coverity.com:443",                                           // REQUIRED
            "username": "$(env:COV_USER:USER:USERNAME)",                                                 // default
            "auth_key_file": "$(cov_user_dir)/authkeys/ak-$(server_host_as_fname)-$(server_port)"        // default
        },
        "stream": "prevent-harmony",                                                                     // REQUIRED
        "compiler_config_file": "$(code_base_dir)/data-coverity/v$(version)/config/coverity_config.xml", // default
        "compiler_configurations": [
            {
                "cov_configure_args": ["--gcc"]
            },
            {
                "cov_configure_args": ["--java"]
            }
        ],
        "intermediate_dir": "$(code_base_dir)/data-coverity/v$(version)/idir",                           // default
        "license_file_dir": "$(code_base_dir)/data-coverity/v$(version)/lic",                            // default
        "scm": {
            "scm": "git"
        },
        "cov_run_desktop": {
            "build_cmd": ["make", "-j$(num_cores)"],
            "build_options": [
                "--encoding", "UTF-8",               
                "--cygwin",
                "--delete-stale-tus"
            ],
            "clean_cmd": ["make", "clean"],
            "restrict_modified_file_regex": "^(?!.*/(cmd-)?(j|cs)?test.*).*\\.(java|c|cpp|cc)$",
            "analysis_args": [
                "--enable-fb"
            ],
            "reference_snapshot": "scm"
        },
        "known_installations": [
            {
                "version": "7.5.0",
                "platform": "linux64",
                "kind": "cov-analysis",
                "directory": "/home/user1/opt/cov-analysis-linux64-7.5.0"
            },
            {
                "version": "7.5.1",
                "platform": "linux64",
                "kind": "cov-analysis",
                "directory": "/home/user1/opt/cov-analysis-linux64-7.5.1"
            }
        ],
        "ide": {
            "path_mapping": {
                "strip_paths": [
                    "path1",
                    "path2"
                ],
                "search_paths": [
                    "path3",
                    "path4"
               ]
            },
            "build_strategy": "CUSTOM"
        },
        "conditional_settings": [
            {
                "when": {
                    "platforms": ["win64", "win32"]
                },
                "settings": {
                    "compiler_configurations": [                                                         // These settings are the default,
                        {                                                                                // except that by default they apply
                            "cov_configure_args": ["--gcc"]                                              // to all platforms.
                        },
                        {
                            "cov_configure_args": ["--java"]
                        },
                        {
                            "cov_configure_args": ["--msvc"]
                        },
                        {
                             "cov_configure_args": ["--cs"]
                        }
                    ],
                "cov_run_desktop": {
                    // adds "cs" extension on Windows
                    "restrict_modified_file_regex": "^(?!.*/(cmd-)?(j|cs)?test.*).*\\.(java|c|cpp|cc|cs)$"
                }
            }
        },
        {
            // On linux64, configure ccache checked in to platform-packages.
            "when": {
                "platforms": ["linux64"]
            },
            "settings": {
                "add_compiler_configurations": [
                    {
                        "cov_configure_args": [
                            "--compiler",
                            "$(code_base_dir)/linux64-packages/bin/ccache",
                            "--comptype",
                            "prefix"
                        ]
                    }
                ]
            }
        }
    ]
}
```
