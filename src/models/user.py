from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base
from src.models.note import Note


class User(Base):
    __tablename__: str = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(index=True, unique=True)
    hashed_password: Mapped[str] = mapped_column()
    is_superuser: Mapped[bool] = mapped_column(default=False)
    notes: Mapped[list["Note"]] = relationship("Note", back_populates="user")

