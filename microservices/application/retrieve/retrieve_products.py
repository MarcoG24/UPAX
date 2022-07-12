from microservices.entry_point_types import RetrieveProductsContainerType

__all__ = ['RetrieveProducts']

class RetrieveProducts:
    def __init__(self, container:RetrieveProductsContainerType) -> None:
        self._database = container.database_repository

    def _retrieve_products(self):
        return self._database.retrieve_products()

    def run(self):
        return self._retrieve_products()