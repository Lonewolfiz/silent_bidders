from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)

print("Welcome to the secret auction program")
is_in_interest=True
bidders={}
while is_in_interest==True:
  name=input("What is your name? ")
  bid=int(input("What is your bid? "))
  bidders[name]=bid
  boolean=input("Are there any other bidders? Type 'yes' or 'no' ")
  if boolean=='yes':
    clear()
    is_in_interest=True
  else:
    is_in_interest=False  
max_bid=1
name_of_highest_bid=''
for x in bidders:
  if max_bid<bidders[x]:
    max_bid=bidders[x]
    name_of_highest_bid=x

print(f"The winner is {name_of_highest_bid} with a bid of {max_bid}")
