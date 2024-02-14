import numpy as np
import onnx
import onnx.compose
import spox.opset.ai.onnx.v17 as op
from spox import argument, build, inline, Tensor

# I'll assume your model inputs are some tensors a, b of these types
# You can adapt this to your case
a = argument(Tensor(np.float32, (1, 1)))
b = argument(Tensor(np.float32, (1, 1)))

print(f"{Tensor(np.float32, (1, 1)) = !s}")

# Load the models
model1 = onnx.load("onnx/1nYeX.onnx")
model2 = onnx.load("onnx/1nYeX.onnx")

# Inline the models and forward the arguments
# Also unwrap all the results - here assume there's just one
(r1,) = inline(model1)(a).values()
(r2,) = inline(model2)(b).values()
#print(inline(model1)(a).values())
#print(r1)
#print(r2)
# Subtract the x' network from the x network -> will be asking that r < 0
# This assumes the outputs are float32 (as op.constant(value_float=...) is)
r = op.sub(r1, r2)
#print(r)

# Build the composed model with given model inputs and outputs (with names)
model = build({'x': a, 'xprime': b}, {'result': r})

onnx.save(model, "onnx/1yexStack.onnx")