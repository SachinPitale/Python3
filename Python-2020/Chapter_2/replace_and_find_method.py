# Replace method 

string = "she is beatiful and she is good dancer"

#Task - replace all the spaces via - 

print(string.replace(" ", "-"))

# Task - replace first 2 character 

print(string.replace("is", "was", 2))

# Find method postion of is word

print(string.find("is")) 

# To find the position of second is word

first_is_word = string.find("is")
print(string.find("is", first_is_word + 1))

# Center method
# It method is used to add the some character or special charater on right and left side

Name = "Sachin"

# Task : To add two star at right and left side

print(Name.center(10, "*"))


print(Name[0])