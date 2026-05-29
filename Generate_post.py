#!/usr/bin/env python3
"""
Social Media Post Generator

Generates optimized social media posts for Twitter/X, LinkedIn, Instagram, and Telegram
from a given topic or announcement.

Usage:
    python generate_posts.py --topic "Your topic here" --platform twitter
    python generate_posts.py --topic "Your topic here" --platform linkedin
    python generate_posts.py --topic "Your topic here" --platform instagram
    python generate_posts.py --topic "Your topic here" --platform telegram
"""

import argparse
import json
import random
from typing import Dict, List, Optional


# Platform configurations
PLATFORM_CONFIG = {
    "twitter": {
        "name": "Twitter/X",
        "max_chars": 280,
        "optimal_chars": 260,
        "tone": "concise, punchy, conversational, engaging",
        "emoji_style": "moderate",
        "hashtag_count": (1, 3),
        "line_breaks": 2,
        "cta_style": "question or invitation",
    },
    "linkedin": {
        "name": "LinkedIn",
        "max_chars": 3000,
        "optimal_chars": 300,
        "tone": "professional, informative, thought-leadership",
        "emoji_style": "professional, minimal",
        "hashtag_count": (3, 5),
        "line_breaks": 3,
        "cta_style": "discussion invitation",
    },
    "instagram": {
        "name": "Instagram",
        "max_chars": 2200,
        "optimal_chars": 150,
        "tone": "visual, authentic, inspiring, community-focused",
        "emoji_style": "expressive, frequent",
        "hashtag_count": (5, 15),
        "line_breaks": 2,
        "cta_style": "engagement question",
    },
    "telegram": {
        "name": "Telegram",
        "max_chars": 4096,
        "optimal_chars": 400,
        "tone": "direct, informative, community-oriented",
        "emoji_style": "informative, moderate",
        "hashtag_count": (2, 4),
        "line_breaks": 3,
        "cta_style": "information or link",
    },
}

# Hashtag templates by topic category
HASHTAG_TEMPLATES = {
    "technology": ["#Tech", "#Innovation", "#Technology", "#DigitalTransformation", "#FutureTech"],
    "business": ["#Business", "#Entrepreneurship", "#Startup", "#Growth", "#Leadership"],
    "product": ["#ProductLaunch", "#NewFeature", "#ProductUpdate", "#Innovation", "#Tech"],
    "team": ["#TeamCulture", "#CompanyLife", "#TeamWork", "#Office", "#Culture"],
    "announcement": ["#News", "#Announcement", "#Update", "#Breaking", "#Important"],
    "milestone": ["#Milestone", "#Achievement", "#Success", "#Celebration", "#Growth"],
    "tips": ["#Tips", "#Advice", "#HowTo", "#Learning", "#Education"],
    "community": ["#Community", "#Together", "#Support", "#Team", "#Together"],
    "general": ["#Update", "#News", "#Info", "#Share", "#Post"],
}

# Hook templates for different platforms
HOOK_TEMPLATES = {
    "twitter": [
        "🚀",
        "🎉",
        "📢",
        "🔥",
        "💡",
        "⚡️",
        "🌟",
        "Here's the thing:",
        "Quick update:",
        "Big news:",
    ],
    "linkedin": [
        "🎉 Milestone Alert:",
        "🚀 Exciting news!",
        "💼 Professional update:",
        "📈 Growth moment:",
        "✨ Proud to share:",
        "Let me tell you about:",
        "Important announcement:",
    ],
    "instagram": [
        "✨",
        "🌟",
        "💫",
        "📸",
        "Behind the scenes:",
        "Our vibe:",
        "Moment of:",
    ],
    "telegram": [
        "📢 Important Update:",
        "🔔 Announcement:",
        "📌 Note:",
        "🔧 Update:",
        "💡 Info:",
        "Important:",
    ],
}

# CTA templates
CTA_TEMPLATES = {
    "twitter": [
        "What do you think?",
        "Retweet if you agree! 🔄",
        "Drop a 💯 if this resonates",
        "Tag someone who needs this",
        "Let's discuss 👇",
    ],
    "linkedin": [
        "What are your thoughts on this?",
        "How does this compare to your experience?",
        "Share your perspective in the comments 👇",
        "What challenges have you faced?",
        "Let's start a conversation about this.",
    ],
    "instagram": [
        "Double tap if you relate! 💙",
        "Save this for later! 💾",
        "Tag a friend who needs to see this! 👥",
        "What's your take? Comment below! 👇",
        "Share your experience in the comments! 💬",
    ],
    "telegram": [
        "Share this with your network!",
        "Questions? Drop them below! 👇",
        "Forward to someone who'd benefit!",
        "Stay tuned for more updates!",
        "Join our community for more!",
    ],
}


