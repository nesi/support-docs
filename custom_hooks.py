import linkcheckmd as lc


def test(*args, **kwargs):
    print("running link checker")
    lc.check_links("docs", ext=".md", recurse=True, use_async=True)
