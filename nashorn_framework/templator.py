from jinja2 import Template
from os.path import join


def render(template_name, folder='templates', **kwargs):
    """
    definition for rendering of template
    :param template_name: str name of template
    :param folder: str name of folder
    :param kwargs: some other params
    :return:
    """
    file_path = join(folder, template_name)
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)
