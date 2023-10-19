import numpy as np
import onnxruntime as ort
import tensorflow as tf
from tensorflow import keras
import onnx
import sys

onnxName = '1nYeX.onnx'
onnx_model = onnx.load(f"./onnx/{onnxName}")

print(onnx.helper.printable_graph(onnx_model.graph))

print("-------")
print("       ")
print("-------")


weights = onnx_model.graph.initializer
print(onnx.numpy_helper.to_array(weights[0]))

print("-------")
print("       ")
print("-------")

x = 0.2

inX = np.array([[x]]).astype(np.float32)

ortSession = ort.InferenceSession(f"./onnx/{onnxName}")
ort_inputs = {ortSession.get_inputs()[0].name: inX}
onnx_result = ortSession.run(None, ort_inputs)

print("x:", x)
print("y:", onnx_result[0][0][0])

for i in range(10):
    j = i/10

    inX = np.array([[j]]).astype(np.float32)

    ortSession = ort.InferenceSession(f"./onnx/{onnxName}")
    ort_inputs = {ortSession.get_inputs()[0].name: inX}
    onnx_result = ortSession.run(None, ort_inputs)

    print("x:", j)
    print("y:", onnx_result[0][0][0])