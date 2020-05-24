import re
f = open('C:\\Users\\RamuGajula\\AppData\\Local\\Programs\\Python\\Python37\\allowed_vlan.txt')

import ciscoconfparse
from ciscoconfparse import CiscoConfParse
import sys
import openpyxl
wb = openpyxl.load_workbook(r"C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
sheet = wb['6BDC-2']
device_file_name = sys.argv[1]
parse = CiscoConfParse("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\show run\\{}".format(device_file_name))
# l3_int = parse.find_objects(r"interface")
# L3_int_list = []
# for obj in l3_int:
#     if obj.re_search_children(r"^\sip address"):
#         L3_int_list.append(obj)
#
# print(L3_int_list)
# int_name = []
# for i in L3_int_list:
#     print(i.text)
#     split_list = i.text.split()
#     int_name.append(split_list[1])
#
# print(int_name)
#
# for i in range(2,581):
#     for j in range(len(int_name)):
#         if sheet['C{}'.format(i)].value == int_name[j]:
#             sheet['G{}'.format(i)].value='L3'
#
# wb.save("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")

# wb = openpyxl.load_workbook(r"C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
# sheet = wb['Fab7-corp-1']

l3_int = parse.find_objects(r"interface")
Trunk_int_list = []
for obj in l3_int:
    if obj.re_search_children(r"allowed vlan"):
        Trunk_int_list.append(obj)

# print(Trunk_int_list)
trunk_int_name = []
for i in Trunk_int_list:
    # print(i.text)
    split_list = i.text.split()
    trunk_int_name.append(split_list[1])

# print(trunk_int_name)
# print(len(trunk_int_name))
line_list = []
f = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\show run\\{}".format(device_file_name),"r")
for line in f:
    # pattern = "r\"(^interface "+trunk_int_name[i]+")(\\n\\s(.*))+(switchport trunk allowed vlan)\\s([0-9,\\,]+)\""
    # pattern = "(^interface "+trunk_int_name[i]+")"
    # print(pattern)
    for i in range(len(trunk_int_name)):
        if trunk_int_name[i] in line:
            # print(line)
            if re.findall(r"(interface)\s+(.*)",line):
                m = re.findall(r"(interface)\s+(.*)",line)
                # print(m[0][1])
            line_list.append(m[0][1])
            # continue
        elif "allowed vlan" in line:
            if re.findall(r"(allowed vlan)\s+(.*)",line):
                m = re.findall(r"(allowed vlan)\s(.*)",line)
                # print(m[0][1])
            # print(line)
            line_list.append(m[0][1])
            break

print(line_list)

for JK in range(2,10000):
    if sheet['C{}'.format(JK)].value in line_list:
        print(sheet['C{}'.format(JK)].value)

        sheet['J{}'.format(JK)]= line_list[line_list.index(sheet['C{}'.format(JK)].value)+1]

wb.save("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
print("======== Entries Added========")
# print(line_list.index(' switchport trunk allowed vlan 310,400,402,407\n'))
