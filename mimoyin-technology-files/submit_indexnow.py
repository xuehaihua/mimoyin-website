#!/usr/bin/env python3
"""
IndexNow URL Submitter for mimoyin.com
Run this script after publishing new content to notify search engines immediately.
"""

import json
import urllib.request
import urllib.error
import sys

# Configuration
API_KEY = "3a5f7c2d-8b1e-4f9a-9c3d-6e8a1b5f7c2d"
WEBSITE_URL = "https://www.mimoyin.com"
API_ENDPOINT = "https://api.indexnow.org/IndexNow"

def submit_urls(urls):
    """Submit URLs to IndexNow API"""
    payload = {
        "host": "www.mimoyin.com",
        "key": API_KEY,
        "keyLocation": f"{WEBSITE_URL}/{API_KEY}.txt",
        "urlList": urls
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        API_ENDPOINT,
        data=data,
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.status
            body = response.read().decode('utf-8')
            print(f"✅ Success! Status: {status}")
            print(f"Response: {body}")
            return True
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error: {e.code}")
        print(f"Response: {e.read().decode('utf-8')}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python submit_urls.py URL1 [URL2 URL3 ...]")
        print("\nExample:")
        print('  python submit_urls.py "https://www.mimoyin.com/"')
        print('  python submit_urls.py "https://www.mimoyin.com/eptfe-membrane/" "https://www.mimoyin.com/tpu-membrane/"')
        sys.exit(1)
    
    urls = sys.argv[1:]
    print(f"📤 Submitting {len(urls)} URL(s) to IndexNow...")
    print()
    
    success = submit_urls(urls)
    
    if success:
        print("\n✅ URLs submitted successfully!")
        print("Search engines (Bing, Yandex, etc.) will index them soon.")
    else:
        print("\n❌ Submission failed. Check the errors above.")

if __name__ == "__main__":
    main()
