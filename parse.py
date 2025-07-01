from crawl import crawl
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def parse_html_into_markdown_format(html_content) -> str:
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        element = soup.find(id='centerCol')

        return md(str(element.text))
    except Exception as error:
        print(f"\nFailed to parse html to markdown: {error}\n")
        raise

if __name__ == "__main__":

    html_content = crawl("https://www.amazon.com/Art-War-DELUXE-Sun-Tzu/dp/9388369696/ref=sr_1_1")

    markdown_content = parse_html_into_markdown_format(html_content)
    with open('output.md', 'w', encoding='utf-8') as file:
        file.write(markdown_content)
