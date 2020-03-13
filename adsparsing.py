import requests
import json




limit=int(input("Choose page limit="))

def write_to_json_file(path,filename,data):
    filePathNameWExt="./"+ path + "/" + filename + ".json"
    with open(filePathNameWExt,"w",encoding="utf-8") as fp:
        json.dump(data,fp,ensure_ascii=False)

page_id=1

while page_id<=limit:
    
    url = "https://www.hurriyetemlak.com/projeler/estate/estateforbounds"

    payload = {'some': 'data','page': page_id}
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload,sort_keys=True), headers=headers)

    page=json.loads(response.content)
    data={}


    ad=0
    while ad<=15:

       path="./ads"
       file_name=f"page{page_id}ads{ad}" 
       edited_page=page["ads"]
       data=edited_page[ad]

       write_to_json_file(path,file_name,data)
       ad+=1

    page_id+=1
