from maraboupy import Marabou
import numpy as np

# %%
# Set the Marabou option to restrict printing
options = Marabou.createOptions(verbosity = 0)


filename = "./onnx/1nyexStack.onnx"
network = Marabou.read_onnx(filename)


input_bound = 10
epsilon = 0.0001

# %%
# Get the input and output variable numbers; [0] since first dimension is batch size
inputVars = network.inputVars[0][0]
outputVars = network.outputVars[0][0]

network.addInequality([inputVars[0], inputVars[1]], [-1, 1], 0)

# %%
# Set input bounds
for inputVar in inputVars:
    network.setLowerBound(inputVar, -10.0)
    network.setUpperBound(inputVar, 10.0)

# %%
# Set output bounds
network.setUpperBound(outputVars[0], -epsilon)


# %%
# Call to Marabou solver
exitCode, vals, stats = network.solve(options = options)
