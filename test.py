Day=int(input("enter the day in numeric form:"))
Month=int(input("enter the month in numeric form:"))
Year=int(input("enter the year as two digits numeric form:"))
#check for invalid Day input
if Day <1 or Day >31:
 print("Error: Invalid Day Input")
    #check for invalid Month input 
elif Month <1 or Month >12:
 print("Error: Invalid Month Input")
        #check for invalid Year Input
elif Year <10 or Year >99:
  print("Error: Invalid Year Input")
        # all input are valid, print sucess message
else: 
 print(f"Sucess: Congratulations! You entered the correct date: {Month}/{Day}/{Year}")
