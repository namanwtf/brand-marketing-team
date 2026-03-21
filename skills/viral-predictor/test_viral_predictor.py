import unittest
import yaml
import os
from agent import ViralPredictor

class TestViralPredictor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = "test_config.yaml"
        test_config = {
            "prediction_models": {"instagram_reels": {"factors": ["hook_strength"]}},
            "scoring": {"threshold_high": 80}
        }
        with open(cls.config_path, 'w') as f:
            yaml.dump(test_config, f)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.config_path):
            os.remove(cls.config_path)

    def test_predict_virality(self):
        predictor = ViralPredictor(self.config_path)
        content = {"text": "Test content for Instagram", "media": "video.mp4"}
        result = predictor.predict_virality(content, "instagram_reels")
        self.assertIn("score", result)
        self.assertEqual(result["platform"], "instagram_reels")

    def test_rank_variants(self):
        predictor = ViralPredictor(self.config_path)
        variants = [
            {"id": "v1", "predicted_score": 75},
            {"id": "v2", "predicted_score": 90},
            {"id": "v3", "predicted_score": 60}
        ]
        ranked = predictor.rank_variants(variants)
        self.assertEqual(ranked[0]["id"], "v2")

    def test_optimize_timing(self):
        predictor = ViralPredictor(self.config_path)
        content = {"text": "Test"}
        result = predictor.optimize_timing(content, "tech_enthusiasts")
        self.assertIn("best_day", result)
        self.assertIn("best_time", result)

if __name__ == "__main__":
    unittest.main()
