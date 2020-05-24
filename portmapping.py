import re
import sys
import openpyxl
wb = openpyxl.load_workbook(r"C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
sheet = wb['Fab7-corp-1']
device_file_name = sys.argv[1]
f = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\show ip int bri\\{}".format(device_file_name),"r")
f_desc = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\interface description\\{}".format(device_file_name),"r")
f_speed_duplex = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\show int status\\{}".format(device_file_name),"r")

j = 0
for line in f:
    # if "Interface" in line:
    #     m = re.findall(r"([a-z,A-Z]+)\s+([a-z,A-Z,-]+)\s+([a-z,A-Z,-,?]+)\s+([a-z,A-Z]+)\s+([a-z,A-Z]+)\s+([a-z,A-Z]+)",line)
    #     # print(m[0][0])
    #
    #     # for i in mo[0]:
    #     #     print(i)
    #     continue
    # else:
        # print(line)
        if re.findall(r"([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.]+)",line):

            if "show int status" in line:
                break
            else:
                m = re.findall(r"([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.,'administratively down']+)\s+([a-z,A-Z,0-9,/,\.]+)",line)

                sheet['C{}'.format(j+2)]= m[0][0]
                sheet['E{}'.format(j+2)]= m[0][4]
                sheet['F{}'.format(j+2)]= m[0][5]
                sheet['H{}'.format(j+2)]= m[0][1]
                    # print(sheet['E{}'.format(j+2)].value)
        j = j+1
k = 0
for line in f_desc:
    if "Interface" in line:
        m = re.findall(r"([a-z,A-Z]+)\s+([a-z,A-Z,-]+)\s+([a-z,A-Z,-,?]+)\s+([a-z,A-Z]+)\s+([a-z,A-Z]+)\s+([a-z,A-Z]+)",line)
        # print(m[0][0])

        # for i in mo[0]:
        #     print(i)
        continue
    else:
        # print(line)
            if re.findall(r"([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+(.*)$",line):

                if "show int status" in line:
                    break
                else:
                    m = re.findall(r"([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.]+)\s+(.*)$",line)
                    # print(m)
                    # Interface[m[0][0]] = {'Ip-address':m[0][1],'OK?':m[0][2],'Method':m[0][3],'Status':m[0][4],'Protocol':m[0][5]}

                    sheet['D{}'.format(k+2)]= m[0][3]

    k = k+1
L = 0
count_of_lines = []
for line in f_speed_duplex:
    if "Interface" in line:
        m = re.findall(r"(.*)\s+(['connected','notconnect','disabled','monitoring','sfpAbsent','down','noOperMem']+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)",line)
        # print(m[0][0])

        # for i in mo[0]:
        #     print(i)
        continue
    else:
        # print(line)
            if re.findall(r"(.*)\s+(['connected','notconnect','disabled','monitoring','sfpAbsent','down','noOperMem']+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)",line):

                if "show int status" in line:
                    break
                else:
                    m = re.findall(r"(.*)\s+(['connected','notconnect','disabled','monitoring','sfpAbsent','down','noOperMem']+)\s+([a-z,A-Z,0-9,/,\.]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.,-]+)\s+([a-z,A-Z,0-9,/,\.]+)",line)
                    count_of_lines.append(m[0][2])

                    # Interface[m[0][0]] = {'Ip-address':m[0][1],'OK?':m[0][2],'Method':m[0][3],'Status':m[0][4],'Protocol':m[0][5]}
                    # print(m)
                    # print(m(3))
                    # print(m(4))
                    # print(m(5))
                    if  m[0][2] == 'trunk':
                        sheet['I{}'.format(L+2)]= 'trunk'
                        # sheet['J{}'.format(L+1)]= '1-4094'


                    elif m[0][2] == 'routed':
                        sheet['I{}'.format(L+2)]= 'NA'

                    else:
                        sheet['I{}'.format(L+2)]= 'Access'





                    sheet['J{}'.format(L+2)]= m[0][2]
                    sheet['K{}'.format(L+2)]= m[0][4]
                    sheet['L{}'.format(L+2)]= m[0][3]

                    # sheet['E{}'.format(j+2)]= m[0][4]
                    # sheet['F{}'.format(j+2)]= m[0][5]
                    # sheet['H{}'.format(j+2)]= m[0][1]
                    # print(sheet['E{}'.format(j+2)].value)

    L = L+1
# #
wb.save("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
print("======== Entries Added========")
