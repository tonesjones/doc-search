---
title: "Creating a project"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-a-project.html"
content_id: "KYB~Bq3qOJPlb9Cup8oSIw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:13:58.984779+00:00"
---

# Creating a project

A project is the base unit in Black Duck. A project can be both a
stand-alone development project and part of another project. For example, Apache Tomcat
is a project in its own right but it may also be part of other, larger projects. You
must create the projects that you want to make available for search by other developers
in your organization.

Projects or applications are limited to 10GB of Managed Code base.

Note: If SCM Integration is
enabled in your environment and you want to create a SCM project, see Creating a SCM project.

To create a project:

1. Log in to Black Duck SCA.
2. Click **+ Create Project** at the top of any page. If SCM
   Integration is enabled in your environment, select **Standard
   Project** from the menu. The **Project Details** page will display.

     
    [image: Create a New Project page]   

   Note: If this page includes additional fields or questions not shown above
   (or described below), it is because your system administrator has created custom fields to
   collect additional information.
3. Enter a project name. This name must be unique among projects in Black Duck,
   although it can have the same name as a project in Black Duck KB.

   Tip: As a best practice, you should think about how other users will
   search for your projects when creating project names. For example, if your
   project is related to 3D graphics, naming it "3DGraphics" means that the user
   must type the entire project name in order to find your project. If you use a
   space or an underscore in the name, for example, "3D Graphics" or "3D_Graphics",
   the additional separator characters will allow users to locate the project using
   the search term "3D". For more information about
   how Black Duck parses project information in search, see
   Searching for projects.
4. Optionally, enter additional information such as:
   - **SCM Repository**: The URL of the source code management (SCM) repository where your
     code resides. This field is visible only if this feature is enabled in your
     environment. It can be manually edited or automatically populated by Detect
     after completing a package manager scan. Manually changing the SCM
     repository URL could break an existing scan if the URLs don't match. Note
     that this feature is available with Detect 8.x or later.
   - **Description**: As a best practice, you should think about how other
     users will search for your projects when creating project descriptions.
     The description should be specific about what the project does and how
     it is unique, so that it is easily distinguishable from other similar
     projects.
5. Type the version for this project in the **Version Name** field.
6. Optionally, enter additional information such as the SCM branch, the project phase, and the
   method in which the project is being delivered.
7. Click **Save**.

   Black Duck displays the *Project Name*
   page. You can rename this version and change its information, and add new versions as needed.

     
    [image: Project Name page]
