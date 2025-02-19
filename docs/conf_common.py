import datetime

current_year = datetime.datetime.now().year

# General information about the project.
project = 'HeadTracker_ESP32'
copyright = u'2025 - {} NineDayCC'.format(current_year)
author = 'NineDayCC'
release = 'v0.1.1'

extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_togglebutton',
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

languages = {
    'zh_CN': '中文',
    'en': 'English'
}

html_theme = 'sphinx_book_theme'
html_static_path = ['../_static']

html_theme_options = {
    "repository_url": "https://github.com/NineDayCC/HeadTracker_ESP32",
    "use_source_button": True,
    "repository_branch": "master",
    "use_edit_page_button": True,
    "use_issues_button": True,
    "show_navbar_depth": 2,
    "show_toc_level": 3,
}