import random
import string

# Lists of words to use in the username
adjectives = ["Swift", "Brave", "Fierce", "Witty", "Epic", "Crazy", "Mighty", "Sneaky"]
nouns = ["Dragon", "Warrior", "Ninja", "Panda", "Falcon", "Knight", "Gamer", "Wizard"]

# Function to generate a random username
def generate_username(include_numbers=True, include_special_chars=True,length=0):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    return username[:length]

# Function to save the username to a file
def save_username(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")

# User interactive mode
if __name__ == "__main__":
    print("Welcome to the Random Username Generator!")
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    length = int(input("Enter the maximum length of the username: "))
    
    for _ in range(num_usernames):
        username = generate_username(include_numbers, include_special_chars, length)
        print("Generated Username:", username)
        save_username(username)
    
    print("Usernames saved to usernames.txt!")