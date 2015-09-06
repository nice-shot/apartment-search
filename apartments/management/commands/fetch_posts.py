"""
Get's the latest relevant posts and uploads them to the DB
"""
from django.core.management.base import BaseCommand
import datetime

from apartments.models import Post
from _post_getter import PostGetter

def parse_time(timestr):
    return datetime.datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S%Z")

class Command(BaseCommand):
    help = __doc__

    def add_arguments(self, parser):
        parser.add_arguments("-w", "--word", action="append", dest="words",
                             help="Word to filter by", required=True)
        parser.add_arguments("-g", "--group", action="append", dest="groups",
                             help="Group ID to search on", required=True)
        parser.add_arguments("-t", "--token", required=True,
                             help="User token to search with")
        parser.add_arguments("-s", "--since", help="Since when to search",
                             default="2015-09-01")

    def handle(self, *args, **options):
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
                Post.object.update_or_create(post_id=fetched_post["id"],
                                             defaults=post_defaults)
