from microservices.entry_point_types import RetrieveProductsContainerType

__all__ = ['RetrieveRecommendations']

class RetrieveRecommendations:
    def __init__(self, container:RetrieveProductsContainerType) -> None:
        self._database = container.database_repository

    def _retrieve_recommendations(self):
        return self._database.retrieve_recommendations()

    def run(self):
        return self._retrieve_recommendations()