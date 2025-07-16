from enum import Enum


class EventType(Enum):
    LOGIN = "login"
    DATA_PROCESSING = "data_processing"


class EventStatus(Enum):
    SUCCESS = "success"
    FAILURE = "failure"
