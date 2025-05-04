import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from markdownify import markdownify as md
import json

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Select only the section with product details
product_section = soup.select_one("div.content")
markdown_content = md(str(product_section))

print(markdown_content)

prompt = [
    {
        "role": "system",
        "content": "You are a helpful assistant that extracts structured data from web content."
    },
    {
        "role": "user",
        "content": (
            "Extract the following details from the Markdown:\n"
            "- Book title\n"
            "- Price\n"
            "- Availability\n\n"
            f"Markdown:\n{markdown_content}\n\n"
            "Respond only with extracted data in JSON format."
        ),
    },
]

api_key = "YOUR_PERPLEXITY_API_KEY"
client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

# Send chat completion request
response = client.chat.completions.create(
    model="sonar-pro",
    messages=prompt,
)

# Export the result in JSON format
scraped_data = json.loads(response.choices[0].message.content)

# Print structured result
print(json.dumps(scraped_data, indent=2))