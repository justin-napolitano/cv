Gender Recognition with TensorFlow
========================================================

Description
----------------------

* Python scripts that call the TensorFlow API to categorize photos according to gender.


Links
------
* `Github <https://github.com/justin-napolitano/Gender-Recognition-from-image>`_


Data Preperation
-------------------

.. code-block:: python

   import logging
    import os

    import numpy as np
    import tensorflow as tf
    from tensorflow.python.framework import ops

    logger = logging.getLogger(__name__)


    def read_data(image_paths, label_list, image_size, batch_size, max_nrof_epochs, num_threads, shuffle, random_flip,
                random_brightness, random_contrast):
        """
        Creates Tensorflow Queue to batch load images. Applies transformations to images as they are loaded.
        :param random_brightness: 
        :param random_flip: 
        :param image_paths: image paths to load
        :param label_list: class labels for image paths
        :param image_size: size to resize images to
        :param batch_size: num of images to load in batch
        :param max_nrof_epochs: total number of epochs to read through image list
        :param num_threads: num threads to use
        :param shuffle: Shuffle images
        :param random_flip: Random Flip image
        :param random_brightness: Apply random brightness transform to image
        :param random_contrast: Apply random contrast transform to image
        :return: images and labels of batch_size
        """

        images = ops.convert_to_tensor(image_paths, dtype=tf.string)
        labels = ops.convert_to_tensor(label_list, dtype=tf.int32)

        # Makes an input queue
        input_queue = tf.compat.v1.train.slice_input_producer((images, labels),
                                                    num_epochs=max_nrof_epochs, shuffle=shuffle, )

        images_labels = []
        imgs = []
        lbls = []
        for _ in range(num_threads):
            image, label = read_image_from_disk(filename_to_label_tuple=input_queue)
            image = tf.compat.v1.random_crop(image, size=[image_size, image_size, 3])
            image.set_shape((image_size, image_size, 3))
            image = tf.image.per_image_standardization(image)

            if random_flip:
                image = tf.image.random_flip_left_right(image)

            if random_brightness:
                image = tf.image.random_brightness(image, max_delta=0.3)

            if random_contrast:
                image = tf.image.random_contrast(image, lower=0.2, upper=1.8)

            imgs.append(image)
            lbls.append(label)
            images_labels.append([image, label])

        image_batch, label_batch = tf.compat.v1.train.batch_join(images_labels,
                                                    batch_size=batch_size,
                                                    capacity=4 * num_threads,
                                                    enqueue_many=False,
                                                    allow_smaller_final_batch=True)
        return image_batch, label_batch


    def read_image_from_disk(filename_to_label_tuple):
        """
        Consumes input tensor and loads image
        :param filename_to_label_tuple: 
        :type filename_to_label_tuple: list
        :return: tuple of image and label
        """
        label = filename_to_label_tuple[1]
        file_contents = tf.io.read_file(filename_to_label_tuple[0])
        example = tf.image.decode_jpeg(file_contents, channels=3)
        return example, label


    def get_image_paths_and_labels(dataset):
        image_paths_flat = []
        labels_flat = []
        for i in range(int(len(dataset))):
            image_paths_flat += dataset[i].image_paths
            labels_flat += [i] * len(dataset[i].image_paths)
        return image_paths_flat, labels_flat


    def get_dataset(input_directory):
        dataset = []

        classes = os.listdir(input_directory)
        classes.sort()
        nrof_classes = len(classes)
        for i in range(nrof_classes):
            class_name = classes[i]
            facedir = os.path.join(input_directory, class_name)
            if os.path.isdir(facedir):
                images = os.listdir(facedir)
                image_paths = [os.path.join(facedir, img) for img in images]
                dataset.append(ImageClass(class_name, image_paths))

        return dataset


    def filter_dataset(dataset, min_images_per_label=10):
        filtered_dataset = []
        for i in range(len(dataset)):
            if len(dataset[i].image_paths) < min_images_per_label:
                logger.info('Skipping class: {}'.format(dataset[i].name))
                continue
            else:
                filtered_dataset.append(dataset[i])
        return filtered_dataset


    def split_dataset(dataset, split_ratio=0.8):
        train_set = []
        test_set = []
        min_nrof_images = 2
        for cls in dataset:
            paths = cls.image_paths
            np.random.shuffle(paths)
            split = int(round(len(paths) * split_ratio))
            if split < min_nrof_images:
                continue  # Not enough images for test set. Skip class...
            train_set.append(ImageClass(cls.name, paths[0:split]))
            test_set.append(ImageClass(cls.name, paths[split:-1]))
        return train_set, test_set


    class ImageClass():
        def __init__(self, name, image_paths):
            self.name = name
            self.image_paths = image_paths

        def __str__(self):
            return self.name + ', ' + str(len(self.image_paths)) + ' images'

        def __len__(self):
            return len(self.image_paths)

