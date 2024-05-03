def get_shortcode(url):
    """
    Extracts the shortcode from a given Instagram post URL.

    Args:
        url (str): The URL of the Instagram post.

    Returns:
        str: The shortcode extracted from the URL.

    Raises:
        IndexError: If the URL does not contain "/p/" or if the shortcode is not found.

    Example:
        >>> get_shortcode("https://www.instagram.com/p/B0000000000/")
        'B0000000000'
    """
    return url.split("/p/")[1].split("/")[0]