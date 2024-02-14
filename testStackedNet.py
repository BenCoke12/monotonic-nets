import numpy as np
import onnxruntime as ort
import onnx
import sys

onnxName = '1yexStack.onnx'
onnx_model = onnx.load(f"./onnx/{onnxName}")

print(onnx.helper.printable_graph(onnx_model.graph))

print("-------")
print("       ")
print("-------")

print(onnx_model)

x = 0.2
xprime = 0.3

inX = np.array([[x]]).astype(np.float32)
inXprime = np.array([[xprime]]).astype(np.float32)

ortSession = ort.InferenceSession(f"./onnx/{onnxName}")

ort_inputs = {ortSession.get_inputs()[0].name: inX, 
              ortSession.get_inputs()[1].name: inXprime}
onnx_result = ortSession.run(None, ort_inputs)

print("x: ", x)
print("xprime: ", xprime)
print("result(x - xprime): ", onnx_result[0][0][0])