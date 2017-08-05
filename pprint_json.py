import json
import sys
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as reader:
        return json.load(reader)


def pretty_print_json(reader):
    print(json.dumps(reader, indent = 4, ensure_ascii=False, sort_keys=True))
    
      
if __name__ == '__main__':
    if len(sys.argv)>1:
        filepath = sys.argv[1]
        reader = load_data(filepath)
        pretty_print_json(reader)
        
    else:
        print("Please, enter the filepath")