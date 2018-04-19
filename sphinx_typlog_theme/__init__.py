import os
__version__ = '0.4.dev'


def get_path():
    """Shortcut for users whose theme is next to their conf.py."""
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def add_badge_roles(app):
    from docutils.nodes import inline, make_id
    from docutils.parsers.rst.roles import set_classes

    def create_badge_role(color=None):
        def badge_role(name, rawtext, text, lineno, inliner,
                       options=None, content=None):
            options = options or {}
            set_classes(options)
            classes = ['badge']
            if color is None:
                classes.append('badge-' + make_id(text))
            else:
                classes.append('badge-' + color)
            if len(text) == 1:
                classes.append('badge-one')
            options['classes'] = classes
            node = inline(rawtext, text, **options)
            return [node], []
        return badge_role

    app.add_role('badge', create_badge_role())
    app.add_role('badge-red', create_badge_role('red'))
    app.add_role('badge-blue', create_badge_role('blue'))
    app.add_role('badge-green', create_badge_role('green'))
    app.add_role('badge-yellow', create_badge_role('yellow'))


def setup(app):
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, 'add_html_theme'):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme('sphinx_typlog_theme', theme_path)

    return {'version': __version__, 'parallel_read_safe': True}
