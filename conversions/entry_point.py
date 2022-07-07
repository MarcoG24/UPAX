from conversions.application.retrieve.retrieve_conversions import RetrieveConversions


def retrieve_conversions(
    event,
    context
):
    '''
    # Temperature
    python aws_lambda_wrapper.py '{\"event_type\": \"temperature\", \"number\": 21 }' --function retrieve_conversions

    # Dough
    python aws_lambda_wrapper.py '{\"event_type\": \"dough\", \"number\": 1221 }' --function retrieve_conversions
    
    # Length
    python aws_lambda_wrapper.py '{\"event_type\": \"length\", \"number\": 1221 }' --function retrieve_conversions
    
    # volume
    python aws_lambda_wrapper.py '{\"event_type\": \"volume\", \"number\": 1221 }' --function retrieve_conversions

    # storage
    python aws_lambda_wrapper.py '{\"event_type\": \"storage\", \"number\": 1221 }' --function retrieve_conversions
    
    '''
    return RetrieveConversions().run(event)