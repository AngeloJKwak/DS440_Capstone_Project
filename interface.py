from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np
from ftfy import fix_text
from ftfy import fix_encoding


#### USER CAN SELECT FILE FOR SCRIPT
file_name = askopenfilename()
file_contents = pd.read_csv(file_name, encoding="utf-8-sig")

#print(file_contents)

df_string = file_contents.applymap(str)

### ENCODING AUTOMATICALLY FIXED
# Below will fix the encoding of the TITLE and PAGENUM as unique non utf-8 characters would show up.

df_string['TITLE'] = df_string['TITLE'].apply(lambda x: fix_encoding(x))
df_string['PAGENUM'] = df_string['PAGENUM'].apply(lambda x: fix_encoding(x))


### Hold headers names
headers = list(df_string.columns.values)

### NLP

## Below is script to recognize when the software has mixed up the first name with the last name. It simply compares the length of the two and if the last name shows to be shorter, it will flip the name values.
# All test academic documents would use just a first initial as a first name. If this needs to be addressed further we can adjust as we need to.

for i in range(len(df_string)):
    try:
        df_string.INTELLCONT_AUTH_1_FNAME[i], df_string.INTELLCONT_AUTH_1_LNAME[i] = np.where(len(df_string.INTELLCONT_AUTH_1_FNAME[i])>len(df_string.INTELLCONT_AUTH_1_LNAME[i]), [df_string.INTELLCONT_AUTH_1_LNAME[i], df_string.INTELLCONT_AUTH_1_FNAME[i]], [df_string.INTELLCONT_AUTH_1_FNAME[i], df_string.INTELLCONT_AUTH_1_LNAME[i]])
    except:
        pass

    try:
        df_string.INTELLCONT_AUTH_2_FNAME[i], df_string.INTELLCONT_AUTH_2_LNAME[i] = np.where(len(df_string.INTELLCONT_AUTH_2_FNAME[i])>len(df_string.INTELLCONT_AUTH_2_LNAME[i]), [df_string.INTELLCONT_AUTH_2_LNAME[i], df_string.INTELLCONT_AUTH_2_FNAME[i]], [df_string.INTELLCONT_AUTH_2_FNAME[i], df_string.INTELLCONT_AUTH_2_LNAME[i]])
    except:
        pass

    try:
        df_string.INTELLCONT_AUTH_3_FNAME[i], df_string.INTELLCONT_AUTH_3_LNAME[i] = np.where(len(df_string.INTELLCONT_AUTH_3_FNAME[i])>len(df_string.INTELLCONT_AUTH_3_LNAME[i]), [df_string.INTELLCONT_AUTH_3_LNAME[i], df_string.INTELLCONT_AUTH_3_FNAME[i]], [df_string.INTELLCONT_AUTH_3_FNAME[i], df_string.INTELLCONT_AUTH_3_LNAME[i]])
    except:
        pass

    try:
        df_string.INTELLCONT_AUTH_4_FNAME[i], df_string.INTELLCONT_AUTH_4_LNAME[i] = np.where(len(df_string.INTELLCONT_AUTH_4_FNAME[i])>len(df_string.INTELLCONT_AUTH_4_LNAME[i]), [df_string.INTELLCONT_AUTH_4_LNAME[i], df_string.INTELLCONT_AUTH_4_FNAME[i]], [df_string.INTELLCONT_AUTH_4_FNAME[i], df_string.INTELLCONT_AUTH_4_LNAME[i]])
    except:
        pass

    try:
        df_string.INTELLCONT_AUTH_5_FNAME[i], df_string.INTELLCONT_AUTH_5_LNAME[i] = np.where(len(df_string.INTELLCONT_AUTH_5_FNAME[i])>len(df_string.INTELLCONT_AUTH_5_LNAME[i]), [df_string.INTELLCONT_AUTH_5_LNAME[i], df_string.INTELLCONT_AUTH_5_FNAME[i]], [df_string.INTELLCONT_AUTH_5_FNAME[i], df_string.INTELLCONT_AUTH_5_LNAME[i]])
    except:
        pass

    try:
        df_string.INTELLCONT_AUTH_6_FNAME[i], df_string.INTELLCONT_AUTH_6_LNAME[i] = np.where(len(df_string.INTELLCONT_AUTH_6_FNAME[i])>len(df_string.INTELLCONT_AUTH_6_LNAME[i]), [df_string.INTELLCONT_AUTH_6_LNAME[i], df_string.INTELLCONT_AUTH_6_FNAME[i]], [df_string.INTELLCONT_AUTH_6_FNAME[i], df_string.INTELLCONT_AUTH_6_LNAME[i]])
    except:
        pass

    try:
        df_string.INTELLCONT_AUTH_7_FNAME[i], df_string.INTELLCONT_AUTH_7_LNAME[i] = np.where(len(df_string.INTELLCONT_AUTH_7_FNAME[i])>len(df_string.INTELLCONT_AUTH_7_LNAME[i]), [df_string.INTELLCONT_AUTH_7_LNAME[i], df_string.INTELLCONT_AUTH_7_FNAME[i]], [df_string.INTELLCONT_AUTH_7_FNAME[i], df_string.INTELLCONT_AUTH_7_LNAME[i]])
    except:
        pass

    try:
        df_string.INTELLCONT_AUTH_8_FNAME[i], df_string.INTELLCONT_AUTH_8_LNAME[i] = np.where(len(df_string.INTELLCONT_AUTH_8_FNAME[i])>len(df_string.INTELLCONT_AUTH_8_LNAME[i]), [df_string.INTELLCONT_AUTH_8_LNAME[i], df_string.INTELLCONT_AUTH_8_FNAME[i]], [df_string.INTELLCONT_AUTH_8_FNAME[i], df_string.INTELLCONT_AUTH_8_LNAME[i]])
    except:
        pass

    try:
        df_string.INTELLCONT_AUTH_9_FNAME[i], df_string.INTELLCONT_AUTH_9_LNAME[i] = np.where(len(df_string.INTELLCONT_AUTH_9_FNAME[i])>len(df_string.INTELLCONT_AUTH_9_LNAME[i]), [df_string.INTELLCONT_AUTH_9_LNAME[i], df_string.INTELLCONT_AUTH_9_FNAME[i]], [df_string.INTELLCONT_AUTH_9_FNAME[i], df_string.INTELLCONT_AUTH_9_LNAME[i]])
    except:
        pass



#df_string.to_csv(r'C:\Users\steph\Desktop\tryme2.txt', header=None, index=None, sep=',', mode='a')
