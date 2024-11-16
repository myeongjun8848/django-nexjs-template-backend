from ninja import Schema
from datetime import datetime

class PostIn(Schema):
    title: str
    content: str


class PostOut(Schema):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

