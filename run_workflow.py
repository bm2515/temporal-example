import asyncio
import traceback

from temporalio.client import Client, WorkflowFailureError

from shared import WELCOME_CAKE_TASK_QUEUE_NAME, WelcomeDetails
from workflows import Greeting

async def main() -> None:
    # Create client connected to server at the given address
    client: Client = await Client.connect("localhost:7233")

    data: WelcomeDetails = WelcomeDetails(
        cohort_name='Cake 2025'
    )

    try:
        result = await client.execute_workflow(
            Greeting.run,
            data,
            id="greet-cake-2025",
            task_queue=WELCOME_CAKE_TASK_QUEUE_NAME,
        )

        print(f"Result: {result}")

    except WorkflowFailureError:
        print("Got expected exception: ", traceback.format_exc())


if __name__ == "__main__":
    asyncio.run(main())
