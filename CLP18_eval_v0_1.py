#!/usr/bin/env python3
########################################
## CLP18_eval: Script
## Version: 0.1 (beta)
##
## The following script is intended to be used for evaluating
## the 2018 CLPsych Shared Task, Subtasks A and B. Results are
## reported using Mean Absolute Error and Disattenuated
## Pearson Correlation.
##
## The file expects two input files:
## The first should be a CSV with the first column containing
## the id and the second column containing the true value.
##
## The second should be a CSV with the first column containing
## the id and the second column containing the predicted value.
##
## A header row is expected for both files.
##
## Command to run: CLP18_eval_v0_1.py [true csv] [pred csv]
##
## Any ids missing in the prediction file are treated as
## the mean of all predictions. Any extra ids in the
## prediction file are ignored.
##
## Creators: Anvesh Myla, Veronica Lynn, H. Andrew Schwartz
from __future__ import print_function

import sys
import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr
from sklearn.metrics import mean_absolute_error


##PARAMETERS:
key_reliab = 0.77  # reliability of the key (an inverse of measurement error)
pred_reliab = 0.70  # reliability expected of the predictions

##HELP MESSAGE:
if len(sys.argv) != 3:
    print("""The file expects two input files:
The first should be a CSV with the first column containing the id and the second column containing the true value.

The second should be a CSV with the first column containing the id and the second column containing the predicted value.

A header row is expected for both files.

Command to run: CLP18_eval_v0_1.py [true csv] [pred csv]""")
    sys.exit(1)

##READ THE DATA
df_key = pd.read_csv(sys.argv[1], skiprows=1, names=['Id', 'True'])
df_pred = pd.read_csv(sys.argv[2], skiprows=1, names=['Id', 'Pred'])

##ALIGN THE DATA
df_key['Pred'] = np.nan
mean = np.mean(df_pred["Pred"].values)  # mean of predictions is used when no prediction is present.
ids_not_in_pred = []
for i in range(len(df_key)):
    try:
        df_key.ix[i, 2] = df_pred[df_pred["Id"] == df_key.ix[i, 0]].values[0][1]
    except IndexError:
        df_key.ix[i, 2] = mean
        ids_not_in_pred.append(int(df_key.ix[i, 0]))

##NOTIFY OF ANY MISSING PREDICTIONS
if len(ids_not_in_pred) == 0:
    print("All the IDs in csv file with true values are present in csv file with predicted values")
else:
    print("IDs in csv file with true values but not in csv file with predicted values :", ids_not_in_pred)
    print("Number of IDs common to both the csv files :", len(df_key) - len(ids_not_in_pred))

##RUN EVALUATION METRICS:
mae = mean_absolute_error(df_key["True"].values, df_key["Pred"].values)
dis_r = pearsonr(df_key["True"].values, df_key["Pred"].values)[0] / np.sqrt(key_reliab * pred_reliab)
print("Mean absolute error : %.3f" % mae)
print("Disattenuated Pearson correlation coefficient : %.4f " % dis_r)
