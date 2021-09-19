
# square = {1:2,2:4,3:9}

square = {num:num**2 for num  in range(11)}


print (square)


square_Qube = {f"The Qube of {num} is  ": num**2 for num in range  (10)}

for k, v in square_Qube.items():
    print (f"{k} : {v}")

string= "Sachin"

word_count = {char:string.count(char) for char in string} 
print   (word_count)