---
title: "Synchronizing multiple Coverity Connect instances"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/synchronizing-multiple-coverity-connect-instances.html"
content_id: "bVTei088MH3le2PGUcmbjw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:39.089973+00:00"
---

# Synchronizing multiple Coverity Connect instances

Coverity Connect Coordination allows you to deploy clusters of Coverity Connect instances
on which centrally managed data is synchronized. Importantly, developer-set triage data
can be updated automatically across the cluster. For Coverity Connect to synchronize
data, it is necessary to set up one instance of Coverity Connect as the central
Coordinator and to configure other Coverity Connect instances into a cluster of
Subscribers with which the Coordinator can communicate.

## Coordinator responsibilities

The following functionality (available through the
Configuration menu) is viewable but not configurable on
the Subscribers so that the Coordinator can manage it centrally:

- Configuration - Users & Groups: All users in
  the cluster are set up and managed in the Coordinator. Note that the
  triage options available to developers include the
  Owner attribute, which is populated by a
  comprehensive list of all users in the cluster. All users that are
  managed by the Coordinator belong to at least one group, so all groups
  in the cluster are also created and managed in the Coordinator. See
  Managing users and Managing groups
  for details.

  For LDAP settings, also use System -
  Configuration on the Coordinator. Note that Subscribers
  cannot modify LDAP configurations in the System configuration. You must
  contact the Coordinator to make changes.
- Configuration - Roles: RBAC permissions and roles
  are configured on the Coordinator. However, roles for projects and
  streams can be applied on each Subscriber through the
  Projects & Streams menu item. See Roles and role-based access control for details.
- Configuration - Triage Stores: One or more Triage
  Stores in the Coordinator support the developer-set triage data that gets synchronized across the
  cluster. When you set up a stream in a Subscriber, you select from a
  list of these Triage Stores. See Managing triage stores
  for details.
- Configuration - Component Maps: All component maps
  and components are managed through the Coordinator. See Using components for details.
- Configuration - Attributes: The custom attributes
  and attribute values that are available to each Coverity Connect
  instance in the cluster are set up and managed in the Coordinator. When
  a developer who is triaging an issue changes an attribute value for an
  issue, that change gets propagated through the cluster. See Configuring triage attributes for details.
- Configuration - System features: The Coordinator
  supports Issue Categorization and LDAP
  Configuration (if you are using LDAP). See Configuring custom issue categories and Integrating with LDAP servers for details.
- Configuration - System - Automatic Owner
  Assignment: The Coordinator controls
  Automatic Owner Assignment. See Configuring automatic owner assignment.

## Locally configured coordinator and subscriber features

Important: For information on installing and
configuring Connect coordinator-subscriber in a Coverity cloud deployment, refer to
Coverity 2026.6.0 Cloud Deployment Administrator and User Guide. Thee procedures
in this section do not apply.

- System - Projects & Streams: You set up and manage
  separate sets of projects and streams locally. Note that sharing projects
  and streams on both the Coordinator and a Subscriber is not a supported use
  case. See Working with projects and streams for
  details.

  Each stream is associated with a Triage Store that is set up on the
  Coordinator. You create this association through the
  Configuration - Projects & Streams on each
  Coverity Connect instance. For guidance, see Editing projects and streams.
- A Coordinator server can optionally be configured to use single sign-on with
  SAML. See Configuring Coverity Connect to use SAML.

If possible, the coordinator instance should act solely as coordinator, and have no
projects, streams, or snapshots configured. This will ensure that no individual
project or stream information is lost in the event of failure.

Note: Local configuration outside the scope of the Coordinator/Subscriber model:

Local
System - Configuration features: *Except when
setting up* 
Issue Categorization and LDAP
Configuration, you perform system configuration locally. See
Configuring and managing the Coverity Connect server.

Configuration - Hierarchies: This page is
accessible only if your license covers Coverity Policy Manager. See Coverity Policy Manager administration

Important: The Subscriber Coverity Connect servers must be the same or
previous release as the Coordinator server. For example, if the Coordinator is
version 8.0, the Subscriber servers may be version 8.0 or 7.7.

## To set up Coverity Connect coordination:

Important: For information on installing and
configuring Connect coordinator-subscriber in a Coverity cloud deployment, refer to
Coverity 2026.6.0 Cloud Deployment Administrator and User Guide. The procedures in this section do not
apply.

1. Take time to understand the synchronization process.

   Review Synchronizing data across the cluster
2. Set up shared features.

   For guidance, see Coordinator Responsibilities.
3. Configure synchronization properties.

   For guidance, see Configuring data synchronization across the cluster.

Note: If the Coverity Connect coordinator goes down, it will synchronize data on the
subscribers once it becomes available again. During the time the coordinator is
down, new issues that are committed to a subscriber are marked as
Pending in the subscriber UI. Such issues will receive a
CID after the coordinator becomes available again.

If one of the Coverity Connect
subscribers in the cluster becomes unavailable (for example, due to a network
failure), the coordinator will update that instance once it becomes available
again. The coordinator will also receive the latest configuration settings and
triage values for the instance that was down once that instance becomes
available again. After receiving the updated data, the coordinator will
propagate it to the other subscribers, as needed.
