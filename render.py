#!/usr/bin/env python3

import markdown2
from datetime import datetime, timedelta
import time

import pytz

with open("contents.md", "r") as contents_file:
    contents = contents_file.read()

with open("template.html", "r") as template_file:
    template = template_file.read()

classesDict = {"table": "table"}

extras = {
    "tables": None,
    "html-classes": classesDict,
    "target-blank-links": None
}

rendered_contents = markdown2.markdown(contents, extras=extras)

timestamp = datetime.fromtimestamp(time.time(), pytz.timezone("Asia/Tbilisi"))
expired_timestamp = timestamp + timedelta(hours=175320)

initial_publish_date_str = "2022-12-03T21:52:42.449005+04:00"

rendered_page = (template.replace("{% block content %}{% endblock %}", rendered_contents)
                 .replace("{{ last_update_readable }}", timestamp.strftime("%Y-%m-%d %H:%M:%S (UTC%Z)"))
                 .replace("{{ published_timestamp.isoformat() }}", initial_publish_date_str)
                 .replace("{{ modified_timestamp.isoformat() }}", timestamp.isoformat())
                 .replace("{{ expiration_timestamp.isoformat() }}", expired_timestamp.isoformat()))


with open("prod/index.html", "w") as rendered_file:
    rendered_file.write(rendered_page)
