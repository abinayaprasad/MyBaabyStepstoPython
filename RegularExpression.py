#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Password Validation:
# Length of the Password Must be not less than 8
# Should have Lowercase alaphabet
# Should have Uppercase alaphabet
# Should have any numbers between 0-9
# should have special characters.
import re 
def password_validat(password):
    pattern=re.compile(r"(^[a-zA-Z0-9$@#.&*]{8,}\d$)")
    a=pattern.search(password)  
    flag = 0
    if (len(password)<8):
        print("The Password lenght is less than 8")
        flag =-1
        
    elif not re.search("[a-z]",password):
        print("Password doesnot have lowercase")
        flag=-1
        
    elif not re.search("[A-Z]",password):
        print("Password doesnot have uppercase")
        flag=-1
        
    elif not re.search("[0-9]",password):
        print("Password doesnot have numbers between 0-9")
        flag=-1
        
    elif not re.search("[$@#&*.]",password):
        print("Password doesnot have any of this special character $ @ # & * .")
        flag=-1
        
    else:
        flag = 0
        print("Valid Password")
        
   
    if flag==-1:
        print("Not a Valid Password")
    
    conv=password.replace(password,"*")*len(password)
    return conv

#MailId Validation:
def MailValidation(email):
    regex = re.compile(r"(\b[A-Za-z0-9_%+.-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)")

    if regex.search(email):
        print("Valid Email")
    else:
        print("Invalid Email")

    return email
#Mobile Number Validation:
def mobile_validation(num):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    regex1=re.compile(r"^\b[0|91]?[6-9][0-9]{9}\b")
    s = regex1.match(num)
    if s:
        print("Valid Number")
    else:
        print("InValid Number")
    return num 

def main():
    email_ID=input("Enter the MailID: ")
    print(MailValidation(email_ID))
    password=input("Enter the Password: ")
    print(password_validat(password))
    phoneNumb=input("Enter the Mobile Number: ")
    print(mobile_validation(phoneNumb))

if __name__=='__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




