import os
import yaml
from openclaw.agents import Skill

class LeadMagnetCreator(Skill):
    def __init__(self, config_path="config.yaml"):
        super().__init__()
        self.config = self._load_config(config_path)

    def _load_config(self, config_path):
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        return {}

    def create_ebook(self, title, topics, num_pages=30):
        self.log_info(f"Creating ebook: {title}")
        return {"asset_type": "ebook", "title": title, "pages": num_pages, "status": "generated"}

    def create_template(self, template_type, content):
        self.log_info(f"Creating template: {template_type}")
        return {"asset_type": f"{template_type}_template", "status": "generated"}

    def create_calculator(self, inputs, outputs):
        self.log_info("Creating interactive calculator")
        return {"asset_type": "calculator", "inputs": inputs, "outputs": outputs, "status": "generated"}

if __name__ == "__main__":
    creator = LeadMagnetCreator()