Data Preprocessing
--------------------

.. code-block:: python

   import argparse
    import glob
    import logging
    import multiprocessing as mp
    import os
    import time

    import cv2


    #import AlignDlib
    from align_dlib import AlignDlib

    logger = logging.getLogger(__name__)

    align_dlib = AlignDlib(os.path.join(os.path.dirname(__file__), 'shape_predictor_68_face_landmarks.dat'))


    def main(input_dir, output_dir, crop_dim):
        start_time = time.time()
        pool = mp.Pool(processes=mp.cpu_count())

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for image_dir in os.listdir(input_dir):
            image_output_dir = os.path.join(output_dir, os.path.basename(os.path.basename(image_dir)))
            if not os.path.exists(image_output_dir):
                os.makedirs(image_output_dir)

        image_paths = glob.glob(os.path.join(input_dir, '**/*.jpg'))
        for index, image_path in enumerate(image_paths):
            image_output_dir = os.path.join(output_dir, os.path.basename(os.path.dirname(image_path)))
            output_path = os.path.join(image_output_dir, os.path.basename(image_path))
            pool.apply_async(preprocess_image, (image_path, output_path, crop_dim))

        pool.close()
        pool.join()
        logger.info('Completed in {} seconds'.format(time.time() - start_time))


    def preprocess_image(input_path, output_path, crop_dim):
        """
        Detect face, align and crop :param input_path. Write output to :param output_path
        :param input_path: Path to input image
        :param output_path: Path to write processed image
        :param crop_dim: dimensions to crop image to
        """
        image = _process_image(input_path, crop_dim)
        if image is not None:
            logger.debug('Writing processed file: {}'.format(output_path))
            cv2.imwrite(output_path, image)
        else:
            logger.warning("Skipping filename: {}".format(input_path))


    def _process_image(filename, crop_dim):
        image = None
        aligned_image = None

        image = _buffer_image(filename)

        if image is not None:
            aligned_image = _align_image(image, crop_dim)
        else:
            raise IOError('Error buffering image: {}'.format(filename))

        return aligned_image


    def _buffer_image(filename):
        logger.debug('Reading image: {}'.format(filename))
        image = cv2.imread(filename, )
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image


    def _align_image(image, crop_dim):
        bb = align_dlib.getLargestFaceBoundingBox(image)
        aligned = align_dlib.align(crop_dim, image, bb, landmarkIndices=AlignDlib.INNER_EYES_AND_BOTTOM_LIP)
        if aligned is not None:
            aligned = cv2.cvtColor(aligned, cv2.COLOR_BGR2RGB)
        return aligned


    if __name__ == '__main__':
        input_directory = r'C:\Users\jnapolitano\OneDrive\Cox Oil\Cox_Oil_JNAP_Branch\Facial_Recognition\medium-facenet-tutorial\Data'
        output_directory = r'C:\Users\jnapolitano\OneDrive\Cox Oil\Cox_Oil_JNAP_Branch\Facial_Recognition\medium-facenet-tutorial\output'
        logging.basicConfig(level=logging.INFO)
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('--input-dir', type=str, action='store', default=input_directory, dest='input_dir')
        parser.add_argument('--output-dir', type=str, action='store', default=output_directory, dest='output_dir')
        parser.add_argument('--crop-dim', type=int, action='store', default=180, dest='crop_dim',
                            help='Size to crop images to')

        args = parser.parse_args()

        main(args.input_dir, args.output_dir, args.crop_dim)


Data Filtration
------------------

