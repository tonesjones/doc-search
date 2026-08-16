---
title: "Managing triage stores"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-triage-stores.html"
content_id: "Ys9G6C0xP7gxARZklyaQCg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:50:21.757163+00:00"
---

# Managing triage stores

A triage store is a repository for the current and historical triage values of CIDs. The state of triage values
for a CID changes when a user triages a CID, for example, by changing its classification
from Unclassified to Bug.

In Coverity Connect, each stream must be associated with a single triage store so that
users can triage issues (instances of CIDs) found in the streams. You can use one triage
store for all Coverity Connect streams, or you can associate streams with separate
triage stores. When streams are associated with the same triage store, any instances of
a CID that are found in the streams will share the same triage values, regardless of the
project to which the streams belong.

Triage store configuration and management takes place through the Triage
Stores menu.

Figure 1. Example: Triage Stores menu
  
 [image: image]

Figure 1 shows a Default
Triage Store configuration.

Note: The Triage Stores menu is viewable but not editable on
Coverity Connect Subscribers. Subscribers are instances of Coverity Connect that
share their triage values through one or more triage stores that are set up in a
Coordinator instance. For details, see Synchronizing multiple Coverity Connect instances.

The Coordinator
instance of Coverity Connect can only manage streams that are local to the
Coordinator. For example, it is not possible to use the Coordinator instance to
associate a stream from a Subscriber instance with a triage store. Instead, an
administrator would need to use the Projects &
Streams menu on the Subscriber for this purpose. The Coverity
Connect Web Services API also supports this functionality (see the Coverity Platform 2026.6.0 SOAP Web Services API Reference).

The Triage Store menu supports the following actions:

- Adding a triage store:
  :   Creates a triage store. The new store does not contain any triage
      values, triage history, or stream associations. Note that if you
      associate a stream with a newly created triage store, any CIDs found
      in the stream will acquire the default
      triage values.

      For required permissions, see Assigning
      roles. A user who adds a triage store becomes the
      Triage Store Owner of the new triage
      store. The new store does not have any other role associations.

      The Add button supports this
      functionality.
- Associating one or more streams with a triage store:
  :   Assigns the triage values that are stored in a triage store to CIDs
      in the associated stream (or streams). Note that these CIDs will not
      retain triage data from any triage store with which their stream was
      previously associated. If a CID has not been triaged in a triage
      store with which a stream is associated, the CID will receive the
      default triage values. For example, assume the following
      scenario:

      **Scenario 1: Triage Stores**

      - Stream A is currently associated with TS1, and Stream A
        contains an instance of CID 123 and CID 456, both with a
        classification of Pending in
        TS1.
      - The instances of CID 123 in streams currently associated with
        TS2 are classified as Bug. CID 456
        has never been triaged in TS2.

      In this case, if you change the association of Stream A from TS1 to
      TS2, the classification of CID 123 in Stream A will change from
      Pending to Bug.
      However, the classification of CID 456 will be
      Unclassified, the default triage value
      for the Classification issue attribute.

      If you disassociate a stream from a triage store, the store will
      retain the triage values for CIDs in that stream.

      For required permissions, see Assigning
      roles.

      The Streams tab supports this
      functionality.

      Note: Stream links are associated with a triage store
      through the streams that they reference, so stream links share
      the same triage data as the streams they reference. For this
      reason, stream links are not listed in the Triage
      Stores menu. Triaging a CID in a project that,
      for example, contains only a stream link will update the triage
      store with which the referenced stream is associated.

      For
      additional information about the relationship of stream
      links to projects, see Primary projects and stream links.
- Deleting a triage store:
  :   Removes a triage store from Coverity Connect along with all its
      triage data and role associations. Note that you cannot delete the
      Default Triage Store or a triage store
      that has streams associated with it. If you need to delete a triage
      store, you must first associate its streams with another triage
      store.

      For required permissions, see Assigning
      roles.

      The Delete button supports this
      functionality.

      Note that if you delete a triage store on a Coordinator instance of
      Coverity Connect when streams from a Subscriber instance are
      associated with the store, Coverity Connect will associate the
      streams from the Subscriber instance with the Empty Triage
      Store.
- Exporting a triage store:
  :   The Export button creates a JSON file with all
      relevant triage data from the selected triage store. All triage
      history and attribute information, including any custom attributes,
      is included in the exported file.

      See Exported triage store JSON elements for details
      on the exported JSON elements.
