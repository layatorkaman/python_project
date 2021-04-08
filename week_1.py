
name_list=input('please enter your name: ')
name_list=name_list.split(',')
new_name_list=[]
for item in name_list:
    new_name_list.append(item.strip())

new_name_list=list(set(new_name_list))    
new_name_list.sort()
#print(new_name_list)



list_runner=[]
#dict_runner={}


for index, name in enumerate(new_name_list):
    dict_runner={}
    dict_runner[index]=name
    list_runner.append(dict_runner)
print(list_runner)


list_distance=[]    
for index,item in enumerate(list_runner):
    
    item['distance']=int(input('{} please enter distance: '.format(item[index])))
    #list_distance.append(dict_runner['distance'])
    #list_runner.append(dict_runner)
    list_distance.append((item['distance'],item[index]))
    
    
list_distance.sort()
list_distance.reverse()

for i in range(3):
    print(list_distance[i])
print("this is a test")
print("*")
    

    
