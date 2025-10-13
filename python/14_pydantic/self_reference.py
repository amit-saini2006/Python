from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

comment = Comment(
    id=1,
    content="This is the main comment",
    replies=[
        Comment(id=2, content="This is a reply"),
        Comment(id=3, content="Another reply")
    ]
)

print(comment)
