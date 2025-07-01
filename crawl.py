from requests.exceptions import RequestException
from urllib3.exceptions import InsecureRequestWarning
import requests

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}

def crawl(url) -> str:
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            verify=False,
            timeout=30
        )
        response.raise_for_status()

        return response.text

    except RequestException as error:
        print(f"\nFailed to crawl url '{url}': {error}\n")
        raise

def crawl_with_smart_proxy(url) -> str:
    proxy_url = "http://<Private token>:@smartproxy.crawlbase.com:8012"  # Use https:// and port 8013 for HTTPS
    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            proxies=proxies,
            verify=False,
            timeout=30
        )
        response.raise_for_status()

        return response.text

    except RequestException as error:
        print(f"\nFailed to crawl url '{url}': {error}\n")
        raise

if __name__ == "__main__":

    html_content = crawl("https://www.amazon.com/Art-War-DELUXE-Sun-Tzu/dp/9388369696/ref=sr_1_1")
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
