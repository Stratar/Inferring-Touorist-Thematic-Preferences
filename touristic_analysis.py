import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Embedding, LSTM, Input, concatenate
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import data_preprocessing as dp


# Tokenize the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Pad sequences to ensure consistent length
max_length = 100  # specify the desired length of sequences
padded_sequences = pad_sequences(sequences, maxlen=max_length)

# Text input branch
text_input_dim = padded_sequences.shape[1]  # dimension of input text sequences
embedding_dim = 100  # specify the desired embedding dimension

text_input = Input(shape=(text_input_dim,))
embedding_layer = Embedding(input_dim, embedding_dim, input_length=text_input_dim)(text_input)
lstm_layer = LSTM(64)(embedding_layer)

# Numerical input branch
numerical_input_dim = numerical_data.shape[1]  # dimension of numerical input data

numerical_input = Input(shape=(numerical_input_dim,))
dense_layer = Dense(32, activation='relu')(numerical_input)

# Concatenate text and numerical branches
concatenated = concatenate([lstm_layer, dense_layer])

# Output layer
output = Dense(num_classes, activation='softmax')(concatenated)

# Create the model
model = keras.Model(inputs=[text_input, numerical_input], outputs=output)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit([padded_sequences, numerical_data], labels, epochs=num_epochs, batch_size=batch_size)

loss, accuracy = model.evaluate([test_text_sequences, test_numerical_data], test_labels)
predictions = model.predict([test_text_sequences, test_numerical_data])
