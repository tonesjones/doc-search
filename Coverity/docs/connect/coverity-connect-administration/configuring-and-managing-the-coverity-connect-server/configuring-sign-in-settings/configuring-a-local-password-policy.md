---
title: "Configuring a local password policy"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-a-local-password-policy.html"
content_id: "NP_18w3NkXm2RQuDG6yLug"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:27.250520+00:00"
---

# Configuring a local password policy

An administrator can specify requirements for the passwords used by local Coverity Connect users.

To access the Password Policy controls, choose
Configuration > System > Authentication and Sign In > Local Password Policy.

  
 [image: image]   

These are the stipulations that can be applied to passwords:

Enable Local Password Policy
:   When on, Coverity Connect applies the stipulations on this page to new
    passwords and (optionally) to existing passwords.

    If this option *is not
    enabled,* then a soft lockout policy takes effect (see Configuring the soft lockout policy).

Minimum password length
:   Choose a value that is between 8 and 128.

    Default: 8

    Note:
    If no local password policy is active, there is still a default minimum password length of 6 characters.

Select the minimum number of each character type.
:   Choose a minimum number of each character type that the password must
    contain. This value can be between 1 and 32. The possible character types
    are uppercase, lowercase, number, and symbol.

    For example, if the minimum password length is 8 and the minimum number of
    character types is 1, then the password `Synops.1`
    meets these criteria. It contains 8 characters, and 1 character type each
    of: an uppercase letter, a lowercase letter, a number, and 1 special
    symbol.

    Default: 1

Number of unsuccessful sign in attempts allowed before the user is locked out
:   Sets the number of failed sign-in attempts to allow before the user is locked out of the
    Coverity Connect interface.

    Once this happens, unless
    password recovery is enabled, the administrator must reset the password for
    this user. See Locking and unlocking a user account for
    more information.

    Default: 3

Prompt users to update their password upon next sign in
:   When on, if an existing password does not meet the updated criteria, the next time the user
    logs in, Coverity Connect will prompt the user to update their
    password to one that does meet the new criteria.

    This is the dialog that
    prompts for a new password:

      
     [image: image]   

    **Exception:** When using the Configuration > Users & Groups panel, an administrator can assign a user a password that
    doesn't meet the criteria described in this section. The usual use for this
    feature is to set up a simple password while creating an account, in the
    expectation that the user will soon change this temporary password.

    If this option is turned off, the password policy restrictions on valid
    passwords *will not be applied* to users who existed before the
    password policy was enabled.
