---
title: "Configuring the project mapping from Coverity Connect to Bugzilla"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-the-project-mapping-from-coverity-connect-to-bugzilla.html"
content_id: "44DA6b77Ilf54pV8pJAKBw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:21.061936+00:00"
---

# Configuring the project mapping from Coverity Connect to Bugzilla

The data that is exported to Bugzilla is defined by a project mapping. A project mapping
specifies how the values of certain fields in a specific Coverity Connect project are
exported to a specified Bugzilla product. One or more project mappings are defined in a
JSON configuration file. To set up the bug tracking system integration, the Coverity
Connect administrator exports a JSON file from Coverity Connect and modifies it as
needed, and then imports the file. The example shows the required fields.

```
{
     // File type and format identifier. These fields are required
     // and must exactly match the values shown here.
     "type": "Coverity Connect BTS configuration",
     "format_version": 1,
     "variables" : {
	"defaultComp" : "Cov Test Component",
	"configMap" : {
		"CC_Other" : "Other"
		
	}
      },
     "configurations": [
       {
         // This is a user-provided name for this configuration and should
         // appear as a column in the BTS config list. Required.
         "name": "Sample Defect Export",
 
         // This is an optional textual description of the configuration.
         "description": "This configures exports defects from the testVA project.",
 
         // This is the set of Coverity Connect projects for which this
         // configuration applies.  When a bug is exported, we look at the
         // currently selected project, and this configuration applies when
         // the current project is in this list.  If multiple configurations
         // list the same project, the last one in the JSON file wins.
         "applies_to_projects": [
               "i18n","sample-ces","race"
         ],
 
         // This specifies the name of a BTS plugin to use to export the
         // defects.  It is required, although in Coverity Connect 8.0 the only allowable
         // value is "bugzilla".
         "bts_plugin": "bugzilla",
 
         // Next is a set of name/value pairs that define the contents of
         // an exported bug as a function of the attributes of the defect
         // that is being exported.  The latter are referred to using <variable> syntax.  
         // The exact set of meaningful attributes is dependent on the selected bts_plugin
         // and how the BTS itself is configured.
         // 
         "export_attributes": {
            // This specifies a mode in which we want to export a defect. It can take a value of "live" or "test". 
            // If it is in test mode, actual export does not happen. To do an actual export, it has to be in "live" mode.
            "mode" : "live",
	     // Bugzilla product that receives the defect.
            "product": "Coverity Test Product",
	      // Other BZ attributes.
            "component": "<configMap[component]|defaultComp>",
            "version": "1.0",
	     "bug_status": "<status>",
        //  "platform": "All",
	 //  "op_sys": "Linux",
	     "bug_severity": "<severity>",
	    
            "bug_file_loc": "<url>",
	      "cf_eventtag": "<eventtag>",
	      "cf_linenumber": "<linenumber>",
  	    "cf_eventdescription": "<eventdescription>",
            "bug_found_by": "PoP",
	      "cf_bug_url": "<function>",	
  	    // The bug title/ summary.
            "short_desc": "CID <cid>: <checker>",
 	     // The description field (comment 0).
            "description": "File: <file>:<linenumber> Function: <function> Checker: <checker> <eventtag>: <eventdescription> Click <url> for more details."
	   
       }
     }
   ]
 }
```

**JSON file attributes:**

`name`
:   Name of the Bugzilla product.

`description`
:   A description of the Bugzilla product.

`applies_to_projects`
:   One or more Coverity Connect projects can be mapped to one Bugzilla
    product.

    Note: A single Coverity Connect project can only be mapped to one Bugzilla
    product at a time. In case of conflict, the most recent Bugzilla product
    mapping will be used.

`bts_plugin`
:   The value must be `bugzilla`.

The following `export_attributes` values are required by Bugzilla. A
`Bugzilla Constant` is a picklist value defined in the Bugzilla
product. If this value does not match the actual value in Bugzilla, an error will occur
when exporting an issue. The actual name of fields in Bugzilla may differ from the
display name shown in the Bugzilla interface. Contact the Bugzilla administrator to
confirm the actual names. Coverity Connect templates may be used in combination with
string text in some cases.

`mode`
:   Allowable values are `test` or `live`. It
    must be set to `live` for defects to actually be
    exported.

`component`
:   `Bugzilla Constant`

`summary`
:   String text and template fields

`version`
:   `Bugzilla Constant`

`description`
:   String text and template fields

`op_sys`
:   `Bugzilla Constant`

`platform`
:   `Bugzilla Constant`

`priority`
:   `Bugzilla Constant`

`severity`
:   `Bugzilla Constant`

The Coverity Connect fields that may be exported are:

- action
- category
- checker
- cid
- classification
- comparison
- component
- cwe
- file
- firstdetected
- firstsnapshot
- firstdate
- firstdesc
- firststream
- firsttarget
- firstversion
- fixtarget
- function
- functionmerge
- impact
- lastsnapshot
- lastdate
- lastdesc
- laststream
- lasttarget
- lastversion
- lasttriaged
- legacy
- mergekey
- mergeextra
- username
- owner
- severity
- status
- type
- url
- eventtag
- eventdescription
- linenumber
