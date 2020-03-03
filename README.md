# venin.py
>> Python based Previledge Esaclation Tool for LINUX <<

A standalone python script which utilizes python built-in modules and misconfigure user managment to get access to shadow file
and duplicates the current user password with the root or any other specified user account.[ ͡0 ͜ʖ ͡0]

-----------------
 ::INSTRUCTIONS::                Please Read Instructions before start!
----------------- 

-> You should have right to use 'cp' command, if you don't this won't work :( (Try Asking your administrator to give you "cp" command access)

-> This script will change the password of specified account with current user's password.

-> Please Only select valid username to which you want to gain access.

-> To check all accounts present in your system type: 'compgen -u' in other terminal window and only input the valid user account(~Dont Forget).

-> Luckily, this tool provide backup option::You can restore the changes by responding '2' when system asks you for that, so that victim will not feel any suspiciousness.

-----------------
 ::WORKS ON::                
-----------------
Versions:
    Python (2.6-7.*)
    Python (3.6-7.*)
    
----------------
 ::Tested ON::                
----------------  
 
Kali Linux
Ubuntu

------------------------
 ::Initializing Script::                
------------------------  

python venin.py

------------------------
 :: How it works? ::                
------------------------  
  
  When the script successfully execute, it will duplicate your password with the specified one.
  For example, if your username is "guest" and passwaord is "12345" and you want to gain access to username "root" and you dont
  know its password.
  Here venin play for you, it will duplicate your password to the root password (means root password is also "12345").
  Now, do "su root" on terminal , it will ask you for password. Enter password "12345" and you successfully got root access.
  
  To restore the changes, select option 2. Thanks!
  
----------------
 ::NOTE::                
----------------  
-> Please only enter valid username from the users list, otherwise things will getting worse.
