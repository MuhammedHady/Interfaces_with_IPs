import glob, os
from ciscoconfparse import CiscoConfParse

directory = r"Enter Files Directory Here"
myfiles = []
for filename in os.listdir(directory):
	suffix=".conf"
	filex = filename.endswith(suffix)
	if filex == True :
		myfiles.append(filename)

for filefile in myfiles:
	parse = CiscoConfParse("%s"%filefile, syntax='ios', factory=True)
	print('#########################################')
	print('\n')
	print(filefile)
	print('-----------')
	for intf_obj in parse.find_objects_w_child('^interface', '^\s+ip address'):
		intf_name = intf_obj.re_match_typed('^interface\s+(\S.+?)$')                         	# getting the interface that has the statement "ip address"
		intf_ip_addr = intf_obj.re_match_iter_typed(r'ip\saddress\s(\d+\.\d+\.\d+\.\d+)\s', result_type=str, group=1, default='')    		# getting the ip on the interface that has the statement "ip address"
		print("{0}: {1}".format(intf_name, intf_ip_addr))										# print the whole line detailed
		print('\n')
	print('#########################################')

	
