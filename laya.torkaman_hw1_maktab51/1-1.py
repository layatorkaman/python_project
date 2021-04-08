""" This program resive the string and replace vowel letter with point"""
my_str=input("enter your string:") #input str
my_str=my_str.lower() # low all letter
letter=["a","i","o","u","e"]
for i in my_str: # this loop checking is vowel letter or no and replace . with vowel ltter
    #if i=="a" or i=="e" or i=="i" or i=="u" or i=="o":
    if i in letter:
    
        my_str=my_str.replace(i,".")
print(my_str) 
