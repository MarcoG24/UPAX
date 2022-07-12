from microservices.entry_point_types import RetrieveProductsContainerType

__all__ = ['CreatePay']

class CreatePay:
    def __init__(self, container:RetrieveProductsContainerType) -> None:
        self._database = container.database_repository
        self._list_of_data = []

    def _create_pay(self):
        return self._database.create_pay(self._list_of_data)

    def _user_info(self, data):
        list_of_names= ['name', 'last_name', 'email', 'phone_number']
        for name in list_of_names:
            self._list_of_data.append(data[name])

    def _delivery_info(self, data):
        list_of_names= ['address', 'complementary_address', 'city', 'state', 'zip']
        for name in list_of_names:
            self._list_of_data.append(data[name])

    def _payment_info(self, data):
        list_of_names= ['card_number', 'name', 'mm', 'yy', 'cvv']
        for name in list_of_names:
            self._list_of_data.append(data[name])

    def _products(self, data):
        list_of_names= ['address', 'complementary_address', 'city', 'state', 'zip']
        for name in list_of_names:
            self._list_of_data.append(data[0][name])
    

    def run(self, event):
        self._user_info(event['order']['user_info'])
        self._delivery_info(event['order']['delivery_info'])
        self._payment_info(event['order']['payment_info'])
        self._products(event['order']['products'])
        return self._create_pay()