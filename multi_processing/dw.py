import requests
import time

# fill with urls to download
img_urls = []

t1 = time.perf_counter()

for img_url in img_urls:
    # get the file in binary adn write in binary too (wb)
    img_bytes = requests.get(img_url).content
    # 3 if unsplash urls
    img_name = img_url.split('/')[-1]
    img_name = f"{img_name}.jpg"
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded...")

t2 = time.perf_counter()

print(f"Downloaded in {t2-t1} seconds")
