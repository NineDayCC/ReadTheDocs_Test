try:
    from conf_common import *
except ImportError:
    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))
    from conf_common import *

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_context = {
    'display_github': True,
    'github_user': 'NineDayCC',
    'github_repo': 'ReadTheDocs_Test',
    'github_version': 'main',
    'conf_py_path': '/docs/en/'
}

html_theme_options = {
    "path_to_docs": "/docs/zh_CN",
}