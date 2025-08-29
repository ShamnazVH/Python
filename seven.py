# 1. Define a class Person with attributes name and age. Create an object and print the attributes.
# 2. What is the purpose of _init_ method in a class?
# 3. What is the difference between a class variable and an instance variable?
# 🔹 Inheritance
# 4. Create a class Animal with a method speak. Inherit it into a class Dog and override the speak method.
# 5. Demonstrate multilevel inheritance using classes Animal, Mammal, and Dog.
# 6. Write a program to show multiple inheritance in Python.
# 🔹 Polymorphism
# 7. What is polymorphism? Give an example using method overriding.
# 8. Write a class Shape with a method area(). Override area() in subclasses Circle and Rectangle. Call area() from a loop of shape objects.
# 9. Demonstrate operator overloading using _add_() in a custom class.
# 🔹 Encapsulation
# 10. What is encapsulation in Python? How do we make an attribute private?
# 11. Create a class Account with private attribute __balance and methods deposit() and get_balance().
# 12. Can you access a private variable outside the class in Python? How?
# 🔹 Applied / Problem-Based Questions
# 13. Create a class hierarchy: Vehicle → Car, Truck. Include attributes like max_speed and methods like drive().
# 14. Write a program where a Student class inherits from Person, adds marks, and has a method to calculate grade.
# 15. Implement a class Bank where account details are encapsulated, and inheritance is used for SavingsAccount and CurrentAccount.





# re.findall() Problems
# Extract all hashtags from a social media post.
# Find all valid email addresses in a block of text.
# import re
# text = '''Please contact our support team at support@example.com for any technical issues you may encounter.
# You can reach out to the HR department at hr@companydemo.org for job-related queries.
# For partnership opportunities, email us at partners@businesshub.net.
# If you have feedback, write to feedback123@demoemail.com — we value your input.
# Our sales team is available at sales.team@democo.com to assist with product pricing.
# For student registration, submit your details to register.student@edu-demo.in.
# Developers can report bugs at devsupport@mockdomain.dev.
# To unsubscribe from newsletters, send a request to unsubscribe@newsdemo.org.
# Internship applicants can submit their resumes to interns.hr@samplecorp.io.
# For media inquiries, reach out to media.relations@demo-news.com.'''
# x = re.findall("@....com\Z", text)
# print(x)
# for x in text:
#     print("yes ,there is a match",x)
# else:
#     print("there is no match")





# Extract all 4-digit numbers (e.g., years) from a paragraph.
# import re
# sen_str = """
# The company was founded in 1998 and expanded globally by 2005.
# In 2010, we launched our first mobile application.
# The project deadline is set for December 2025.
# She graduated from university in 2017 with honors.
# Our latest product line was introduced in early 2023.
# The next conference is scheduled for March 2026.
# This technology was first patented in 2001.
# They celebrated their 50th anniversary in 2022.
# The new policy will come into effect in 2024.
# Historical data from 1980 to 2020 shows steady growth.
# """
# # sen_str = "hello to the programming world!"
# # a = re.findall(r"\b\d{4}\b",sen_str)
# a = re.findall(r"[0-9][0-9][0-9][0-9]",sen_str)
# if a:
#     print("yes ,there is a match: ",a)
# else:
#     print("there is no match")





# Get all capitalized words from a sentence.
'''sentence = "This is a SIMPLE example to SHOW how UPPERCASE words can be USED in a sentence."
y = sentence.isupper()
if y in sentence:
    print("yes ,there is a match",y)
else:
    print("there is no match")'''



# Extract all hexadecimal color codes (like #FF5733) from CSS code.

# 🔍 re.search() Problems
# Check if a string contains a valid PAN number (e.g., ABCDE1234F).

# Check if a sentence starts with a capital letter and ends with a full stop.

# Search for a date in YYYY-MM-DD format in a text.

# Check if a string contains a valid Indian vehicle registration number (e.g., KL-07-AB-1234).




# ✂ re.sub() Problems
# Replace all occurrences of multiple spaces with a single space.
# import re
# txt = "The    rain   in   Spain"
# x = re.sub(r' +', " ", txt)
# print(x)


