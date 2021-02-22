# Here be our API endpoints
vulnerabilities = {
    'name': {'type': 'string'},
    'severity': {'type': 'string'},
    'cvss_base_score': {'type': 'string'},
    'from_scan': {'type': 'integer'},
    'sid': {'type': 'integer'},
    'description': {'type': 'string'},
    'solution': {'type': 'string'},
    'affected_assets': {'type': 'list'}
}
assets = {
    'sid': {'type': 'integer'},
    'name': {'type': 'string'},
    'description': {'type': 'string'}
}
scans = {
    'sid': {'type': 'integer'},
    'requested_by': {'type': 'integer'},
    'started_at': {'type': 'datetime'},
    'finished_at': {'type': 'datetime'},
    'name': {'type': 'string'},
    'status': {'type': 'string'},
    'scanners': {'type': 'list'},
    'assets_scanned': {'type': 'list'},
    'severity_counts': {'type': 'dict'}

}
users = {
    'sid': {'type': 'integer'},
    'username': {'type': 'string'},
    'email': {'type': 'string'},
    'first_name': {'type': 'string'},
    'last_name': {'type': 'string'}
}
DOMAIN = {
    'assets': {
        'additional_lookup': {'field': 'sid'},
        'schema': assets
    },
    'scans': {
        'additional_lookup': {'field': 'sid'},
        'schema': scans
    },
    'users': {
        'additional_lookup': {'field': 'sid'},
        'schema': users
    },
    'vulnerabilities': {
        'item_title': 'Vulnerability',
        'additional_lookup': {'field': 'sid'},
        'schema': vulnerabilities
    }
}
MONGO_HOST = 'mongodb'
MONGO_PORT = 27017
MONGO_DBNAME = 'test'
ID_FIELD = 'sid'
