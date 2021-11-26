#!/usr/bin/env python3
"""
Author : mhmarand <mhmarand@localhost>
Date   : 2021-11-22
Purpose: A Silly word game popularly known as Mad Libs 
"""
#-------------------------------------------------------------------------------------------------------
def main():
#Game Introduction

    print("Hello, Welcome to Mad Libs!".center(80))
    print("Enter a word when prompted to to make a suprise statement!".center(80))
    str(input("Press Enter to Start".center(80)))

#Getting User input on different words to enter into the paragraph

    Name = str(input("Enter a Name: ")) 
    Verb = str(input("Enter a Verb: "))
    Noun = str(input("Enter a Noun: "))
    Part = str(input("Enter a body Part: "))
    Name2 = str(input("Enter the name of a significant other: "))
    Verb2 = str(input("Enter a Verb: "))
    Adjective = str(input("Enter an adjective: "))
    Noun2 = str(input("Enter a Noun: "))
    Verb3 = str(input("Enter a Verb: "))
    Occupation = str(input("Enter an occupation: "))
    Number = str(input("Enter a Number: "))
    Verb4 = str(input("Enter a Verb: "))
    Name3 = str(input("Enter your name: ")) 

# Printing the statement and filling in with user inputs

    print("A Marriage Proposal Letter:". center(80))
    print("Dear Mr. and Mrs.", Name,",")

    print("Will you let me", Verb, "your", Noun,"?")
    print("Ever since I have laid", Part, "on", Name2, "I have", Verb2, "madly in love with them.")
    print("They are the most", Adjective, Noun2, "I have ever seen and I hope that someday we will", Verb3, "happily ever after.")
    print("I have a job as a/an" ,Occupation, "that pays", Number, "dollars each month.")
    print("I promise to", Verb4, "them with kindness and respect.")

    print("Sincerely,")
    print(Name3)

    restart()
# giving the user the option to quit or play again
def restart():
    Replay= str(input("Would you like to replay? (y/n)"))
    if Replay == "y":
        main()
    elif Replay== "n":
        print("Thanks for playing!")
        quit()
    else:
        print("Please enter a valid input y or n")
        restart()

while True:
     main()