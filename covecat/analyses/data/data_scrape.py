# load libraries
import os
import pandas as pd

# initialize empty list to hold .csv files
storage = [output for output in os.listdir(os.getcwd()) if output.endswith('.csv')]

# grab file name 
exp_name = storage[0].split('_')
filename = '{}_alldata.csv'.format(exp_name[0])
        
# seed all_data file with first file
all_data = pd.read_csv(storage.pop(0))

for output in storage:

    # load individual datafile w/o first row (column titles)
    participant_data = pd.read_csv(output)
    
    # append above data to sum total file
    all_data = pd.concat([all_data, participant_data])

# save all_data to .csv format
## retrieve parent directory
save_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

## save to parent directory
all_data.to_csv(os.path.join(save_path, filename), index = False)


