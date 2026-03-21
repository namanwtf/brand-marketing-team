import unittest
import yaml
import os
from agent import CompetitorContentMonitor

class TestCompetitorContentMonitor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = "test_config.yaml"
        test_config = {
            "competitors": {"rival_corp": {"monitoring_frequency": "hourly"}},
            "analysis": {"sentiment_analysis": True}
        }
        with open(cls.config_path, 'w') as f:
            yaml.dump(test_config, f)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.config_path):
            os.remove(cls.config_path)

    def test_track_publishing(self):
        monitor = CompetitorContentMonitor(self.config_path)
        result = monitor.track_publishing("rival_corp")
        self.assertEqual(result["status"], "success")

    def test_analyze_content_gap(self):
        monitor = CompetitorContentMonitor(self.config_path)
        gaps = monitor.analyze_content_gap(["topic_a"], ["topic_a", "topic_b"])
        self.assertIn("gaps", gaps)

    def test_send_alert(self):
        monitor = CompetitorContentMonitor(self.config_path)
        result = monitor.send_alert("New competitor post")
        self.assertEqual(result["status"], "sent")

if __name__ == "__main__":
    unittest.main()
