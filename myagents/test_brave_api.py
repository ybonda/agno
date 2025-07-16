import requests
import os

# Test the Brave API directly
def test_brave_api():
    api_key = os.getenv("BRAVE_API_KEY")
    if not api_key:
        print("❌ BRAVE_API_KEY environment variable not set")
        print("Get your API key from: https://api.search.brave.com/app/keys")
        return
    
    print(f"✅ API key found: {api_key[:10]}...")
    
    try:
        response = requests.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers={
                "X-Subscription-Token": api_key,
            },
            params={
                "q": "chatgpt pricing",
                "count": 3,
                "country": "us",
                "search_lang": "en",
            },
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API call successful!")
            
            if "web" in data and "results" in data["web"]:
                print(f"Found {len(data['web']['results'])} results:")
                for i, result in enumerate(data["web"]["results"][:3], 1):
                    print(f"{i}. {result.get('title', 'No title')}")
                    print(f"   URL: {result.get('url', 'No URL')}")
                    print(f"   Description: {result.get('description', 'No description')[:100]}...")
                    print()
            else:
                print("❌ No web results in response")
                print("Response structure:", list(data.keys()))
        else:
            print(f"❌ API call failed: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_brave_api() 