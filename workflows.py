from datetime import timedelta
import asyncio

from temporalio import workflow
from temporalio.common import RetryPolicy
from temporalio.exceptions import ActivityError

with workflow.unsafe.imports_passed_through():
    from activities import GreetingActivities
    from shared import WelcomeDetails


@workflow.defn
class Greeting:
    @workflow.run
    async def run(self, welcome_details: WelcomeDetails) -> str:

        retry_policy = RetryPolicy(
            maximum_attempts=3,
            maximum_interval=timedelta(seconds=2),
            non_retryable_error_types=[],
        )

        try:    
            greeting_output = await workflow.execute_activity_method(
                GreetingActivities.greetings,
                WelcomeDetails(welcome_details.cohort_name),
                start_to_close_timeout=timedelta(seconds=5),
                retry_policy=retry_policy,
            )
            return greeting_output

        except ActivityError as greeting_err:
            workflow.logger.error(f"The greetings workflow failed with exception: {greeting_err}")
            raise greeting_err