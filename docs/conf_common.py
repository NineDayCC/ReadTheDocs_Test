import datetime

current_year = datetime.datetime.now().year

# General information about the project.
project = 'HeadTracker_ESP32'
copyright = u'2025 - {} NineDayCC'.format(current_year)
author = 'NineDayCC'
release = 'v0.1.1'

extensions = [
    'myst_parser'  # 启用 Markdown 支持
]

languages = {
    'zh_CN': '中文',
    'en': 'English'
}

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    "repository_url": "https://github.com/NineDayCC/HeadTracker_ESP32",
    "use_source_button": True,
    "repository_branch": "master",
    "use_edit_page_button": True,
    "use_issues_button": True,
}