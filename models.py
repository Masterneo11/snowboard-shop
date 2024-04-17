

from pydantic import BaseModel


class Snowboard(BaseModel):

    id: int
    length: int
    color: str
    has_bindings: bool
    brand: str

# class Snowboard_info(BaseModel):

#     id: UUID 

# class Brand(Enum):

#     NITRO = 1
#     SALOMON = 2 
#     BURTON = 3
