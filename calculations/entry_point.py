
from calculations.application.retrieve.retrieve_calculations import RetrieveCalculations


def retrieve_calculations(
    event,
    context
):
    '''
    # Retrieve Fibonacci
    ## Run in mac
    python aws_lambda_wrapper.py '{\
        "event_type": "fibonacci",\
        "number": 8\
        }' --function retrieve_calculations

    ## Run in windows
    python aws_lambda_wrapper.py '{\"event_type\": \"fibonacci\", \"number\": 8 }' --function retrieve_calculations

    # Retrieve Collatz sequence
    ## Run in mac
    python aws_lambda_wrapper.py '{\
        "event_type": "collatz",\
        "number": 8\
        }' --function retrieve_calculations

    ## Run in windows
    python aws_lambda_wrapper.py '{\"event_type\": \"collatz\", \"number\": 8 }' --function retrieve_calculations

    # Retrieve Factorial
    ## Run in mac
    python aws_lambda_wrapper.py '{\
        "event_type": "factorial",\
        "number": 8\
        }' --function retrieve_calculations

    ## Run in windows
    python aws_lambda_wrapper.py '{\"event_type\": \"factorial\", \"number\": 8 }' --function retrieve_calculations

    # Retrieve IMC
    ## Run in mac
    python aws_lambda_wrapper.py '{\
        "event_type": "imc",\
        "kg": 93\
        "height": 1.75\
        }' --function retrieve_calculations

    ## Run in windows
    python aws_lambda_wrapper.py '{\"event_type\": \"imc\", \"kg\": 93, \"height\": 1.75 }' --function retrieve_calculations
    '''
    
    return RetrieveCalculations().run(event)