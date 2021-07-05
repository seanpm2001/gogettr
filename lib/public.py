from lib.capabilities import user_activity, all_posts
from lib.api import ApiClient


class PublicClient:
    """A client for all the public GETTR methods. If the API doesn't require an account to pull the data, it belongs here."""

    def __init__(self):
        self.api_client = ApiClient()

        # Set up capabilities
        self.user_activity = user_activity.UserActivity(self.api_client).pull
        self.all_posts = all_posts.AllPosts(self.api_client).pull