
import re# REVIEW:
import sys
import openpyxl
device_file_name = sys.argv[1]
f = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\TX Pauses\\{}".format(device_file_name),"r")
wb = openpyxl.load_workbook(r"C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\test.xlsx")
sheet = wb['ERP-DR-2']
int_Ports = []
TX_count = []
ie_count = []
id_count = []
oe_count = []
od_count = []
k = 0
for line in f:
    # pattern = "r\"(^interface "+trunk_int_name[i]+")(\\n\\s(.*))+(switchport trunk allowed vlan)\\s([0-9,\\,]+)\""
    # pattern = "(^interface "+trunk_int_name[i]+")"
    # print(pattern)
########### Interface##############
    if re.findall(r"(.*)\s+is\s+(.*)",line):
        mo = re.findall(r"(.*)\s+is\s+(.*)",line)
        # print(mo[0][0])
        sheet['A{}'.format(k+2)]= mo[0][0]
        int_Ports.append(mo[0][0])
########### Input Errors ##########
    elif re.findall(r"([0-9]+)\s+input\s+error",line):
        mo_ie = re.findall(r"([0-9]+)\s+input\s+error",line)
        sheet['B{}'.format(k+2)]= mo_ie[0]
        ie_count.append(mo_ie[0])
########### Input Discards ##########
    elif re.findall(r".*\s+([0-9]+)\s+input discard",line):
        mo_id = re.findall(r".*\s+([0-9]+)\s+input discard",line)
        sheet['C{}'.format(k+2)]= mo_id[0]
        id_count.append(mo_id[0])
########### Output Errors ##########
    elif re.findall(r"([0-9]+)\s+output\s+error",line):
        mo_oe = re.findall(r"([0-9]+)\s+output\s+error",line)
        sheet['D{}'.format(k+2)]= mo_oe[0]
        oe_count.append(mo_oe[0])
########### Output Discards ##########
    elif re.findall(r".*\s+([0-9]+)\s+output discard",line):
        mo_od = re.findall(r".*\s+([0-9]+)\s+output discard",line)
        sheet['E{}'.format(k+2)]= mo_od[0]
        od_count.append(mo_od[0])
########### Tx Pauses ##########
    elif re.findall(r"([0-9]+)\s+Tx\s+pause",line):
        mo_tx = re.findall(r"([0-9]+)\s+Tx\s+pause",line)
        sheet['F{}'.format(k+2)]= mo_tx[0]
        TX_count.append(mo_tx[0])
    # else:
    #     continue
        k = k+1
print(len(int_Ports))
print(len(ie_count))
print(len(id_count))
print(len(oe_count))
print(len(od_count))
print(len(TX_count))

wb.save("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\test.xlsx")
print("======== Entries Added========")




# print(len(TX_count))
