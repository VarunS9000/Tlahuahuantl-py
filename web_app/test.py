import pickle
import json
map_ = {}

for i in range(3,29):
    map_[f'{i}'] = {}

with open(f'ref_map_org2.pkl', 'rb') as pickle_file:
        ref_map = pickle.load(pickle_file)
        
with open(f'ref_map_norm2.pkl', 'rb') as pickle_file:
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
        
        ref_map[k][cnt] = ref_map[k][cnt].replace(' ?Ç','?Ç')
        ref_map[k][cnt] = ref_map[k][cnt].replace(' ?Ç','?Ç')
        ref_map[k][cnt] = ref_map[k][cnt].replace(' ?Ç','?Ç')
        
        ref_map[k][cnt] = ref_map[k][cnt].replace(' ?ç','?ç')
        ref_map[k][cnt] = ref_map[k][cnt].replace(' ?ç','?ç')
        ref_map[k][cnt] = ref_map[k][cnt].replace(' ?ç','?ç')
        
        
        
        
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace('Ã§','ç')
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace('Â§','Ç')
        
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace(' ?Ç','?Ç')
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace(' ?Ç','?Ç')
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace(' ?Ç','?Ç')
        
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace(' ?ç','?ç')
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace(' ?ç','?ç')
        norm_ref_map[k][cnt] = norm_ref_map[k][cnt].replace(' ?ç','?ç')


for i in range(3,29):
    with open(f'final_pts_data_new/final_pts{i}.pkl', 'rb') as pickle_file:
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
            
            
    word_to_index = {}
    for a in range(len(word_data)): #line
        for b in range(len(word_data[a])): #word
            key1 = f'{word_data[a][b][0][0],word_data[a][b][0][1]}'
            key1 = key1.replace('(','')
            key1 = key1.replace(')','')
            key1 = key1.replace(' ','')
            key2 = f'{word_data[a][b][1][0],word_data[a][b][1][1]}'
            key2 = key2.replace('(','')
            key2 = key2.replace(')','')
            key2 = key2.replace(' ','')
            value = [[a,b],word_data[a][b][0],word_data[a][b][1]]
            
            word_to_index[key1] = value
            word_to_index[key2] = value
         
    
    map_[f'{i}']['character_points'] = data
    map_[f'{i}']['word_points'] = word_data
    map_[f'{i}']['word_to_index'] = word_to_index
    map_[f'{i}']['content'] = ref_map[i]
    map_[f'{i}']['norm_content'] = norm_ref_map[i]
    map_[f'{i}']['imgSrc'] = f'resized_img/{i}.jpg'

with open('points_and_content.json', 'w') as json_file:
    json.dump(map_, json_file)
