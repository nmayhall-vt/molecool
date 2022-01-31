import numpy as np
import os
import molecool

print(molecool.canvas())

pdb_file = os.path.join('molecool','molecool','data', 'pdb', 'water.pdb')
pdb_file = os.path.join('molecool','data', 'pdb', 'water.pdb')
print(pdb_file)
symbols, coords = molecool.open_pdb(pdb_file)
print(symbols)
print(coords)

#test_atoms = ["H", "O"]
test_coords = np.array([[1,0,0],[0,0,0], [0,1,0]])
print(molecool.calculate_angle(coords[0,:], coords[1,:], coords[2,:], degrees=True))
#molecool.write_xyz("test.xyz", test_atoms, test_coords)
#print(molecool.calculate_angle([1,0,0], [0,0,0], [0,1,0], degrees=True))

