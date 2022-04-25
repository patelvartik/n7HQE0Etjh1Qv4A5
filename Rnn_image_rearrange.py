# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:53:51 2022

@author: patel
"""

import os
import shutil

def get_images(path2ajpgs):
    listOfClasses = os.listdir(path2ajpgs)
    ids = []
    labels = []
    for catg in listOfClasses:
        path2catg = os.path.join(path2ajpgs, catg)
        listOfSubCats = os.listdir(path2catg)
        path2subCats= [os.path.join(path2catg,los) for los in listOfSubCats]
        ids.extend(path2subCats)
        labels.extend([catg]*len(listOfSubCats))
    return ids, labels, listOfClasses 

### Training
training_dir = os.path.join('MonReader_images', 'training')

train_ids,train_labels,catgs = get_images(training_dir)

new_training_dir = os.path.join('MonReader_images_Rnn', 'training')

for i,oldpath in enumerate(train_ids) :
    new_folder_path= os.path.join(new_training_dir,train_labels[i],oldpath[-18:-14])
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        
    newpath=os.path.join(new_folder_path,oldpath[-13:])
    print(oldpath)
    print(newpath)
    
    shutil.copyfile(oldpath, newpath)
    
### Testing
testing_dir = os.path.join('MonReader_images', 'testing')

test_ids,test_labels,catgs = get_images(testing_dir)

new_testing_dir = os.path.join('MonReader_images_Rnn', 'testing')

for i,oldpath in enumerate(test_ids) :
    new_folder_path= os.path.join(new_testing_dir,test_labels[i],oldpath[-18:-14])
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        
    newpath=os.path.join(new_folder_path,oldpath[-13:])
    print(oldpath)
    print(newpath)
    
    shutil.copyfile(oldpath, newpath)