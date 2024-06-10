from dataclasses import dataclass
from typing import List

from pydantic import BaseModel


@dataclass
class Announcement:
    title: str
    body: str


@dataclass
class CreditEntry:
    agentSymbol: str
    credits: int


@dataclass
class ChartEntry:
    agentSymbol: str
    chartCount: int


@dataclass
class Leaderboard:
    mostCredits: List[CreditEntry]
    mostSubmittedCharts: List[ChartEntry]


@dataclass
class Link:
    name: str
    url: str


@dataclass
class ServerReset:
    frequency: str
    next: str


@dataclass
class Stats:
    agents: int
    ships: int
    systems: int
    waypoints: int


@dataclass
class Status:
    announcements: List[Announcement]
    description: str
    leaderboards: Leaderboard
    links: List[Link]
    resetDate: str
    serverResets: ServerReset
    stats: Stats
    status: str
    version: str
