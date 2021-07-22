import requests 
import os
from json2html import json2html
import json
import re
import importlib
import subprocess
import yaml
class ZendeskAPI:
    def __init__(self, zendesk_url, username, password):
        self.zendesk_url = zendesk_url
        self.username = username
        self.password = password
    
    def _get(self, path, **kwargs):
        auth = (self.username, self.password)
        return requests.get(f"{self.zendesk_url}/{path}", auth = auth, **kwargs)
    
    def _post(self, path, **kwargs):
        auth = (self.username, self.password)
        return requests.post(f"{self.zendesk_url}/{path}", auth = auth, **kwargs)
    
    def _put(self, path, **kwargs):
        auth = (self.username, self.password)
        return requests.put(f"{self.zendesk_url}/{path}", auth = auth, **kwargs)
    
    def _delete(self, path, **kwargs):
        auth = (self.username, self.password)
        return requests.delete(f"{self.zendesk_url}/{path}", auth = auth, **kwargs)
        
    
    def get_section_articles(self, section_id):
        result = self._get("articles/search.json", params = {"section": section_id, "per_page": 100})
        
        articles = []
        data = result.json()
        articles += data["results"]
        
        count = data["count"]
        page = 2
        
        while (100*(page - 1) < count):
            print(f"getting {page} page results")
            result = self._get("articles/search.json", params = {"section": section_id, "per_page": 100, "page": page})
            data = result.json()
            articles += data["results"]
            page += 1
            
        return articles
    
    def delete_article(self, article_id):
        result = self._delete(f"articles/{article_id}.json")
        return result
    
    def update_article_contents(self, article_id, title, body):
        translation = {"translation" : {
                "title": title,
                "body": body
            }}
        result = self._put(f"articles/{article_id}/translations/en-gb", json = translation)
        return result
    
    def update_article_labels(self, article_id, labels):
        article = {"article": {
            "label_names": labels
        }}
        result = self._put(f"articles/{article_id}", json = article)
        return result
    
    def post_article(self, section_id, title, body, labels):
        article = {"article": {
                    "section_id": section_id,
                    "title":  title,
                    "body": body,
                    "user_segment_id": 90870,
                    "permission_group_id": 23775,
                    "label_names": labels,
                    "locale": "en-gb"
                }}
        result = self._post(f"en-gb/sections/{section_id}/articles", json = article)
        return result

def to_markdown(html):
    """ Use pandoc to convert HTML pages to Markdown """
    markdown = subprocess.run(["pandoc", "-t","markdown+grid_tables", "-f", "html"],
                            input = html, stdout = subprocess.PIPE,
                            check = True,
                            encoding='utf-8').stdout
    return markdown

def create_category_index(category):
    return f"""\
        {{% extends "category.md" -%}}
        {category['description']}
        {{% block content -%}}
        {{% endblock %}}
    """

def create_article(article):
    return to_markdown(article["body"])



username = os.environ["ZENDESK_USERNAME"]
password = os.environ["ZENDESK_PASSWORD"]

doc_root_dir = "/home/cwal219/Desktop/mkdocs_support/docs"
#module_list_location = os.environ["ZENDESK_MODULE_LIST"]


zendesk_url = "https://nesi.zendesk.com/api/v2/help_center"

# def unpack(thing, indent):
#     try: print(" " * indent + thing["name"])
#     except: pass
#     if 'categories' in thing:
#         for category in thing["categories"]: unpack(category, indent+4)
#     elif 'sections' in thing:
#         for section in thing["sections"]: unpack(section, indent+4)
#     elif 'articles' in thing:
#         for article in thing["articles"]: unpack(article, indent+4)


site_nav={"nav":[]}

z = ZendeskAPI(zendesk_url, username, password)

for category in z._get("categories.json").json()["categories"]:

    category_sanitized=category['name'].replace(' ', '_')
    site_nav["nav"].append({category_sanitized:[]})

    try: os.mkdir(f"{doc_root_dir}/{category_sanitized}")
    except FileExistsError: pass

    # with open(f"{doc_root_dir}/{category_sanitized}/index.md", 'w') as index_file:
    #     index_file.write(create_category_index(category))

    print(category["description"])
    section_nav=[]
    for section in z._get(f"categories/{category['id']}/sections.json").json()["sections"]:

        section_sanitized=section['name'].replace(' ', '_')

        try: os.mkdir(f"{doc_root_dir}/{category_sanitized}/{section_sanitized}")
        except FileExistsError: pass

        # with open(f"{doc_root_dir}/{category_sanitized}/{section_sanitized}/index.md", 'w') as index_file:
        #     index_file.write(create_category_index(category))

        print(f"    {section['name']}")
        nav_article=[]
        for article in z._get(f"sections/{section['id']}/articles.json").json()["articles"]:
            article_sanitized=article['name'].replace(' ', '_').replace('/', '-')
            nav_article.append(article_sanitized)
            with open(f"{doc_root_dir}/{category_sanitized}/{section_sanitized}/{article_sanitized}.md", 'w') as article_file:
                article_file.write(create_article(article))
            print(f"        {article['name']}")
        section_nav.append({section_sanitized:nav_article})
    site_nav["nav"].append({category_sanitized:section_nav})

print(yaml.dump(site_nav))