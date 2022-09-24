data=[{"firstname":"Rahul","lastname":"kumar"},{"firstname":"suraj","lastname":"sk"},{"firstname":"yashik","lastname":"jain"}]

Names = []
for val in data:
    concat = val['firstname'] + val['lastname']
    Names.append(concat)
    # fullname = ",".join(concat)
k = ",".join(Names)
print(k)




# output:-Rahul kumar,suraj