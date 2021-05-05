import os, glob
import pandas as pd
import csv


# path = ""
# all_files = glob.glob(os.path.join(path, "*.csv"))
# df_from_each_file = (pd.read_csv(f, header= None) for f in all_files)
# df_merged   = pd.concat(df_from_each_file, ignore_index= True)
# df_merged.to_csv( "merged.csv")

# final = pd.read_csv("merged.csv")
# final = final.drop(['Unnamed: 0'], axis = 1)
# print(final.head(10))

# final.to_csv("final_list.csv", header = None )

# os.remove('merged.csv')

People_List = [['Jon','Smith',21],['Mark','Brown',38],['Maria','Lee',42],['Jill','Jones',28],['Jack','Ford',55]]

flatlist = [ item for elem in People_List for item in elem]
df = pd.DataFrame(flatlist,columns=['url'])
df.to_csv('test.csv')
