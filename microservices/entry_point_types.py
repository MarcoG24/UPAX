from typing import NamedTuple
from microservices.infrastructure.planet_scale import PlanetScaleRepository


class RetrieveProductsContainerType(NamedTuple):
    database_repository: PlanetScaleRepository