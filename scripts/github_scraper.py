import requests
import json
import time
import sys


def read_token_from_file():
    with open("secrets/github_api_token.txt", "r") as file:
        token = file.readline().strip()
    return token


def fetch_public_repositories(github_api_token):
    dataset = []

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"Bearer {github_api_token}",
    }

    for stars in range(50, 101):
        for page in range(1, 50):
            query = f"language:java stars:{stars}"
            params = {"q": query, "per_page": 100, "page": page}
            print(f"[QUERY]: {query}, [PAGE]: {page}", file=sys.stderr)

            url = "https://api.github.com/search/repositories"
            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            repository_data = data["items"]
            if repository_data == []:
                break
            dataset += repository_data

            time.sleep(3)

    print(json.dumps(dataset))


def main():
    github_api_token = read_token_from_file()
    fetch_public_repositories(github_api_token)


if __name__ == "__main__":
    main()
