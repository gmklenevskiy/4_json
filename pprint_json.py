import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as reader:
        parsed = json.load(reader)
        pretty_print_json(parsed)


def pretty_print_json(data):
    print(json.dumps(data, indent = 4, ensure_ascii=False, sort_keys=True))
    
    
    
if __name__ == '__main__':
    if len(sys.argv)>1:
        filepath = sys.argv[1]
        load_data(filepath)
    else:
        print("Please, enter the filepath")