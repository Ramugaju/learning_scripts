import re
import sys
import openpyxl
wb = openpyxl.load_workbook(r"C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
sheet = wb['EBIZ-2']
device_file_name = sys.argv[1]
f = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\show int brief nexus\\{}".format(device_file_name),"r")
f_desc = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\interface description\\{}".format(device_file_name),"r")
f_speed_duplex = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\show int status\\{}".format(device_file_name),"r")
#####([a-z,A-Z,//,0-9]+)\s+([0-9,-]+)\s+(eth)\s+([a-z,-]+)\s+(['up','down']+)\s+(.*)\s+(.*\(D\))\s+(.*)$#####
j = 0
for line in f:
    if "Interface" in line:
        m = re.findall(r"([a-z,A-Z,//,0-9]+)\s+([0-9,-,a-z]+)\s+(eth)\s+([a-z,-]+)\s+(['up','down']+)\s+(.*)\s+(.*\([D,I,S]\))\s+(.*)",line)
        # print(m[0][0])

        # for i in mo[0]:
        #     print(i)
        continue
    else:
        # print(line)
            if re.findall(r"([a-z,A-Z,//,0-9]+)\s+([0-9,\-,a-z]+)\s+(eth)\s+([a-z,-]+)\s+(['up','down']+)\s+(.*)\s+(.*\([D,I,S]\))\s+(.*)",line):

                if "show int status" in line:
                    break
                elif re.findall(r"([a-z,A-Z,//,0-9]+)\s+([0-9,\-,a-z]+)\s+(eth)\s+([a-z,-]+)\s+(['up','down']+)\s+(.*)\s+(.*\([D,I,S]\))\s+(.*)",line):
                     m_int = re.findall(r"([a-z,A-Z,//,0-9]+)\s+([0-9,\-,a-z]+)\s+(eth)\s+([a-z,-]+)\s+(['up','down']+)\s+(.*)\s+(.*\([D,I,S]\))\s+(.*)",line)
                     print(m_int)
                    # sheet['C{}'.format(j+2)]= m[0][0]
                     sheet['C{}'.format(j+2)]= m_int[0][0].strip()
                     sheet['E{}'.format(j+2)]= m_int[0][4].strip()
                     sheet['F{}'.format(j+2)]= m_int[0][5].strip()
                     sheet['H{}'.format(j+2)]= m_int[0][3].strip()
                else:
                    continue
                    # print(sheet['E{}'.format(j+2)].value)
                j = j+1
k = 0
for line in f_desc:

        if re.findall(r"(.*)\s+(eth)\s+(\d{1,3}\w*)\s+(.*)$",line):


            m = re.findall(r"(.*)\s+(eth)\s+(\d{1,3}\w*)\s+(.*)$",line)
            print(m)

            # sheet['C{}'.format(k+2)]= m[0][0].strip()
            sheet['D{}'.format(k+2)]= m[0][3]

        elif re.findall(r"(Po\d+)\s+(.*)$",line):

                mo = re.findall(r"(Po\d+)\s+(.*)$",line)
                print(mo)
                # sheet['C{}'.format(k+2)]= mo[0][0]
                sheet['D{}'.format(k+2)]= mo[0][1]
        elif re.findall(r"(Vlan\d+)\s+(.*)$",line):

                m_vlan = re.findall(r"(Vlan\d+)\s+(.*)$",line)
                print(m_vlan)
                # sheet['C{}'.format(k+2)]= m_vlan[0][0]
                sheet['D{}'.format(k+2)]= m_vlan[0][1]
                    # Interface[m[0][0]] = {'Ip-address':m[0][1],'OK?':m[0][2],'Method':m[0][3],'Status':m[0][4],'Protocol':m[0][5]}
        else:
            continue
                    # sheet['D{}'.format(k+2)]= m[0][3]
        k = k+1
# L = 0
# count_of_lines = []
# for line in f_speed_duplex:
#     if "Interface" in line:
#         m = re.findall(r"(.*)\s+(['connected','notconnect','disabled','monitoring','sfpAbsent','down','noOperMem']+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)",line)
#         # print(m[0][0])
#
#         # for i in mo[0]:
#         #     print(i)
#         continue
#     else:
#         # print(line)
#             if re.findall(r"(.*)\s+(['connected','notconnect','disabled','monitoring','sfpAbsent','down','noOperMem']+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)",line):
#
#                 if "show int status" in line:
#                     break
#                 else:
#                     m = re.findall(r"(.*)\s+(['connected','notconnect','disabled','monitoring','sfpAbsent','down','noOperMem']+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)",line)
#                     count_of_lines.append(m[0][2])
#
#                     # Interface[m[0][0]] = {'Ip-address':m[0][1],'OK?':m[0][2],'Method':m[0][3],'Status':m[0][4],'Protocol':m[0][5]}
#                     # print(m)
#                     # print(m(3))
#                     # print(m(4))
#                     # print(m(5))
#                     if  m[0][2] == 'trunk':
#                         sheet['I{}'.format(L+1)]= 'trunk'
#                         # sheet['J{}'.format(L+1)]= '1-4094'
#                         sheet['G{}'.format(L+1)]= 'L2'
#
#                     elif m[0][2] == 'routed':
#                         sheet['I{}'.format(L+1)]= 'NA'
#                         sheet['G{}'.format(L+1)]= 'L3'
#                     else:
#                         sheet['I{}'.format(L+1)]= 'Access'
#                         sheet['G{}'.format(L+1)]= 'L2'
#
#
#
#
#                     sheet['J{}'.format(L+1)]= m[0][2]
#                     sheet['K{}'.format(L+1)]= m[0][4]
#                     sheet['L{}'.format(L+1)]= m[0][3]
#
#                     # sheet['E{}'.format(j+2)]= m[0][4]
#                     # sheet['F{}'.format(j+2)]= m[0][5]
#                     # sheet['H{}'.format(j+2)]= m[0][1]
#                     # print(sheet['E{}'.format(j+2)].value)
#
#     L = L+1
# #
wb.save("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
print("======== Entries Added========")
