import requests
import shutil

def __init__() -> None:
    pass

def generate_cover() -> None:
    category = 'technology'
    api_url = 'https://api.api-ninjas.com/v1/randomimage?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'hWxkl+qpoS//4bpl57Kqcg==rhMW35IKIYM83DvR', 'Accept': 'image/jpg'}, stream=True)
    if response.status_code == requests.codes.ok:
        with open('src/images/cover.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        print("Error:", response.status_code, response.text)