

from pydantic import BaseModel
from enum import Enum

class Snowboard(BaseModel):

    id: int
    length: int
    color: str
    has_bindings: bool
    


class Brand(Enum):

     NITRO = "Nitro"
     SALOMON = "Saloman"
     BURTON = "Burton"
