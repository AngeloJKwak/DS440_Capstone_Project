from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np
from ftfy import fix_text
from ftfy import fix_encoding


#### USER CAN SELECT FILE FOR SCRIPT
file_name = askopenfilename()
file_contents = pd.read_csv(file_name, encoding="utf-8-sig")

print(file_contents)

df_string = file_contents.applymap(str)

### ENCODING AUTOMATICALLY FIXED
#for m in range(len(file_contents)):
headers = list(df_string.columns.values)

df_string.applymap(lambda text: fix_encoding(text))

print(df_string)




tonp = np.array(df_string)
df_string.to_numpy()
x = tonp[:, 38:64]


x2 = pd.DataFrame(data = x[:,:])

print(x2)


print(headers)




#df_string.to_csv(r'C:\Users\steph\Desktop\tryme.txt', header=None, index=None, sep=',', mode='a')
### NLP
