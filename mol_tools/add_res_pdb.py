import sys
import os
import re

if os.path.isfile(sys.argv[2]):
    print("Output file already exist! Skipping")
    sys.exit(1)


ifile = open(sys.argv[1], 'r')
res_str = sys.argv[2]
# build res_array
#

res_array = []
ofile = open(sys.argv[3], 'w')
res_num = re.split("[a-zA-Z]", res_str)
res_num = [ a for a in res_num if a ]
res_name = re.split("\d", res_str)
res_name = [ a for a in res_name if a ]

if len(res_num) != len(res_name):
    print("Res string invalid!")
    sys.exit(1)

res_list = []
for name, num in zip(res_name, res_num):
    for i in range(int(num)):
        res_list.append(name)

line = ifile.readline()
ofile.write(line)
line = ifile.readline()
ofile.write(line)

cnt = 0
while True:
    line = ifile.readline()
    if line[:6] != "HETATM":
        break

    new_line = line[:17] + res_list[cnt] + line[20:]

    ofile.write(new_line)
    cnt += 1

line = ifile.readline()
while line:
    ofile.write(line)
    line = ifile.readline()
