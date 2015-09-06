"""
Get's the latest relevant posts and uploads them to the DB
"""
import logging
import datetime

from django.core.management.base import BaseCommand

from apartments.models import Post
from ._post_getter import PostGetter

def parse_time(timestr):
    return datetime.datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S%Z")

class Command(BaseCommand):
    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument("-w", "--word", action="append", dest="words",
                             help="Word to filter by", required=True)
        parser.add_argument("-g", "--group", action="append", dest="groups",
                             help="Group ID to search on", required=True)
        parser.add_argument("-t", "--token", required=True,
                             help="User token to search with")
        parser.add_argument("-s", "--since", help="Since when to search",
                             default="2015-09-01")

    def handle(self, *args, **options):
        log = logging.getLogger("post_fetch")
        new_counter = 0
        for group in options["groups"]:
            post_gtter = PostGetter(group, options["words"], options["token"],
                                    options["since"])
            for fetched_post in post_gtter.get_posts():
                post_defaults = {
                    "message": fetched_post["message"],
                    "user": fetched_post["from"]["name"],
                    "created_time": fetched_post["created_time"],
                    "updated_time": fetched_post["updated_time"]
                }
                obj, created = Post.objects.update_or_create(
                    post_id=fetched_post["id"],
                    defaults=post_defaults
                )
                if created:
                    log.debug("Added new post: %s", obj.post_id)
                    new_counter += 1
                else:
                    log.debug("Updated post: %s", obj.post_id)
        log.info("Found %d new posts!", new_counter)
