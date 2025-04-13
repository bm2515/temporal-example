import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities import GreetingActivities
from shared import WELCOME_CAKE_TASK_QUEUE_NAME
from workflows import Greeting


async def main() -> None:
    client: Client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    greeting_activities = GreetingActivities()
    worker: Worker = Worker(
        client,
        task_queue=WELCOME_CAKE_TASK_QUEUE_NAME,
        workflows=[Greeting],
        activities=[greeting_activities.greetings],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
