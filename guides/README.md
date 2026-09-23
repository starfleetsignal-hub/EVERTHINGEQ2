# Forum player guides

forums.daybreakgames.com/robots.txt disallows all crawling, so guides are added one by one
from links the user picks. Each guide gets a page on our site with our own summary, the
author's name and a link to the original thread. The guide text is never copied.

guides.json is a list of entries:

    {
      "title": "Almost complete guide to Heroic Opportunities",
      "author": "forum username",
      "url": "https://forums.daybreakgames.com/eq2/index.php?threads/...",
      "posted": "YYYY-MM-DD",
      "updated": "YYYY-MM-DD or null",
      "topics": {"zones": [], "classes": [], "expansions": [], "tags": []},
      "summary": "Our own summary in Markdown (a few paragraphs, no quoted guide text).",
      "fetched": "YYYY-MM-DDTHH:MM:SSZ"
    }

Ready-made guide pages are in guides/pages/<slug>.md (copy them to content/guides/ when building the site) with front matter from the entry and a
credit line: "Guide by <author> on the EverQuest II forums. Read the original: <url>".
