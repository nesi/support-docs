![Build Status](https://gitlab.com/pages/mkdocs/badges/master/build.svg)

---

Example [MkDocs] website using GitLab Pages.

Learn more about GitLab Pages at https://pages.gitlab.io and the official
documentation https://docs.gitlab.com/ce/user/project/pages/.

---

## GitLab CI

This project's static Pages are built by [GitLab CI][ci], following the steps
defined in [`.gitlab-ci.yml`](.gitlab-ci.yml):

```
image: python:3.8-buster

before_script:
  - pip install -r requirements.txt

test:
  stage: test
  script:
  - mkdocs build --strict --verbose --site-dir test
  artifacts:
    paths:
    - test
  except:
  - master

pages:
  stage: deploy
  script:
  - mkdocs build --strict --verbose
  artifacts:
    paths:
    - public
  only:
  - master
```

## Building locally

To work locally with this project, you'll have to follow the steps below:

1. Fork, clone or download this project
1. [Install][] MkDocs
1. Preview your project: `mkdocs serve`,
   your site can be accessed under `localhost:8000`
1. Add content
1. Generate the website: `mkdocs build` (optional)

Read more at MkDocs [documentation][].

## GitLab User or Group Pages

To use this project as your user/group website, you will need one additional
step: just rename your project to `namespace.gitlab.io`, where `namespace` is
your `username` or `groupname`. This can be done by navigating to your
project's **Settings**.

You'll need to configure your site too: change this line
in your `mkdocs.yml`, from `"https://pages.gitlab.io/mkdocs/"` to
`site_url = "https://namespace.gitlab.io"`.

Read more about [user/group Pages][userpages] and [project Pages][projpages].

## Did you fork this project?

If you forked this project for your own use, please go to your project's
**Settings** and remove the forking relationship, which won't be necessary
unless you want to contribute back to the upstream project.

## Troubleshooting

1. CSS is missing! That means two things:

    Either that you have wrongly set up the CSS URL in your templates, or
    your static generator has a configuration option that needs to be explicitly
    set in order to serve static assets under a relative URL.

[ci]: https://about.gitlab.com/gitlab-ci/
[mkdocs]: http://www.mkdocs.org
[install]: http://www.mkdocs.org/#installation
[documentation]: http://www.mkdocs.org
[userpages]: https://docs.gitlab.com/ce/user/project/pages/introduction.html#user-or-group-pages
[projpages]: https://docs.gitlab.com/ce/user/project/pages/introduction.html#project-pages

---

Forked from https://gitlab.com/morph027/mkdocs
