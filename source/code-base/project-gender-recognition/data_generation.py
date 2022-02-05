import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import matplotlib.pyplot as plt
#from keras import backend as K
#K.set_image_dim_ordering('th')

def main():
    data_directory = r'C:\Users\jnapolitano\OneDrive - Napolitano\projects\python\GenderRecognition'
    train_dir = r'C:\Users\jnapolitano\OneDrive - Napolitano\projects\python\GenderRecognition\processed_data\test'
    validation_dir = r'C:\Users\jnapolitano\OneDrive - Napolitano\projects\python\GenderRecognition\processed_data\validate'
    count = 0
    for root, dirs, files in os.walk(train_dir, topdown=False):
        for name in files:
            #print(name)
            count +=1
    total_train = count
   # print(count)
    count = 0
    for root, dirs, files in os.walk(validation_dir, topdown=False):
        for name in files:
            #print(name)
            count +=1

    
    total_val = count
    #print(total_train)
    #print(total_val)
    batch_size = 20
    epochs = 100
    IMG_HEIGHT = 224
    IMG_WIDTH = 224

    train_data_gen, val_data_gen = create_generators(train_dir,validation_dir,batch_size,IMG_HEIGHT, IMG_WIDTH)
    model = create_model(IMG_HEIGHT,IMG_WIDTH)
    history = run_model(model, train_data_gen,val_data_gen,total_train,batch_size,epochs,total_val)
    plot_data(history,epochs)
 
def create_generators(train_dir, validation_dir, batch_size, IMG_HEIGHT,IMG_WIDTH):


    image_gen_train = ImageDataGenerator(
                        rescale=1./255,
                        rotation_range=45,
                        width_shift_range=.15,
                        height_shift_range=.15,
                        horizontal_flip=True,
                        zoom_range=0.5
                        )
    image_gen_val = ImageDataGenerator(rescale=1./255)




    train_data_gen = image_gen_train.flow_from_directory(batch_size=batch_size,
                                                        directory=train_dir,
                                                        shuffle=True,
                                                        target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                        class_mode='binary')

    val_data_gen = image_gen_val.flow_from_directory(batch_size=batch_size,
                                                    directory=validation_dir,
                                                    target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                    class_mode='binary')
    
    return train_data_gen, val_data_gen

def create_model(IMG_HEIGHT,IMG_WIDTH):
 
    IMG_SHAPE = (IMG_HEIGHT, IMG_WIDTH, 3)
    base_model = tf.keras.applications.MobileNetV2(input_shape=(IMG_HEIGHT, IMG_WIDTH, 3),
                                               include_top=False)
    #base_model.trainable = False
    base_model.trainable = True
    fine_tune_at = 100
    for layer in base_model.layers[:fine_tune_at]:
        layer.trainable = False

    model = tf.keras.Sequential([
        base_model,  # 1
        tf.keras.layers.Conv2D(32, 3, activation='relu'),  # 2
        tf.keras.layers.Dropout(0.2),  # 3
        tf.keras.layers.GlobalAveragePooling2D(),  # 4
        Dense(1, activation='relu')  # 5
    ])

    model.compile(optimizer='adam',
                loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                metrics=['accuracy'])

    model_new = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', 
           input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
    MaxPooling2D(),
    Dropout(0.2),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Dropout(0.2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1)
    ])

    model_new.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    
    return model_new


def run_model(model, train_data_gen,val_data_gen,total_train,batch_size,epochs,total_val):

    history = model.fit(
        train_data_gen,
        steps_per_epoch=total_train // batch_size,
        epochs=epochs,
        validation_data=val_data_gen,
        validation_steps=total_val // batch_size
    )

    return history
def plot_data(history, epochs):


    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss=history.history['loss']
    val_loss=history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()


if __name__ == '__main__':
    main()