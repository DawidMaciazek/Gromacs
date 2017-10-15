import numpy as np
import pandas as pd
from collections import defaultdict
# 1 read mol

bond_radius = defaultdict(lambda: 1.1)

def read_xyz(name):
    df = pd.read_csv(name, skiprows=2, header=None, delimiter=r"\s+")
    h_selection = df.iloc[:, 0] == "H"
    h = df[h_selection]
    el = df[~h_selection]

    return h, el

def sort_h(h, el):
    h_coords = np.array(h.iloc[:,1:].as_matrix(), dtype=float)
    final_list = []

    for index, row in el.iterrows():
        el_name = row[0]

        el_coord = np.array(row[1:].as_matrix(), dtype=float)
        r = bond_radius[el_name]

        h_bond_len = np.linalg.norm(h_coords - el_coord, axis=1)
        h_bond_list = h_bond_len < r

        el_line = "{} {} {} {}".format(el_name, *list(map(str, el_coord)))
        final_list.append(el_line)

        for h_single in h_coords[h_bond_list]:
            h_line = "H {} {} {}".format(*list(map(str, h_single)))
            final_list.append(h_line)

        h_coords = h_coords[np.logical_not(h_bond_list)]
    print("Left over size: {}".format(len(h_coords)))
    return final_list

def write_xyz(name, atom_list):
    atoms = len(atom_list)
    out = open(name, 'w')
    out.write("{}\nSorted xyz\n".format(atoms))
    out.write("\n".join(atom_list))

name = "10mer.xyz"
h, el = read_xyz(name)
atom_list = sort_h(h, el)
write_xyz("10mer.xyz", atom_list)

