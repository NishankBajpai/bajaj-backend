from pydantic import BaseModel
from typing import List, Union

class DataRequest(BaseModel):
    data: List[Union[str, int]]
