import asyncio
import os

from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()
os.environ.setdefault("OLLAMA_BASE_URL", "http://localhost:11434/v1")
os.environ.setdefault("OLLAMA_API_KEY", "ollama")

agent = Agent(
    "ollama:gemma4:e4b",
    system_prompt=(
        "You are a blog strategist and editor. "
        "Use the available tools to gather content ideas, structure, and writing hooks, then produce a useful blog recommendation."
    ),
)


@agent.tool_plain
def suggest_title(topic: str) -> str:
    titles = {
        "ai productivity": "AI Productivity for Busy Teams: 7 High-Impact Habits",
        "remote work": "Remote Work That Actually Works: Systems for Focus and Trust",
        "content marketing": "Content Marketing Without Burnout: A Sustainable Weekly System",
    }
    return titles.get(
        topic.lower(),
        f"Suggested title for '{topic}': {topic.title()} That Delivers Results",
    )


@agent.tool_plain
def build_outline(topic: str, audience: str) -> str:
    return (
        f"Blog outline for '{topic}' aimed at {audience}:\n"
        "1. Hook: the problem and why it matters\n"
        "2. What the audience is struggling with\n"
        "3. Three practical strategies\n"
        "4. Common mistakes to avoid\n"
        "5. A simple action plan for the next week\n"
        "6. Closing takeaway and CTA"
    )


@agent.tool_plain
def get_blog_hooks(topic: str) -> str:
    hooks = {
        "ai productivity": "Most teams do not need more AI tools; they need a better workflow for using the ones they already have.",
        "remote work": "Remote work succeeds when clarity, systems, and trust replace micromanagement.",
        "content marketing": "The best content strategy is not more posting; it is better repetition with sharper audience focus.",
    }
    return hooks.get(
        topic.lower(),
        f"A strong hook for '{topic}': start with a real pain point and show the business impact clearly.",
    )


async def main():
    result = await agent.run(
        "Create a blog post for beginners about using AI to improve team productivity. "
        "Give me a strong title, a simple outline, and an engaging opening hook."
    )
    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
