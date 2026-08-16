---
title: "Managing tags"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/managing-tags.html"
content_id: "taDfvEyETE~XVCKhDVhFfw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:05.921469+00:00"
---

# Managing tags

You can add tags to projects and custom components to describe them and provide
additional metadata, such as the programming language, frameworks, operating systems,
purpose, and any other information that you think might help other users find it. Tags
act as keywords when searching and filtering.

- Tags for components in Black Duck KB have been created by the users
  at [The Open
  Hub](https://www.openhub.net/).
- Tags for projects are created by project team members.
- Tags for custom components are created by users with the Component Manager role.

Best practices for tagging projects and custom components:

- Use a few, specific tags rather than many tags. Tags are limited to 20 for each
  project or custom component.
- Tags must be at least one character long (nulls not allowed) and are limited to
  50 characters in length. You can use letters and numbers to create tags.
- The only special characters supported in tags are the underscore (_), the plus
  sign (+), and parentheses ( ). You cannot use spaces in tags.
- Do not use punctuation unless it is necessary for the tag, for example, C vs. C#
  vs. C++.
- Use singular nouns, for example, “server” instead of “servers”.

**To add tags to a project:**

1. Log in to Black Duck SCA.
2. Select the project name using the **Watching** or **My Projects**
   dashboard. The *Project Name* page appears.
3. Type the tag in the Tags field and press **Enter**.

   The tag is added to the project.

**To add tags to a custom component:**

1. Log in to Black Duck with the Component Manager role.
2. Click [image: Manage icon] > **Component Management**.

   The Component Management page appears.
3. Select the name of the custom component to go to the *Custom Component Name*
   page.
4. Type the tag in the Tags and press **Enter**.

   The tag is added to the custom component.

**To edit a tag:**

1. Click the **Tags** field.
2. Select **X** next to the tag you wish to edit.
3. Type the revised text in the field and press **Enter**.

**To remove a tag:**

1. Click the **Tags** field.
2. Select **X** next to the tag.
