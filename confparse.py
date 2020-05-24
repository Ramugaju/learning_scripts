import ciscoconfparse
from ciscoconfparse import CiscoConfParse
import sys
import openpyxl
wb = openpyxl.load_workbook(r"C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
sheet = wb['Fab7-corp-1']
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

wb = openpyxl.load_workbook(r"C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
sheet = wb['Fab7-corp-1']

l3_int = parse.find_objects(r"interface")
Trunk_int_list = []
for obj in l3_int:
    if obj.re_search_children(r"^\sswitchport mode trunk"):
        Trunk_int_list.append(obj)

print(Trunk_int_list)
trunk_int_name = []
for i in Trunk_int_list:
    print(i.text)
    split_list = i.text.split()
    trunk_int_name.append(split_list[1])

print(trunk_int_name)
for i in range(2,581):
    for j in range(len(trunk_int_name)):
        if sheet['C{}'.format(i)].value == trunk_int_name[j]:
            sheet['G{}'.format(i)].value='L2'
            sheet['I{}'.format(i)].value='Trunk'

wb.save("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
