import requests
import csv

# Function to fetch posts and print titles
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    # If request was succesful, parse the JSON data
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

# Function to fetch posts and save them into a CSV file
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    # If request was successful, parse the JSON data and save to CSV
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()