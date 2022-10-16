from scipy.spatial.distance import hamming
import numpy as np
import random

codeLength = 16
minDistance = 5
maxCodeInt = pow(2,16)
code = [ np.zeros(codeLength) ]

for i in range(maxCodeInt):
    listOfBits = [ int(x) for x in list( format( i, "b" ) ) ]
    candidate = np.pad( listOfBits, (codeLength-len(listOfBits),0) )
    if all([codeLength*hamming(candidate,member) >= minDistance for member in code]):
        code.append(candidate)

print(len(code))
