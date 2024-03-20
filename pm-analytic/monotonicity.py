from maraboupy import Marabou
import numpy as np

# Set the Marabou option to restrict printing
options = Marabou.createOptions(verbosity = 0)#, produceProofs=True)

filename = "../onnx/analyticStack.onnx"
network = Marabou.read_onnx(filename)

# %%
# Get the input and output variable numbers; [0] since first dimension is batch size
inputVars = network.inputVars[0][0]
outputVars = network.outputVars[0][0]

network.addInequality([inputVars[0], inputVars[1]], [-1, 1], -0.001)
network.addInequality([outputVars[0], outputVars[1]], [1, -1], 0)

for inputVar in inputVars:
    network.setLowerBound(inputVar, 0.0)
    network.setUpperBound(inputVar, 40.0)

# %%
# Call to Marabou solver
exitCode, vals, stats = network.solve(options = options)
