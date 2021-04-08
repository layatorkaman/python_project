"""this program resive a string and detect the letter that is vowel or no .and delet vowel and replace unvowel with point and unvowel"""
my_str=input("enter your string:") # input str
my_str=my_str.lower() #low the str
for i in my_str: # checking if is vowel delet else replace with point and letter
    if i=="a" or i=="o" or i=="i" or i=="u" or i=="e":
        my_str=my_str.replace(i,"")
      
    else:
        my_str=my_str.replace(i,".{}".format(i))
    
print(my_str)
