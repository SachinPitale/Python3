

try:
    print('a')
except Exception as e:
    print (e)
else:
    print("All try block code execute successfully")
finally:
    print ("This will always execute")