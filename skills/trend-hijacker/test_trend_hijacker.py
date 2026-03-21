import unittest
import yaml
import os
from agent import TrendHijacker

class TestTrendHijacker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = "test_config.yaml"
        test_config = {
            "trend_sources": ["twitter", "reddit"],
            "monitoring": {"scan_interval_minutes": 30, "min_velocity_threshold": 100},
            "filters": {"excluded_keywords": ["controversial"], "required_sentiment": "positive"}
        }
        with open(cls.config_path, 'w') as f:
            yaml.dump(test_config, f)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.config_path):
            os.remove(cls.config_path)

    def test_detect_trends(self):
        hijacker = TrendHijacker(self.config_path)
        trends = hijacker.detect_trends()
        self.assertIsInstance(trends, list)

    def test_generate_content_angles(self):
        hijacker = TrendHijacker(self.config_path)
        trend = {"topic": "AI_Photography", "velocity": 200, "sentiment": "positive"}
        angles = hijacker.generate_content_angles(trend, "tech_enthusiasts")
        self.assertIsInstance(angles, list)

    def test_filter_by_sentiment(self):
        hijacker = TrendHijacker(self.config_path)
        trends = [
            {"topic": "Good Trend", "velocity": 150, "sentiment": "positive"},
            {"topic": "Bad Trend", "velocity": 150, "sentiment": "negative"}
        ]
        filtered = hijacker._filter_by_sentiment(trends)
        self.assertEqual(len(filtered), 1)

    def test_calculate_velocity_score(self):
        hijacker = TrendHijacker(self.config_path)
        trend_data = {"current_mentions": 1000, "previous_mentions": 200, "time_window_hours": 1}
        velocity = hijacker._calculate_velocity(trend_data)
        self.assertEqual(velocity, 400)

if __name__ == "__main__":
    unittest.main()
