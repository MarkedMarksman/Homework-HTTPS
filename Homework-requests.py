
import requests

def find_smartest_superhero(name):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    main = requests.get(url=url)
    heroes_list = name.split(', ')
    heroes = {}
    intgelligence_list = []
    for i in main.json():
        if i.get('name') in heroes_list:
            heroes[i['name']] = i['powerstats']['intelligence']
    for number in heroes.values():
        intgelligence_list.append(int(number))
    for key,value in heroes.items():
        if value == max(intgelligence_list):
            res = f'Самый умный герой {key} c количеством интеллекта {value}'
    return print(res)
    
if __name__ == '__main__':
    find_smartest_superhero('Hulk, Captain America, Thanos')

class YandexDisk():

    def __init__(self,token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type':'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    
    def _upload_file_link(self,path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path' : path_to_file, 'overwrite': 'true'}
        response = requests.get(upload_url,headers=headers,params=params)
        return response.json()
    def upload_file_to_disk(self,path_to_file,file_name):
        link = self._upload_file_link(path_to_file=path_to_file)
        url = link.get('href')
        with open(file_name,'r') as file:
            response = requests.put(url,data=open(file_name,'rb'))
            response.raise_for_status()
    
TOKEN = ""
if __name__ == '__main__':
    file_path = 'test.txt'
    file_name = 'test.txt'
    ya = YandexDisk(token=TOKEN)
    res = (ya.upload_file_to_disk(path_to_file=file_path,file_name=file_name))
    if res == None:
        print(f'Файл загружен')
    else:
        print(f'При загрузке файла возникла ошибка')