
import yaml
import argparse
import os

# --- Configuration Loading ---
def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

# --- Content Generation Logic ---
def generate_twitter_content(content, config, brand_voice_override=None):
    brand_name = config['brand_name']
    brand_voice = brand_voice_override or config['brand_voice']
    platform_config = config['platforms']['twitter']
    tone_modifier = platform_config['tone_modifier']
    hashtags = " ".join(platform_config['hashtags'])

    # Simple AI-like generation simulation
    prompt = f"As a {brand_voice}, {tone_modifier} expert for {brand_name}, rephrase this for Twitter/X (max {platform_config['max_length']} chars, include hashtags): '{content}'. Include these hashtags: {hashtags}"
    # In a real scenario, this would call an LLM API
    generated_text = f"📢 {content}. Get ready to connect! {hashtags}"
    if len(generated_text) > platform_config['max_length']:
        generated_text = generated_text[:platform_config['max_length'] - len("... " + hashtags)] + "... " + hashtags

    image_prompt = f"A visually striking image representing '{content}', suitable for Twitter, clean and modern design."
    return generated_text, image_prompt

def generate_linkedin_content(content, config, brand_voice_override=None):
    brand_name = config['brand_name']
    brand_voice = brand_voice_override or config['brand_voice']
    platform_config = config['platforms']['linkedin']
    tone_modifier = platform_config['tone_modifier']
    hashtags = " ".join(platform_config['hashtags'])

    prompt = f"As a {brand_voice}, {tone_modifier} expert for {brand_name}, write a professional LinkedIn post about: '{content}'. (max {platform_config['max_length']} chars, include hashtags):. Include these hashtags: {hashtags}"
    generated_text = f"💡 Insights from {brand_name}: {content}. This development is poised to make a significant impact. Connect with us for more details! {hashtags}"
    if len(generated_text) > platform_config['max_length']:
        generated_text = generated_text[:platform_config['max_length'] - len("... " + hashtags)] + "... " + hashtags
        
    image_prompt = f"Professional, corporate image for LinkedIn post about '{content}'. Focus on innovation and impact."
    return generated_text, image_prompt

def generate_instagram_content(content, config, brand_voice_override=None):
    brand_name = config['brand_name']
    brand_voice = brand_voice_override or config['brand_voice']
    platform_config = config['platforms']['instagram']
    tone_modifier = platform_config['tone_modifier']
    hashtags = " ".join(platform_config['hashtags'])

    prompt = f"As a {brand_voice}, {tone_modifier} expert for {brand_name}, write an engaging Instagram caption about: '{content}'. (max {platform_config['max_length']} chars, include relevant emojis):. Include these hashtags: {hashtags}"
    generated_text = f"✨ So excited about this! {content}. We're bringing you something truly special. Tap the link in bio to learn more! #YourBrand #Innovation {hashtags}"
    if len(generated_text) > platform_config['max_length']:
        generated_text = generated_text[:platform_config['max_length'] - len("... " + hashtags)] + "... " + hashtags

    image_prompt = f"Creative, high-quality image for Instagram, visually representing '{content}'. Emphasize aesthetics and brand lifestyle."
    return generated_text, image_prompt

def generate_tiktok_content(content, config, brand_voice_override=None):
    brand_name = config['brand_name']
    brand_voice = brand_voice_override or config['brand_voice']
    platform_config = config['platforms']['tiktok']
    tone_modifier = platform_config['tone_modifier']

    prompt = f"As a {brand_voice}, {tone_modifier} expert for {brand_name}, create a short, engaging TikTok video script idea about: '{content}'. Focus on trends and dynamic visuals. (approx. {platform_config['max_length']} words)"
    generated_text = f"🎬 TikTok Idea: Quick cut video showcasing '{content}' with a popular sound. Text overlay: 'Mind Blown! 🤯'. Caption: 'You won't believe this!' #YourBrand #Trends"
    # Word count approximation
    if len(generated_text.split()) > platform_config['max_length']:
        generated_text = " ".join(generated_text.split()[:platform_config['max_length']-5]) + "..."


    video_prompt = f"Short, dynamic video for TikTok showcasing '{content}'. Focus on fast cuts, trending audio, and clear text overlays highlighting key aspects. Use bright, engaging colors and energetic transitions. Suitable for a young, tech-savvy audience."
    return generated_text, video_prompt

def generate_email_newsletter_content(content, config, brand_voice_override=None):
    brand_name = config['brand_name']
    brand_voice = brand_voice_override or config['brand_voice']
    platform_config = config['platforms']['email_newsletter']
    tone_modifier = platform_config['tone_modifier']

    prompt = f"As a {brand_voice}, {tone_modifier} expert for {brand_name}, write an engaging email newsletter section based on: '{content}'. (approx. {platform_config['max_length']} words)"
    generated_text = f"Subject: Exciting News from {brand_name}!

Dear Subscriber,

We're thrilled to share {content}. Our team has been working hard to bring you the latest. Read more on our blog.

Best,
The {brand_name} Team"
    # Word count approximation
    if len(generated_text.split()) > platform_config['max_length']:
        generated_text = " ".join(generated_text.split()[:platform_config['max_length']-5]) + "..."


    image_prompt = f"Hero image for an email newsletter about '{content}'. Professional, inviting, and representative of the main topic. Could be an abstract concept or a product shot."
    return generated_text, image_prompt

# --- Main Execution ---
def main():
    parser = argparse.ArgumentParser(description="Generate multi-platform content variations.")
    parser.add_argument("content", help="The core content to adapt.")
    parser.add_argument("--platforms", default="all", help="Comma-separated list of platforms to generate content for (e.g., twitter,linkedin). Default is 'all'.")
    parser.add_argument("--voice", help="Override the brand voice defined in config.yaml for this run.")

    args = parser.parse_args()

    # Load configuration
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir, 'config.yaml')
    config = load_config(config_path)

    # Determine target platforms
    target_platforms = args.platforms.lower().split(',') if args.platforms != 'all' else config['platforms'].keys()

    platform_generators = {
        'twitter': generate_twitter_content,
        'linkedin': generate_linkedin_content,
        'instagram': generate_instagram_content,
        'tiktok': generate_tiktok_content,
        'email_newsletter': generate_email_newsletter_content,
    }

    results = {}
    for platform in target_platforms:
        if platform in platform_generators:
            generated_content, media_prompt = platform_generators[platform](args.content, config, args.voice)
            results[platform] = {
                'content': generated_content,
                'media_prompt': media_prompt
            }
        else:
            print(f"Warning: Platform '{platform}' not supported.")

    # Output results
    for platform, data in results.items():
        print(f"--- {platform.upper()} ---
")
        print(f"Content:
{data['content']}
")
        print(f"Media Prompt:
{data['media_prompt']}
")
        print("-" * 30 + "\n")

if __name__ == "__main__":
    main()
