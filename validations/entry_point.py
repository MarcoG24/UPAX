
from validations.application.retrieve.validations_retrieve import RetrieveValidations


def retrieve_validations(
    event,
    context
):
    '''
    # Fibonacci
    python aws_lambda_wrapper.py '{\"event_type\": \"fibonacci\", \"number\": 21 }' --function retrieve_validations

    # Factorial
    python aws_lambda_wrapper.py '{\"event_type\": \"factorial\", \"number\": 21 }' --function retrieve_validations

    # Is Prime
    python aws_lambda_wrapper.py '{\"event_type\": \"prime\", \"number\": 21 }' --function retrieve_validations

    # Is palindrome
    python aws_lambda_wrapper.py '{\"event_type\": \"palindrome\", \"number\": 9669669 }' --function retrieve_validations
    
    # All
    python aws_lambda_wrapper.py '{\"event_type\": \"all\", \"number\": 21 }' --function retrieve_validations
    
    '''
    return RetrieveValidations().run(event)