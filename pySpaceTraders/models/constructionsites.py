from dataclasses import dataclass
from typing import List

from pySpaceTraders.models.cargo import Cargo
from pySpaceTraders.models.enums import TradeSymbol


@dataclass
class ConstructionMaterial:
    tradeSymbol: TradeSymbol
    required: int
    fulfilled: int


@dataclass
class ConstructionSite:
    symbol: str
    materials: List[ConstructionMaterial]
    isComplete: bool


@dataclass
class ConstructionSiteSupplyResponse:
    constructionSite: ConstructionSite
    cargo: Cargo