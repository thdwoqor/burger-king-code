from typing import Optional

from pydantic import BaseModel


class Store(BaseModel):
    id: int
    code: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    result: Optional[str] = None


class CodeNumber(BaseModel):
    CN1: int
    CN2: int
    CN3: int
    CN4: int
    CN5: int
    CN6: int
