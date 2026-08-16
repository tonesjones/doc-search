---
title: "Searching for vulnerabilities"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/searching-for-vulnerabilities.html"
content_id: "erBrND4vir0pOzdV4YNX2Q"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:25:34.103570+00:00"
---

# Searching for vulnerabilities

You can search Black Duck for published security vulnerabilities.
Searching by vulnerability is an efficient way to:

- Identify if a new or existing security vulnerability affects a component that is
  included in your projects.
- Review the severity of the security vulnerability to determine if remediation is
  required.
- Create a custom vulnerability dashboard so that you can focus on the
  vulnerabilities that are important to you.

To search for vulnerabilities:

1. Click [image: Search icon] to open the Find page and select the **Vulnerabilities** tab.
2. Optionally, type your search term in the Search Term field.
3. Optionally, select any filters, as described in the next section, "Using search filters".

   Note that you can enter a search term only, include filters with the search term,
   or just search using filters.
4. Optionally, save this search, so
   that the results appear on the Dashboard page.

The Find page displays the vulnerabilities that meet your search criteria.

  
 [image: Vulnerability Search Results]   

You can also perform a global search by typing your search term in the Search field
located at the top of the application and pressing **Enter** or clicking [image: Search icon] . If not displayed, select the **Vulnerabilities** tab to view your results.
Note that entering a global search term initiates a new search and resets any filters
you previously selected.

## Using search filters

For each filter:

- Click [image: Expand icon] to display the filter values.
- If you select more than one type of filter, Black Duck displays items that
  match *all* values. If you select more than one value for a specific
  filter, Black Duck displays items that match either value.

  For example, if you use the remediation status filter and select new and needs review, the
  search results display all vulnerabilities that have a remediation status of
  new *or* needs review. If you select a remediation status of new and a
  security filter of high, the search results display only those
  vulnerabilities that meet have a remediation status of new *and* a high
  security level.

Use the following filters to narrow your results when searching for
vulnerabilities:

- Affecting Projects. When selected, this filter limits results to vulnerabilities found in
  your Active and LTS projects. When cleared, results include vulnerabilities
  from both your projects and the Black Duck KnowledgeBase.
- Default Remediation. Selecting this filter displays vulnerabilities that are automatically remediated.
- Exploit. Select whether a vulnerability is Exploitable or has No Known Exploit.
- First Detected. When the vulnerability first appeared in a BOM.
- Overall Score. Enter the minimum overall score value; Black Duck displays
  vulnerabilities that have this score or higher.
- Published Year. Year the vulnerability was published.
- Severity. Select from Critical, High, Medium, or Low as determined by the selected security configuration.
- Solution. Select whether a solution is available for a vulnerability.
- Source. BDSA or NVD.
- Vulnerability Tags. Select one or more vulnerability tags.

  Note: If searching for CISA Known Exploited Vulnerabilities, you must also check the Affecting
  Projects checkbox to display results.
- Workaround. Select whether a workaround is available for a vulnerability.

Attention: Filter options and tags are not all supported for KnowledgeBase
vulnerability queries and some queries are only supported for local vulnerabilities
affecting project versions (using the checkbox). This means different behavior may
be observed when using the Find page with and without the **Affecting Projects**
checkbox enabled.

## About the search results

Search results show all vulnerabilities that meet your search criteria. The following
information is shown for each vulnerability:

  
 [image: Vulnerability search results]   

- Select the vulnerability ID to view more information on the vulnerability,
  such as additional score values. You can view National Vulnerability
  Database (NVD) information by selecting the CVE number or view Black
  Duck Security Advisory (BDSA) information by selecting the BDSA
  number.
- View the number of project versions that affected by this vulnerability next
  to **Used By**.

    
   [image: Usage Text]   

  Select **Project Versions** to open the **Affected Projects** tab for
  the vulnerability which lists the project versions affected by this
  vulnerability.

    
   [image: Affected projects]
- View the overall risk score. The search results show the Temporal Score for
  BDSA vulnerabilities or the Base Score for NVD vulnerabilities and the
  associated risk level. Note that the score shown and risk level depends on
  the selected security rankings.

  Select the score to view individual scores: temporal, base, exploitability,
  and impact for BDSA; base, exploitability, and impact for NVD.
- View whether a solution, workaround, or exploit is available:
  - [image: image] indicates
    that there is a solution or workaround available for this
    vulnerability.
  - [image: Exploit icon] indicates there is an exploit for this
    vulnerability.
- For each vulnerability, the search results also show:
  - First Detected.
  - Published date.
  - Last modified date. Note that this date displays the last time the vulnerability was modified in
    the KnowledgeBase. It does not necessarily mean the vulnerability
    information was updated itself.
  - Common Weakness Enumeration (CWE) number for this security
    vulnerability.

Note: Search results are limited to a maximum of 10,000 items.

## Exporting to CSV

You can export your search results to CSV which converts the individual rows to tabular data. To do
so, click the [image: Export CSV button] button and select CSV.
