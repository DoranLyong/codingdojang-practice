filename = input("Enter the file name: ") 

tempfile = open(filename)
tempfile = tempfile.read() 
print(tempfile)


temp_str = tempfile.replace("\t", "    ") # tap -> 4-whitespace
print(temp_str)


# == Save == # 
savefile = open("save_edit.py", 'w')
savefile.write(temp_str)

savefile.close()

