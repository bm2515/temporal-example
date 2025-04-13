from dataclasses import dataclass

WELCOME_CAKE_TASK_QUEUE_NAME = "WELCOME_CAKE_TASK_QUEUE"


@dataclass
class WelcomeDetails:
    cohort_name: str