import telnetlib
import time

def telnet_script(ip):
    wait=2
#------------------Sign in ---------------------------#
    
    connection=telnetlib.Telnet(ip,23,5)
    output=connection.read_until("Username:")
    connection.write("admin"+"\n")

    output=connection.read_until("Password:")
    connection.write("cisco"+"\n")
    time.sleep(wait)
    
#----------------- Sign in --------------------------#

#----------------- Command loop ---------------------#
    
    command_file= raw_input('Enter the name of the file with commands with extension:\n')
    selected_file= open(command_file)
    for each_line in selected_file.readlines():
        time.sleep(wait)
        connection.write(each_line)
        time.sleep(wait)
        connection.write("\n")
        
#----------------- Command loop ---------------------#
        
 #   connection.write("Configure terminal"+"\n")
 #   time.sleep(wait)
 #   connection.write("hostname python-switch1"+"\n")
 #   time.sleep(wait)
 #   connection.write("do show users"+"\n")
 #  time.sleep(wait)

    output=connection.read_very_eager()
    file = open("python-switch1","w")
    file.write(output)
    file.close
    print(output)
    time.sleep(wait)
    connection.close()
    

telnet_script('10.106.57.225')
