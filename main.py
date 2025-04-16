import requests

def main():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("✅ Kết nối thành công đến GitHub API!")
    else:
        print(f"❌ Kết nối thất bại. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
