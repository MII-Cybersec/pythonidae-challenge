## Challenge 03

Given a `CSV (Comma-Separated Value)` file. 

Read the file and parse the entries to a list of entries. Each entry should be represented in a primitive data structure (list/tuple/dictionary).

Note: handle empty field carefully.

## Test

Use the CSV file [sample-02a.csv](resources/sample-02a.csv).

This file has 6 entries (6 lines), each has 3 fields. One of possible result would be:

```
result = [
    ("Jackson", "Thompson", "jackson.thompson@hotmail.com"), 
    ("Luke", "Wallace", "luke.wallace@lycos.com"), 
    ("David", "Wright", "david.wright@hotmail.com"), 
    ("Nathaniel", "Butler", "nathaniel.butler@aol.com"), 
    ("Noah", "Simpson", "noah.simpson@hotmail.com"), 
    ("Eli", "Mitchell", "eli.mitchell@aol.com"), 
]
```

To test handling empty field, use the CSV file [sample-02b.csv](resources/sample-02b.csv).

This file has 6 entries (6 lines), each has 3 fields. One of possible result would be:

```
result = [
    ("Jackson", "Thompson", "jackson.thompson@hotmail.com"), 
    ("Luke", "Wallace", "luke.wallace@lycos.com"), 
    ("David", "", "david.wright@hotmail.com"), 
    ("Nathaniel", "Butler", "nathaniel.butler@aol.com"), 
    ("Noah", "Simpson", "noah.simpson@hotmail.com"), 
    ("Eli", "", "eli.mitchell@aol.com"), 
]
```

## Remarks

CSV or Comma-Separated Value is common simple structured file which laid data in form of table. In some cases semicolon is used instead of comma to separate the values.

CSV is commonly used to hold data, either a report generated from system or as input. Malicious content can be crafted and injected to CSV and in vulnerable system will get the payload executed.