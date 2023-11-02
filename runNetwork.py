import numpy as np
import onnxruntime as ort
import tensorflow as tf
from tensorflow import keras
import onnx
import sys

onnxName = '1nYeX.onnx'
#onnx_model = onnx.load(f"./onnx/{onnxName}")

x = 0.5

inX = np.array([[x]]).astype(np.float32)

ortSession = ort.InferenceSession(f"./onnx/{onnxName}")
ort_inputs = {ortSession.get_inputs()[0].name: inX}
onnx_result = ortSession.run(None, ort_inputs)

print("x:", x)
print("y:", onnx_result[0][0][0])
