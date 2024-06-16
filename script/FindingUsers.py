import sys

import requests


site = sys.argv[1]
# append /wp-json/wp/v2/users to the site URL
users_url = site + "/wp-json/wp/v2/users"

# send a GET request to the users URL
response = requests.get(users_url)

# URLs to check
urls_to_check = [
    ("/wp-json/wp/v2/users", "WP REST API users endpoint"),
    ("/author-sitemap.xml", "Author sitemap"),
    ("/wp-json/wp/v2/users/1", "WP REST API user with ID 1"),
    ("/wp-sitemap-users-1.xml", "WP user sitemap"),
]


# Function to check if a URL is accessible and print the result
def check_url(url, description):
    full_url = site + url
    try:
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Found {description} at: {full_url}")
        elif response.status_code == 404:
            pass
        else:
            print(f"Failed to check {description}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred while checking {description}: {e}")


# check if the request was successful (status code 200)
if response.status_code == 200:
    # get the JSON data from the response
    users_data = response.json()

    # check if there are users
    if users_data:
        # loop through the users data
        for user in users_data:
            # get the user ID, name, and slug
            user_id = user["id"]
            user_name = user["name"]
            user_slug = user["slug"]

            # print the user details
            print(f"User ID: {user_id}")
            print(f"User Name: {user_name}")
            print(f"User Slug: {user_slug}")
            print()
    else:
        print("No users found.")
else:
    print(f"Failed to fetch users. Status code: {response.status_code}")

# Loop through the URLs and check each one
for url, description in urls_to_check:
    check_url(url, description)
