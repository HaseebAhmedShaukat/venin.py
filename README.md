 
# venin.py
Python-based Privilege Escalation Tool for LINUX 

A standalone python script that utilizes python built-in modules and misconfigures user management to get access to shadow file
and duplicates the current user password with the root or any other specified user account.[ ͡0 ͜ʖ ͡0]

------
NOTE               
------ 
The purpose of this tool is just for the awareness of the system's owner so they can configure user management rightly before they get exploited. 

-----------------
INSTRUCTIONS                Please Read Instructions before start!
----------------- 

-> You should have the right to use 'cp' command, if you don't this won't work :( (Try Asking your administrator to give you "cp" command access)

-> This script will change the password of a specified account with the current user's password.

-> Please Only select a valid username to which you want to gain access otherwise, things will get worse.

-> To check all accounts present in your system type: 'compgen -u' in other terminal windows and only input the valid user account(~Dont Forget).

-> Luckily, this tool also provides backup option: You can restore the changes by responding '2' when the system asks you for that, so the victim will not feel any suspiciousness.

-------------
 WORKS ON                
-------------
Versions:
    Python (2.6-7.*),
    Python (3.6-7.*)
    
------------
 Tested ON                
------------  
 
Kali Linux,
Ubuntu

-----------------
Initializing Script               
-----------------

python venin.py

---------------
How it works?                
---------------  
  
  When the script successfully executes, it will duplicate your password with the specified one.
  For example, if your username is "guest" and password is "12345" and you want to gain access to username "root" and you don't
  know its password.
  Here venin play for you, it will duplicate your password to the root password (means root password is also "12345").
  Now, do "su root" on terminal, it will ask you for a password. Enter the password "12345" and you successfully got root access.
  
  To restore the changes, select option 2. Thanks!
  


