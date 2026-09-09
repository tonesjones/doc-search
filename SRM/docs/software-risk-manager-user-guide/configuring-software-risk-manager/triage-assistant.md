---
title: "Triage Assistant"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/triage-assistant.html"
content_id: "YWSVQ0TFl4ZX7gfE0VGcCg"
version: "latest"
section: "Software Risk Manager User Guide"
scraped_at: "2026-09-08T20:02:58.310422+00:00"
content_hash: "5a310c96e025d5081bd87f442bdd6547d8d19b8480b6920a2b18c34ca2efc627"
---

# Triage Assistant

If machine learning is enabled, Software Risk Manager is capable of automatically
(re)training a prediction model so that it does not have to be done manually. The ML
Service Management section will automatically transition from an *Idle* state to a
*Working* state when Software Risk Manager automatically initiates a training
session. Whether automatic updates of the prediction model occur at all, and the time at
which they occur, are configurable through the SRM props file (see the Install Guide for more information.)

Click the Settings icon in the navigation bar and select Machine Learning (ML) Control
Panel from the top menu to open the Machine Learning Control Panel page.

[image: image]

There are two parts to the Machine Learning Control Panel:

- **Configure Machine Learning for Predicted Status.** This part involves
  switching on the service management and retraining the prediction model.
- **Identify projects that may be outliers for the predicted status.** This
  part involves adding exclusions.

## Configuring Machine Learning for Predicted Status

Machine learning configuration allows admins to manually trigger the training of the
prediction model. To make use of machine learning, Software Risk Manager requires
that at least 100 findings have been actively triaged. These triaged finding can
come from multiple projects. If you have not met this requirement, then you will be
presented with a statement detailing how many findings you have actively triaged and
a statement detailing the minimum requirements.

The ML Service Management section of the control panel transitions back and forth
between two states. The first is an *Idle* state, which means that Software
Risk Manager is not currently training a prediction model. The second is a
*Working* state, which means that Software Risk Manager is currently
training a prediction model. If the section is in an *Idle* state, then either
a Build Prediction Model button or an Update Prediction Model button will be
present. Specifically, the Build Prediction Model button will be present if a
prediction model has not been trained, and the Update Prediction Model button will
be present if a prediction model has been trained.

[image: image]

When ML Service Management is off, Software Risk Manager will begin training a
prediction model when the Retrain Prediction Model button is clicked. This will
transition the section into a *On* state.

Once training has completed, the section will transition back to an *Idle* state
and will present the user with when the last training session completed, how long it
took, and whether or not it succeeded.

## Managing Exclusions

The Excluded Projects section allows admins to configure which projects should not be
considered when Software Risk Manager trains a prediction model. All excluded
projects are listed.

### Viewing Existing Exclusions

**To view an existing exclusion:**

1. Click the Settings icon in the navigation bar and select Machine
   Learning (ML) Control Panel from the top menu.

   [image: image]
2. Use the search field to search by name or click the column header to
   re-sort the list.

### Adding an Exclusion

Adding exclusions will exclude the selected project from prediction models that
Software Risk Manager trains.

**To add an exclusion:**

1. Click the Settings icon in the navigation bar and select Machine
   Learning (ML) Control Panel from the top menu.

   [image: image]
2. Click Add Exclusion.

   [image: image]
3. Select from the list of exclusions or use the search field to search by
   name.
4. Click Add Exclusion.

### Removing an Exclusion

You can also choose to re-include an excluded project so that it may be
considered during training by removing it.

**To remove an exclusion:**

1. Click the Settings icon in the navigation bar and select Machine
   Learning (ML) Control Panel from the top menu.

   [image: image]
2. Locate the exclusion you want to delete.

   You can use search field to
   search by name or click the column header to re-sort the list.

   [image: image]
3. Click Remove.
