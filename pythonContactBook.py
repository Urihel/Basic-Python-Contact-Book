def navigationMenu( ):
    print("1. Add New Contact")
    print("2. Search Contact List")
    print("3. Exit Program")
    menuNumber = int(input('Enter Menu Number Here: '))
    return menuNumber 
#############################
def menuOptionOne(nm,dict1):
     if nm == 1:
        #print('menu option 1 works')
        print('\n')
        contactName = str(input("Add Contact Name Here:  "))
        phoneNumber = str(input("Add Contact Phone Number Here: ")) 
        dict1[contactName] = phoneNumber
        #print(dict1)
        print('\n')
#############################  
def searchContactName(nm,dict1):
    if nm == 2:
        print('\n')
        contactSearch = str(input("Type contact name here: "))
        if contactSearch in dict1:
            print(f'First Name: {contactSearch}')
            print(f'Phone Number: {dict1[contactSearch]}')
            print('\n')
#############################        
def closeProgram(nm):
    if nm == 3:
        quit()

#---------------------main function------------
dict1 = {}
while True:
    nm = navigationMenu( )
    menuOptionOne(nm,dict1)
    searchContactName(nm,dict1)
    closeProgram(nm)
    #print(dict1)  checks to see if dict1 is updating
    
    
    
    
        



