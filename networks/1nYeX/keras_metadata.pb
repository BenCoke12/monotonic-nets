
�root"_tf_keras_sequential*�{"name": "sequential", "trainable": true, "expects_training_arg": true, "dtype": "float32", "batch_input_shape": null, "must_restore_from_config": false, "preserve_input_structure_in_config": false, "autocast": false, "class_name": "Sequential", "config": {"name": "sequential", "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "dense_input"}}, {"class_name": "Dense", "config": {"name": "dense", "trainable": true, "dtype": "float32", "units": 1, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "Ones", "config": {}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": {"class_name": "MinMaxNorm", "config": {"min_value": 1.0, "max_value": 1.0, "rate": 1.0, "axis": 1}}, "bias_constraint": {"class_name": "MinMaxNorm", "config": {"min_value": 0.0, "max_value": 0.0, "rate": 1.0, "axis": 0}}}}]}, "shared_object_id": 6, "build_input_shape": {"class_name": "TensorShape", "items": [null, 1]}, "is_graph_network": true, "full_save_spec": {"class_name": "__tuple__", "items": [[{"class_name": "TypeSpec", "type_spec": "tf.TensorSpec", "serialized": [{"class_name": "TensorShape", "items": [1, 1]}, "float32", "dense_input"]}], {}]}, "save_spec": {"class_name": "TypeSpec", "type_spec": "tf.TensorSpec", "serialized": [{"class_name": "TensorShape", "items": [1, 1]}, "float32", "dense_input"]}, "keras_version": "2.13.1", "backend": "tensorflow", "model_config": {"class_name": "Sequential", "config": {"name": "sequential", "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 1]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "dense_input"}, "shared_object_id": 0}, {"class_name": "Dense", "config": {"name": "dense", "trainable": true, "dtype": "float32", "units": 1, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 1}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 2}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": {"class_name": "MinMaxNorm", "config": {"min_value": 1.0, "max_value": 1.0, "rate": 1.0, "axis": 1}, "shared_object_id": 3}, "bias_constraint": {"class_name": "MinMaxNorm", "config": {"min_value": 0.0, "max_value": 0.0, "rate": 1.0, "axis": 0}, "shared_object_id": 4}}, "shared_object_id": 5}]}}}2
�	root.layer_with_weights-0"_tf_keras_layer*�	{"name": "dense", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "preserve_input_structure_in_config": false, "autocast": true, "class_name": "Dense", "config": {"name": "dense", "trainable": true, "dtype": "float32", "units": 1, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "Ones", "config": {}, "shared_object_id": 1}, "bias_initializer": {"class_name": "Zeros", "config": {}, "shared_object_id": 2}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": {"class_name": "MinMaxNorm", "config": {"min_value": 1.0, "max_value": 1.0, "rate": 1.0, "axis": 1}, "shared_object_id": 3}, "bias_constraint": {"class_name": "MinMaxNorm", "config": {"min_value": 0.0, "max_value": 0.0, "rate": 1.0, "axis": 0}, "shared_object_id": 4}}, "shared_object_id": 5, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 1}}, "shared_object_id": 7}, "build_input_shape": {"class_name": "TensorShape", "items": [1, 1]}}2