name: social-media-generator description: Automatically generate optimized social media posts for Twitter/X, LinkedIn, Instagram, and Telegram from topics or announcements version: 1.0.0 author: assistant keywords: [social-media, twitter, linkedin, instagram, telegram, content-generation]
Social Media Generator Skill
A skill that automatically generates optimized social media posts for multiple platforms from a single topic or announcement input.

Frontmatter
Copyname: social-media-generator
description: Generate platform-optimized social media posts from topics
version: 1.0.0
entry_point: generate_posts.py
Platform Specifications
Twitter/X
Character Limit: 280 characters (standard), 4000 for premium users
Recommended: Keep under 260 characters for retweets
Tone: Concise, punchy, engaging, conversational
Hashtags: 1-3 relevant hashtags maximum
Best Practices: Use threads for longer content, include media suggestions, add engagement hooks
LinkedIn
Character Limit: 3000 characters for posts
Recommended: 150-300 characters for optimal engagement
Tone: Professional, informative, thought-leadership oriented
Hashtags: 3-5 industry-relevant hashtags
Best Practices: Start with a hook, use line breaks for readability, include call-to-action
Instagram
Character Limit: 2200 characters for captions
Recommended: 100-150 characters for engagement
Tone: Visual, authentic, inspiring, community-focused
Hashtags: 5-15 relevant hashtags (can include in comments)
Best Practices: Focus on visual description, use emojis, include engagement questions
Telegram
Character Limit: 4096 characters
Recommended: 200-500 characters
Tone: Direct, informative, community-oriented
Hashtags: 2-4 hashtags, or none (Telegram uses links better)
Best Practices: Use formatting (bold, italic), include links, mention channel context
Usage
The skill accepts two parameters:

topic - The subject, announcement, or content to convert into a post
platform - One of: twitter, linkedin, instagram, telegram
Output Format
Returns a structured post object containing:

content: The main post text
hashtags: Array of suggested hashtags
media_suggestions: Array of suggested media types
character_count: Length of the post
engagement_hooks: Suggested ways to boost engagement
Example
Input:

Copy{
  "topic": "Launched new AI-powered analytics dashboard for small businesses",
  "platform": "linkedin"
}
Output:

Copy{
  "content": "🚀 Exciting news! We just launched our new AI-powered analytics dashboard designed specifically for small businesses.\n\nTransform your data into actionable insights without the enterprise price tag. Early users are seeing 40% faster decision-making.\n\nWhat metrics matter most to your business? Let's discuss in the comments 👇\n\n#SmallBusiness #AI #Analytics #DataDriven #TechLaunch",
  "hashtags": ["#SmallBusiness", "#AI", "#Analytics", "#DataDriven", "#TechLaunch"],
  "media_suggestions": ["product screenshot", "demo gif", "team celebration photo"],
  "character_count": 387,
  "engagement_hooks": ["Ask a question about metrics", "Invite comments", "Share early user results"]
}
name: social-media-generator description: Automatically generate optimized social media posts for Twitter/X, LinkedIn, Instagram, and Telegram from topics or announcements version: 1.0.0 author: assistant keywords: [social-media, twitter, linkedin, instagram, telegram, content-generation]
Social Media Generator Skill
A skill that automatically generates optimized social media posts for multiple platforms from a single topic or announcement input.

Frontmatter
Copyname: social-media-generator
description: Generate platform-optimized social media posts from topics
version: 1.0.0
entry_point: generate_posts.py
Platform Specifications
Twitter/X
Character Limit: 280 characters (standard), 4000 for premium users
Recommended: Keep under 260 characters for retweets
Tone: Concise, punchy, engaging, conversational
Hashtags: 1-3 relevant hashtags maximum
Best Practices: Use threads for longer content, include media suggestions, add engagement hooks
LinkedIn
Character Limit: 3000 characters for posts
Recommended: 150-300 characters for optimal engagement
Tone: Professional, informative, thought-leadership oriented
Hashtags: 3-5 industry-relevant hashtags
Best Practices: Start with a hook, use line breaks for readability, include call-to-action
Instagram
Character Limit: 2200 characters for captions
Recommended: 100-150 characters for engagement
Tone: Visual, authentic, inspiring, community-focused
Hashtags: 5-15 relevant hashtags (can include in comments)
Best Practices: Focus on visual description, use emojis, include engagement questions
Telegram
Character Limit: 4096 characters
Recommended: 200-500 characters
Tone: Direct, informative, community-oriented
Hashtags: 2-4 hashtags, or none (Telegram uses links better)
Best Practices: Use formatting (bold, italic), include links, mention channel context
Usage
The skill accepts two parameters:

topic - The subject, announcement, or content to convert into a post
platform - One of: twitter, linkedin, instagram, telegram
Output Format
Returns a structured post object containing:

content: The main post text
hashtags: Array of suggested hashtags
media_suggestions: Array of suggested media types
character_count: Length of the post
engagement_hooks: Suggested ways to boost engagement
Example
Input:

Copy{
  "topic": "Launched new AI-powered analytics dashboard for small businesses",
  "platform": "linkedin"
}
Output:

Copy{
  "content": "🚀 Exciting news! We just launched our new AI-powered analytics dashboard designed specifically for small businesses.\n\nTransform your data into actionable insights without the enterprise price tag. Early users are seeing 40% faster decision-making.\n\nWhat metrics matter most to your business? Let's discuss in the comments 👇\n\n#SmallBusiness #AI #Analytics #DataDriven #TechLaunch",
  "hashtags": ["#SmallBusiness", "#AI", "#Analytics", "#DataDriven", "#TechLaunch"],
  "media_suggestions": ["product screenshot", "demo gif", "team celebration photo"],
  "character_count": 387,
  "engagement_hooks": ["Ask a question about metrics", "Invite comments", "Share early user results"]
}
Social Media Generator Skill
Frontmatter
Copyname: social-media-generator
description: Auto-generates platform-optimized social media posts for Twitter/X, LinkedIn, Instagram, and Telegram from any topic or announcement
version: 1.0.0
author: assistant
keywords: [social media, content generation, twitter, linkedin, instagram, telegram, posts]
Platform Specifications
Twitter/X
Character limit: 280 characters (standard), 25,000 for premium
Tone: Conversational, punchy, engaging
Hashtags: 1-3 relevant hashtags, placed at end
Best practices: Use threads for longer content, include emojis sparingly, hook in first 100 characters
LinkedIn
Character limit: 3,000 characters
Tone: Professional, insightful, value-driven
Hashtags: 3-5 industry-relevant hashtags
Best practices: Start with strong hook, use line breaks for readability, include call-to-action
Instagram
Character limit: 2,200 characters (caption)
Tone: Visual, engaging, authentic
Hashtags: 5-15 relevant hashtags (can be in comments)
Best practices: Emojis encouraged, storytelling format, question to engage audience
Telegram
Character limit: 4,096 characters
Tone: Direct, informative, community-focused
Hashtags: 2-5 hashtags for topic organization
Best practices: Clear formatting with markdown, links included, update-style announcements
Usage
Copypython generate_posts.py --topic "Your topic here" --platform twitter
Or for all platforms:

Copypython generate_posts.py --topic "Your topic here" --platform all
Output Format
Each generated post includes:

Platform-optimized content
Hashtag recommendations
Character count
Engagement tips