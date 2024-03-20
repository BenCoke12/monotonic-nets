import numpy as np
import onnxruntime as ort
import tensorflow as tf
from tensorflow import keras
import onnx

#run the stacked projectile motion analytic network on given inputs
onnxName = 'analyticStack.onnx'

#input pair
x = [34.42492631006219, 34.42392631006219]

inX = np.array([x]).astype(np.float32)

ortSession = ort.InferenceSession(f"../onnx/{onnxName}")
ort_inputs = {ortSession.get_inputs()[0].name: inX}
onnx_result = ortSession.run(None, ort_inputs)

print("---Stacked Network---")
print("x:", x)
print("y:", onnx_result[0][0])

#run the non stacked network on the given inputs
analyticOnnx = 'analytic.onnx'

inx = np.array([[x[0]]]).astype(np.float32)

inxprime = np.array([[x[1]]]).astype(np.float32)

ortSession = ort.InferenceSession(f"../onnx/{analyticOnnx}")
ort_inputsx = {ortSession.get_inputs()[0].name: inx}

onnx_resultx = ortSession.run(None, ort_inputsx)

print("\n---Non-stacked Network---")
print("x:", x[0])
print("y:", onnx_resultx[0][0])

ort_inputsxprime = {ortSession.get_inputs()[0].name: inxprime}
onnx_resultxprime = ortSession.run(None, ort_inputsxprime)

print("xprime: ", x[1])
print("yprime:", onnx_resultxprime[0][0])