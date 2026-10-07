---
title: "Communication with Black Duck services"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/communication-with-black-duck-services.html"
content_id: "HduYuIV76HlaU91skcwFJw"
version: "2026.7"
section: "Architecture and Network Communications"
scraped_at: "2026-10-04T23:32:21.848088+00:00"
content_hash: "b736740bc7fecd487af786f279dd2dae1d1fb5abd89caad6fe0cd7245d0d2122"
---

# Communication with Black Duck services

Black Duck interacts purely as a client of the servers hosted by Black Duck at secure data centers. Black Duck understands that Black Duck is being used in conjunction with our customer's valuable software intellectual property and treats the Internet-based communications between a customer installation of our products and the data center servers with due care, ensuring that no scanned code or proprietary customer data ever leaves the customer's premises.

All information sent to the customer's Black Duck SCA servers is treated as confidential information by Black Duck in accordance with our customer agreements. By default, all communication with Black Duck servers is done via HTTPS. More specifically, all data being transmitted is encrypted with TLS 1.3 (or TLS 1.2 if the client does not support TLS1.3). Customer sites always initiate connections with Black Duck SCA services; the hosted Black Duck SCA services never call out to the Black Duck application. The customer's Black Duck servers contain the HTTPS certificate, the Black Duck application initiates all connection requests using the certificate’s public key.

The information that is sent to the KB web services is for retrieving other information needed by the Black Duck application, for example, open-source metadata. Black Duck SCA does not retain any sensitive customer application data on its servers. Customer data is used by the KB matching service and retained on the server only during this ephemeral matching process. Once completed all customer data, including filenames, is deleted. No data is retained whatsoever.

More details on the specific communications between a customer site installation of Black Duck and the Black Duck services are included below:

- Registration service
- KnowledgeBase service
- Black Duck Hosted customer instances monitors
- SCA scan service
