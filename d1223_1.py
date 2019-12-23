json = {"name":"donggyun",
        "age":"21",
        "where":"병점동",
        "phone_number":"010-9922-6913",
        "friends":[{"name":"hyungjun","age":"21"},
                  {"name":"donggeun","age":"21"}]}


print(json['name'])
print(json['age'])
print(json['where'])
print(json['phone_number'])
friends = json['friends']
for friend in friends:
    print(friend)