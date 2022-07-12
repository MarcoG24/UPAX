from microservices.entry_point_types import RetrieveProductsContainerType

__all__ = ['RetrieveOrdersByMail']

class RetrieveOrdersByMail:
    def __init__(self, container:RetrieveProductsContainerType) -> None:
        self._database = container.database_repository

    def _retrieve_orders_by_mail(self, email:str):
        return self._database.retrieve_orders_by_mail(email)

    def run(self, email:str):
        return self._retrieve_orders_by_mail(email)