import yaml
import json
import sys


def main():
    b = sys.argv[1]
    method = sys.argv[2]
    r = sys.argv[3]
    command = 'python3 cnn_model_selected.py ' + method + ' ' + b
    data_dim = 0
    print(command)
    if r == '40':
        data_dim = {"_type": "choice", "_value": [144]}
    elif r == '30':
        data_dim = {"_type": "choice", "_value": [108]}
    elif r == '20':
        data_dim = {"_type": "choice", "_value": [144]}
    elif r == '10':
        data_dim = {"_type": "choice", "_value": [36]}           

    with open("config.yml") as f:
        list_doc = yaml.load(f)
        list_doc["trial"]["command"] = command
    with open("config.yml", "w") as f:
        yaml.dump(list_doc, f, default_flow_style=False)

    with open("search_space.json", 'r') as f:
        json_doc = json.load(f)

    with open("search_space.json", 'w') as f:
        json_doc['data_dim'] = data_dim
        json.dump(json_doc, f, indent=4)

if __name__ == '__main__':
    main()
