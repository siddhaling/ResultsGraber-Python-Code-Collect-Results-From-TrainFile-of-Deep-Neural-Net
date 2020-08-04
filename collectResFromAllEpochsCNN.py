#import the required packages
import numpy as np
import pandas as pd
import os
import glob

#change the directory to current directory
os.chdir('change to current dir')

# The 'resultFiles' is the folder containing results collected during Epochs of Convolutional Neural Network
resultFolder='model1'

#Read all the file with txt extension. For example CNN_5CV.txt file contains the results and other details collected during CNN epochs
resFiles=glob.glob(resultFolder+'/*.txt')

#create an empty dataframe with columns such as 'ModelNum','CNN','Epoch','Loss','Acc','Val_loss','Val_acc'
resTable=pd.DataFrame(columns=['ModelNum','CNN','Epoch','Loss','Acc','Val_loss','Val_acc'])

#Iterate through each result file
for i in range(0,len(resFiles)):
    print(i,resFiles[i])
    #Extract model number and CNN from the folder and file name
    ModelNum=resFiles[i].split('\\')[-2]
    CNN=resFiles[i].split('\\')[-1].split('_')[0]
    Epoch=np.NaN
    Loss=np.NaN
    Acc=np.NaN
    Val_loss=np.NaN
    Val_acc=np.NaN
    #open the text file to read and read all the lines
    fin=open(resFiles[i],'r')
    lines=fin.readlines()
    #Iterate through each line and look for keywords such as 'Epoch', 'step - loss:'
    #When the line contain 'Epoch' keyword then from this line the epoch count is extracted
    #When the line contain 'step - loss:' keyword then from this line various values such as 
    # 'Loss','Acc','Val_loss','Val_acc' are extracted in the following loop.
    for ln in lines:        
        if 'Epoch' in ln:        
            Epoch=ln.split(' ')[-1].split('/')[-2].rstrip()
            print(ln,Epoch)
        if 'step - loss:' in ln:            
            elements=ln.split('-')
            if(len(elements)>=4):
                Loss=elements[-4].split(':')[1]
                Acc=elements[-3].split(':')[1]
                Val_loss=elements[-2].split(':')[1]
                Val_acc=elements[-1].split(':')[1].rstrip()
    #Append the various information such as 'ModelNum','CNN', 'Loss','Acc','Val_loss','Val_acc' into dataframe
                resTable=resTable.append({'ModelNum':ModelNum,'CNN':CNN,'Epoch':Epoch,'Loss':Loss,'Acc':Acc,'Val_loss':Val_loss,'Val_acc':Val_acc},ignore_index=True)
                print('ModelNum',ModelNum,'CNN',CNN,'Epoch',Epoch,'Loss',Loss,'Acc',Acc,'Val_loss',Val_loss,'Val_acc',Val_acc)
    fin.close()
#write the dataframe into an excel file.
resTable.to_excel('epochsResIntoExcel.xls',index = None, header=True)