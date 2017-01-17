# Example [MkDocs](http://mkdocs.org/) website using GitLab Pages.

Learn more about GitLab Pages at https://pages.gitlab.io and the official
documentation http://doc.gitlab.com/ee/pages/README.html.

## GitLab CI

This project's static Pages are built by [GitLab CI][ci], following the steps
defined in [`.gitlab-ci.yml`](.gitlab-ci.yml):

```
image: python:alpine

before_script:
  - pip install mkdocs
  # add your custom theme (https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes) if not inside a theme_dir
  # - pip install mkdocs-material

pages:
  script:
  - mkdocs build
  - mv site public
  artifacts:
    paths:
    - public
  only:
  - master
```

## Building locally

To work locally with this project, you'll have to follow the steps below:

1. Fork, clone or download this project
1. [Install](http://www.mkdocs.org/#installation) MkDocs
1. Preview your project: `mkdocs serve`
1. Add content
1. Generate the website: `mkdocs build` (optional)

Read more at MkDocs's [documentation](http://www.mkdocs.org/).

### Preview your site

If you clone or download this project to your local computer and run `mkdocs serve`,
your site can be accessed under `localhost:8000`.

## GitLab User or Group Pages

To use this project as your user/group website, you will need one additional
step: just rename your project to `namespace.gitlab.io`, where `namespace` is
your `username` or `groupname`. This can be done by navigating to your
project's **Settings**.

You'll need to configure your site too: change this line
in your `mkdocs.yml`, from `"https://pages.gitlab.io/hugo/"` to `site_url = "https://namespace.gitlab.io"`.

Read more about [user/group Pages][userpages] and [project Pages][projpages].