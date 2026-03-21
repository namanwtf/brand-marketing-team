import unittest
import yaml
import os
from agent import LeadMagnetCreator

class TestLeadMagnetCreator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = "test_config.yaml"
        test_config = {
            "lead_magnet_types": {"ebook": {"min_pages": 20, "max_pages": 100}},
            "branding": {"primary_color": "#1E90FF"}
        }
        with open(cls.config_path, 'w') as f:
            yaml.dump(test_config, f)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.config_path):
            os.remove(cls.config_path)

    def test_create_ebook(self):
        creator = LeadMagnetCreator(self.config_path)
        result = creator.create_ebook("Test Guide", ["topic1", "topic2"], 30)
        self.assertEqual(result["status"], "generated")
        self.assertEqual(result["asset_type"], "ebook")

    def test_create_template(self):
        creator = LeadMagnetCreator(self.config_path)
        result = creator.create_template("checklist", ["item1", "item2"])
        self.assertIn("template", result["asset_type"])

    def test_create_calculator(self):
        creator = LeadMagnetCreator(self.config_path)
        result = creator.create_calculator(["input1"], ["output1"])
        self.assertEqual(result["asset_type"], "calculator")

if __name__ == "__main__":
    unittest.main()
