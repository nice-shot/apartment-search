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

    def __init__(self, group_id, keywords, token="", since="2015-09-01"):
        """
        :param group_id: The Facebook object ID for the group
        :type group_id: str
        :param keywords: A list of keywords to search for in the posts
        :type keywords: list[str]
        :param token: User access token
        :type token: str
        :param seen_posts: A list of post-ids that were already seen
        :type seen_posts: list[str]
        :param since: A date string used to filter old posts
        :type since: str
        """
        self.log = logging.getLogger("post_fetch.getter." + group_id)
        self.keywords = keywords

        self.base_url = "https://graph.facebook.com/v2.0/{}/feed?{}".format(
            group_id,
            urlencode({
                "access_token": token,
                "since": since,
                "fields": ",".join(self.FIELDS),
                "limit": self.POST_LIMIT
            })
        )
        self.log.info("Created new post fetcher for page: %s with words: %r",
                      group_id, self.keywords)

    def get_posts(self, url=None):
        """
        Starts getting posts from the given page. If the url is omitted - grabs
        from the main page's feed

        :param url: The page to grab feeds from
        :type url: str
        """
        if not url:
            url = self.base_url

        self.log.debug("Getting URL: %s", url)
        page_data = json.loads(urlopen(url).read().decode("utf-8"))

        for post in page_data.get("data", []):
            if "message" not in post:
                continue

            for word in self.keywords:
                if word in post["message"]:
                    self.log.debug("Emitting post: %s", post["id"])
                    yield post
                    break

        paging = page_data.get("paging", {})

        if "next" in paging:
            for post in self.get_posts(paging["next"]):
                yield post

        return
