
from time import sleep 

print('Some info outside other functions')

def process_data(data):
    print('Beginning data processing')
    modified_data = data + ' is modified'
    sleep(3)
    print('Data processing finished')
    return modified_data
