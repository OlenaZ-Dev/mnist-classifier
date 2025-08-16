# Simple MNIST classifier (TensorFlow / Keras)
# Goal: recognize hand-written digits 0–9

import tensorflow
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load data
# x_* are images (28x28, grayscale), y_* are labels (0..9)
(x_train, y_train), (x_test, y_test) =  tensorflow.keras.datasets.mnist.load_data()


# Normalize pixels to 0..1 so training is more stable
x_train, x_test = x_train/ 255.0, x_test/255.0

# Build a small neural network
# - Flatten: turn 28x28 image into a vector (784 numbers)
# - Dense(128, relu): hidden layer that learns useful patterns
# - Dense(10, softmax): output probabilities for digits 0..9
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'), 
    layers.Dense(10, activation='softmax')
])

# Choose how to train
# - optimizer='adam': popular choice, usually works well
# - loss='sparse_categorical_crossentropy': labels are integers (0..9)
# - metrics=['accuracy']: show percent of correct predictions
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# Train for 5 epochs.
# We also check test set each epoch as "validation_data"
history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Final evaluation on the test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")


# Plot learning curves: train vs test accuracy
plt.plot(history.history['accuracy'], label='Train accuracy')
plt.plot(history.history['val_accuracy'], label='Test accuracy')
plt.legend()
plt.show()

