# Raghav Sriram
# Period 6 ML Gabor
# Chapter 16

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

# Uploaded is a dictionary containing the content of 'romeo_juliet.txt'
input_text = uploaded['romeo_juliet.txt'].decode("utf-8")

letter_corpus = sorted(set(input_text))
char_to_ind = {u:i for i, u in enumerate(letter_corpus)}
ind_to_char = np.array(letter_corpus)
encoded_text = np.array([char_to_ind[c] for c in input_text])

seq_len = 180
total_num_seq = len(input_text) // (seq_len + 1)

char_dataset = tf.data.Dataset.from_tensor_slices(encoded_text)
sequences = char_dataset.batch(seq_len + 1, drop_remainder=True)

def create_seq_targets(seq):
    input_txt = seq[:-1]  # Given input characters
    target_txt = seq[1:]  # Target character
    return input_txt, target_txt

dataset = sequences.map(create_seq_targets)

batch_size = 1
buffer_size = 10000
dataset = dataset.shuffle(buffer_size).batch(batch_size, drop_remainder=True)

vocab_size = len(letter_corpus)
embed_dim = 64
rnn_neurons = 1026

def sparse_cat_loss(y_true, y_pred):
    return sparse_categorical_crossentropy(y_true, y_pred, from_logits=True)

def create_model(vocab_size, embed_dim, rnn_neurons, batch_size):
    model = Sequential()
    model.add(Embedding(vocab_size, embed_dim, batch_input_shape=[batch_size, None]))
    model.add(GRU(rnn_neurons, return_sequences=True, stateful=True, recurrent_initializer='glorot_uniform'))
    model.add(Dense(vocab_size))
    model.compile(optimizer='adam', loss=sparse_cat_loss, metrics=['accuracy'])
    return model

model = create_model(vocab_size, embed_dim, rnn_neurons, batch_size)
model.summary()

# Training the model
epochs = 30
model.fit(dataset, epochs=epochs)

# Generating Text
def generate_text(model, start_seed, gen_size=100, temp=1.0):
    num_generate = gen_size
    input_eval = [char_to_ind[s] for s in start_seed]
    input_eval = tf.expand_dims(input_eval, 0)
    text_generated = []
    model.reset_states()
    
    for i in range(num_generate):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0)
        predictions = predictions / temp
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(ind_to_char[predicted_id])
        
    return (start_seed + ''.join(text_generated))

print(generate_text(model, "But", gen_size=1000))
