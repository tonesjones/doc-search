---
title: "Apply your default policies to your portfolio"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/apply-your-default-policies-to-your-portfolio.html"
content_id: "zFAUvf_pQmUMKCE5VneXWA"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:57:03.504194+00:00"
content_hash: "d38fe4487f5b0becd6773cfc3fa39fd345ae6c766a18d0adb154698cb8ebd767"
---

# Apply your default policies to your portfolio

As an Organization Admin, you can reset policy inheritance throughout your portfolio. This allows you to apply your organization's default policies to applications, projects, and branches, and reset any custom policy assignments.

Follow these steps when you want to push your organization's default policies to applications, projects, or branches that are currently in the Modified state. After resetting, those levels return to the Inherited state and will receive future policy updates automatically.

CAUTION:

Resetting inheritance cannot be undone. Any custom policy assignments at the selected levels will be replaced with your organization's default policies.

1. Go to My Organization > Policies.
2. Select Reset Inheritance next to the type of policy you wish to apply throughout your portfolio.

   The Reset inheritance window opens.
3. Use the checkboxes to select which levels to reset. Options include:
   - Applications
   - Projects
   - Branches

   The number of applications, projects, or branches that will be affected appears below each checkbox you select.
4. Select Reset Inheritance.

   A notification appears, and Polaris starts updating policy assignments. Depending on the size of your portfolio, this can take some time.

   Important: This action is not tracked in audit logs, and does not generate a notification when updates are complete.
5. (Optional) Repeat these steps to reset inheritance for other types of policies, as required.
