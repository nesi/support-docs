"""
Cleans up rendered page HTML before mkdocs-llmstxt converts it to the per-page
markdown served next to each page (e.g. `GROMACS/index.md`) and used for llms.txt.

Configured with `preprocess:` in the llmstxt section of mkdocs.yml. The plugin's own
`autoclean` is turned off there and called at the end of `preprocess()` instead,
because it deletes tab labels before we get a chance to keep them.
"""

from bs4 import NavigableString
from mkdocs_llmstxt import autoclean


def _drop_hidden(soup):
    """Elements hidden until JavaScript shows them, e.g. the empty module version warning."""
    for element in soup.select('[style*="display: none"], [style*="display:none"]'):
        element.decompose()


def _admonition(soup, element, kind, title, body):
    """Replace an admonition with a blockquote that starts with its bold title."""
    quote = soup.new_tag("blockquote")
    heading = soup.new_tag("p")
    strong = soup.new_tag("strong")
    # Untitled admonitions render their type as the title ("Warning"), so only add the type when it differs.
    strong.string = title if not kind or title.lower() == kind.lower() else f"{kind.capitalize()}: {title}"
    heading.append(strong)
    quote.append(heading)
    for child in body:
        quote.append(child.extract())
    element.replace_with(quote)


def _admonitions(soup):
    """`!!! type "Title"` renders as a div, `??? type "Title"` as details/summary."""
    for element in soup.select("div.admonition"):
        kind = next((c for c in element.get("class", []) if c != "admonition"), "")
        title_tag = element.find("p", class_="admonition-title")
        title = title_tag.get_text(strip=True) if title_tag else kind.capitalize()
        if title_tag:
            title_tag.decompose()
        _admonition(soup, element, kind, title, list(element.children))
    for element in soup.select("details"):
        kind = next(iter(element.get("class", [])), "")
        summary = element.find("summary")
        title = summary.get_text(strip=True) if summary else kind.capitalize()
        if summary:
            summary.decompose()
        _admonition(soup, element, kind, title, list(element.children))


def _tabs(soup):
    """Content tabs: keep each tab's label as a bold line above its content."""
    for tabbed_set in soup.select("div.tabbed-set"):
        labels = [label.get_text(strip=True) for label in tabbed_set.select(".tabbed-labels label")]
        blocks = tabbed_set.select(".tabbed-content > .tabbed-block")
        container = soup.new_tag("div")
        for label, block in zip(labels, blocks):
            heading = soup.new_tag("p")
            strong = soup.new_tag("strong")
            strong.string = label
            heading.append(strong)
            container.append(heading)
            for child in list(block.children):
                container.append(child.extract())
        tabbed_set.replace_with(container)


def _app_page_widgets(soup):
    """Application pages: the version buttons from overrides/partials/app/app_version.html."""
    for nav in soup.select('nav[class*="md-tags-ver-"]'):
        versions = [button.get_text(strip=True) for button in nav.find_all("button")]
        paragraph = soup.new_tag("p")
        paragraph.append(NavigableString("Available versions: " + ", ".join(f"`{v}`" for v in versions)))
        nav.replace_with(paragraph)
    # The `module load` block is raw HTML, so it has no language for the converter to pick up
    # (the converter reads the class from the <pre> or its parent).
    for code in soup.select('pre > code[id^="mod_"]'):
        code.parent["class"] = code.parent.get("class", []) + ["language-sh"]


def preprocess(soup, output):
    _drop_hidden(soup)
    _tabs(soup)
    _admonitions(soup)
    _app_page_widgets(soup)
    autoclean(soup)
