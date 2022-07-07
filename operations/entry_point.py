
from operations.application.retrieve.retrieve_operations import RetrieveOperations


def retrieve_operations(
    event,
    context
):
    '''
    # Numbers random
    python aws_lambda_wrapper.py '{\"event_type\": \"random\", \"a\": 1, \"b\": 50, \"total\": 5 }' --function retrieve_operations
    '''
    return RetrieveOperations().run(event)