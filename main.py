cost= 0
discount=3

#sandwich choice
sandwich= input("Choose a sandwich: chicken ($5.25), beef ($6.25), or tofu ($5.75)\n")
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
  discount= discount-1

#beverage choice
drinksize="none"
wantsdrink= input("Would you like a beverage?: yes or no\n")
if wantsdrink== "yes":
  drinksize= input("Choose a drink size: small ($1.00), medium ($1.75), or large ($2.25)\n")
  if drinksize == "small":
    print("You chose a small drink.")
    cost= cost + 1
  elif drinksize== "medium":
    print("You chose a medium drink.")
    cost= cost + 1.75
  elif drinksize== "large":
    print("You chose a large drink.")
    cost= cost +2.25
else:
  print("You do not want a beverage.")
  discount= discount-1

#fries choice 
frysize="none"
wantsfries= input("Would you like a side of french fries?: yes or no\n")
if wantsfries== "yes":
  frysize= input("Choose a size for your french fries: small $1.00, medium $1.50, large $2.00\n")
  if frysize== "small":
    megasize= input ("Would you like to mega-size your fries to a large?: yes (only $1 extra) or no\n")
    if megasize== "yes":
      frysize= "large"
      print("You chose a large side of french fries.")
      cost= cost + 2
    elif megasize== "no":
      print("You chose a small side of french fries.")
      cost= cost + 1
  elif frysize== "medium":
    print("You chose a medium side of french fries.")
    cost= cost+ 1.5
  elif frysize== "large":
    print("You chose a large side of french fries.") 
    cost= cost + 2
else:
  print("You do not want french fries.")
  discount= discount-1

#ketchup packets
count=0
ketchupamnt= input("How many ketchup packets would you like? Enter a number. ($0.25 each)\n")
while int(ketchupamnt) > count:
  cost= cost + 0.25
  count= count + 1

#discount and final cost
if discount ==3:
  print("You received a $1 discount!")
  cost= cost -1

#final options
print("Your choices:")
#sandwich
if sandwich == "chicken":
  print("Chicken sandwich,")
if sandwich== "beef":
  print ("Beef sandwich,")
if sandwich == "tofu":
  print("Tofu sandwich,")
#drink
if drinksize== "small":
  print("Small beverage,")
if drinksize== "medium":
  print("Medium beverage,")
if drinksize== "large":
  print ("Large beverage,")
#fries
if frysize== "small":
  print("Small french fries,")
if frysize== "medium":
  print("Medium french fries,")
if frysize== "large":
  print("Large french fries,")
#kethcup
if int(ketchupamnt)>0:
  print(ketchupamnt +" ketchup packets")
print("Final cost: $"+ str(cost))