- Importing a triage store:
  :   The Import button accepts a JSON triage data
      file and uses it to create a new triage store. Exported triage store JSON elements contains
      information on the various triage store JSON elements.

      There are several important considerations for formatting the import
      file:
      - In general, if a triage data file does not specify a
        value for a particular field, it will be given the
        default value (e.g. owner will be
        "unassigned").
      - Validation of imported triage data will only succeed when
        all the referenced data, such as users and custom triage
        attributes, are already available on the target Coverity
        Connect instance.
      - Importing the JSON triage data file creates a new triage
        store, it does not overwrite an existing one.
      - Import is not available to subscriber instances of
        Coverity Connect. Coordinators may import triage stores,
        which will be reflected on subscriber
        instances.
      - The importing of triage data will create Merged Defects
        (identified by their merge key value) if they do not yet
        exist on the target Coverity Connect instance. If a CID
        is specified, the merged defect will be assigned that
        CID value.

        This can cause collision errors in the following
        scenarios:
        1. The merged defect already exists on the
           target Coverity Connect instance, but has a CID
           value that differs from the imported triage
           data.
        2. The merged defect does not yet exist on the
           target Coverity Connect instance, but its
           specified CID value is already used by an existing
           defect.In the event of a collision, the error will be
        flagged, and the user should edit the import file to
        remove or modify the offending CID value.
- Assigning roles:
  :   Allows you to assign to users or groups one or more roles that have
      permissions to a triage store (or to other features in the UI).

      To add a triage
      store, a user or group requires the Create Triage
      Stores permission. The System
      Admin and Project Admin roles
      have this permission by default.

      To delete triage
      stores, a user or group requires the Manage Triage
      Stores permission. The System
      Admin and Triage Store Owner
      role have this permission by default.

      To associate a stream with a triage store, a user or group
      requires the Manage Streams permission on the
      stream. The user or group also must have one of the following
      permissions to the triage store: Manage Triage
      Stores, View issues, or
      Triage issues. To discover the built-in
      roles that have these permissions by default, see Figure 1.

      To triage CIDs found in streams that are associated with a triage
      store, a user (or group to which the user belongs) requires the
      View issues and Triage
      issues permissions at the global level or at three
      separate lower levels (a triage store, a component, and a project or
      stream). By default, the User group is
      assigned the Developer role, which has this
      permission at the global level. To use the permission at lower
      levels, you might add to a triage store, component, and stream a
      user (or group) with a role that includes the Triage
      issues and View issues
      permissions. (Note that you also need to assign any additional
      permissions that the user requires to work with the stream and
      component, such as the ability to view issues and view the source.)
      For a detailed example, see Scenario: Granting triage permissions on a synchronized Coverity Connect enterprise cluster. To understand permissions and associate them with a role, see
      Roles and role-based access control.

      The Roles menu supports this
      functionality.

Coverity Connect provides two built-in triage stores.

**Built-in Triage Stores**

- Default Triage Store:
  :   Serves as a default store for new streams (though it is possible to
      associate a stream with a different store when creating or editing
      the stream). In addition, this built-in triage store cannot be
      deleted.

      If you decide that all your streams should share a single triage
      store, Coverity recommends that you use this store instead of
      creating a new one for that purpose. For details on this topic, see
      Scenario: Sharing triage data across code branches (recommended).

      For required permissions to the Default Triage
      Store, see Assigning
      roles.
- Empty Triage Store
  :   This store will be empty except in the case that it contains orphaned
      streams.

      Users cannot triage instances of CIDs contained in streams that are
      associated with this store. To enable triage, you need to associate the streams with another triage store. This is
      the only operation you can perform with the Empty Triage
      Store.

      Coverity Connect associates streams with this store under the
      following conditions:

      - When creating a stream, if a user or administrator does not
        have permission to any triage stores. In other words, the
        user is not assigned a role that has the Manage
        Triage Stores, View
        issues, or Triage
        issues permission on *any* triage
        store.
      - After deleting a triage store on a Coordinator instance when
        streams from a Subscriber instance are associated with the
        store. Coverity Connect will associate the streams from the
        Subscriber instance with the Empty Triage
        Store.

**Triage scope.** When a user triages a CID in a project, the update
applies by default to all triage stores that are associated with streams (in the
project) that contain that CID. However, it is possible for users to perform triage on
select triage stores.

**User-set attributes for CIDs:**

- Classification attribute (default value:
  Unclassified)
- Severity attribute (default value:
  Unspecified)
- Action attribute (default value:
  Undecided)
- Fix Target attribute (default value:
  Untargeted). This built-in attribute is hidden from
  the Triage pane by default.
- Ext. Reference attribute (default value: an empty
  field)
- Owner attribute (default value:
  Unassigned)
- Comment attribute (default value: an empty field)
- Custom issue attributes

For more information about issue attributes and values, see Triage attributes.

Note: Users *do not* set the Status of a CID
(New, Triaged,
Dismissed, or Fixed), which is set
by Coverity Connect.
