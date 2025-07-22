from enum import Enum


class QueryType(Enum):
    READ = "read"
    WRITE = "write"
    REPORT = "report"


class SchemaType(Enum):
    USER = "user"
