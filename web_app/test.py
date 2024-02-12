import pickle
import json
map_ = {}

for i in range(3,29):
    map_[f'{i}'] = {}

with open(f'ref_map.pkl', 'rb') as pickle_file:
        ref_map = pickle.load(pickle_file)
        
with open(f'norm_ref_map.pkl', 'rb') as pickle_file:
        norm_ref_map = pickle.load(pickle_file)
        


for k in range(3,29):
    to_remove = []

    for ele in ref_map[k]:
        
        if len(ele.strip()) == 0:
            to_remove.append(ele)
            
    for t in to_remove:
        ref_map[k].remove(t)
    
    
        

characters_list = ["(" + str(i) + ")" for i in range(1, 51)]

for k in range(3,29):
    for i in range(len(ref_map[k])):
        for c in characters_list:
            ref_map[k][i] = ref_map[k][i].replace(c,'')
            

for k in range(3,29):
    for cnt in range(len(ref_map[k])):
        ref_map[k][cnt] = ref_map[k][cnt].replace('Ã§','ç')
        ref_map[k][cnt] = ref_map[k][cnt].replace('Â§','Ç')
        
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace('Ã§','ç')
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace('Â§','Ç')


for i in range(3,29):
    with open(f'final_points_data/final_pts{i}.pkl', 'rb') as pickle_file:
        data = pickle.load(pickle_file)

    word_data = []
    for _ in range(len(data)):
        word_data.append([])
    
    start = 0
    end = 0  
    for j in range(len(data)):
        line = data[j]
        start = 0
        end = 0
        for k in range(len(line)):
            if len(line[k])!=0:
                end+=1
            else:
                word_data[j].append([line[start],line[end-1]])
                end+=1
                start = end
        
        word_data[j].append([line[start],line[end-1]])
            
            
        
    
    map_[f'{i}']['character_points'] = data
    map_[f'{i}']['word_points'] = word_data
    map_[f'{i}']['content'] = ref_map[i]
    map_[f'{i}']['norm_content'] = norm_ref_map[i]
    map_[f'{i}']['imgSrc'] = f'resized_img/{i}.jpg'

with open('points_and_content.json', 'w') as json_file:
    json.dump(map_, json_file)
