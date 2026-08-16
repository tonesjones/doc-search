---
title: "Manually adding an AI model to a BOM"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/manually-adding-an-ai-model-to-a-bom.html"
content_id: "_ymw~Hg1waQtZ8wesmVnWA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:34.158886+00:00"
---

# Manually adding an AI model to a BOM

Black Duck supports the ability to add AI models to your Bill of
Materials (BOM), allowing for comprehensive tracking and management of AI components
within your projects. This feature enables organizations to maintain visibility into the
AI models they use, monitor associated risks, and ensure compliance with relevant
policies.

This section will walk you through the process of adding AI models to your BOM,
configuring their properties, and managing them effectively within your project
ecosystem.

## Prerequisites

Before adding AI models to your BOM, ensure the following requirements are met:

- **Feature Activation**

  The AI Model Scanning feature must be enabled on your product registration
  key. If you do not see this functionality in your Black Duck instance,
  please contact your Black Duck representative or
  support team to have this feature activated for your organization.
- **User Permissions**

  To add and manage AI models in a BOM, you must have appropriate permissions,
  including:

  - Project access with editing capabilities
  - BOM Management permissions
- **Scan Configuration**

  You must have performed a Detect scan using the following parameter:

  ```
  --detect.blackduck.signature.scanner.individual.file.matching=ALL
  ```

## Adding an AI model to a BOM

Adding AI models to your Bill of Materials follows a similar workflow to manually adding
components. This streamlined process ensures consistency in your BOM
management practices.

1. **Navigate to the Project Version**

   - Access your project list from the main dashboard.
   - Select the specific project and version where you want to add the AI
     model.
2. **Access the BOM**

   - Click on the **Components** tab to view the current Bill of
     Materials.
3. **Initiate the Add Process**

   - Locate and click the **Add** button near the top of the BOM
     view.
   - From the dropdown menu, select **AI Model**.
4. **Enter AI Model Details**

   - In the dialog that appears, provide the following information:

     - **AI Model**: Enter the name of the AI model.
     - **Commit**: Specify the commit version of the AI
       model.
   - Optionally, provide additional details by expanding the **Advanced
     Attributes** section:

     - Enter the **Purpose** for adding this component.
     - Select **Modification** if you modified this component and
       optionally, enter information regarding the modification.
5. **Confirm and Save**

   - Review the entered information
   - Click "Add" or "Save" to add the AI model to your BOM
