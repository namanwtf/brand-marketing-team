import unittest
import yaml
import os
from agent import PricingPsychology

class TestPricingPsychology(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config_path = "test_config.yaml"
        test_config = {
            "pricing_strategies": {"decoy_effect": {"enabled": True}, "anchoring": {"reference_price_ratio": 1.3}}
        }
        with open(cls.config_path, 'w') as f:
            yaml.dump(test_config, f)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.config_path):
            os.remove(cls.config_path)

    def test_apply_decoy_effect(self):
        pricing = PricingPsychology(self.config_path)
        result = pricing.apply_decoy_effect([29, 79, 99], 1)
        self.assertEqual(result["strategy"], "decoy")
        self.assertEqual(result["highlighted"], 1)

    def test_apply_anchoring(self):
        pricing = PricingPsychology(self.config_path)
        result = pricing.apply_anchoring(79, 1.3)
        self.assertEqual(result["target_price"], 79)
        self.assertEqual(result["anchor_price"], 102.7)

    def test_apply_charm_pricing(self):
        pricing = PricingPsychology(self.config_path)
        result = pricing.apply_charm_pricing(50)
        self.assertEqual(result["original"], 50)
        self.assertEqual(result["charm"], 49.99)

if __name__ == "__main__":
    unittest.main()
