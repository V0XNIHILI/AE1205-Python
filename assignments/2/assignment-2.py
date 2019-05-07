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
                sQuestion = sSplitLine[0]
                sNextOptions = sSplitLine[1]

                bAnswer = Input.IsTrue(Input.Ask(sQuestion, ["y", "n"]))

                iParameterToCheck = 0

                if bAnswer == False:
                    iParameterToCheck = 1

                sNextOption = sNextOptions.split(" / ")[iParameterToCheck].strip()

                if sNextOption.isdigit() == True:
                    counter = int(sNextOption)
                    continue

                bGuessCorrect = Input.IsTrue(Input.Ask("\n> I think I found your animal! Is it a(n) " + sNextOption + "?", ["y", "n"]))

                if bGuessCorrect == True:
                    print("> So I found your animal in " + str(iAmountOfSteps) + " steps! It turned out to be a(n) " + sNextOption)
                    break

                else:

                    iNewQuestionNumber = len(linQuestions)

                    # Update the question which wasn't good enough
                    linQuestions[counter] = linQuestions[counter].replace(sNextOption, str(iNewQuestionNumber))

                    sNewName = Input.Ask("\n> Enter the name of your new animal:")
                    sQuestionToDifferentiate = Input.Ask("> Enter a question to differentiate between the wrong and correct animal:")
                    
                    bAnswerToQuestionForCorrectAnimal = Input.IsTrue(Input.Ask("> What is the answer to this question for the correct animal? (y/n)", ["y", "n"]))

                    sNewQuestion = sQuestionToDifferentiate + " -> "

                    if bAnswerToQuestionForCorrectAnimal == True:
                        sNewQuestion += sNewName + " / " + sAnimalName

                    else:
                        sNewQuestion += sAnimalName + " / " + sNewName

                    # Add the new quesion to the list
                    linQuestions.append("\n" + sNewQuestion)

                    # Update animal question file
                    updateQuestionsFile = open("animals.vox", "w")
                    updateQuestionsFile.writelines(linQuestions)
                    updateQuestionsFile.close()

                    break

        # Ask if the user wants to try again
        sTryAgain = Input.Ask("\n> Do you want to try again?", ["y", "n"])   

        if Input.IsTrue(sTryAgain) == False:
            break

# Empty line so its easier to read
print("")