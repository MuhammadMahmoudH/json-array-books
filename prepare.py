import json
import os

# Get the full path to the JSON file
filepath = os.path.abspath("hisn_almuslim.json")
# print(filepath)

# Check if the file exists
# if os.path.isfile(filepath):
# Load the JSON file
with open(filepath, 'r', encoding='utf-8') as file:
    data = json.load(file)

output = []

for key in data.keys():
    counter = 0
    # Get the text and footnote values of the key
    text = ''
    # print(len(data[key]['text']))
    if (len(data[key]['text']) >= 1):
        for row in data[key]['text']:
            # print(row + '\\n')
            text += row + '\n'
            counter+=1
    else:
        print('--------------------')
        text = data[key]['text']
    # print(text)
    # print(counter)
    keys = key
    output.append({
        'context': keys,
        'correct_response': text
    })

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)