.. code-block:: python
    
    #FilterDataset.py
    import logging
    import os
    import argparse
    import math
    import shutil
    logger = logging.getLogger(__name__)

    def get_dataset(input_directory):
        dataset = []

        classes = os.listdir(input_directory)
        classes.sort()
        nrof_classes = len(classes)
        for i in range(nrof_classes):
            class_name = classes[i]
            facedir = os.path.join(input_directory, class_name)
            if os.path.isdir(facedir):
                images = os.listdir(facedir)
                image_paths = [os.path.join(facedir, img) for img in images]
                dataset.append(ImageClass(class_name, image_paths))

        return dataset

        #FilterDataset.py
    import logging
    import os
    import argparse
    import math
    import shutil
    logger = logging.getLogger(__name__)

    def get_dataset(input_directory):
        dataset = []

        classes = os.listdir(input_directory)
        classes.sort()
        nrof_classes = len(classes)
        for i in range(nrof_classes):
    def filter_dataset(dataset, min_images_per_label=10):
        bad_dataset = []
        good_dataset = []
        for i in range(len(dataset)):
            if len(dataset[i].image_paths) < min_images_per_label:
                logger.info('Skipping class: {}'.format(dataset[i].name))
                bad_dataset.append(dataset[i])
            else:
                good_dataset.append(dataset[i])
        return good_dataset, bad_dataset


    def clean_directory(input_dir,dataset,out_dir):
        if dataset == []:
            return False
        for image in dataset:
            for photo in image.image_paths:
            #directory_path = os.path.join(input_dir,image.name)
                shutil.copy(photo, out_dir)
            #print(directory_path)
        return True
            

    def validate_dataset(dataset,input_dir,output_dir):
        for image in dataset: 
            output = os.path.join(output_dir,image.name)
            os.makedirs(output)
            for i in range(image.quarter):
                shutil.move(image.image_paths[i],output)

    def test_dateset(dataset,good_dir,test_dir,validate_dir,input_dir):
        if dataset == []:
            return
        for image in dataset: 
            validate_output = os.path.join(validate_dir,image.name)
            test_output = os.path.join(test_dir,image.name)
            current_dir = os.path.join(input_dir,image.name)
            os.makedirs(validate_output)
            os.makedirs(test_output)
            for i in range(image.quarter):
                shutil.move(image.image_paths[i],validate_output)

            for i in range(image.quarter,len(image)):
                shutil.move(image.image_paths[i],test_output)
        #os.rmdir(current_dir)
        
    class ImageClass():
        def __init__(self, name, image_paths):
            self.name = name
            self.image_paths = image_paths
            self.quarter = math.floor(len(self.image_paths)/4)

        def __str__(self):
            return self.name + ', ' + str(len(self.image_paths)) + ' images'

        def __len__(self):
            return len(self.image_paths)


    def validate_data(input_directory):
        classes = os.listdir(input_directory)
        nrof_classes = len(classes)
        elist = []
        for i in range(nrof_classes):
            class_name = classes[i]
            print(class_name)
            classdir = os.path.join(input_directory, class_name)
            files = os.listdir(classdir)
            for f in files:
                f_extns = f.split(".")
                elist.append(f_extns[-1])
                #print(f_extns)
        elist.sort()
        print(elist)
        
    if __name__ == "__main__":


    #its interesting that i use a windows machine to write this code.  That must have been the one and only time. 

        parser = argparse.ArgumentParser(add_help=True)
        input_dir = r'C:\Users\jnapolitano\OneDrive - Napolitano\projects\python\GenderRecognition\raw_data'
        bad_dir = r'C:\Users\jnapolitano\OneDrive - Napolitano\projects\python\GenderRecognition\processed_data\bad'
        good_dir = r'C:\Users\jnapolitano\OneDrive - Napolitano\projects\python\GenderRecognition\processed_data\good'
        test_dir = r'C:\Users\jnapolitano\OneDrive - Napolitano\projects\python\GenderRecognition\processed_data\test'
        validate_dir = r'C:\Users\jnapolitano\OneDrive - Napolitano\projects\python\GenderRecognition\processed_data\validate'



        parser.add_argument('--input-dir', type=str, action='store', default=input_dir, dest='input_dir',
                            help='Input path of data to train on')
        #dataset = get_dataset(input_dir)
        #print(dataset[2].image_paths)
        #good_dataset,bad_dataset = filter_dataset(dataset)
        #print(delete_dataset[2].name)
        #move_bad = clean_directory(input_dir,bad_dataset,bad_dir)
        #move_good = clean_directory(input_dir,good_dataset,good_dir)
        #validate_dataset(dataset,good_dir,validate_dir)
        #test_dateset(dataset,good_dir,test_dir, validate_dir, good_dir)
        validate_data(test_dir)


Model Training and Verification
---------------------------------

.. code-block:: python
    

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