def extract_keywords(topic: str) -> List[str]:
    """Extract potential keywords from the topic."""
    # Simple keyword extraction
    words = topic.lower().split()
    stop_words = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by"}
    keywords = [w.strip(".,!?;:") for w in words if w.lower() not in stop_words and len(w) > 3]
    return list(set(keywords))[:5]


def categorize_topic(topic: str) -> str:
    """Categorize the topic to suggest relevant hashtags."""
    topic_lower = topic.lower()
    
    if any(word in topic_lower for word in ["launch", "release", "feature", "update", "new"]):
        return "product"
    elif any(word in topic_lower for word in ["team", "office", "culture", "hiring", "people"]):
        return "team"
    elif any(word in topic_lower for word in ["milestone", "anniversary", "celebration", "achievement"]):
        return "milestone"
    elif any(word in topic_lower for word in ["tip", "advice", "how to", "guide", "tutorial"]):
        return "tips"
    elif any(word in topic_lower for word in ["community", "support", "help", "together"]):
        return "community"
    elif any(word in topic_lower for word in ["tech", "ai", "software", "app", "digital"]):
        return "technology"
    elif any(word in topic_lower for word in ["business", "company", "startup", "growth", "revenue"]):
        return "business"
    else:
        return "announcement"


def generate_hashtags(topic: str, platform: str, count: Optional[int] = None) -> List[str]:
    """Generate relevant hashtags based on topic and platform."""
    category = categorize_topic(topic)
    base_hashtags = HASHTAG_TEMPLATES.get(category, HASHTAG_TEMPLATES["general"])
    
    # Extract keywords for custom hashtags
    keywords = extract_keywords(topic)
    custom_hashtags = [f"#{word.capitalize()}" for word in keywords[:3]]
    
    # Combine and deduplicate
    all_hashtags = list(set(base_hashtags + custom_hashtags))
    random.shuffle(all_hashtags)
    
    # Get platform-specific count
    if count is None:
        min_count, max_count = PLATFORM_CONFIG[platform]["hashtag_count"]
        count = random.randint(min_count, max_count)
    
    return all_hashtags[:count]


def generate_content(topic: str, platform: str) -> str:
    """Generate the main post content based on topic and platform."""
    config = PLATFORM_CONFIG[platform]
    
    # Select appropriate hook
    hook = random.choice(HOOK_TEMPLATES[platform])
    
    # Build content based on platform style
    if platform == "twitter":
        # Short, punchy Twitter style
        lines = [
            f"{hook} {topic[:100]}",
            "",
            random.choice(CTA_TEMPLATES["twitter"]),
        ]
        content = "\n".join(lines)
        
    elif platform == "linkedin":
        # Professional LinkedIn style
        lines = [
            f"{hook}",
            "",
            f"{topic[:200]}",
            "",
            "This is a significant step forward that we're excited to share with our network.",
            "",
            random.choice(CTA_TEMPLATES["linkedin"]),
        ]
        content = "\n".join(lines)
        
    elif platform == "instagram":
        # Visual Instagram style
        emojis = ["✨", "🌟", "💫", "🎨", "📸", "💪", "🔥"]
        selected_emojis = random.sample(emojis, 3)
        
        lines = [
            f"{topic[:150]}",
            "",
            f"{random.choice(selected_emojis)} {random.choice(selected_emojis)}",
            "",
            random.choice(CTA_TEMPLATES["instagram"]),
        ]
        content = "\n".join(lines)
        
    else:  # telegram
        # Informative Telegram style
        lines = [
            f"{hook}",
            "",
            f"{topic[:300]}",
            "",
            "We'll keep you updated with more details.",
            "",
            random.choice(CTA_TEMPLATES["telegram"]),
        ]
        content = "\n".join(lines)
    
    # Trim to optimal length
    optimal = config["optimal_chars"]
    if len(content) > optimal:
        # Try to break at a sentence boundary
        sentences = content.split(". ")
        truncated = sentences[0]
        for sent in sentences[1:]:
            if len(truncated) + len(sent) + 2 <= optimal:
                truncated += ". " + sent
            else:
                break
        content = truncated + "."
    
    return content.strip()


