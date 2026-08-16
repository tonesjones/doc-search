---
title: "Reviewing defects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/reviewing-defects.html"
content_id: "MCYf~LJRBDbDbPPCgmCMgQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:46.331663+00:00"
---

# Reviewing defects

Once `cov-run-desktop` has completed, the console will display the
standard output, which will consist of a completion message followed by a list of all
defects found. For example, see the code below, which contains two defects:

```
int nullBug(int *p)
{
  if (p != NULL) {
    // ...
  }
  // ...
  return *p;              // oops, 'p' might be NULL here
}
  
int compareBug(char const *a, char const *b)
{
  if (strcmp == 0) {      // oops, forgot to actually call 'strcmp'
    return 1;
  }
  else {
    return 0;
  }
}
```

When run on this code sample, `cov-run-desktop` will return the
following console output:

```
Detected 2 defect occurrences that pass the filter criteria.

test.c:7: CID 10029 (#1 of 1):
  Type: Dereference after null check (FORWARD_NULL)
  Classification: Unclassified
  Severity: Unspecified
  Action: Undecided
  Owner: admin
  Defect only exists locally.
test.c:3:
  1. path: Condition "p != NULL", taking false branch
test.c:3:
  2. var_compare_op: Comparing "p" to null implies that "p" might be null.
test.c:7:
  3. var_deref_op: Dereferencing null pointer "p".

test.c:12: CID 10028 (#1 of 1):
  Type: Function address comparison (BAD_COMPARE)
  Classification: Unclassified
  Severity: Unspecified
  Action: Undecided
  Owner: admin
  Defect only exists locally.
test.c:12:
  func_conv: This implicit conversion to a function pointer is suspicious: "strcmp == NULL".
test.c:12:
  remediation: Did you intend to call "strcmp"?

cov-run-desktop took 12.4 seconds.
```

As the first line indicates, this output shows
two defect occurrences (separated by a blank line), and a final message which says how
long `cov-run-desktop` took to run - in this case, 12.4 seconds. The illustration below provides detail on the output for an
individual defect occurrence.

Figure 1. Defect output explained
[image: image]

For additional information about checkers, and the defects they produce, see the Coverity 2026.6.0 Checker Reference.
