# North Seattle College, CSC 110
# Lab Week 10
# Author: Luca Andolina
# Email: luca627@comcast.net

# global constants:
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)

# first main function here simply to display the welcome message once.
def main():
    print("Welcome to the Vigenere Cipher!")




#  second main function definition:
def main2():
    # User interface:
    print("Enter 1 to encrypt a message.")
    print("Enter 2 to decrypt a message.")
    print("Enter 0 to exit.")
    print()
    choice = int(input("What would you like to do? "))

#If statement that calls a function if user enters 1    
        
    if (choice == 1 ):
        plaintext = str(input("Enter a plaintext message to encrypt: "))
        key = (input("Enter a message to use as the key: "))        
        one = enc(key, plaintext)
        print (one)
        print ("")
        main2()
        

#If statement that calls a function if user enters 2      


    if (choice == 2 ):
        plaintext = str(input("Enter a ciphertext message to decrypt: "))
        key = (input("Enter a message to use as the key: "))        
        one = dec(key, plaintext)
        print (one)
        print ("")
        main2()
    
    
# This funciton encrypts a message using a Vigenere cipher
# parameter: a string that defines the number of positions to shift after added with the first message
# parameter: plaintext, a string that is the message in plaintext
# returns the encrypted message as a ciphertext
def enc(key, plaintext):
    
    ciphertext ="Resulting ciphertext: "
    for i in range(len(plaintext)):
      
        if plaintext[i] == " ":
            ciphertext += " "
        
            
            
        else:
        

            char_pos = ALPHABET.index(plaintext[i])
            char_pos2 = ALPHABET.index(key[i%len(key)])
            new_pos = ((char_pos + char_pos2)% ALPHABET_SIZE)
            enc_char = ALPHABET[new_pos]
            ciphertext += enc_char
            
    return ciphertext

# This funciton decrypts a message using a Vigenere cipher
# parameter: key, a string that defines the number of positions to shift after added with the first message
# parameter: ciphertext, a string that is the message as a ciphertext
# returns the decrypted message as a plaintext
def dec(key, ciphertext):
    plaintext ="Resulting plaintext: " ""
    for i in range(len(ciphertext)):
        if ciphertext[i] == " ":
            plaintext += " "
        
            
            
        else:

            char_pos = ALPHABET.index(ciphertext[i])
            char_pos2 = ALPHABET.index(key[i%len(key)])
            new_pos = ((char_pos - char_pos2)% ALPHABET_SIZE)
            enc_char = ALPHABET[new_pos]
            plaintext += enc_char
    return plaintext

# call to main:
main()
main2()
