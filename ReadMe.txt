
*************************************************************************************************
This is a python code to read epoch information produced by CNN and store into Excel sheet
*************************************************************************************************

Package Version
python 3.6.8
pandas 0.24.1

This python code is most handy to extract details that are collected during Convolutional Neural Network epoch.

During training phase of a CNN will generate information related to epochs.

The information generated during Epoch as example:

Number of train samples in Dataset:  482
Number of test samples in Dataset:  121
Train on 482 samples, validate on 121 samples
Epoch 1/10

 10/482 [..............................] - ETA: 2:45 - loss: 2.3024 - acc: 0.0000e+00
 20/482 [>.............................] - ETA: 2:15 - loss: 2.2919 - acc: 0.1500    
 30/482 [>.............................] - ETA: 2:03 - loss: 2.2769 - acc: 0.3333
 40/482 [=>............................] - ETA: 1:56 - loss: 2.2564 - acc: 0.4000
 50/482 [==>...........................] - ETA: 1:49 - loss: 2.2267 - acc: 0.4800
 60/482 [==>...........................] - ETA: 1:44 - loss: 2.1841 - acc: 0.5167
........
482/482 [==============================] - 114s 237ms/step - loss: 0.7871 - acc: 0.7842 - val_loss: 0.6362 - val_acc: 0.6942

There are 482 samples in training and 121 in test samples.
It will iterate through 482 images and produces the loss and accuracy measurements.
At the end of 482 sample it will provide very valuable results such as loss and accuracy in training and testing sets.

This program will read the given such a result file and extract information related to epochs then produce an Excel file.  

See the output as an example the file epochsResIntoExcel.xls.

How to run this python code?
The input to this python code is a text file which is generated during Deep Learning training phase.
An example of the input text file CNN1_5CV.txt is kept in model1 folder.

You need to change to current directory and download the folders model1 along with python code collectResFromAllEpochsCNN.py.
The output will be an exel file epochsResIntoExcel.xls containing details such as 'ModelNum','CNN','Epoch','Loss','Acc','Val_loss','Val_acc'.

Further Projects and Contact
www.researchreader.com

https://medium.com/@dr.siddhaling

Dr. Siddhaling Urolagin,
dr.siddhaling@gmail.com

