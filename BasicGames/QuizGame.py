# Python Quiz Game

# Tuple of questions:
 
questions = ("How many elements are in the periodic table? ", 
             "Which animal lays the largest eggs? ", 
             "What is the most abundant gas in Earth's atmosphere? ",
             "How many bones are in the human body? ",
             "Which planet in the solar system is the hottest? ")

# 2D Tuple of options (4 options for every question):

options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
           ("A. 206", "B. 207", "C. 208", "D. 209"), 
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# Tuple of answers:

answers = ("C", "D", "A", "A", "B")

# List of guesses (appending guesses to the list cannot be done with a tuple):

guesses = []


score = 0           # score variable tracks score
question_num = 0    # keeps track of the question

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    print()

    guess = input("Enter A, B, C, D: ").upper()
    print()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("------------------------")
print("        RESULTS         ")
print("------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)

print(f"Your score is: {score}%")
