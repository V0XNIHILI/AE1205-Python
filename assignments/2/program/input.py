class Input:
    @staticmethod
    def Ask (questionText, allowedInputs = None, wrongInputText = "Your input is invalid. Please try again!"):
        sInput = ""

        sInputValid = False

        if allowedInputs == None:
            sInput = input(questionText + " ")

        else:
            while True:
                sInput = input(questionText + " ")

                for allowedInput in allowedInputs:
                    if sInput == allowedInput:
                        sInputValid = True
                        break
                
                if sInputValid == True:
                    break
                else:
                    print("\n> " + wrongInputText + "\n")
        
        return sInput

    def IsTrue (answerText):
        bAnswer = False

        if answerText == "y":
            bAnswer = True

        return bAnswer