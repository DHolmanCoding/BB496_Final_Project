# PYMOL automated alignment

BB494 Final Coding Assignment


@ Douglas Holman

1. Set up your working directory to contain the following files:
Read_Me.txt
pdb_ids.txt (optional)
get_pdb_files.py
get_pdb_ids.py
get_rmsd_extrema 4.0.py
rmsd_b.py

2. To start things off, open PYMOL and enter the following comands into the PYMOL command line:
os.chdir(r"C:\Users\PUT_YOUR_PATH_HERE")
run rmsd_b.py

2. if you do not have a protein of interest selected, you may run get_pdb_ids.py to generate a pdb_ids.txt file

3. Once you have a pdb_ids.txt file, please run get_pdb_files.py to populate your working directory with the first 25 pdb_id .pdb files

4. Now, return to the PYMOL command line and run get_rmsd_extrema 4.0.py

5. observe the maximum and minimum rmsd and the corresponding pdb IDs that are displayed on the screen for your viewing pleasure and observe the following new files in your directory:
best.pdb
worst.pdb
best.png
worst.png
and two alignment.pdb type files corresponding to your best/worst comparison


