import asyncio

from temporalio import activity

from service import GreetingService
from shared import (
    WelcomeDetails,
)


class GreetingActivities:
    def __init__(self):
        self.greeting = GreetingService('greeting-api.example.noon.com')

    @activity.defn
    async def greetings(self, data: WelcomeDetails) -> str:
        
        greetings = await asyncio.to_thread(
            self.greeting.send_greeting, data.cohort_name
        )
        return greetings
            