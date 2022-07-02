f=open("people1.txt","w")
f.write("priyanka - shimla\n"
"neela - delhi\n"
"sashi - jaipur\n"
"sarika - delhi\n"
"deepti - shimla\n"
"harshad - delhi\n"
"trishna - delhi\n"
"pradeep - jaipur\n"
"sekhar - delhi\n"
"nand - delhi\n"
"anoop - delhi\n"
"balwinder - jaipur\n")

f.close()


my_file = open("people1.txt")
file_data = my_file.read()
print (file_data)
my_file.close