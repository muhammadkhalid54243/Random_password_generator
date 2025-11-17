import random
import string

def random_password_generator():
    length = int(input("Enter desired length of the supposed password").strip())
    is_upper = input("password should include uppercase letters?(yes/no)").strip().lower()
    is_digits = input("password should include digits?(yes/no)").strip().lower()
    is_special = input("password should include special characters?(yes/no)").strip().lower()
    
    # the password length must be atleast 4 characters
    if length < 4:
        print("password length must be atleast four characters")
        return "program crashes"
    
    # getting all possiable characters 
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase if is_upper == "yes" else ""
    digits = string.digits if is_digits == "yes" else ""
    specials = string.punctuation if is_special == "yes" else ""
    
    # concatination all the characters into one string
    all_characters = lowers + uppers + digits + specials
    
    # take the must have character types
    required_characters = []
    if is_digits == "yes":
        required_characters.append(random.choice(digits))
    if is_upper == "yes":
        required_characters.append(random.choice(uppers))
    if is_special == "yes":
        required_characters.append(random.choice(specials))
    
    # getting the remaining lenght the should be included in password
    remaing_length = length - len(required_characters)
    
    password = required_characters
    
    
    # add the remaining characters to the password beside the required ones
    for _ in range(remaing_length):
        password.append(random.choice(all_characters))
    
    # shuffles the character to more randomized it
    random.shuffle(password)
    
    # convert the password list to a string so it can be used
    string_password = "".join(password)
    
        
    return string_password
    
    



#calling fucntion
print(random_password_generator())
