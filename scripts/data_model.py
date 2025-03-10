# generated by datamodel-codegen:
#   filename:  records.json
#   timestamp: 2025-02-28T18:25:45+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, RootModel


class ModelItem(BaseModel):
    cdi_id: str
    year: int
    status: str
    pi_name: str
    title: str
    short_title: str
    givenname: str
    surname: str
    pi_org: str
    pi_missionarea: str
    id: str


class Model(RootModel[List[ModelItem]]):
    root: List[ModelItem]
