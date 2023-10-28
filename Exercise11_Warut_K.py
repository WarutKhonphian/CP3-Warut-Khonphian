num = int(input("Enter total rows : ")) 
spacs = num
for i in range(num):
    print(((spacs)*" ")+((2*(i+1)-1)*"*"))
    spacs  = spacs -1