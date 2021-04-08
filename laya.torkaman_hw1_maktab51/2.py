""" this program resive a str with + and then sort and sum"""
my_str=input("enter your sentence:") # resive str
my_str=my_str.split("+") #strip
my_str.sort() #sort the number

new_str=" "

new_str="".join(my_str) # for create new str we use of join
print(new_str)

my_list=[]
sumt=0
for i in my_str: # sum the number and print
    my_list.append(int(i))
    sumt+=int(i)
print("sum is {}".format(sumt))
    
    
    

