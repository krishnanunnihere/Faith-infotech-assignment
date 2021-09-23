from collections import defaultdict

patientDetails_dict=defaultdict(list)

while True:
  print("\n\t\t\t\tMenu for Patient Management \n\n\t\t\t\t1.Add a new patient's details\n\t\t\t\t2.View list of patients\n\t\t\t\t3.exit\n")
  choice=int(input("Your choice:"))
  if choice==2:
    if not bool(patientDetails_dict): #check if the dictionary is empty
      print("\nNo details available\n")
    else:
      print("\nList of patients in list:\n")
      for j in range(len(patientDetails_dict)):
        print(patientDetails_dict[j][1])
  elif choice==1:
    print("\nInput details of new patient\n")
    reg_no=int(input("Enter the register number:"))
    name=input("\nEnter name of patient:")
    dob=input("\nEnter dob(dd-mm-yyyy):")
    gender=input("\nEnter gender of the patient(m/f):")
    address=input("\nEnter address:")
    phone_no=int(input("\nEnter phone number of patient:"))
    patientDetails_dict[len(patientDetails_dict)]=[reg_no,name,dob,gender,address,phone_no]
    print("\nSuccesfully added new patient.")
  elif choice==3:
    break
  else:
    print("invalid input")

  
