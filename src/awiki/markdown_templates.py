from .config import AwikiConfig
from .err import AwikiError
import os
from jinja2 import Environment, FileSystemLoader


def get_md_template(self, template_name, awiki_config=None):
    awiki_config = awiki_config or AwikiConfig()
    templates_path = os.path.join(awiki_config.project_root, "markdown_templates")
    template_filename = f"{template_name}.template.md"
    template_path = os.path.join(templates_path, template_filename)
    if not os.path.exists(md_templ_filename):
        raise AwikiError(f"template not found: {md_templ_filename}")
    return Environment(loader=FileSystemLoader(templates_path)).get_template(
        template_filename
    )
