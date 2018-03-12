import os
__version__ = '0.3.2'


def get_path():
    """Shortcut for users whose theme is next to their conf.py."""
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def setup(app):
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, 'add_html_theme'):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme('sphinx_typlog_theme', theme_path)
    return {'version': __version__, 'parallel_read_safe': True}
