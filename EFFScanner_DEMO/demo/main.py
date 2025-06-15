# Read up to the 8th comma in a string
input_str = "a,b,c,d,e,f,g,h,i,j,k"
parts = input_str.split(',', 7)
result = ','.join(parts[:7])
print(result)  # Output: a,b,c,d,e,f,g,h,i