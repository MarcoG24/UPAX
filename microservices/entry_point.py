
from microservices.application.create.create_pay import CreatePay
from microservices.application.retrieve.retrieve_advertisements import RetrieveAdvertisements
from microservices.application.retrieve.retrieve_orders_by_mail import RetrieveOrdersByMail
from microservices.application.retrieve.retrieve_products import RetrieveProducts
from microservices.application.retrieve.retrieve_recommendations import RetrieveRecommendations
from microservices.entry_point_types import RetrieveProductsContainerType
from microservices.infrastructure.planet_scale import PlanetScaleRepository


def _get_retrieve_data_container():
    return RetrieveProductsContainerType(
        database_repository= PlanetScaleRepository()
    )

def retrieve_advertisements_handler(
    event,
    context
):
    '''
    python aws_lambda_wrapper.py '{}' --function retrieve_advertisements_handler
    '''
    
    return RetrieveAdvertisements(
        container=_get_retrieve_data_container()
    ).run(**event)

def retrieve_recommendations_handler(
    event,
    context
):
    '''
    python aws_lambda_wrapper.py '{}' --function retrieve_recommendations_handler
    '''
    
    return RetrieveRecommendations(
        container=_get_retrieve_data_container()
    ).run(**event)

def retrieve_products_handler(
    event,
    context
):
    '''
    python aws_lambda_wrapper.py '{}' --function retrieve_products_handler
    '''
    
    return RetrieveProducts(
        container=_get_retrieve_data_container()
    ).run(**event)

def retrieve_orders_by_mail_handler(
    event,
    context
):
    '''
    python aws_lambda_wrapper.py '{\"email\": \"marco@gmail.com\"}' --function retrieve_orders_by_mail_handler
    '''
    
    return RetrieveOrdersByMail(
        container=_get_retrieve_data_container()
    ).run(**event)

def create_pay(
    event,
    context
):
    '''
    python aws_lambda_wrapper.py '{\"order\":{\"user_info\":{\"name\":\"José\",\"last_name\":\"López\",\"email\":\"jlopez@gmail.com\",\"phone_number\":\"+525518628190\"},\"delivery_info\":{\"address\":\"Main St\",\"complementary_address\":\"Apartment 301, Floor 3\",\"city\":\"CDMX\",\"state\":\"CDMX\",\"zip\":\"01234\"},\"payment_info\":{\"card_number\":\"xxxxxxxxxxxxx\",\"name\":\"José López\",\"mm\":\"12\",\"yy\":\"27\",\"cvv\":\"024\"},\"products\":[{\"id\":1,\"amount\":5}]}}' --function create_pay
    '''
    
    return CreatePay(
        container=_get_retrieve_data_container()
    ).run(event)