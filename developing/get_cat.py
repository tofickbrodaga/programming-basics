import requests

URL = 'https://cataas.com'
OK = 200

def get_cat(filename: str = 'cat.jpg') -> None:
    response = requests.get(URL)
    if response.status_code != OK:
        print(f'Request to Cataas falied with')
        print(f'Status code: {response.status_code}')
        return
    with open(filename, 'wb') as cat_file:
        cat_file.write(response.content)
        print(f'cat was saved to file {filename}')

get_cat()