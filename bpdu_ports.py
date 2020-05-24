
import re# REVIEW:
import sys
device_file_name = sys.argv[1]
f = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\show span detail\\{}".format(device_file_name),"r")
for line in f:
    # pattern = "r\"(^interface "+trunk_int_name[i]+")(\\n\\s(.*))+(switchport trunk allowed vlan)\\s([0-9,\\,]+)\""
    # pattern = "(^interface "+trunk_int_name[i]+")"
    # print(pattern)
    BPDU_Ports = []
    if re.findall(r"\((.*)\)",line):
        mo = re.findall(r"\((.*)\)",line)
        # print(mo)
        BPDU_Ports.append(mo)
print(BPDU_Ports)      # print(mo)
# count_int = []
    # f2 = open("C:\\Users\\RamuGajula\\Desktop\\Py-portmapping\\show span detail\\{}".format(device_file_name),"r")
    # for line2 in f2:
    #     if re.findall(r"(BPDU:)\s+sent\s([0-9]+),\sreceived\s([0-9]+)",line2):
    #         mo_BPDU = re.findall(r"(BPDU:)\s+sent\s([0-9]+),\sreceived\s([0-9]+)",line2)
    #         # print(mo_BPDU)
    #         BPDU_Ports.append(mo_BPDU[0][2])
    #         break
    # continue

# print(BPDU_Ports)

# print(len(count_int))

        # else:
        #     print(line)
                # print(mo_BPDU)

    #
    # for i in range(len(trunk_int_name)):
    #     if trunk_int_name[i] in line:
    #         # print(line)
    #         if re.findall(r"(interface)\s+(.*)",line):
    #             m = re.findall(r"(interface)\s+(.*)",line)
    #             print(m[0][1])
    #         line_list.append(m[0][1])
    #         # continue
    #     elif "allowed vlan" in line:
    #         if re.findall(r"(allowed vlan)\s+(.*)",line):
    #             m = re.findall(r"(allowed vlan)\s(.*)",line)
    #             print(m[0][1])
    #         # print(line)
    #         line_list.append(m[0][1])
    #         break
