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
