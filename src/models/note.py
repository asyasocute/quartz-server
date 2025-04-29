from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base 


class Note(Base):
    __tablename__: str = "note"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    text: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship("User", back_populates="notes")
