# Nadav's Apartment Search!

This program will find me an apartment!
It will;

1. Get all the posts from the relevant Facebook pages
2. Filter the relevant posts that include the keywords I'll be searching for
   ("נחלאות", "מרכז העיר...")
3. Alert when new posts pop up - either by mail, iOS notification or sms. The
   alert will include the contents of the post.
4. Allow me to view the different posts in a quick and easy way.

# Modules

## Retrieve

Gets the Facebook IDs of the relevant pages/groups and a list of keywords and
yields all the posts from these pages that match.
