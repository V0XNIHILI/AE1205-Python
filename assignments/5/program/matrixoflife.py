import random
import numpy

class MatrixOfLife:

    def __init__ (self, matrixWidth, matrixHeight, populateRandomly):

        self.matrixWidth = matrixWidth
        self.matrixHeight = matrixHeight

        self.matrix = numpy.zeros(shape=(self.matrixWidth, self.matrixHeight))

        if populateRandomly == True:
            for iCurrentWidth in range(self.matrixWidth):
                for iCurrentHeight in range(self.matrixHeight):
                        value = random.randint(0, 1)
                        
                        self.matrix[iCurrentWidth, iCurrentHeight] = value

    def evolve (self):

        paddedMatrix = numpy.zeros(shape=(self.matrixWidth + 2, self.matrixHeight + 2))
        paddedMatrix[1:1+self.matrix.shape[0], 1:1+self.matrix.shape[1]] = self.matrix

        # Using numpy.roll we move the original matrix up, down,
        # right, left, right up, left up, right down and left down

        shiftedMatrixUp = numpy.roll(paddedMatrix, -1, axis=0)
        shiftedMatrixDown = numpy.roll(paddedMatrix, 1, axis=0)
        shiftedMatrixRight= numpy.roll(paddedMatrix, 1, axis=1)
        shiftedMatrixLeft = numpy.roll(paddedMatrix, -1, axis=1)

        shiftedMatrixRightUp = numpy.roll(shiftedMatrixUp, 1, axis=1)
        shiftedMatrixLeftUp = numpy.roll(shiftedMatrixUp, -1, axis=1)
        shiftedMatrixRightDown = numpy.roll(shiftedMatrixDown, 1, axis=1)
        shiftedMatrixLeftDown = numpy.roll(shiftedMatrixDown, -1, axis=1)

        decisionMatrix = numpy.sum([shiftedMatrixUp, shiftedMatrixDown, shiftedMatrixRight, shiftedMatrixLeft, shiftedMatrixRightUp, shiftedMatrixLeftUp, shiftedMatrixRightDown, shiftedMatrixLeftDown], axis=0)

        # Because of the fact that the matrix is padded,
        # we need to skip the padding while looping through the matrix

        for iCurrentWidth in range(self.matrixWidth):
            for iCurrentHeight in range(self.matrixHeight):
                    decisionValue = decisionMatrix[iCurrentWidth + 1, iCurrentHeight + 1]

                    # Implement the Game of Life rules
                    if decisionValue <= 1:
                        self.matrix[iCurrentWidth, iCurrentHeight] = 0

                    elif decisionValue == 3:
                        self.matrix[iCurrentWidth, iCurrentHeight] = 1

                    elif decisionValue >= 4:
                        self.matrix[iCurrentWidth, iCurrentHeight] = 0

    def tostring (self):

        print(self.matrix)
