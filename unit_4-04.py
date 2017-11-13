#created by Matthew Walsh
#created for ICS3U
#created on nov 2017
#convert mark into percentage

mark_4_plus = 98
mark_4 = 91
mark_4_minus = 83
mark_3_plus = 78
mark_3 = 75
mark_3_minus = 71
mark_2_plus = 68
mark_2 = 65
mark_2_minus = 61
mark_1_plus = 58
mark_1 = 55
mark_1_minus = 51
mark_NE = 25

def calculate_mark(user_input):
	     #convert mark to percentage
     if user_input == "NE":
        user_input = mark_NE
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "1+":
        user_input = mark_1_plus
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "1":
        user_input = mark_1
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "1-":
        user_input = mark_1_minus
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "2":
        user_input = mark_2
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "2+": 
        user_input = mark_2_plus
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "2-": 
        user_input = mark_2_minus
        print("You mark is: " + str(user_input) + "%")    	
     elif user_input == "3":
        user_input = mark_3
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "3+":
        user_input = mark_3_plus
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "3-":
        user_input = mark_3_minus
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "4":
        user_input = mark_4
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "4+":
        user_input = mark_4_plus
        print("You mark is: " + str(user_input) + "%")
     elif user_input == "4-":
        user_input = mark_4_minus
        print("You mark is: " + str(user_input) + "%")
     else:
        print("-1")
        get_mark()
        
def get_mark(): 	 
	#get mark as input 
    user_input = raw_input("Please enter any level from NE - 4+: ")    
    if user_input == "ne":
       user_input = user_input.upper()
        	       
    calculate_mark(user_input)   	

get_mark()        
