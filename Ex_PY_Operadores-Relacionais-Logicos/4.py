x, y, z= 7, 8, False

a= x >= y or z	
print(f"A= {a}") #false

b= x + y * x % 7 == 0	
print(f"B= {b}") #false

c= x >= y or not (not z)
print(f"C= {c}") #false

d= x // y == 0	
print(f"D= {d}") #True



