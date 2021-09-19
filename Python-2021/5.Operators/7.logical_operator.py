"""
Logical Operator:
============================

1. and : if any of the condition is false, result will be false
2. or : if any of the condition is true, result will be true
3. not : not True ==> False, not False ==> True

"""
#And Logical Operator
print (1<2 and 5 in [1,2,3,4])
print (1<2 and 2<3 and 3<4)
print (1<2 and 2<3 and 5<4)
# all is equivalent to and operator, only syntax changed
print (all([1<2,2<3,5<4]))

#OR Logical Operator

print (1<2 or 5 in [1,2,3,4])
print (1<2 or 2<3 or 3<4)
print (4<2 or 9<3 or 5<4)
# any is equivalent to or operator, only syntax changed
print (any([4<2 or 9<3 or 5<4]))

print (2>3)
print (not 2>3)