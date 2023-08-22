
from time import sleep 

print('Some info outside other functions')

def process_data(data):
    print('Beginning data processing')
    modified_data = data + ' is modified'
    sleep(3)
    print('Data processing finished')
    return modified_data

if __name__ == '__main__':
    data = 'my data from the web'
    print(data)
    processed_data = process_data(data)
    print(processed_data)