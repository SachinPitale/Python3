names = ['sachin pitale','mohit','hershit', 'ab','z']
print (max(names, key = lambda item : len(item)))
print (min(names, key = lambda item : len(item)))



students = {
    'hershit' : {'score':50, 'age':24},
    'mohit': {'score':75, 'age':19},
    'rohit' : {'score':76, 'age':23}

}
print(max(students, key = lambda item: students[item]['score']))


student2  = [
    {'name': 'hershit', 'score':50, 'age':24},
     {'name': 'mohit', 'score':75, 'age':27},
      {'name': 'rohit', 'score':85, 'age':29}


]

print (max(student2, key = lambda item: item.get('age'))['name'])