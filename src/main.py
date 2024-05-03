from pwinput import pwinput
import instaloader
from instaloader import Post
from list_utils import get_random_list_items
from string_utils import get_shortcode


def main():
    """
    The main entry point of the program::
    1. Creates an instance of the Instaloader class.
    2. Prompts the user to enter their username and password.
    3. Logs in to Instagram using the provided credentials.
    4. Prompts the user to enter the URL of a post.
    5. Extracts the shortcode from the provided URL.
    6. Retrieves the post object corresponding to the shortcode.
    7. Retrieves the comments on the post.
    8. Selects two random comments from the list of comments.
    9. Prints the username and text of each selected comment.

    Parameters:
    None

    Returns:
    None
    """
    ig = instaloader.Instaloader()

    print("Log in\n")
    username = input("Username: ")
    password = pwinput()

    print("\nLogging in...")
    ig.login(username, password)

    url = input("\nPost URL: ")
    shortcode = get_shortcode(url)

    print("\nFinding post...")
    post = Post.from_shortcode(ig.context, shortcode)

    print("\nGetting comments...")
    comments = list(post.get_comments())

    valid = False
    number = 0

    while not valid:
        number = int(input("\nHow many comments would you like to select? "))
        if number > len(comments):
            print("Number of comments to select cannot exceed total number of comments (" + str(len(comments)) + ")")
        else:
            valid = True

    print("\nSelecting " + str(number) + " random comments...")
    two_random_comments = get_random_list_items(comments, number)

    for comment in two_random_comments:
        print(comment.owner.username + ": " + comment.text)


if __name__ == "__main__":
    main()
