---
title: "Options: Models"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/options-models.html"
content_id: "Tg82M7PbAs~q_FSZ8jsYMA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:46.046322+00:00"
---

# Options: Models

--model-file <file>.xmldb
:   Uses the specified file to override any function models that are
    automatically derived from the implementation. It can determine whether a
    specified file is for user or derived models. Note that if the default file
    at <install_dir>/config/user_models.xmldb
    exists, it is used even without specifying this option. This option can be
    specified multiple times.

    Note that you can only use this option on the output of
    `cov-collect-models`
    or `cov-make-library`.
    For more information, see "Model search order"
    in Customizing Coverity.
