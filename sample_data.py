from typing import List
from uuid import uuid4

from models import User, Gender, Role


sample_db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.FEMALE,
        roles=[Role.STUDENT]
    ),
    User(
        id=uuid4(),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.MALE,
        roles=[Role.ADMIN, Role.USER]
    )
]