from ninja import Schema
from typing import Union


class ArtIn(Schema):
    prompt: Union[str, None] = "Daimyo's procession of 20cm in length that only I can see."
    seed: Union[int, None] = 42
    scale: Union[float, None] = 0.7
    ddim_steps: Union[int, None] = 50
    n_iter: Union[int, None] = 1

