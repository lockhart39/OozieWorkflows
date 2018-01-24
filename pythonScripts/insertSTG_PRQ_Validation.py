'''
Created by Taylor on 01/24/2018
Purpose: python script to validate staging and parquet insertion process
usage: $ python insertSTG_PRQ_Validation.py stagingDBName stagingTableName parquetDBName parquetTableName

'''


# imports
from subprocess import check_output
import sys


try:
    stgDB = sys.argv[1]
    stgTable = sys.argv[2]
    prqDB = sys.argv[3]
    prqTable = sys.argv[4]
except:
    print "Include system arguments for database and table names for staging and parquet ($ python insertSTG_PRQ_Validation.py stagingDBName stagingTableName parquetDBName parquetTableName)"



with open("insertionValidation_STG.hql", "w") as hqlScript:
    hqlScript.write("SET hive.exec.dynamic.partition.mode=non-strict;"+"\n")
    hqlScript.write("SELECT COUNT(*) FROM "+ stgDB + "." + stgTable + "\n")
hqlScript.close()


stg_Result = check_output(["hive", "-f", "insertionValidation_STG.hql"])

# currently writes in warning statements, deal with that later

with open("stgCount.txt", "w") as results:
    results.write(str(stg_Result))
results.close()

'''
Doing the same for prq
'''

with open("insertionValidation_PRQ.hql", "w") as hqlScript:
    hqlScript.write("SET hive.exec.dynamic.partition.mode=non-strict;"+"\n")
    hqlScript.write("SELECT COUNT(*) FROM "+ prqDB + "." + prqTable + "\n")
hqlScript.close()


prq_Result = check_output(["hive", "-f", "insertionValidation_PRQ.hql"])

# currently writes in warning statements, deal with that later

with open("prqCount.txt", "w") as results:
    results.write(str(prq_Result))
results.close()



'''
The next step will be to read the counts from the two results textfiles
then compare them
'''

print "---- Comparing count results ----"

countResults = []
count1 = 0
count2 = 0



with open("stgCount.txt", "r") as input1:
    for i in input1:
        if count1 < 1:
            countResults.append(i)
            count1 += 1
        else:
            break


with open("prqCount.txt", "r") as input2:
    for i in input2:
        if count2 < 1:
            countResults.append(i)
            count2 += 1
        else:
            break


with open("comparingCounts.txt","w") as final:
    for i in countResults:
        final.write(str(i))
final.close()










