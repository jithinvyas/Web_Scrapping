import requests
import os
url = "https://images.spiceworks.com/wp-content/uploads/2022/08/02141047/facets-of-data-analytics.jpg"

os.chdir("D:\\")

with open ('image1.jpg', 'wb') as f:
    f.write(requests.get(url).content)