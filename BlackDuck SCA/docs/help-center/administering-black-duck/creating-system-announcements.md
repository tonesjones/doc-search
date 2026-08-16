---
title: "Creating system announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/creating-system-announcements.html"
content_id: "XlqPhLFm9FWWq~DHR2E_JA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:31:25.997276+00:00"
---

# Creating system announcements

System Administrators can create custom announcements or messages to be displayed in a variety
of locations in Black Duck.

For example, use system announcements to tell your users about upcoming events or if you
need to show a disclaimer indicating what happens for unauthorized use.

There are four types of messages that you can create:

- Login. A message that appears to the user when they are logging in to Black
  Duck.

  Since this message appears for all users – including unauthenticated users –
  Black Duck recommends that you do not use this type of system announcement to
  display sensitive information.
- Banner. A message that appears at the top of every page.
- Footer. A message that appears in the footer of every page.

    
   [image: Footer Announcement]
- Welcome. A message that appears after the user logs in to Black Duck.

  Unlike other announcements, you can provide an option so that users can suppress
  this message: users will not see this message again unless you edit the
  message.

Note that you can only create one announcement of each type.

To create a system announcement:

1. Log in to Black Duck with the System Administrator role.
2. Click [image: Administration icon] .
3. Select **Announcements** to display the **Announcements** page.

     
    [image: Login Announcement Page]
4. Select the type of announcement.
5. Enter a title for this announcement.
6. Enter the announcement text. If not selected, click **Edit** and enter the
   text. Click **Preview** to view your announcement as it will appear to your
   users.

   You must use markdown language when creating the announcement. See the next
   section for more information.
7. For the Welcome announcement, select whether the user can suppress the
   announcement.

   If you select to suppress the announcement, the user will see the following
   option ("Don't show this again") in the announcement. However, the announcement
   will reappear to the user if you make any changes to the announcement.
8. Optionally, enter the start and end date for this announcement. By default the
   start date is today, with no end date, indicating a persistent announcement.
   Dates are inclusive: the announcement will appear for the date range you select
   here, including the start and end dates.
9. Select whether to enable the message. Once enabled, the announcement will appear
   to users once you click **Save**.
10. Click **Save**.

## Markdown language

You must use markdown language when creating the announcement.

Click [here](https://www.markdownguide.org/basic-syntax/) for more information on the syntax for markdown
language.

The following is the list of allowable tags for system announcements:

- h1, h2, h3, h4, h5, h6

  Note that h1 and h2 tags are converted to h3 tags.
- blockquote
- p
- a
- ul
- ol
- nl
- li
- b
- i
- strong
- em
- strike
- abbr
- code
- hr
- b
- table
- thead
- caption
- tbody
- tr
- th
- td
- pre
- iframe
- Anchor tags <a> are only allowed with the following attributes:
  - href
  - name
  - target

Note that images are not allowed.
