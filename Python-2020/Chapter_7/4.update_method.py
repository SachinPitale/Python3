# Update method is used for add one dict to other dict

user_info = {
    'name' : 'sachin',
    'age' : '29',
    'movies' : ['abc','xyz'],
    'songs' : ['pqr','qpn']
}

print (user_info)


more_info = {
    'name' : 'Sachin Pitale',
    'state': 'MH',
    'Tune' : ['efg','srt']
}


print (more_info)

user_info.update(more_info)
print (user_info)
