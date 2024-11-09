from .err import AwikiError
from .config import AwikiConfig
import os
import markdown
import yaml


class Page:
    """
    DOESN'T STORE PAGE INFORMATION
    """

    def __init__(self, page_name, config=None):
        self.cfg = config or AwikiConfig()
        self.page_name = page_name
        self.root = os.path.join(
            self.cfg.project_root, self.cfg.pages_dir, self.page_name
        )
        self.md_path = os.path.join(self.root, "page.md")
        self.exists = os.path.exists(self.md_path)

    def load(self):
        """
        Loads page.md.
        returns metadata and page content
        """
        if not self.exists:
            raise AwikiError(f"can't read {page_name}: no such page")
        # metadata up to ---
        meta_lines = []
        md = ""
        with open(self.md_path) as f:
            for line in f:
                if line.strip() == "---":
                    break
                meta_lines.append(line)
            md = f.read()
        meta = yaml.safe_load("".join(meta_lines))
        html = markdown.markdown(md)
        return meta, html, md

    def save(self, meta, md):
        """
        Writes metadata and page content to page.md
        """
        meta_yaml = yaml.dump(meta)
        with open(self.md_path, "w") as f:
            f.write(meta_yaml)
            f.write("---\n")
            f.write(md)
