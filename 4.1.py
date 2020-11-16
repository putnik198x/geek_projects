from sys import argv

script_name, script_virobotka, script_stavka, sctipt_hrs = argv

print("имя: ", script_name)
print("итого: ", int(sctipt_hrs)*int(script_stavka) + int(script_virobotka))