from typing import Optional

from pydantic_geojson import MultiPolygonModel
from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    address: MultiPolygonModel


def test_multipolygon_model():
    address_dict = {
        "type": "MultiPolygon",
        "coordinates": [
            [[[107, 7], [108, 7], [108, 8], [107, 8], [107, 7]]],
            [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]
        ]
    }
    address = MultiPolygonModel(**address_dict)
    my_hero = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48, address=address)
