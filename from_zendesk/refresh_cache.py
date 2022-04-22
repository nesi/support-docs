import json
import os

import requests
import yaml


def main():
    """main"""
    username = os.environ["ZENDESK_USERNAME"]
    password = os.environ["ZENDESK_PASSWORD"]

    cache_root_dir = "from_zendesk/cache"

    # module_list_location = os.environ["ZENDESK_MODULE_LIST"]

    zendesk_url = "https://nesi.zendesk.com/api/v2/help_center"
    z = ZendeskAPI(zendesk_url, username, password)

    # Make directorys for storing json files
    try:
        os.mkdir(f"{cache_root_dir}/categories")
    except FileExistsError:
        pass
    try:
        os.mkdir(f"{cache_root_dir}/sections")
    except FileExistsError:
        pass
    root = z._get("categories.json").json()
    root = z._get("").json()

    with open(f"{cache_root_dir}/root.json", "w+") as f:
        f.write(json.dumps(root))

    for category in root["categories"]:

        sections = z._get(f"categories/{category['id']}/sections.json").json()

        with open(f"{cache_root_dir}/categories/{category['id']}.json", "w+") as f:
            f.write(json.dumps(sections))

        for section in sections["sections"]:
            articles = z._get(f"sections/{section['id']}/articles.json").json()

            with open(f"{cache_root_dir}/sections/{section['id']}.json", "w+") as f:
                f.write(json.dumps(articles))

    # with open(f"{cache_root_dir}/index.html"


class ZendeskAPI:
    """For interfacing with zendesk docs"""

    def __init__(self, zendesk_url, username, password):
        self.zendesk_url = zendesk_url
        self.username = username
        self.password = password

    def _get(self, path, **kwargs):
        auth = (self.username, self.password)
        return requests.get(f"{self.zendesk_url}/{path}", auth=auth, **kwargs)

    def _post(self, path, **kwargs):
        auth = (self.username, self.password)
        return requests.post(f"{self.zendesk_url}/{path}", auth=auth, **kwargs)

    def _put(self, path, **kwargs):
        auth = (self.username, self.password)
        return requests.put(f"{self.zendesk_url}/{path}", auth=auth, **kwargs)

    def _delete(self, path, **kwargs):
        auth = (self.username, self.password)
        return requests.delete(f"{self.zendesk_url}/{path}", auth=auth, **kwargs)

    def get_section_articles(self, section_id):
        result = self._get(
            "articles/search.json", params={"section": section_id, "per_page": 100}
        )

        articles = []
        data = result.json()
        articles += data["results"]

        count = data["count"]
        page = 2

        while 100 * (page - 1) < count:
            print(f"getting {page} page results")
            result = self._get(
                "articles/search.json",
                params={"section": section_id, "per_page": 100, "page": page},
            )
            data = result.json()
            articles += data["results"]
            page += 1

        return articles

    def delete_article(self, article_id):
        result = self._delete(f"articles/{article_id}.json")
        return result

    def update_article_contents(self, article_id, title, body):
        translation = {"translation": {"title": title, "body": body}}
        result = self._put(
            f"articles/{article_id}/translations/en-gb", json=translation
        )
        return result

    def update_article_labels(self, article_id, labels):
        article = {"article": {"label_names": labels}}
        result = self._put(f"articles/{article_id}", json=article)
        return result

    def post_article(self, section_id, title, body, labels):
        article = {
            "article": {
                "section_id": section_id,
                "title": title,
                "body": body,
                "user_segment_id": 90870,
                "permission_group_id": 23775,
                "label_names": labels,
                "locale": "en-gb",
            }
        }
        result = self._post(f"en-gb/sections/{section_id}/articles", json=article)
        return result


def create_category_index(category):
    return f"""\
        {{% extends "category.md" -%}}
        {category['description']}
        {{% block content -%}}
        {{% endblock %}}
    """


main()
