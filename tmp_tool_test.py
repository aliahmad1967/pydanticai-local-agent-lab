import os, asyncio
from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()
os.environ.setdefault('OLLAMA_BASE_URL', 'http://localhost:11434/v1')
os.environ.setdefault('OLLAMA_API_KEY', 'ollama')

agent = Agent(
    'ollama:gemma4:e4b',
    system_prompt='You are a helpful assistant. Use a tool when needed and answer briefly.'
)

@agent.tool_plain
def get_weather(city: str) -> str:
    data = {
        'paris': 'Paris is 18°C and cloudy.',
        'london': 'London is 16°C and rainy.',
        'tokyo': 'Tokyo is 24°C and sunny.',
    }
    return data.get(city.lower(), f'I do not have live data for {city}, but it is likely a pleasant day.')

async def main():
    result = await agent.run('What is the weather in Paris?')
    print(result.output)

asyncio.run(main())
