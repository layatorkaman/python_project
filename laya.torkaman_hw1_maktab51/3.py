""" this program count the vote  """
n=int(input("how many vote we have got:")) # input number of vote
my_dict={} 
while n>0: # this loop control number of vote
    var=input("please enter your vote:")
    my_dict[var]=my_dict.get(var,0)+1 # creat a key in dectionary for each kandid and count thier number
    n-=1
f=list(my_dict.items()) # convert  dictionary to list
f.sort() #sort
for i in f: #print each person and vote
   print("{} {}".format(i[0],i[1]))
   
