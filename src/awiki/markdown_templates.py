from .config import AwikiConfig
from .err import AwikiError
import os
from jinja2 import Environment, FileSystemLoader


def get_md_template(template_name, awiki_config=None):
    awiki_config = awiki_config or AwikiConfig()
    templates_dir = os.path.join(awiki_config.project_root, awiki_config.awiki_dir, "markdown_templates")
    template_filename = f"{template_name}.template.md"
    template_path = os.path.join(templates_dir, template_filename)
    if not os.path.exists(template_path):
        raise AwikiError(f"template not found: {template_path}")
    return Environment(loader=FileSystemLoader(templates_dir)).get_template(
        template_filename
    )
