def swapFileData (file1,file2):
    with open(file1,'r') as a:
        data_a = a.read()
    with open(file2,'r') as b:
        data_b = b.read()
    with open(file1,'w') as a:
        a.write(data_b)
    with open(file2,'w') as b:
        b.write(data_a)
    print("Your files are swapped:)")

print("Hey! You can swap files now:)")
print("Enter the name of the files you want to SWAP")    
file1=input("First file : ")
file2=input("Second file : ")
swapFileData (file1,file2)
