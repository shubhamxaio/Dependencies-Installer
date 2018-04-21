import os
import json

def install_dependencies(pip_package, version):
	try:
		a = os.system("pip install "+pip_package+"=="+str(version))
		if a == 0:
			print(pip_package+'=='+version+'...', "OK")
		else:
			print(pip_package+'=='+version+'...', "FAIL")
	except Exception as exception:
		print("[Error]: ", str(exception))


json_data = json.load(open('dependencies.json'))

for package in json_data['Dependencies']:
	install_dependencies(package, json_data['Dependencies'][package])