
import unittest
import os
import sys
import io
from unittest.mock import patch

# Add the parent directory to the path to allow agent.py to be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from agent import main, load_config, generate_twitter_content, generate_linkedin_content, generate_instagram_content, generate_tiktok_content, generate_email_newsletter_content

class TestContentMultiplier(unittest.TestCase):

    def setUp(self):
        self.config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        self.config = load_config(self.config_path)
        self.test_content = "Our groundbreaking research reveals new insights into AI ethics and regulation."

    def test_load_config(self):
        self.assertIsNotNone(self.config)
        self.assertIn('brand_name', self.config)
        self.assertIn('platforms', self.config)

    def test_generate_twitter_content(self):
        content, image_prompt = generate_twitter_content(self.test_content, self.config)
        self.assertIsInstance(content, str)
        self.assertIsInstance(image_prompt, str)
        self.assertLessEqual(len(content), self.config['platforms']['twitter']['max_length'])
        self.assertIn('#YourBrand', content)
        self.assertIn('Twitter', image_prompt)

    def test_generate_linkedin_content(self):
        content, image_prompt = generate_linkedin_content(self.test_content, self.config)
        self.assertIsInstance(content, str)
        self.assertIsInstance(image_prompt, str)
        self.assertLessEqual(len(content), self.config['platforms']['linkedin']['max_length'])
        self.assertIn('#Professional', content)
        self.assertIn('LinkedIn', image_prompt)

    def test_generate_instagram_content(self):
        content, image_prompt = generate_instagram_content(self.test_content, self.config)
        self.assertIsInstance(content, str)
        self.assertIsInstance(image_prompt, str)
        self.assertLessEqual(len(content), self.config['platforms']['instagram']['max_length'])
        self.assertIn('#VisualStorytelling', content)
        self.assertIn('Instagram', image_prompt)

    def test_generate_tiktok_content(self):
        content, video_prompt = generate_tiktok_content(self.test_content, self.config)
        self.assertIsInstance(content, str)
        self.assertIsInstance(video_prompt, str)
        self.assertLessEqual(len(content.split()), self.config['platforms']['tiktok']['max_length'])
        self.assertIn('TikTok', content)
        self.assertIn('TikTok', video_prompt)

    def test_generate_email_newsletter_content(self):
        content, image_prompt = generate_email_newsletter_content(self.test_content, self.config)
        self.assertIsInstance(content, str)
        self.assertIsInstance(image_prompt, str)
        self.assertLessEqual(len(content.split()), self.config['platforms']['email_newsletter']['max_length'])
        self.assertIn('Subject:', content)
        self.assertIn('email newsletter', image_prompt)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_all_platforms(self, mock_stdout):
        with patch('sys.argv', ['agent.py', self.test_content, '--platforms', 'all']):
            main()
            output = mock_stdout.getvalue()
            self.assertIn('--- TWITTER ---', output)
            self.assertIn('--- LINKEDIN ---', output)
            self.assertIn('--- INSTAGRAM ---', output)
            self.assertIn('--- TIKTOK ---', output)
            self.assertIn('--- EMAIL_NEWSLETTER ---', output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_specific_platforms(self, mock_stdout):
        with patch('sys.argv', ['agent.py', self.test_content, '--platforms', 'twitter,linkedin']):
            main()
            output = mock_stdout.getvalue()
            self.assertIn('--- TWITTER ---', output)
            self.assertIn('--- LINKEDIN ---', output)
            self.assertNotIn('--- INSTAGRAM ---', output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_voice_override(self, mock_stdout):
        with patch('sys.argv', ['agent.py', self.test_content, '--platforms', 'twitter', '--voice', 'playful, youthful']):
            main()
            output = mock_stdout.getvalue()
            # Cannot directly assert on voice change in output without LLM integration
            # We just verify it runs without error and produces output.
            self.assertIn('--- TWITTER ---', output)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
