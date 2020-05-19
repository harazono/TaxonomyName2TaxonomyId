# TaxonomyName2TaxonomyId
## requirement
- pprint
- argparse
- requests
- json
- openpyxl
- xml
You can install these packages with pip3

## usage
`python3 TaxonomyName2TaxonomyId.py sampleInput.txt`
sampleInput.txt contains taxonomy names(one name in a line).
Results are displayed as follows:
```
🍵TaxonomyName2TaxonomyId$ ./TaxonomyName2TaxonomyId.py sampleInput.txt 
Ailuropoda melanoleuca&9646||
Anas platyrhynchos&8839||
Bos taurus&9913||
Bubalus bubalis&89462||
Canis familiaris&9615||
Capra hircus&9925||
Equus caballus&9796||
Equus ferus&1114792||
Gallus gallus&9031||
Ovis aries&9940||
Sus scrofa&9823||
Macaca mulatta&9544||
Oryctolagus cuniculus&9986
🍵TaxonomyName2TaxonomyId$ 
```
Taxonomy name and taxonomy id is conbined with `&` and taxonomies are conbined with `||\n`
