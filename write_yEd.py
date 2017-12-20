#Author: Bukhsh
#Date: 20th December, 2017
#This script write a tgf file that can be opened in the graphhing package yEd.

filename = 'testcases/case2736sp.m'
with open(filename) as f:
    content = f.readlines()
flag_bus = 0 #flag down for bus data
flag_branch = 0
buses = []
branches = []
for line in content:
    if '];' in line:
        flag_bus    = 0 #flag down if end of bus is reached
        flag_branch = 0 #flag down if end of bus is reached
    if (flag_bus==1):
        buses.append(line.split()[0])
    if (flag_branch==1):
        branches.append(line.split()[0:2])
    if ('mpc.bus' in line) and ('name' not in line):
        flag_bus = 1 #flag up
    if 'mpc.branch' in line:
        flag_branch = 1 #flag up

fileyEd = 'yEdFiles/' + filename.split('/')[-1].split('.')[0]+'.tgf'
out = open(fileyEd,'w')
for i in buses:
    out.write(i+' '+i+'\n')
out.write('#\n')
for i in branches:
    out.write(i[0]+' '+i[1]+'\n')

out.close()
