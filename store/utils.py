import requests
from .models import Products

# to theck if a given url is active
class UrlTest():
    def test(url):
        try:
            response = requests.get(url)

            if response.status_code == 200:
                return int(200)
            else:
                return int(404)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while making the request: {e}")
            return int(404)


