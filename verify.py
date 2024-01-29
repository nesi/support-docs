import re
import sys
import json
import urllib
import yaml
import requests


BASE = "https://nesi.zendesk.com/api/v2/help_center/en-gb"


results = {}

# for k, v in yaml.safe_load(open("docs/redirect_map.yml")).items():
#     print(f"{BASE}/{''.join(k.split('.')[:-1])})")

for input_file in sys.argv:

    # print(requests.get(f"{BASE}/{k.split('.')[:-1]}"))
    # print(f"{BASE}/{k.split('.')[:-1]}")
    with open(input_file, "r") as f:
        sec = json.load(f)

        link = "http://www.somesite.com/details.pl?urn=2344"
        f = urllib.urlopen(link)
        myfile = f.read()

        for page in sec:
            if "body" not in page:
                continue
            matches = re.findall(r"<table[\s\S]*?</table>", page["body"], re.MULTILINE)
            if not matches:
                continue
            results[titlefication(page['name'])] = [len(re.findall(r"<tr[\s\S]*?</tr>", match, re.MULTILINE)) for match in matches]