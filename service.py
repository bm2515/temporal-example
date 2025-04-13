import uuid
from dataclasses import dataclass
from typing import NoReturn


@dataclass
class GreetingService:

    def __init__(self, host: str) -> None:
        self.host: str = host
        
    def send_greeting(self, greet_entity) -> str:
        return f"Hello {greet_entity}"