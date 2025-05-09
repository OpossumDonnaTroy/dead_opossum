import os 
import json

base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, 'new_dataset', 'data.json')
data = json.loads(open(data_path, encoding='utf-8').read())

annotations = data['Annotations']

uniqs = list()
duplicated = list()
for index, unfiltered_item in enumerate(annotations):
    print(index)
    for uniq_item in uniqs:
        if unfiltered_item['ImageFrameId'] == uniq_item['ImageFrameId']:
            if unfiltered_item['Points'] == uniq_item['Points']:
                duplicated.append(unfiltered_item)
                break
    uniqs.append(unfiltered_item)
    
print(f'\nuniqs {len(uniqs)}')               
print(f'duplicated {len(duplicated)}')                
            
data['Annotations'] = uniqs
processed_path = os.path.join(base_path, 'processed_dataset', 'data.json')
with open(processed_path, 'w', encoding='utf-8') as fp:
    json.dump(data, fp) 

