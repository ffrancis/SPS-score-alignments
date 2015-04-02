"""
Parse D2 qscore out put

By Felix Francis
felixfrancier@gmail.com

"""


############################################################
#Time to run the code: start timer
############################################################
import time
t0 = time.time()

import pandas as pd
import csv
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import statsmodels.api as sm

# input_file = "4mer_score_file.txt"
# input_file = "5mer_score_file.txt"
# input_file = "6mer_score_file.txt"
# input_file = "7mer_score_file.txt"
# input_file = "8mer_score_file.txt"
# ]]input_file = "9mer_score_file.txt"
# input_file = "10mer_score_file.txt"
# input_file = "11mer_score_file.txt"
# input_file = "12mer_score_file.txt"
input_file = "13mer_score_file.txt"
# input_file = "14mer_score_file.txt"
# input_file = "15mer_score_file.txt"
# input_file = "16mer_score_file.txt"
#input_file = "test.txt"

### INPUT FILE



### READ INPUT DATA
data            = open(input_file, "r")
rows            = (row.strip().split() for row in data)
rows            = (zip(*rows))

mafft           = map(float, (filter(lambda a: a != "null", (list (rows[1][1:])))))         # Select corresponding columns in rows, remove "null" and convert str to float
D2              = map(float, (filter(lambda a: a != "null", (list (rows[2][1:])))))
D2S             = map(float, (filter(lambda a: a != "null", (list (rows[3][1:])))))
D2St            = map(float, (filter(lambda a: a != "null", (list (rows[4][1:])))))


'''
# HISTOGRAM
plt.hist(mafft, 50, histtype="step", color='blue', lw=1., label='mafft')
plt.hist(D2, 50, histtype="step", color='green', lw=1., label='D2')
plt.hist(D2S, 50, histtype="step", color='red', lw=1., label='D2S')
plt.hist(D2St, 50, histtype="step", color='black', lw=1, label='D2St')     
plt.legend(loc='upper right')
plt.title("Alignment SPS-scores - "+str(input_file [:-15]))
plt.xlabel("SPS-score")
plt.ylabel("Frequency")
plt.show()
'''

'''
# BOX PLOT
list = [mafft, D2, D2S, D2St]
plt.boxplot(list)
plt.xticks([1, 2, 3, 4], ['mafft', 'D2', 'D2S', 'D2St'])
plt.ylim((-.02,1.02))
plt.title("Alignment SPS-scores - "+str(input_file [:-15]))
plt.xlabel("Guide tree used")
plt.ylabel("SPS-scores")
plt.show()
'''

# VIOLIN PLOT
list = [mafft, D2, D2S, D2St]

#plt.rcParams['figure.subplot.bottom'] = 0.23  # keep labels visible
fig = plt.figure()
ax = fig.add_subplot(111)
sm.graphics.violinplot(list, ax=ax, plot_opts={'violin_fc':'grey', 'violin_alpha':0.25})
plt.xticks([1, 2, 3, 4], ['mafft', 'D2', 'D2S', 'D2St'])
#plt.ylim((-.02,1.02))
plt.title("Alignment SPS-scores - "+str(input_file [:-15]))
plt.xlabel("Guide tree used")
plt.ylabel("SPS-scores")

#sm.graphics.boxplots.violinplot(list)
plt.show()





'''             
csv_dict = csv.DictReader(data, delimiter="\t", quotechar="\"")

#print csv_dict.fieldnames
# 'Alignment_name', 'mafft_Q-score', 'D2_Q-score', 'D2S_Q-score', 'D2St_Q-score', 'mafft_TC-score', 'D2_TC-score', 'D2S_TC-score', 'D2St_TC-score'

for item in csv_dict:
                print item
'''


'''
with open ('../data/motif_matrix.txt') as input_data:
	seq = [line.strip() for line in input_data.readlines()]
	seq1 =[]
	for i in seq:
		j = (str(i).upper()).split()
		seq1.append(j)
		
#print len(seq1[0])	
'''
############################################################
#Time to run the code: end timer
############################################################
t1 = time.time()

total = t1-t0
print '\n', "Time to run code = ", total, " seconds", '\n'