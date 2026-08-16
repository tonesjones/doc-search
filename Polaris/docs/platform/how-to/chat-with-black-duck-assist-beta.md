---
title: "Chat with Black Duck Assist (Beta)"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/chat-with-black-duck-assist-beta-.html"
content_id: "YRTPA9xAReyNBIxUAmKtnQ"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-08-12T19:56:23.203680+00:00"
content_hash: "7975113520eea2ef9c2b51a6076e5f7fde0a2cac57949876f97d230ae0adca9c"
---

# Chat with Black Duck Assist (Beta)

Learn how to enable and use Black Duck Assist to gain insight into your organization's data.

## Overview

Black Duck Assist is a chat interface that communicates with a large language model (LLM) and the data in your portfolio, allowing you to ask questions about the applications, projects, branches, and vulnerabilities in your portfolio in natural language. It also leverages Polaris documentation, so responses can include product guidance and best practices.

  
 [image: ui bd assist]   

Please note:

- Black Duck Assist only has read access to the data in your portfolio, and cannot make changes for you.
- Black Duck Assist only generates responses using the data you have access to. This ensures responses to any user's conversations only include data from the applications they can access.

### Data privacy

Black Duck Assist communicates with a LLM that runs on a private cloud service. Please note:

- None of the prompts or responses exchanged between Black Duck Assist and the LLM are used to:
  - Train or improve the LLM.
  - Improve the LLM provider's other products or services.
- User-submitted feedback on responses is not sent to the LLM, but is collected by Polaris.
- Data exchanged between Black Duck Assist and the LLM is encrypted for storage and transmission.
- Documentation content used by Black Duck Assist is sourced from official Polaris product documentation.

### Accuracy and completeness

Warning:

Black Duck Assist generates results created by artificial intelligence (AI) or other automated technologies. Such results are provided for informational purposes only and should not be relied upon for any specific purpose without verification of its accuracy or completeness.

### Local storage

Polaris does not store your conversation data. Instead, conversations you create in Black Duck Assist are saved to your browser's local storage. Consequently:

- Conversations you create in one browser won't appear in other browsers.
- Saved conversations are deleted when you delete your browser's local files.

## Enable Black Duck Assist (AI Chatbot)

Black Duck Assist is disabled by default and can only be enabled by an Organization Administrator. To enable Black Duck Assist, follow these steps:

1. Go to My Organization > Black Duck Assist.
2. Select Enable AI Chatbot [Beta].

## Start a conversation

To start a conversation, follow these steps:

1. After you open Black Duck Assist, select New Chat (near the bottom of the Conversations panel).

   Tip: Show or hide the Conversations panel using the [image: bd assist show convo icon] icon near the prompt text box.
2. Start your conversation by either:
   - Selecting an example prompt.
   - Writing a prompt in the text box below the Example Prompts and pressing ENTER.

   The prompt you use is saved as the conversation title.
3. (Optional) After Black Duck Assist provides a response, you can give positive ( [image: bd assist feedback positive icon] ) or negative ( [image: bd assist feedback negative icon] ) feedback using the icons beneath the response.

   When you select a feedback icon, a window opens where you can provide comments about the response. Select Submit Feedback to save feedback.

## Delete conversations

You can delete conversations in two ways:

CAUTION:

Conversations you delete cannot be recovered.

- **Delete a specific conversation:** Select the delete [image: bd assist delete icon] icon near the title of a conversation you wish to delete. When you do, a confirmation appears. Select Delete to delete the conversation.
- **Delete all conversations:** Select Clear All (near the bottom of the Conversations panel). When you do, a confirmation appears. Select Yes, delete all to delete all conversations.

  Note: Clearing your browser's cache will also delete all conversations.
