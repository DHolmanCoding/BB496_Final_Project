"""
Get PDB_IDs for FXR and write them to a file.
"""

import urllib2

url = 'http://www.rcsb.org/pdb/rest/search'

queryText = """
<?xml version="1.0" encoding="UTF-8"?>
<orgPdbQuery>
<version>B0907</version>
<queryType>org.pdb.query.simple.AdvancedKeywordQuery</queryType>
<description>Text Search for: FXR</description>
<keywords>FXR</keywords>
</orgPdbQuery>
"""

print "query:\n", queryText
print "querying PDB...\n"
query = urllib2.Request(url, data=queryText)
pdb_id = urllib2.urlopen(query)

## get a list of all the PDB IDs and store it under results
results = pdb_id.read().split('\n')[:-1]

# # # print type(results)
# # # print results

## generate a text file with all the protein ids (this is a dummy file with FXR) 
## We are only going to take the first 25 pdb_ids due to computing costs
with open('pdb_ids.txt', 'w') as f:
    for pdbid in results[:25]:
        f.write(pdbid + '\n')

print "Done getting pdb ids."


