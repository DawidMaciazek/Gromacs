import sys

def read_xyz(iname):
    infile = open(iname)
    atom_number = int(infile.readline())
    infile.readline()

    atoms = []
    for i in range(atom_number):
        line = infile.readline()
        sp = line.split()
        atoms.append([sp[0], ' '.join(sp[1:])])

    return atoms

def write_xyz(olist, oname):
    ofile = open(oname, 'w')

    atom_number = len(olist)
    ofile.write("{}\n\n".format(atom_number))

    for i in range(atom_number):
        catom = olist[i]
        ofile.write("{} {} # {} {}\n".format(catom[0], catom[1], ,catom[2], catom[3]))


mers = int(sys.argv[1])
iname = sys.argv[2]

print mers, iname

atom_list = read_xyz(iname)

# global chain mers*8-1
#

atom_main_list = atom_list[:mers*8]
atom_hyd_list = atom_list[mers*8:]

olist = []

m_cnt=0
h_cnt=0

if True: # first mer
    # main chain
    # C1
    res_name = "SMR"
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C1", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H1", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H2", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H3", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # C2
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C2", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H4", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # ----------------
    # Main residue
    res_name = "PNI"

    catom = atom_main_list[m_cnt][:]
    catom.extend(["C3", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_main_list[m_cnt][:]
    catom.extend(["O", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_main_list[m_cnt][:]
    catom.extend(["N", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["HN", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # end  Metan

    catom = atom_main_list[m_cnt][:]
    catom.extend(["C4", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H1", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # met 1
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C5", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H2", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H3", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H4", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # met 2
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C6", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H5", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H6", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H7", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)


for i in range(mers-2):
    # main chain
    # C1
    res_name = "MMR"
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C1", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H1", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H2", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # C2
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C2", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H4", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # ----------------
    # Main residue
    res_name = "PNI"

    catom = atom_main_list[m_cnt][:]
    catom.extend(["C3", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_main_list[m_cnt][:]
    catom.extend(["O", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_main_list[m_cnt][:]
    catom.extend(["N", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["HN", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # end  Metan

    catom = atom_main_list[m_cnt][:]
    catom.extend(["C4", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H1", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # met 1
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C5", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H2", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H3", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H4", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # met 2
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C6", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H5", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H6", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H7", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)


if True: # ending mer
    # main chain
    # C1
    res_name = "EMR"
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C1", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H1", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H2", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # C2
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C2", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H3", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H4", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # ----------------
    # Main residue
    res_name = "PNI"

    catom = atom_main_list[m_cnt][:]
    catom.extend(["C3", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_main_list[m_cnt][:]
    catom.extend(["O", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_main_list[m_cnt][:]
    catom.extend(["N", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["HN", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # end  Metan

    catom = atom_main_list[m_cnt][:]
    catom.extend(["C4", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H1", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # met 1
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C5", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H2", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H3", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H4", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    # met 2
    catom = atom_main_list[m_cnt][:]
    catom.extend(["C6", res_name])
    m_cnt = m_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H5", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H6", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)

    catom = atom_hyd_list[h_cnt][:]
    catom.extend(["H7", res_name])
    h_cnt = h_cnt + 1
    olist.append(catom)



print olist
write_xyz(olist, "out.xyz")
