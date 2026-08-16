---
title: "Primary projects and stream links"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/primary-projects-and-stream-links.html"
content_id: "Fcc6LPZGEbpQSiT4FXpQDw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:49.723214+00:00"
---

# Primary projects and stream links

When you associate a stream with a project, that project becomes the primary project for
the stream. The project also becomes the primary project for any stream links that were
created from those streams. A stream link is a reference to a stream that can occur in
other projects.

Streams and stream links that are associated with the primary project inherit the roles
from the primary project. In this way, primary projects provide a way for project owners
to centrally define and manage access role permissions for streams and stream links.

After you create and associate streams with the primary project, the streams can be
associated with other projects by stream links (for details, see Associating a stream with multiple projects). Stream links behave the
same as the stream to which you create the link. The following figure shows the
relationship of multiple project/stream associations. The red lines represent the
association of streams to a primary projects, while the dotted blue lines represent a
stream link association:  
 [image: image]

See the Primary
project use case for an example of the process.
