---
title: "Analyzing Code in a Git Repository"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/analyzing-code-in-a-git-repository.html"
content_id: "bk4fDuRqsLBdNIuNTp4Wqw"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:03:13.865790+00:00"
content_hash: "d760f6abc0cabb54196b362e49dce07b1e1b3ed608e073f9ba341879945497bb"
---

# Analyzing Code in a Git Repository

Software Risk Manager can be used to analyze code stored in a Git repository.

## Configuring a Project to Use a Git Repository

**To configure a project to use a Git repository:**

1. Click the Projects icon in the navigation bar to open the Projects page.
2. Click the project's dropdown configuration icon and select Git Config.
3. Enter the Repository URL and branch name.
4. If the repository requires credentials to access, click *Use Credentials*
   and enter the credentials.
5. Click *Test Configuration* to validate the configuration.
6. Click *Ok* to save the configuration.

   The *Git Configuration* popup will appear.

   [image: image]

The form inside is used to tell Software Risk Manager to use a Git repository as the
subject of analysis for this project. Once configured, Software Risk Manager will
automatically include the contents of the configured repository as an input for each
analysis with this
project.

The Git Configuration window has two fields: *Repository URL* and *Branch*.
The *Repository URL* should be filled out with the URL that you would use to
clone the repository. The *Branch* field should be filled with the name of the
branch in that repository that you want Software Risk Manager to analyze. By default,
the branch is set to "main", which is the main branch for most Git repositories.

For many projects, setting up a Git configuration is as easy as copying the
repository's URL into the text field and clicking *Test Configuration*.
For example, if you wanted to analyze the contents of the open-source
[WebGoat](https://github.com/WebGoat/WebGoat) repository, you would find the
clone URL on the side of the GitHub repository page, then copy it into the
*Repository URL* field in the *Git Configuration* window.

[image: image]

[image: image]

Software Risk Manager will verify the repository's existence and determine whether it
needs credentials to connect. Click *Ok* to save and close the form.

Note: For public (open-source) repositories, credentials are not required. However, if
credentials are required, see Working with Git
Credentials for more information on how to manage credentials.

Once you have entered a URL and branch, and entered whatever credentials are
necessary, click *Ok* to save the configuration. Doing so will close the window and
tell Software Risk Manager to obtain a local clone of the configured repository.
Depending on the size of the repository, the length of its history, and your network
connection, the clone operation may take anywhere from seconds to hours. Once
started, a progress bar will be displayed underneath the project's title on the
Projects page.

The "cloning" job has several subtasks, so you will see the progress bar fill up
several times. When the job is complete, the progress bar will turn blue, remain for
a couple of seconds, then slide out of view.

Once the clone is ready, the New Analysis page will automatically include the latest
contents of the configured branch of the configured repository as an input. See the
Analysis Overview section
for more detail.

## Working with Git Credentials

Some Git repositories are private and require credentials for access. Software Risk
Manager supports three forms of authentication: HTTP, SSH and OAuth Client Credentials.
Depending on the URL in the Repository URL field, Software Risk Manager will automatically
determine which type of credentials are required.

If you try to test the configuration for a private repository without entering
credentials, Software Risk Manager will automatically enable *Use Credentials*
and require that they are entered. Similarly, if credentials are provided when
configuring a public repository, Software Risk Manager will automatically disable
*Use Credentials*.

### HTTP Credentials

HTTP credentials consist of a username and password. For GitHub repositories,
these will generally be your GitHub account name and password. GitHub also
supports creating "Personal access tokens," which can be used in place of a
password.

[image: image]

### SSH Credentials

SSH uses a pair of files known together as a "keypair," or separately as a
"private key" and "public key." For Software Risk Manager to connect to a
repository through SSH, it needs your private key. The system in charge of the
repository's security will also need your public key.

If you are trying to access a private GitHub repository, visit your SSH Keys page
at <https://github.com/settings/ssh>
to register your SSH key with GitHub. GitHub also provides help with SSH-related
issues at <https://help.github.com/categories/ssh/>.

Some users will already have an SSH keypair on their computer. The two files are
generally located in `<userhome>/.ssh/` and will be named
`id_rsa` for the private key and `id_rsa.pub`
for the public key. It is possible to use this pair, but you may want to
generate a separate pair for use with Software Risk Manager.

Once you have located or generated a keypair, copy the contents of the private
key file into the Private Key field.

[image: image]

When generating a keypair, you have the option to provide a passphrase for the
private key. If you do this, Software Risk Manager will need that passphrase to
use your private key. Enter it in the Key Passphrase field.

### OAuth Client Credentials

OAuth client credentials use the OAuth 2.0 *client credentials grant* flow to
authenticate with a repository host. Instead of a personal username and password,
you provide a **Client ID**, **Client Secret**, and your authorization server's
**Token URL**. Software Risk Manager will automatically fetch an access token from
that endpoint and use it to access the repository, refreshing it automatically once
it expires.

This authentication method is well-suited for service-to-service integrations where
no individual user account is involved. It is supported by several Git hosting
platforms, including Bitbucket and GitLab, when OAuth applications are configured
at the organization or project level.

[image: image]

If Software Risk Manager recognizes the configured repository URL, it may
pre-populate the Token URL field with a suggested value for that host. This
field is always editable; if your authorization server uses a different endpoint,
you can replace the pre-filled value with the correct URL before saving.

### Two-Factor Authentication with GitHub

If you need to connect to a GitHub repository, and your GitHub account has
two-factor authentication set up, you cannot use your regular username and
password to authenticate. To connect over HTTP (e.g.,
`https://github.com/user/repo`), you will have to set up a
Personal Access Token and use it in place of your regular password. You can
still connect over SSH (e.g., `git@github.com:user/repo.git`) as
usual.
