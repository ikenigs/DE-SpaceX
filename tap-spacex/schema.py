schema = {
    'type': 'object',
    'properties': {
        'fairings': {'type': ['object', 'null']},
        'links': {'type': 'object'},  # complex nested object
        'static_fire_date_utc': {'type': ['string', 'null'], 'format': 'date-time'},
        'static_fire_date_unix': {'type': ['number', 'null']},
        'net': {'type': 'boolean'},
        'window': {'type': ['number', 'null']},
        'rocket': {'type': 'string'},
        'success': {'type': ['boolean', 'null']},
        'failures': {'type': ['array', 'null']},
        'details': {'type': ['string', 'null']},
        'crew': {'type': ['array', 'null']},
        'ships': {'type': ['array', 'null']},
        'capsules': {'type': ['array', 'null']},
        'payloads': {'type': ['array', 'null']},
        'launchpad': {'type': 'string'},
        'flight_number': {'type': 'integer'},
        'name': {'type': 'string'},
        'date_utc': {'type': 'string', 'format': 'date-time'},
        'date_unix': {'type': 'integer'},
        'date_local': {'type': 'string'},
        'date_precision': {'type': 'string'},
        'upcoming': {'type': 'boolean'},
        'cores': {'type': ['array', 'null']},
        'auto_update': {'type': 'boolean'},
        'tbd': {'type': 'boolean'},
        'launch_library_id': {'type': ['string', 'null']},
        'id': {'type': 'string'}
    }
}
