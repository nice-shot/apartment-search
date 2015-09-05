"""
Retrieves posts from a Facebook group and filters them based on a given word
"""
import json
import logging
from urllib.parse import urlencode
from urllib.request import urlopen

class PostGetter(object):
    """
    An iterator that yields the next relevant post from the given page
    """
    POST_LIMIT = 30
    FIELDS = ["message", "created_time", "updated_time", "from"]

    def __init__(self, group_id, keywords, token=None, last_id=None):
        """
        :param group_id: The Facebook object ID for the group
        :type group_id: int
        :param keywords: A list of keywords to search for in the posts
        :type keywords: list[str]
        :param token: User access token
        :type token: str
        :param last_id: Last post that we checked
        :type last_id: int
        """
        self.log = logging.getLogger(__name__ + "." + str(group_id))
        base_url = "https://graph.facebook.com/v2.0/{}/feed?{}".format(
            group_id,
            urlencode({
                "access_token": token,
                "fields": ",".join(self.FIELDS),
                "limit": self.POST_LIMIT
            })
        )
        self.page_data = json.loads(urlopen(base_url).read().decode("utf-8"))

        self.keywords = keywords
        self.last_id = last_id

    def get_post(self):
        for post in self.page_data["data"]:
            for word in self.keywords:
                yield post

        return
