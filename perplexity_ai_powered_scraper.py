from crawl import crawl
from parse import parse_html_into_markdown_format
from openai import OpenAI
import json

URL = "https://www.amazon.com/Art-War-DELUXE-Sun-Tzu/dp/9388369696/ref=sr_1_1"

html_content = crawl(URL)
markdown_content = parse_html_into_markdown_format(html_content)

prompt = [
    {
        "role": "system",
        "content": "You are a helpful assistant that summarizes an Amazon product book page."
    },
    {
        "role": "user",
        "content": (
            "Extract the following details from the Markdown:\n"
            "- 1 sentence summary\n"
            "- Search the web for recommended reading\n"
            "- Prices\n\n"
            f"Markdown:\n{markdown_content}\n\n"
            "Respond only with extracted data in JSON format."
        ),
    },
]

client = OpenAI(api_key="<perplexity.ai API KEY>", base_url="https://api.perplexity.ai")

# Send chat completion request
response = client.chat.completions.create(
    model="sonar-pro",
    messages=prompt,
)

# Export the result in JSON format
scraped_data = json.loads(response.choices[0].message.content)

print(json.dumps(scraped_data, indent=2))
