from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class User(Base):
    __tablename__: str = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(index=True, unique=True)
    # email: Mapped[str] = mapped_column(index=True, unique=True)
    # first_name: Mapped[str]
    # last_name: Mapped[str]
    hashed_password: Mapped[str] = mapped_column()
    is_superuser: Mapped[bool] = mapped_column(default=False)