def generate_media_suggestions(platform: str, topic: str) -> List[str]:
    """Generate media suggestions based on platform and topic."""
    topic_lower = topic.lower()
    
    if platform == "twitter":
        suggestions = ["image", "gif", "thread", "poll"]
    elif platform == "linkedin":
        suggestions = ["infographic", "team photo", "product screenshot", "chart/graph"]
    elif platform == "instagram":
        suggestions = ["photo", "carousel", "reel", "story"]
    else:  # telegram
        suggestions = ["screenshot", "link preview", "document", "image"]
    
    # Add topic-specific suggestions
    if "launch" in topic_lower or "release" in topic_lower:
        suggestions.insert(0, "product demo")
    elif "team" in topic_lower or "culture" in topic_lower:
        suggestions.insert(0, "team photo")
    elif "tips" in topic_lower or "advice" in topic_lower:
        suggestions.insert(0, "infographic")
    
    return suggestions[:3]


def generate_engagement_hooks(platform: str) -> List[str]:
    """Generate engagement suggestions for the post."""
    hooks = {
        "twitter": [
            "Use a trending hashtag",
            "Post during peak hours (9-11 AM or 1-3 PM)",
            "Include a question to drive replies",
            "Tag relevant accounts",
        ],
        "linkedin": [
            "Tag industry leaders",
            "Post mid-week (Tue-Thu) for max reach",
            "Include a poll for engagement",
            "Respond to all comments within 2 hours",
        ],
        "instagram": [
            "Use all 30 hashtags for reach",
            "Post during evening hours",
            "Add to relevant story highlights",
            "Engage with similar accounts",
        ],
        "telegram": [
            "Pin the message",
            "Share in relevant groups",
            "Add a poll for interaction",
            "Schedule for optimal timezone",
        ],
    }
    return random.sample(hooks[platform], 2)


