first=123
second=456
third=789

if first==second==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)

first=123
second=123
third=123

if first==second==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)

first=123
second=100
third=123

if first==second==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)