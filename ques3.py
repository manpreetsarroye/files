my_file2 = open("people2.txt", "w")
my_file2.write("Abhishek - Gurgaon")
my_file2.write("Ranveer - Delhi")
my_file2.close()

print ("AbhishekRanveer")
print ("---------------------------------")
print ("Abhishek\nRanveer")
print ("---------------------------------")
print ("Abhishek\n\nRanveer")
print ("---------------------------------")

my_file3 = open("people3.txt", "w")
my_file3.write("Abhishek - Gurgaon\n")
my_file3.write("Ranveer - Delhi")
my_file3.close