"""
Get PDB files for each of the PDB_IDs read from a file named 'pdb_ids.txt'.
"""

import urllib2

pdb_id_list = []
with open('pdb_ids.txt') as f:
    for pdb_id in f:
        pdb_id_list.append(pdb_id.strip('\n'))

for pdb_id in pdb_id_list:
    url = 'https://files.rcsb.org/download/{}.pdb'.format(pdb_id)
    pdb_file = urllib2.urlopen(url)
    with open(pdb_id + '.pdb', 'w') as coordinates:
        coordinates.write(pdb_file.read())

print "Done writing pdb files."