# Replace all phone numbers with [PHONE].
# import re
# a = '''For more information, contact John at 9876543210 
# or reach our office at (080)12345678 during business hours'''
# x = re.sub(r'\b\d{10}\b','[phone]',a)
# print(x)



# Remove all non-alphanumeric characters from a string.
# import re
# txt = "#The rain in Spain!"
# cleaned = re.sub(r'[^\w\s]', '', txt)
# print(cleaned)


# \b ensures we match the word "bad" as a whole word (not part of another word like "badminton").
# re.IGNORECASE makes it case-insensitive.
# Replace all instances of a word (e.g., "bad") with "*" (case-insensitive).
# import re
# text = "This is a Bad example of a bad BAD situation."
# # Replace all case-insensitive matches of 'bad' with '*'
# result = re.sub(r'\bbad\b', '*', text, flags=re.IGNORECASE)
# print(result)



# ✂ re.split() Problems
# Split a paragraph into sentences based on punctuation.
# import re
# para = """"Hello! Did you see John's book—*The Art of Code*—on the table? It's amazing, really: a must-read for developers. (Yes, even beginners!)  """
# v = r"(['.', ',', ';', ':', '?', '!', '-', '_', '(', ')', '[', ']',
#                '{', '}', '"', "'", '…', '/', '\\', '|', '@', '#', '$', '%',
#                  '^', '&', '*', '~', '`', '<', '>'])
# for v in para:
#     print("there is a match")
#     w= re.split(v,para)
#     print(w)
# else:
#     print("there is no match")


# Split a string by commas or semicolons.
# import re
# a = '''I went to the market to buy apples, bananas, and grapes; met 
# an old friend on the way; and realized, quite suddenly, that I had 
# forgotten my wallet, my phone, and even my shopping list.'''
# x = re.split("[,;]",a)
# print(x)




# Split a file path (e.g., C:/Users/Name/Desktop/file.txt) into its components.
# import re
# # path = "C:/Users/Name/Desktop/file.txt"
# path = "C:\\Users\\Name\\Desktop\\file.txt"
# x = re.split(r"[\\//\/]", path)
# print(x)




# Break a log line using multiple delimiters like :, -, and whitespace.
# import re
# def split_log_line(log_line):
#     # Split using colon (:), dash (-), or any whitespace
#     parts = re.split(r'[:\-\s]+', log_line)
#     return parts

# # Example log line
# log = "2025-07-10 10:30:00 - ERROR: Failed to connect to database"

# # Split and print
# result = split_log_line(log)
# print(result)



# # Verify if a password contains at least one digit, one uppercase letter, and one special character.
# import re

# def is_valid_password(password):
#     # Check for at least one digit
#     has_digit = re.search(r"\d", password)
    
#     # Check for at least one uppercase letter
#     has_upper = re.search(r"[A-Z]", password)
    
#     # Check for at least one special character
#     has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

#     if has_digit and has_upper and has_special:
#         return True
#     else:
#         return False

# # Example usage:
# password = input("Enter a password to check: ")
# if is_valid_password(password):
#     print("Valid password ✅")
# else:
#     print("Invalid password ❌ (must include a digit, an uppercase letter, and a special character)")


#or

# import re
# def is_valid_password(password):
#     # Check for at least one digit
#     has_digit = re.search(r"\d", password)
    
#     # Check for at least one uppercase letter
#     has_upper = re.search(r"[A-Z]", password)
    
#     # Check for at least one special character
#     has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

#     if has_digit and has_upper and has_special:
#         print("Valid password ✅")
#     else:
#         print("Invalid password ❌ (must include a digit, an uppercase letter, and a special character)")

# # Example usage:
# password = input("Enter a password to check: ")
# is_valid_password(password)


# Mask all email addresses in a text with [EMAIL HIDDEN].
# import re
# txt = "i logged into verity@gmail.com"
# x = re.sub(r"", txt)
# print(x)

# # Split a camelCase string into individual words.
# import re
# txt = "The rainIn Spain"
# x = re.split(r"[a-z]+[A-Z]?|([A-Z]?)", txt)
# print(x)


#perform tuple operations

my_tuple = (1,2,3,4,9)
x = list(my_tuple)
x.append(10)
x.insert(1,11)
x.remove(9)
new = tuple(x)
print(new)

