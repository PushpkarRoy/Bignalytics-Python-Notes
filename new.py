# Q2️⃣ Age Validation (Real Input Case)

# A user enters age as string input.
# Write code to:

# Convert it into integer

# Print: "Eligible to vote" if age ≥ 18

# Handle the situation where user enters invalid value like "twenty"

# ++++++++++++++++++++++++++++++
age = int(input("Enter your age :- "))
print("Your age is :- ", age)

if age > 18:
    print("You are elagable for the Vot")
else:
    print("Sorry but you are under age")


# Q3️⃣ Email Username Extraction


# +++++++++++++++++++++++
email = input("enter your email :- ")
print("Your_email is :- ", email)

user_name = email.split("@")[0]
print("Your user name is :- ", user_name)


# Q4️⃣ Password Length Check

# A user creates a password (string).
# Write code to:

# Check if password length is at least 8 characters

# Print True or False

# ++++++++++++++++++++++++++++++++++++  
name = input("Enter your name :- ")
password = input("Enter your password :- ")
if len(password) >  8:
        print(
               "True\n"
        "Your name is " + name + "\n"
        "Your password is " + password
        )
else:
    print(
          "False\n"
        "Please try another password\n"
        "Password must be at least 8 characters"
    )


# Q5️⃣ Product Price Input Issue

# A product price is taken as input:

# price = "499.99"


# Write code to:

# Convert it to float

# Add 18% GST

# Print final price

# ++++++++++++++++++++++++++++++++
price = str(input("Enter your price :- "))
float_price = float(price)
cal_gst = (float_price * 18)/ 100
final_price = float_price + cal_gst
print("your final price is :- ", final_price)


# Q6️⃣ Yes / No User Response

# User enters input like:

# "yes", "YES", "Yes", " no "
# Write code to:

# Clean the input

# Convert it into boolean

# Print True for yes, False for no


# your_answe = input("ente the answe :- ")
# lower_change = your_answe.lower
# cal_change = your_answe.capitalize

# +++++++++++++++++++++++++++++++++++++++++++++++
your_answe = input("Enter your answer := ")
first_change = your_answe.lower()
secont_change = first_change.capitalize()
print(secont_change)

if secont_change == "Yes":
    print(True)
elif secont_change == "No":
    print(False)
else:
    print("Inner error please fix it")


# Q7️⃣ Text Length Validation (Real Use)

# A user writes a review comment.
# Write code to:

# Check if comment length is more than 100 characters

# Print "Long Review" or "Short Review"

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
feedback = input("write your comment and feedback = ")
if len(feedback) >= 100:
    print("long comment \n thanks for your effort and time")
else:
    print("short \nthanks for your comment")

# Q8️⃣ Name Formatting (Resume Case)

# User enters:

# name = "pushpkar roy"


# Write code to:

# Convert it into "Pushpkar Roy"

# Print it

name = input("Enter Your name : - ")
f_name = name.split()[0]
fc_name = f_name.capitalize()
l_name = name.split()[1]
lc_name = l_name.capitalize()
final_name = fc_name + " " + lc_name
print(final_name)





print()