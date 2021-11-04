print("Program mencari bilangan terbesar") 

a = int(input("Masukan nilai a: "))
b = int(input("Masukan nilai b: "))
c = int(input("Masukan nilai c: "))

if a > b and a > c:
    print ("A yang terbesar")
elif b > a and b > c:
    print ("B yang terbesar")
else:
    print("C yang terbesar")
    