def generate_post(topic: str, platform: str) -> Dict:
    """
    Generate a complete social media post.
    
    Args:
        topic: The subject or announcement to convert
        platform: One of: twitter, linkedin, instagram, telegram
    
    Returns:
        Dictionary containing the post and metadata
    """
    # Validate platform
    if platform not in PLATFORM_CONFIG:
        raise ValueError(f"Invalid platform: {platform}. Choose from: {', '.join(PLATFORM_CONFIG.keys())}")
    
    config = PLATFORM_CONFIG[platform]
    
    # Generate components
    content = generate_content(topic, platform)
    hashtags = generate_hashtags(topic, platform)
    
    # Combine content with hashtags
    if platform == "instagram":
        # Instagram: hashtags often in comments or after multiple line breaks
        full_content = f"{content}\n\n\n\n" + "\n".join(hashtags)
    else:
        full_content = f"{content}\n\n" + " ".join(hashtags)
    
    # Generate metadata
    result = {
        "platform": config["name"],
        "content": full_content,
        "hashtags": hashtags,
        "media_suggestions": generate_media_suggestions(platform, topic),
        "character_count": len(full_content),
        "max_characters": config["max_chars"],
        "tone": config["tone"],
        "engagement_hooks": generate_engagement_hooks(platform),
        "metadata": {
            "original_topic": topic,
            "category": categorize_topic(topic),
            "optimal_length": config["optimal_chars"],
        }
    }
    
    return result


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Generate optimized social media posts from topics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_posts.py --topic "Launched new feature" --platform twitter
  python generate_posts.py --topic "Company milestone" --platform linkedin
  python generate_posts.py --topic "Behind the scenes" --platform instagram
  python generate_posts.py --topic "Important update" --platform telegram
        """
    )
    
    parser.add_argument(
        "--topic", "-t",
        required=True,
        help="The topic or announcement to convert into a post"
    )
    
    parser.add_argument(
        "--platform", "-p",
        required=True,
        choices=["twitter", "linkedin", "instagram", "telegram"],
        help="Target platform: twitter, linkedin, instagram, or telegram"
    )
    
    parser.add_argument(
        "--format", "-f",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )
    
    args = parser.parse_args()
    
    try:
        result = generate_post(args.topic, args.platform)
        
        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            # Pretty print for terminal
            print(f"\n{'='*60}")
            print(f"SOCIAL MEDIA POST - {result['platform']}")
            print(f"{'='*60}\n")
            print(f"📝 Content:\n{result['content']}\n")
            print(f"📊 Stats:")
            print(f"   • Characters: {result['character_count']} / {result['max_characters']}")
            print(f"   • Tone: {result['tone']}")
            print(f"\n🏷️ Hashtags: {' '.join(result['hashtags'])}")
            print(f"\n🎨 Media Suggestions: {', '.join(result['media_suggestions'])}")
            print(f"\n💡 Engagement Tips:")
            for tip in result['engagement_hooks']:
                print(f"   • {tip}")
            print(f"\n{'='*60}\n")
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    import sys
    main()
#!/usr/bin/env python3
"""
Social Media Post Generator
Generates platform-optimized posts for Twitter/X, LinkedIn, Instagram, and Telegram
"""

import argparse
import sys
from typing import Dict, List, Optional


class SocialMediaGenerator:
    """Generate social media posts optimized for different platforms."""
    
    PLATFORM_CONFIGS = {
        'twitter': {
            'name': 'Twitter/X',
            'max_chars': 280,
            'max_hashtags': 3,
            'tone': 'conversational',
            'emoji_style': 'minimal',
            'description': 'Short, punchy posts with strong hooks'
        },
        'linkedin': {
            'name': 'LinkedIn',
            'max_chars': 3000,
            'max_hashtags': 5,
            'tone': 'professional',
            'emoji_style': 'none',
            'description': 'Professional, value-driven content'
        },
        'instagram': {
            'name': 'Instagram',
            'max_chars': 2200,
            'max_hashtags': 15,
            'tone': 'authentic',
            'emoji_style': 'abundant',
            'description': 'Visual, engaging stories with emojis'
        },
        'telegram': {
            'name': 'Telegram',
            'max_chars': 4096,
            'max_hashtags': 5,
            'tone': 'informative',
            'emoji_style': 'moderate',
            'description': 'Direct, update-style announcements'
        }
    }
    
    TONE_GUIDELINES = {
        'conversational': {
            'greeting': ['Hey', 'Quick update', 'Big news', 'Excited to share'],
            'style': 'casual, friendly, engaging',
            'sentence_length': 'short',
            'questions': True
        },
        'professional': {
            'greeting': ['Excited to announce', 'Proud to share', 'Important update', 'We're thrilled'],
            'style': 'formal, insightful, value-focused',
            'sentence_length': 'medium',
            'questions': False
        },
        'authentic': {
            'greeting': ['✨ Sharing something special', '💫 Big moment', '🎉 Can't wait to share', '🚀 Something amazing'],
            'style': 'personal, story-driven, emotional',
            'sentence_length': 'varied',
            'questions': True
        },
        'informative': {
            'greeting': ['📢 Announcement', '🔔 Update', '📌 Important', '🎯 New feature'],
            'style': 'clear, factual, direct',
            'sentence_length': 'medium',
            'questions': False
        }
    }
    
    HASHTAG_CATEGORIES = {
        'tech': ['#Tech', '#Innovation', '#Technology', '#Blockchain', '#Crypto', '#Web3', '#DeFi', '#NFT'],
        'business': ['#Business', '#Startup', '#Entrepreneur', '#Growth', '#Leadership', '#Success'],
        'community': ['#Community', '#Building', '#Together', '#Support', '#Network'],
        'announcement': ['#Announcement', '#New', '#Launch', '#ComingSoon', '#Exciting'],
        'general': ['#SocialMedia', '#Content', '#Digital', '#Online', '#Connect']
    }
    
    def __init__(self):
        self.topic = ""
        self.platform = ""
        self.tone = ""
    
    def analyze_topic(self, topic: str) -> Dict:
        """Analyze topic to determine relevant hashtags and tone."""
        topic_lower = topic.lower()
        
        # Determine categories based on keywords
        categories = ['general']
        if any(word in topic_lower for word in ['blockchain', 'crypto', 'web3', 'near', 'defi', 'nft', 'legion']):
            categories.append('tech')
        if any(word in topic_lower for word in ['launch', 'release', 'announce', 'new', 'update']):
            categories.append('announcement')
        if any(word in topic_lower for word in ['team', 'partnership', 'collaboration', 'growth']):
            categories.append('business')
        if any(word in topic_lower for word in ['community', 'users', 'members', 'support']):
            categories.append('community')
        
        return {
            'topic': topic,
            'categories': list(set(categories)),
            'keywords': self.extract_keywords(topic)
        }
    
    def extract_keywords(self, topic: str) -> List[str]:
        """Extract key terms from topic."""
        # Simple extraction - split and filter
        words = topic.lower().split()
        stop_words = ['a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of']
        keywords = [w for w in words if w not in stop_words and len(w) > 2]
        return list(set(keywords))[:5]
    
    def generate_hashtags(self, analysis: Dict, platform: str) -> List[str]:
        """Generate relevant hashtags based on topic analysis and platform."""
        max_hashtags = self.PLATFORM_CONFIGS[platform]['max_hashtags']
        hashtags = []
        
        # Add category-specific hashtags
        for category in analysis['categories']:
            if category in self.HASHTAG_CATEGORIES:
                hashtags.extend(self.HASHTAG_CATEGORIES[category])
        
        # Add topic-specific hashtags
        for keyword in analysis['keywords']:
            hashtags.append(f"#{keyword.capitalize()}")
        
        # Remove duplicates and limit
        hashtags = list(dict.fromkeys(hashtags))[:max_hashtags]
        return hashtags
    
    def generate_post_content(self, topic: str, platform: str, tone: str = None) -> str:
        """Generate the main post content."""
        if tone is None:
            tone = self.PLATFORM_CONFIGS[platform]['tone']
        
        guidance = self.TONE_GUIDELINES[tone]
        greeting = self._pick_greeting(guidance['greeting'])
        
        if platform == 'twitter':
            return self._generate_twitter_post(topic, greeting, guidance)
        elif platform == 'linkedin':
            return self._generate_linkedin_post(topic, greeting, guidance)
        elif platform == 'instagram':
            return self._generate_instagram_post(topic, greeting, guidance)
        elif platform == 'telegram':
            return self._generate_telegram_post(topic, greeting, guidance)
        else:
            return f"Platform {platform} not supported"
    
    def _pick_greeting(self, greetings: List[str]) -> str:
        """Pick a random greeting from list."""
        import random
        return random.choice(greetings)
    
    def _generate_twitter_post(self, topic: str, greeting: str, guidance: Dict) -> str:
        """Generate Twitter/X post."""
        # Keep it under 280 chars with hashtags
        content_parts = [
            f"{greeting} to share about {topic}! 🚀",
            f"This is a game-changer for the community.",
            f"Stay tuned for more updates!",
        ]
        
        content = " ".join(content_parts)
        
        # Ensure under limit
        if len(content) > 240:
            content = content[:237] + "..."
        
        return content
    
    def _generate_linkedin_post(self, topic: str, greeting: str, guidance: Dict) -> str:
        """Generate LinkedIn post."""
        content = f"""{greeting} to announce significant developments around {topic}.

