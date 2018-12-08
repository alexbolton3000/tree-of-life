import requests 


SEARCH_URL = 'http://phylopic.org/api/a/name/search'
BASE_URL = 'http://phylopic.org'


def phylopic_search(name):
    print('------------------ phylopic_search')
    payload = dict(text=name)
    response = requests.get(SEARCH_URL, params=payload)
    print(response)
    # print(dir(response))
    if response.ok:
        return response.json()
    # return response.text()


def phylopic_get_image_url(id):
    print('------------------ phylopic_get_image_url')
    payload = dict(options='svgFile')
    response = requests.get(
        f'http://phylopic.org/api/a/name/{id}/images', 
        params=payload)
    # if response.ok:
    #   return response.json()
    data = response.json()
    print(data)
    print(data['result'].get('same'))
    urls = []

    # Check `same` first
    if data['result'].get('same'):
        print("using same")
        for images in data['result']['same']:
            try:
                if images['svgFile']:
                    urls.append(f"{BASE_URL}{images['svgFile']['url']}")
            except KeyError:
                print('no svg in same')
                pass
    if not urls and data['result'].get('supertaxa'):
        print('using supertaxa')
        for images in data['result']['supertaxa']:
            try:
                if images['svgFile']:
                    urls.append(f"{BASE_URL}{images['svgFile']['url']}")
            except KeyError:
                print('no svg in supertaxa')

    return urls


def search_image(name):
    results = phylopic_search(name)

    ids = []
    for r in results['result']:
        try:
            ids.append(r['canonicalName']['uid'])
        except KeyError:
            print('NO VALID KEY FOUND')
    print(ids)

    image_urls = []
    for id in ids:
        image_urls = phylopic_get_image_url(id)
        if image_urls:
            break

    return image_urls
    

# def name_to_url(name):
#         image_id = image_manager.search_image(self.name)
#         image_url = image_manager.phylopic_get_image_url(image_id)
        

# def save_image(url, ):
#     new_file_name = 
#     r = requests.get(url, allow_redirects=True)
#     open('google.ico', 'wb').write(r.content)
    



# # r = search_image('felis catus')
# r = phylopic_get_image_url('0c0d9740-d855-423a-86f2-66097f918f12')
# print(r)

