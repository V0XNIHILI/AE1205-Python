# ------------------------------------------------------
# Property definitions [SI UNITS!]
# ------------------------------------------------------

import os
from input import Input

# ------------------------------------------------------
# Terminal Setup
# ------------------------------------------------------

print("")
print("=============================")
print("| V0X's Easy Animal Guesser |")
print("=============================")
print("\nLast edited on 7 May 2019")
print("\n------------------------------\n")

print("> Think of an animal. I will try to guess it.")

# ------------------------------------------------------
# Guessing
# ------------------------------------------------------

iAmountOfSteps = 0

# Open the questions file if it exists, else create a new file
if os.path.isfile("animals.vox"):

    while True:

        questionsFile = open("animals.vox", "r")
        linQuestions = questionsFile.readlines()
        questionsFile.close()

        if len(linQuestions) != 0:

            # Empty line so its easier to read
            print("")

            counter = 0

            while True:

                iAmountOfSteps += 1

                sSplitLine = linQuestions[counter].split(" -> ")
                sNextOptions = sSplitLine[1]

                sQuestion = sSplitLine[0]
                sAnswer = Input.Ask(sQuestion, ["y", "n"])
                bAnswer = Input.IsTrue(sAnswer)

                iParameterToCheck = 0

                if bAnswer == False:
                    iParameterToCheck = 1

                if str.isdigit(sNextOptions.split(" / ")[iParameterToCheck].strip()) == True:
                    counter = int(sNextOptions.split(" / ")[iParameterToCheck].strip())
                    continue

                sAnimalName = sNextOptions.split(" / ")[iParameterToCheck].strip()

                sGuessCorrect = Input.Ask("\n> I think I found your animal! Is it a(n) " + sAnimalName + "?", ["y", "n"])
                bGuessCorrect = Input.IsTrue(sGuessCorrect)

                if bGuessCorrect == True:
                    print("> So I found your animal! It turned out to be a(n) " + sAnimalName)
                    break

                else:

                    iNewQuestionNumber = len(linQuestions)
                    linQuestions[counter] = linQuestions[counter].replace(sAnimalName, str(iNewQuestionNumber))

                    sNewName = Input.Ask("\n> Enter the name of your new animal:")
                    sQuestionToDifferentiate = Input.Ask("> Enter a question to differentiate between the wrong and correct animal:")
                    
                    sAnswerToQuestionForCorrectAnimal = Input.Ask("> What is the answer to this question for the correct animal? (y/n)", ["y", "n"])
                    bAnswerToQuestionForCorrectAnimal = Input.IsTrue(sAnswerToQuestionForCorrectAnimal)

                    sNewQuestion = sQuestionToDifferentiate + " -> "

                    if bAnswerToQuestionForCorrectAnimal == True:
                        sNewQuestion += sNewName + " / " + sAnimalName

                    else:
                        sNewQuestion += sAnimalName + " / " + sNewName

                    linQuestions.append("\n" + sNewQuestion)

                    # Update animal question file
                    updateQuestionsFile = open("animals.vox", "w")
                    updateQuestionsFile.writelines(linQuestions)
                    updateQuestionsFile.close()

                    break

        sTryAgain = Input.Ask("\n> Do you want to try again?", ["y", "n"])   

        if Input.IsTrue(sTryAgain) == False:
            break

# Empty line so its easier to read
print("")