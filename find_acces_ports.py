import re
f = open('C:\\Users\\RamuGajula\\AppData\\Local\\Programs\\Python\\Python37\\allowed_vlan.txt')

import ciscoconfparse
from ciscoconfparse import CiscoConfParse
import sys
import openpyxl
# wb = openpyxl.load_workbook(r"C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
# sheet = wb['Fab7-corp-1']
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
    if obj.re_search_children(r"switchport access vlan"):
        Trunk_int_list.append(obj)

print(Trunk_int_list)
trunk_int_name = []
for i in Trunk_int_list:
    print(i.text)
    split_list = i.text.split()
    trunk_int_name.append(split_list[1])

print(trunk_int_name)
# print(len(trunk_int_name))
line_list = []
f = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\show run\\{}".format(device_file_name),"r")
for line in f:
    # pattern = "r\"(^interface "+trunk_int_name[i]+")(\\n\\s(.*))+(switchport trunk allowed vlan)\\s([0-9,\\,]+)\""
    # pattern = "(^interface "+trunk_int_name[i]+")"
    # print(pattern)
    for i in range(len(trunk_int_name)):
        if trunk_int_name[i] in line:
            line_list.append(line)
            # continue
        elif "switchport access vlan" in line:
            line_list.append(line)
            break

print(line_list)
