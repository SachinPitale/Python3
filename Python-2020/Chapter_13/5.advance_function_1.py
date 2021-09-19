l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

def average_finder(*args):
    average = []
    for i in zip(*args):
        average.append(sum(i)/len(i))
    return average

print (average_finder(l1,l2,l3))


average_finder = lambda *args: [sum(i)/len(i) for i in zip *args]