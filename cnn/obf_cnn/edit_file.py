import yaml
import json
import sys


def main():
    b = sys.argv[1]
    method = sys.argv[2]
    r = sys.argv[3]
    eps_heavy = sys.argv[4]
    eps_light = sys.argv[5]
    command = 'python3 cnn_model_selected.py ' + method + ' ' + b + ' ' + r + ' ' + eps_heavy + ' ' + eps_light
    conv = {"_type":"choice", "_value":[8, 16, 32, 64, 128, 256, 512]}
    pool = {"_type":"choice", "_value":[1, 3, 5, 7]}
    data_dim = 0
    print(command)
    if b == '0.25':
        data_dim = {"_type": "choice", "_value": [720]}
        conv = {"_type":"choice", "_value":[8, 16, 32, 64, 128, 256]}
        pool = {"_type":"choice", "_value":[1, 3, 5, 7]}
    elif b == '0.05':
        data_dim = {"_type": "choice", "_value": [3600]}
        conv = {"_type":"choice", "_value":[8, 16, 32, 64, 128, 256]}
        pool = {"_type":"choice", "_value":[1, 3, 5, 7]}
    elif b == '0.5':
        data_dim = {"_type": "choice", "_value": [360]}
        conv = {"_type":"choice", "_value":[4, 8, 16, 32, 64, 128]}
        pool = {"_type":"choice", "_value":[1, 3, 5]}
    elif b == '1.0':
        data_dim = {"_type": "choice", "_value": [180]}
        conv = {"_type":"choice", "_value":[4, 8, 16, 32, 64]}
        pool = {"_type":"choice", "_value":[1, 3, 5]}
    elif b == '2.0':
        data_dim = {"_type": "choice", "_value": [90]}           
        pool = {"_type":"choice", "_value":[1,2,3]}
        conv = {"_type":"choice", "_value":[2,4,8,16,32]}

    with open("config.yml") as f:
        list_doc = yaml.load(f)
        list_doc["trial"]["command"] = command
    with open("config.yml", "w") as f:
        yaml.dump(list_doc, f, default_flow_style=False)

    with open("search_space.json", 'r') as f:
        json_doc = json.load(f)

    with open("search_space.json", 'w') as f:
        json_doc['data_dim'] = data_dim
        json_doc['conv1'] = json_doc['conv2'] = json_doc['conv3'] = json_doc['conv4'] = conv
        json_doc['pool1'] = json_doc['pool2'] = json_doc['pool3'] = json_doc['pool4'] = pool
        json.dump(json_doc, f, indent=4)

if __name__ == '__main__':
    main()
