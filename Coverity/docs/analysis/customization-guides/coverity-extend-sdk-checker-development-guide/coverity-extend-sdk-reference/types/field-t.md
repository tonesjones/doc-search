---
title: "field_t"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/field_t.html"
content_id: "RFWwYHrXvEImjaZTg~sBDQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T23:39:57.892044+00:00"
---

# field_t

This class represents a member of a union.

- `string name` — The name of the member.
- `type_t type` — The type of the member.
- `bool is_bit_field` — Determine if the field is a bit field.
- `bool is_anonymous_bit_field` — Determine if the field is an
  anonymous bit field.
- `defined_class_type_t get_owner_class` — Retrieve the owner
  class as `defined_class_type_t`.
- `class_type_t *owner_class` — Retrieve the type as
  `member_type_t`.
- `unsigned get_offset` — Retrieve the offset, in bytes, from
  the beginning of the object.
- `unsigned char get_bit_offset` — If a bit field, this is the
  non-byte offset (0 otherwise). The bit field's bit offset is therefore
  `get_offset() * 8 + get_bit_offset()`.
- `bool is_signed_bitfield` — True if the type of a bitfield is
  explicitly signed, For example, `signed int`.
- `bool is_mutable` — Determine if this is a mutable field
  (mutable keyword).
