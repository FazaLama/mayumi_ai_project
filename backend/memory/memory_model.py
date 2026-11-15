from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid


@dataclass
class Memory:

    content: str

    category: str

    importance: float = 0.5

    source: str = "system"

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    user_id: Optional[str] = None