from maraboupy import Marabou
import numpy as np

# %%
# Set the Marabou option to restrict printing
options = Marabou.createOptions(verbosity = 0)#, produceProofs=True)


filename = "./onnx/3231poscaseStack.onnx"
network = Marabou.read_onnx(filename)


#input_bound = 10
epsilon = 0.00001
delta = 0.01

# %%
# Get the input and output variable numbers; [0] since first dimension is batch size
inputVars = network.inputVars[0][0]
outputVars = network.outputVars[0][0]

network.addInequality([inputVars[0], inputVars[3]], [-1, 1], -epsilon)
network.addEquality([inputVars[1], inputVars[4]], [1, -1], 0)
network.addEquality([inputVars[2], inputVars[5]], [1, -1], 0)

# %%
# Set input bounds
for inputVar in inputVars:
    network.setLowerBound(inputVar, -1.0)
    network.setUpperBound(inputVar, 1.0)

# %%
# Set output bounds
network.setUpperBound(outputVars[0], -delta)


# %%
# Call to Marabou solver
exitCode, vals, stats = network.solve(options = options)

print(vals)
