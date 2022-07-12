import json
from calculations.entry_point import retrieve_calculations
from conversions.entry_point import retrieve_conversions
from helpers.entry_point import get_params
from microservices.entry_point import (
    retrieve_advertisements_handler,
    retrieve_orders_by_mail_handler,
    retrieve_recommendations_handler
)
from operations.entry_point import retrieve_operations
from validations.entry_point import retrieve_validations


if __name__ == "__main__":
    '''
    This main is for local testing purposes
    '''
    EVENT_PARAMS, CONTEXT, DEBUG, FUNCTION = get_params()
    EVENT = json.loads(EVENT_PARAMS)

    command_arguments = dict(
        event=EVENT,
        context=CONTEXT
    )

    functions = {
        'retrieve_calculations': lambda: print(json.dumps(
            retrieve_calculations(**command_arguments)
        )),
        'retrieve_validations': lambda: print(json.dumps(
            retrieve_validations(**command_arguments)
        )),
        'retrieve_operations': lambda: print(json.dumps(
            retrieve_operations(**command_arguments)
        )),
        'retrieve_conversions': lambda: print(json.dumps(
            retrieve_conversions(**command_arguments)
        )),
        'retrieve_advertisements_handler': lambda: print(json.dumps(
            retrieve_advertisements_handler(**command_arguments)
        )),
        'retrieve_recommendations_handler': lambda: print(json.dumps(
            retrieve_recommendations_handler(**command_arguments)
        )),
        'retrieve_orders_by_mail_handler': lambda: print(json.dumps(
            retrieve_orders_by_mail_handler(**command_arguments)
        ))
    }
    if FUNCTION:
        functions[FUNCTION] ()