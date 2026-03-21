import unittest
import os
import yaml
from agent import CampaignOrchestrator

class TestCampaignOrchestrator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = "test_config.yaml"
        test_config = {
            "campaigns": [
                {
                    "id": "test_campaign_1",
                    "name": "Test Campaign",
                    "duration_weeks": 2,
                    "channels": {
                        "instagram": {"budget_allocation": 0.5, "targets": ["test_users"]}
                    },
                    "objectives": [{"metric": "engagement", "target": 1000, "period": "weekly"}]
                }
            ]
        }
        with open(cls.config_path, 'w') as f:
            yaml.dump(test_config, f)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.config_path):
            os.remove(cls.config_path)

    def test_orchestrate_existing_campaign(self):
        orchestrator = CampaignOrchestrator(self.config_path)
        result = orchestrator.orchestrate_campaign("test_campaign_1")
        self.assertEqual(result["status"], "success")
        self.assertIn("Test Campaign", result["message"])

    def test_orchestrate_nonexistent_campaign(self):
        orchestrator = CampaignOrchestrator(self.config_path)
        result = orchestrator.orchestrate_campaign("invalid_campaign")
        self.assertEqual(result["status"], "failed")
        self.assertIn("not found", result["message"])

    def test_monitor_campaign(self):
        orchestrator = CampaignOrchestrator(self.config_path)
        result = orchestrator.monitor_campaign("test_campaign_1")
        self.assertEqual(result["status"], "success")
        self.assertIn("metrics", result)

    def test_adjust_campaign(self):
        orchestrator = CampaignOrchestrator(self.config_path)
        result = orchestrator.adjust_campaign("test_campaign_1", {"budget_increase": 0.1})
        self.assertEqual(result["status"], "success")

if __name__ == "__main__":
    unittest.main()
