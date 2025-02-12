# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

author = 'NineDayCC'
release = 'v0.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser'  # 启用 Markdown 支持
]

# 配置可用语言
languages = {
    'zh_CN': '中文',
    'en': 'English'
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    'display_github': True,
    'github_user': 'NineDayCC',
    'github_repo': 'ReadTheDocs_Test',
    'github_version': 'main',
    # 'conf_py_path': '/docs/source/',
}