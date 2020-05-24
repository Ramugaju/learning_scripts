import re
import sys
import openpyxl
wb = openpyxl.load_workbook(r"C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
sheet = wb['Fab7-corp-2']
device_file_name = sys.argv[1]
f = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\interface description\\{}".format(device_file_name),"r")
Interface ={}
j = 0
for line in f:
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
                    print(m)
                    # Interface[m[0][0]] = {'Ip-address':m[0][1],'OK?':m[0][2],'Method':m[0][3],'Status':m[0][4],'Protocol':m[0][5]}

                    sheet['D{}'.format(j+2)]= m[0][3]
                    # sheet['E{}'.format(j+2)]= m[0][4]
                    # sheet['F{}'.format(j+2)]= m[0][5]
                    # sheet['H{}'.format(j+2)]= m[0][1]
                    # print(sheet['E{}'.format(j+2)].value)
    j = j+1


#
wb.save("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\Port-Mapping.xlsx")
print("======== Entries Added========")
