import numpy as np
import onnxruntime as ort
import tensorflow as tf
from tensorflow import keras
import onnx
import sys

onnxName = '3231negcaseBase.onnx'
#onnx_model = onnx.load(f"./onnx/{onnxName}")

x = [-0.8057954545454548, 0.9999999999999998, 0.20386363636363658]

inX = np.array([x]).astype(np.float32)

ortSession = ort.InferenceSession(f"./onnx/{onnxName}")
ort_inputs = {ortSession.get_inputs()[0].name: inX}
onnx_result = ortSession.run(None, ort_inputs)

print("x:", x)
print("y:", onnx_result[0][0][0])

x2 = [-0.8397727272727274, 1.0, 0.20386363636363658]

inX2 = np.array([x]).astype(np.float32)

ortSession = ort.InferenceSession(f"./onnx/{onnxName}")
ort_inputs2 = {ortSession.get_inputs()[0].name: inX2}
onnx_result2 = ortSession.run(None, ort_inputs2)

print("x2:", x2)
print("y2:", onnx_result[0][0][0])