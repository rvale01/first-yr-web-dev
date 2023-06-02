from passlib.hash import sha256_crypt
from datetime import datetime

print('Choose a function:\n1 for Add new user\n2 for Login\n')
choice = int(input('Enter your choice: '))

if choice==1:
    print('Adding new User\n')    
    user_name = input('Enter User Name ')
    password = input('Enter Password ')

    salt = datetime.now()   #Creating salt to make password unique
    print('Salt is: ', salt)

    password_hashvalue = sha256_crypt.hash(password+str(salt))

    fh = open('userlogindb.txt', 'w+')
    if fh:
        user_record = user_name + ', ' + str(salt) + ', ' + password_hashvalue
        fh.write(user_record)
    else:
        print ('could not create file')
    fh.close()

    print ('Check file ')
    fh = open('userlogindb.txt')
    if fh:
        for line in fh:
            print(line)
    else:
        print('Error in opening file ')
    fh.close()
elif choice==2:
    print ('Login: Check user account \n')
    user_name = input('Enter user name ')
    password = input('Enter password ')
    line_list = []
    fh = open('userlogindb.txt')
    if fh:
        for line in fh:
            #print(line)
            line_list = line.rstrip().split(', ')
            #print(line_list)
        
            if user_name == line_list[0]:
                salt_retrieved = line_list[1]
                #print(salt_retrieved)
                password_hash_value = line_list[2]
                #print(password_hash_value)
                for_password_hash = password+salt_retrieved            
                output = sha256_crypt.verify(for_password_hash, password_hash_value)
                if output:
                    print('Success: User and Password matched ')
                else:
                    print('Failure: User and Password did not match ') 
            else:
                print ('Invalid user or password')
    else:
        print('Error in opening file ')
    fh.close()
else:
    print('Incorrect choice - start again')