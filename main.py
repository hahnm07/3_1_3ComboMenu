cost= 0
sandwich= input("Choose a sandwich:\nchicken $5.25, beef $6.25, or tofu $5.75\n")

if sandwich == "chicken":
  print("You chose a chicken sandwich.")
  cost = cost + 5.25
elif sandwich== "beef":
  print ("You chose a beef sandwich.")
  cost =cost + 6.25
elif sandwich == "tofu":
  print("You chose a tofu sandwich.")
  cost =cost + 5.75
else:
  print("Please correctly enter one of the choices above.")