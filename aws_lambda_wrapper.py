import json
from calculations.entry_point import retrieve_calculations
from helpers.entry_point import get_params


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
        ))
    }
    if FUNCTION:
        functions[FUNCTION] ()