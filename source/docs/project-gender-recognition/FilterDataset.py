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
