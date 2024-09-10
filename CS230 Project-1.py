# # build an application to store URL’s of any length and return ashortened version of the URL in Python.

from url_shortener import shorten_url, expand_url

def main():
    print("Welcome to URL Shortener")
    
    while True:
        print("\nMenu:")
        print("1. Shorten a URL")
        print("2. Expand a shortened URL")
        print("3. Exit")

        choice = input("Enter '1' to shorten a URL, '2' to expand a URL, or '3' to exit: ")

        if choice == '1':
            full_url = input("Enter the full URL: ")
            short_url = shorten_url(full_url)
            print(f"Shortened URL: {short_url}")
        elif choice == '2':
            short_url = input("Enter the shortened URL: ")
            full_url = expand_url(short_url)
            print(f"Full URL: {full_url}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
