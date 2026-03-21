import json

def generate_ad_creative(product_name, key_features, target_audience, platform, tone, num_variants):
    """Generates a full ad creative set with headlines, body copy, CTAs, and visual concept prompts.

    Args:
        product_name (str): The name of the product (e.g., "Tecno Pova 6 Pro 5G").
        key_features (list): List of key features (e.g., ["108MP Camera", "6000mAh Battery"]).
        target_audience (str): Description of the target audience.
        platform (str): Target ad platform (e.g., "Facebook, Instagram").
        tone (str): The desired tone (e.g., "Excited, powerful").
        num_variants (int): Number of creative variants to generate.

    Returns:
        list: A list of dictionaries, each representing an ad creative variant.
    """
    print(f"Generating {num_variants} ad creative variants for {product_name} on {platform}...")
    # Placeholder for actual AI generation logic
    variants = []
    for i in range(num_variants):
        variants.append({
            "platform": platform,
            "headline": f"[AI Gen] Headline Variant {i+1} for {product_name}",
            "primary_text": f"[AI Gen] Body copy variant {i+1} focusing on {' and '.join(key_features)} for {target_audience}.",
            "cta": f"[AI Gen] CTA Variant {i+1}",
            "visual_concept_prompt": f"[AI Gen] Visual prompt variant {i+1} for {product_name} with {tone} tone."
        })
    return json.dumps(variants, indent=2)

def generate_headlines(product_name, key_features, tone, num_headlines):
    """Focuses specifically on generating multiple headlines.

    Args:
        product_name (str): The name of the product.
        key_features (list): List of key features.
        tone (str): The desired tone.
        num_headlines (int): Number of headlines to generate.

    Returns:
        list: A list of generated headlines.
    """
    print(f"Generating {num_headlines} headlines for {product_name} with {tone} tone...")
    headlines = [f"[AI Gen] Headline {i+1} for {product_name} ({', '.join(key_features)})" for i in range(num_headlines)]
    return json.dumps(headlines, indent=2)

def generate_ctas(product_name, tone, num_ctas):
    """Generates multiple call-to-action options.

    Args:
        product_name (str): The name of the product.
        tone (str): The desired tone.
        num_ctas (int): Number of CTAs to generate.

    Returns:
        list: A list of generated CTAs.
    """
    print(f"Generating {num_ctas} CTAs for {product_name} with {tone} tone...")
    ctas = [f"[AI Gen] CTA {i+1} - {product_name}" for i in range(num_ctas)]
    return json.dumps(ctas, indent=2)

def generate_visual_prompts(product_name, key_features, tone, num_prompts):
    """Creates prompts for visual assets.

    Args:
        product_name (str): The name of the product.
        key_features (list): List of key features.
        tone (str): The desired tone.
        num_prompts (int): Number of visual prompts to generate.

    Returns:
        list: A list of generated visual prompts.
    """
    print(f"Generating {num_prompts} visual prompts for {product_name} with {tone} tone...")
    prompts = [f"[AI Gen] Visual prompt {i+1}: {product_name}, highlighting {', '.join(key_features)} with a {tone} aesthetic." for i in range(num_prompts)]
    return json.dumps(prompts, indent=2)
