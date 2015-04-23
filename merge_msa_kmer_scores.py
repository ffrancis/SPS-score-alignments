###/home/ffrancis/anaconda/bin/env python

'''
Compiled by		:	Felix Francis (felixfrancier@gmail.com)
Description		:	merge kmer tables
Requirements	:	Python 2.7, R
'''


############################################################
#Time to run the code: start timer
############################################################
import time
t0 = time.time()



## PYTHON FUNCTIONS
import subprocess as sp									# To get python to run another program                                                                        
import pandas as pd
import functools
import glob
import os



## PATH TO INPUT FILES
path = "/home/felixfrancier/Dropbox/PROGRAMMING_DATABASE/Python/Parsing/d2_msa_output_scores/test/"


# for file in glob.glob(path+"*mer_score_file.txt"):
#     print(file)
    
    
    
################################################################################################   
### FUNCTION TO REPLACE THE STRING "-score" WITH "_score_kmer"
def replace_char(file_name, path):
    kmer        = file_name[0:4]
    f0 = open(os.devnull, 'w')
    sp.call(["sed", "-i", "s/-score/_score_%s/g" %kmer, "%s%s" %(path,file_name)], stdout=f0)
#replace_char(file_name, path)   
   
### CODE TO REPLACE "-score" WITH "_score_kmer" FOR ALL FILES IN THE GIVEN PATH
#input_files = glob.glob(path+ "*mer_score_file.txt")
input_files = [os.path.basename(x) for x in glob.glob(path+ "*mer_score_file.txt")]
for file in input_files:
    #print file
    replace_char(file, path)

    
### USE PANDAS TO MERGE MULTIPLE FILES BASED ON A COMMON INDEX (http://stackoverflow.com/questions/26243432/python-merging-multiple-text-files)
input_files = glob.glob(path+ "*mer_score_file.txt")
input_files = sorted(input_files)                                                                           # ALPHABETICALLY SORT THE FILE NAMES
print input_files
dfs = [pd.read_csv(filename,sep='\t',header=0).set_index('Alignment_name') for filename in input_files]
#print dfs
mergefunc = functools.partial(pd.merge, left_index=True, right_index=True)
merged = functools.reduce(mergefunc, dfs)
#print merged
merged.to_csv(path+ "MERGED_SCORES.csv", index=False)
################################################################################################ 






############################################################
#Time to run the code: end timer
############################################################
t1 = time.time()

total = t1-t0
print '\n', "Time to run code = ", total, " seconds", '\n'