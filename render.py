#!/usr/bin/env python3

import markdown2
from datetime import datetime, timedelta
import time

import pytz


articles = [
    {
        "export_filename": "index.html",
        "lang": "ka",
        "title": "ADHD საქართველოში - ყურადღების დეფიციტის ჰიპერაქტიურობის აშლილობა (ადჰდ)",
        "description": "ერთად გავზარდოთ ცნობიერება ADHD-ს მიმართ საქართველოს ჯანდაცვის სისტემაში!",
        "last_update_str": "გვერდის ბოლო განახლების თარიღი:",
        "file": "articles/contents-ka.md",
        "canonical": "https://adhd.ge/",
        "initial_publish_date": "2022-12-03T21:52:42.449005+04:00"
    },
    {
        "export_filename": "index-en.html",
        "lang": "en",
        "title": "ADHD in Georgia - Attention deficit hyperactivity disorder",
        "description": "Let's raise awareness of ADHD in the Georgian healthcare system together!",
        "last_update_str": "Page last updated on:",
        "file": "articles/contents-en.md",
        "canonical": "https://adhd.ge/index-en.html",
        "initial_publish_date": "2023-02-27T23:49:05.595561+04:00"
    }
]


with open("template.html", "r") as template_file:
    template = template_file.read()

classesDict = {"table": "table"}

extras = {
    "tables": None,
    "html-classes": classesDict,
    "target-blank-links": None
}

for article in articles:
    with open(article["file"], "r") as contents_file:
        contents = contents_file.read()

    rendered_contents = markdown2.markdown(contents, extras=extras)

    timestamp = datetime.fromtimestamp(time.time(), pytz.timezone("Asia/Tbilisi"))
    expired_timestamp = timestamp + timedelta(hours=175320)

    rendered_page = (template.replace("{% block content %}{% endblock %}", rendered_contents))

    metadata = {
        "LAST_UPDATE_READABLE": timestamp.strftime("%Y-%m-%d %H:%M:%S (UTC%Z)"),
        "METADATA_PUBLISHED_TIMESTAMP": article["initial_publish_date"],
        "METADATA_MODIFIED_TIMESTAMP": timestamp.isoformat(),
        "METADATA_EXPIRATION_TIMESTAMP": expired_timestamp.isoformat(),
        "METADATA_LANG": article["lang"],
        "METADATA_TITLE": article["title"],
        "METADATA_CANONICAL_URL": article["canonical"],
        "METADATA_DESCRIPTION": article["description"],
        "LANG_LAST_UPDATE_STR": article["last_update_str"],
        "HTML_EXTRA_NAV": ""
    }

    extra_navs = {
        "index.html": "<li class=\"nav-item\"><a href=\"/\" class=\"nav-link\">🇬🇪 ქართული</a></li>",
        "index.en.html": "<li class=\"nav-item\"><a href=\"/index.en.html\" class=\"nav-link\">🇬🇧 English</a></li>"
    }

    for FILENAME, HTML in extra_navs.items():
        if not FILENAME == article["export_filename"]:
            metadata["HTML_EXTRA_NAV"] += HTML

    for TAG, VALUE in metadata.items():
        rendered_page = rendered_page.replace("{{ " + TAG + " }}", VALUE)

    with open(f"prod/{article['export_filename']}", "w") as rendered_file:
        rendered_file.write(rendered_page)

print("articles generated!")
