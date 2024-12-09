
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    try:
        date = input("Input a Date: ")
        sp = date.rsplit("/")  # Split it into a list 
        print(sp)
        # add your code here.  
        # Check that the length of sp is acutally 3 before assuming the split did something.
    except:
        print("there was an error please enter a new date")
