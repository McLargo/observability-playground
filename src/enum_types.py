from enum import Enum


class QueryType(Enum):
    READ = "read"
    WRITE = "write"
    REPORT = "report"


class SchemaType(Enum):
    USER = "user"


class EventType(Enum):
    LOGIN = "login"
    DATA_PROCESSING = "data_processing"


class EventStatus(Enum):
    SUCCESS = "success"
    FAILURE = "failure"
