# Simple MNIST Classifier (TensorFlow / Keras)

Goal: recognize hand-written digits 0–9 using a small neural network.

⸻

## 🔧 Tech stack
	•	Python
	•	TensorFlow / Keras
	•	Matplotlib

⸻

## 📊 What it does
	•	Loads the MNIST dataset (hand-written digits).
	•	Normalizes images (pixel values → 0..1).
	•	Builds a simple neural network:
	•	Flatten (28×28 → 784 vector)
	•	Dense(128, ReLU) – hidden layer
	•	Dense(10, Softmax) – output layer (digits 0–9)
	•	Trains for 5 epochs.
	•	Test accuracy ≈ 0.98.
	•	Plots training vs test accuracy.

⸻

## 🚀 Run it
#Python 3.9+
pip install tensorflow matplotlib
python mnist_tf.py

## 📊 Result
	•	Final test accuracy: 97.7%
	•	Small simple model (1 hidden layer, 5 epochs) is enough to recognize handwritten digits well.

# 🇵🇱 Wersja Polska

Prosty klasyfikator MNIST (TensorFlow / Keras)

Cel: rozpoznawanie odręcznych cyfr 0–9 przy użyciu małej sieci neuronowej.

⸻

## 🔧 Stos technologiczny
	•	Python
	•	TensorFlow / Keras
	•	Matplotlib

⸻

## 📊 Co robi projekt
	•	Ładuje zbiór danych MNIST (odręczne cyfry).
	•	Normalizuje obrazy (wartości pikseli → 0..1).
	•	Buduje prostą sieć neuronową:
	•	Flatten (28×28 → wektor 784)
	•	Dense(128, ReLU) – warstwa ukryta
	•	Dense(10, Softmax) – warstwa wyjściowa (cyfry 0–9)
	•	Trenuje model przez 5 epok.
	•	Osiąga dokładność testową ≈ 0.98.
	•	Rysuje wykres: dokładność uczenia vs testowa.

⸻

## 🚀 Uruchomienie
#Python 3.9+
pip install tensorflow matplotlib
python mnist_tf.py

## 📊 Wyniki
	•	Końcowa dokładność testu: 97.7%
	•	Nawet mały, prosty model (1 warstwa ukryta, 5 epok) dobrze rozpoznaje cyfry odręczne.
