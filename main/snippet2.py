import os, glob
import pandas as pd
import csv
import time


date = time.strftime("%Y%m%d%H%M")

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

# def sort_merge_urls(folder):
#     '''
#     Takes the path of the folder (string) as argument
    
#     Sort all the links into two categorie:
#         - clean_url: ready to be extracted
#         - sponsored_url : url needing some more url extraction work
#     The Path File must be changed to your directory specification
#     '''
#     try:
#         all_files = glob.glob(os.path.join(folder, "*.csv"))
#         date = time.strftime("%Y%m%d%H%M")

#         for file in all_files:
#             with open(file, "r") as csv_file:
#                 csv_reader = csv.reader(csv_file)

#                 with open(f"clean_url_{date}.csv", "a") as clean_file:
#                     clean_csv_writer = csv.writer(clean_file)
                    
#                     with open(f"sponsored_url_{date}.csv", "a") as sponsored_file:
#                         sponsored_csv_writer = csv.writer(sponsored_file)

#                         for line in csv_reader:              
#                             if "new-real-estate-project" in line[0]:
#                                 sponsored_csv_writer.writerow(line)
#                             else:
#                                 clean_csv_writer.writerow(line)
#     except :
#         raise Exception

# folder = ""
# sort_merge_urls(folder)