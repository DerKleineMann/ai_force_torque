# File for data preparation before training

# Libraries
import pandas as pd
import os

# Parameters
IS_JSON_SUPPORTED = False
DATA_FOLDER = "versuch_f1"
FILENAME="data_prep.py"
DIRNAME=os.path.abspath(FILENAME).replace(FILENAME,'')
DF_POINTS_RANGE = 11
DF_POINTS_LENGTH = 3000

# JSON Support

# DataFrame new labels
df_labels=['t_Sec','t_nSec',
           'exT_A1','exT_A2','exT_A3','exT_A4','exT_A5','exT_A6','ext_A7',
           'msT_A1','msT_A2','msT_A3','msT_A4','msT_A5','msT_A6','msT_A7',
           'Fx','Fx1',
           'Fy','Fy1',
           'Fz','Fz1',
           'Tx','Tx1',
           'Ty','Ty1',
           'Tz','Tz1',
           'cur_A1','cur_A2','cur_A3','cur_A4','cur_A5','cur_A6','cur_A7',
           'comd_A1','comd_A2','comd_A3','comd_A4','comd_A5','comd_A6','comd_A7',
           'curCart_x','curCart_y','curCart_z',
           'comdCart_x','comdCart_y','comdCart_z']

# Create directory if needed
if not os.path.isdir(DIRNAME+'data/temp/'+DATA_FOLDER+'/'):
    os.system('mkdir '+DIRNAME+'data/temp/'+DATA_FOLDER)
# Unzip from raw data
if not os.listdir(DIRNAME+'data/temp/'+DATA_FOLDER+'/'):
    os.system('unzip '+DIRNAME+'data/zip/'+DATA_FOLDER+'.zip -d '+DIRNAME+'data/temp/'+DATA_FOLDER+'/')
    print(">> Data unpacked")
else :
    print(">> Data already unpacked, skipping")

# Import from text files
for i in range(0,DF_POINTS_RANGE):
    for j in range(0,DF_POINTS_RANGE):
        file = open(DIRNAME+'data/temp/'+DATA_FOLDER+"/f_"+ str(i) + "_" + str(j) +"_demoRecord.txt",'r')

        # Retrieving each line of data in file
        file_lines = []
        for line in file:
            file_lines.append(line.strip())
        data = file_lines[1:] # Excluding first line of file (labels)

        # Stripping data of zeros
        clean_data = []
        for data_line in data :
            split_line = data_line.split(' ')
            split_line[:]=[x for x in split_line if x]
            clean_data.append(split_line)

        # Creation of DataFrames
        df = pd.DataFrame(clean_data, columns=df_labels)
        df = df.astype(float)
        locals()[f'df{i}_{j}'] = df

        # "Key" column (stores point coordinates on data line)
        locals()[f'df{i}_{j}']['key']="{0},{1}".format(i,j)

        # Reshaping data to leave the last X points
        locals()[f'df{i}_{j}_reshape']=locals()[f'df{i}_{j}'][-DF_POINTS_LENGTH:].reset_index()
print(">> Data imported")

# Merge every DataFrame into one
full_df = pd.DataFrame()
for i in range (0,DF_POINTS_RANGE):
    for j in range (0,DF_POINTS_RANGE):
        full_df = pd.concat([full_df,locals()[f'df{i}_{j}']],ignore_index=True)
print(">> Data merged")

# Save to feather file
full_df.to_feather(DIRNAME+'data/feather/'+DATA_FOLDER+'_'+str(DF_POINTS_LENGTH)+'.feather')
print(">> Data saved to : "+DATA_FOLDER+'_'+str(DF_POINTS_LENGTH)+'.feather')

# Wipe temporary directory
os.system('rm -r '+DIRNAME+'data/temp/'+DATA_FOLDER)
    
