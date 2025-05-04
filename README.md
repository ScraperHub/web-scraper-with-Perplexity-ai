# web-scraper-with-Perplexity-ai

## 📝 Description

This project demonstrates how to combine traditional web scraping with AI-powered structured data extraction using Perplexity AI. The scraper fetches product data from a website using requests and BeautifulSoup, converts it to Markdown with markdownify, and sends the content to Perplexity’s OpenAI-compatible API for intelligent JSON output.

📖 Full tutorial available here: [How to Use Perplexity AI for Web Scraping](https://crawlbase.com/blog/how-to-use-perlexity-ai-for-web-scraping/)

## 🔧 Setup Instructions

### 1. Install Dependencies

```bash
pip install requests beautifulsoup4 openai markdownify
```

### 2. Get Perplexity AI API Key

- Sign up at [Perplexity.ai](https://docs.perplexity.ai/guides/getting-started)
- Use the OpenAI-compatible API key and set:

```python
client = OpenAI(api_key="YOUR_PERPLEXITY_API_KEY", base_url="https://api.perplexity.ai")
```

## 🚀 How to Run

```bash
python perplexity_ai_powered_scraper.py
```

✅ The script will output structured product details like:

```json
{
	"title": "A Light in the Attic",
	"price": "£51.77",
	"availability": "In stock"
}
```

## 🛡 Bonus: Using Crawlbase Smart Proxy

If the target website blocks your scraper, you can integrate [Crawlbase Smart Proxy](https://crawlbase.com/smart-proxy) to avoid bans and captchas. Just modify the `requests.get()` call:

```python
proxies = {
    "http": "http://_USER_TOKEN_:@smartproxy.crawlbase.com:8012",
    "https": "http://_USER_TOKEN_:@smartproxy.crawlbase.com:8012",
}
response = requests.get(url, headers=headers, proxies=proxies, verify=False)
```

🛠 Replace `_USER_TOKEN_` with your token from Crawlbase.
