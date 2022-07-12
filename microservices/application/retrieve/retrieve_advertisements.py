from microservices.entry_point_types import RetrieveProductsContainerType

__all__ = ['RetrieveAdvertisements']

class RetrieveAdvertisements:
    def __init__(self, container:RetrieveProductsContainerType) -> None:
        self._database = container.database_repository

    def _retrieve_advertisements(self):
        return self._database.retrieve_advertisements()

    def run(self):
        return self._retrieve_advertisements()