This represents a major milestone in our journey and demonstrates our commitment to innovation and delivering value to our community.

Key highlights:
• Strategic advancement in our roadmap
• Enhanced capabilities for users
• Continued focus on excellence

We're excited about what this means for the future and grateful for the support from our incredible community.

What are your thoughts on this development? Let's discuss in the comments!

#Innovation #Growth #Community #Technology #Leadership"""
        
        return content
    
    def _generate_instagram_post(self, topic: str, greeting: str, guidance: Dict) -> str:
        """Generate Instagram post."""
        content = f"""{greeting} about {topic}! ✨

🎉 This is such an exciting moment for us!

💫 We've been working hard on this and can't wait for you to experience it.

🚀 The journey has been incredible, and this is just the beginning!

💪 Thank you to our amazing community for your continued support!

👇 What are you most excited about? Drop a comment below!

#Community #Innovation #Exciting #NewBeginnings #Grateful #BuildingTogether #FutureIsHere"""
        
        return content
    
    def _generate_telegram_post(self, topic: str, greeting: str, guidance: Dict) -> str:
        """Generate Telegram post."""
        content = f"""{greeting}

**{topic}**

📢 We're pleased to share important updates with our community.

This development marks a significant step forward in our mission to deliver exceptional value and innovation.

**What to expect:**
• Enhanced features and capabilities
• Improved user experience
• Continued commitment to excellence

Stay tuned for more detailed announcements coming soon!

🔔 Enable notifications to never miss an update.

#Update #Announcement #Community #Technology"""
        
        return content
    
    def generate(self, topic: str, platform: str, tone: Optional[str] = None) -> Dict:
        """Generate a complete social media post."""
        if platform not in self.PLATFORM_CONFIGS:
            return {
                'error': f'Platform "{platform}" not supported. Choose from: {", ".join(self.PLATFORM_CONFIGS.keys())}'
            }
        
        if tone and tone not in self.TONE_GUIDELINES:
            tone = self.PLATFORM_CONFIGS[platform]['tone']
        
        # Analyze topic
        analysis = self.analyze_topic(topic)
        
        # Generate content
        content = self.generate_post_content(topic, platform, tone)
        
        # Generate hashtags
        hashtags = self.generate_hashtags(analysis, platform)
        
        # Combine content and hashtags
        full_post = content
        if hashtags:
            full_post += "\n\n" + " ".join(hashtags)
        
        # Check character count
        char_count = len(full_post)
        max_chars = self.PLATFORM_CONFIGS[platform]['max_chars']
        
        # Build result
        result = {
            'platform': self.PLATFORM_CONFIGS[platform]['name'],
            'platform_key': platform,
            'topic': topic,
            'tone': tone or self.PLATFORM_CONFIGS[platform]['tone'],
            'content': content,
            'hashtags': hashtags,
            'full_post': full_post,
            'character_count': char_count,
            'max_characters': max_chars,
            'within_limit': char_count <= max_chars,
            'engagement_tips': self._get_engagement_tips(platform)
        }
        
        return result
    
    def _get_engagement_tips(self, platform: str) -> List[str]:
        """Get platform-specific engagement tips."""
        tips = {
            'twitter': [
                'Post during peak hours (9-11 AM or 1-3 PM)',
                'Include a visual (image/GIF) for 2x engagement',
                'Reply to comments within 1 hour for better reach'
            ],
            'linkedin': [
                'Post Tuesday-Thursday for best reach',
                'Engage with comments within 2 hours',
                'Share behind-the-scenes content alongside announcements'
            ],
            'instagram': [
                'Use Stories to tease the post',
                'Post when your audience is most active',
                'Respond to DMs and comments promptly'
            ],
            'telegram': [
                'Pin important posts',
                'Use reactions to encourage engagement',
                'Share updates consistently to build anticipation'
            ]
        }
        return tips.get(platform, ['Post consistently', 'Engage with your audience'])
    
    def format_output(self, result: Dict) -> str:
        """Format the result for display."""
        if 'error' in result:
            return f"❌ Error: {result['error']}"
        
        output = []
        output.append("=" * 60)
        output.append(f"📱 {result['platform']} Post Generator")
        output.append("=" * 60)
        output.append(f"\n📝 Topic: {result['topic']}")
        output.append(f"🎯 Tone: {result['tone']}")
        output.append(f"\n📄 Content:\n{result['content']}")
        
        if result['hashtags']:
            output.append(f"\n🏷️ Hashtags:\n{' '.join(result['hashtags'])}")
        
        output.append(f"\n📊 Stats:")
        output.append(f"   • Character count: {result['character_count']}/{result['max_characters']}")
        output.append(f"   • Within limit: {'✅ Yes' if result['within_limit'] else '❌ No'}")
        
        output.append(f"\n💡 Engagement Tips:")
        for tip in result['engagement_tips']:
            output.append(f"   • {tip}")
        
        output.append("\n" + "=" * 60)
        output.append("📋 COPY-READY POST:")
        output.append("=" * 60)
        output.append(result['full_post'])
        output.append("=" * 60)
        
        return "\n".join(output)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate platform-optimized social media posts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_posts.py --topic "Near Legion launching new features" --platform twitter
  python generate_posts.py --topic "Near Legion" --platform linkedin
  python generate_posts.py --topic "Near Legion" --platform all
        """
    )
    
    parser.add_argument(
        '--topic', '-t',
        required=True,
        help='The topic or announcement to generate posts about'
    )
    
    parser.add_argument(
        '--platform', '-p',
        required=True,
        choices=['twitter', 'linkedin', 'instagram', 'telegram', 'all'],
        help='Target platform (twitter, linkedin, instagram, telegram, or all)'
    )
    
    parser.add_argument(
        '--tone',
        choices=['conversational', 'professional', 'authentic', 'informative'],
        help='Override default tone for the platform'
    )
    
    parser.add_argument(
        '--json', '-j',
        action='store_true',
        help='Output as JSON instead of formatted text'
    )
    
    args = parser.parse_args()
    
    generator = SocialMediaGenerator()
    
    if args.platform == 'all':
        platforms = ['twitter', 'linkedin', 'instagram', 'telegram']
        for platform in platforms:
            result = generator.generate(args.topic, platform, args.tone)
            if args.json:
                import json
                print(json.dumps(result, indent=2))
            else:
                print(generator.format_output(result))
                print("\n")
    else:
        result = generator.generate(args.topic, args.platform, args.tone)
        if args.json:
            import json
            print(json.dumps(result, indent=2))
        else:
            print(generator.format_output(result))


if __name__ == '__main__':
    main()