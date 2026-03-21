import os
import yaml
from openclaw.agents import Skill

class PricingPsychology(Skill):
    def __init__(self, config_path="config.yaml"):
        super().__init__()
        self.config = self._load_config(config_path)

    def _load_config(self, config_path):
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        return {}

    def apply_decoy_effect(self, prices, target_index=1):
        self.log_info("Applying decoy effect pricing strategy")
        return {"strategy": "decoy", "recommended_order": prices, "highlighted": target_index}

    def apply_anchoring(self, target_price, anchor_ratio=1.3):
        anchor = round(target_price * anchor_ratio, 2)
        self.log_info(f"Anchoring with reference price: {anchor}")
        return {"anchor_price": anchor, "target_price": target_price}

    def apply_charm_pricing(self, price):
        charm = round(price - 0.01, 2)
        self.log_info(f"Charm pricing: {price} -> {charm}")
        return {"original": price, "charm": charm}

if __name__ == "__main__":
    pricing = PricingPsychology()
