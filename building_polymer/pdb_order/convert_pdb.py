import sys

pdbname = sys.argv[1]
xyzname = sys.argv[2]

pdbf = open(pdbname, 'r')
xyzf = open(xyzname, 'r')

ofile = open("out.pdb", 'w')

atom_num = int(xyzf.readline())
xyzf.readline()

ofile.write(pdbf.readline())
ofile.write(pdbf.readline())

for i in range(atom_num):
    xline_sp = xyzf.readline().split()
    name = xline_sp[5].ljust(3)
    res = xline_sp[6]

    pline = pdbf.readline()

    oline = pline[:13]
    oline += name
    oline += pline[16:17]
    oline += res
    oline += pline[20:]
    ofile.write(oline)

pline = pdbf.readline()

while pline:
    ofile.write(pline)
    pline = pdbf.readline()
