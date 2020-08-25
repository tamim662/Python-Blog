list=[[72,'Queen St. Cafe'], [81,'Dumplings R Us'],[85,'Mexican Grill']]

result=sorted(sort_list, key=lambda l:l[0])#where you can change key value by change index of l; l[1] or l[2]

print(result)
>>> [[72, 'Queen St. Cafe'], [81, 'Dumplings R Us'], [85, 'Mexican Grill']]

result=sorted(sort_list, key=lambda l:l[1])
print(result)
>>> [[81, 'Dumplings R Us'], [85, 'Mexican Grill'], [72, 'Queen St. Cafe']]


# Another cool thing you can use is 'Reverse" that will change the order from ascending to descending
result=sorted(sort_list, key=lambda l:l[0],reverse=True)
print(result)

>>> [[85, 'Mexican Grill'], [81, 'Dumplings R Us'], [72, 'Queen St. Cafe']]
