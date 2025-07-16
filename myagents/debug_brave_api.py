import requests
import os

def debug_brave_api():
    api_key = os.getenv("BRAVE_API_KEY")
    if not api_key:
        print("❌ BRAVE_API_KEY environment variable not set")
        return
    
    print(f"Testing API key: {api_key[:10]}...")
    print(f"Full API key length: {len(api_key)}")
    
    # Test with a simple query first
    headers = {
        "X-Subscription-Token": api_key,
        "Accept": "application/json",
    }
    
    params = {
        "q": "test",
        "count": 1,
    }
    
    print(f"Headers: {headers}")
    print(f"Params: {params}")
    
    try:
        response = requests.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers=headers,
            params=params,
            timeout=10
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API call successful!")
            print(f"Response keys: {list(data.keys())}")
        else:
            print(f"❌ API call failed: {response.status_code}")
            print(f"Response: {response.text}")
            
        # Also test with different authentication methods
        print("\n" + "="*50)
        print("Testing alternative authentication...")
        
        # Some APIs use different header names
        alt_headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        }
        
        alt_response = requests.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers=alt_headers,
            params=params,
            timeout=10
        )
        
        print(f"Alt Status Code: {alt_response.status_code}")
        if alt_response.status_code != 200:
            print(f"Alt Response: {alt_response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    debug_brave_api() 