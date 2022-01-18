#%%
import csv
def problem3_7(csv_pricefile, flower):
    pass # replace this pass (a do-nothing) statement with your code
    infile = open(csv_pricefile)
    reader = csv.reader(infile)
    for row in reader:
        if row[0] == flower:
            print(row[1])