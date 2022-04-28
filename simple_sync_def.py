simple_transfer_def = {
        'Comment': 'Transfer a file or directory in Globus',
        'StartAt': 'ExampleTransfer',
        'States': {
            'ExampleTransfer': {
                'Comment': 'Transfer a file or directory in Globus',
                'Type': 'Action',
                'ActionUrl': 'https://actions.automate.globus.org/transfer/transfer',
                'Parameters': {
                    'source_endpoint_id.$': '$.example_transfer_source_endpoint_id',
                    'destination_endpoint_id.$': '$.example_transfer_destination_endpoint_id',
                    'transfer_items': [
                        {
                            'source_path.$': '$.example_transfer_source_path',
                            'destination_path.$': '$.example_transfer_destination_path',
                            'recursive.$': '$.example_transfer_recursive',
                        }
                    ]
                },
                'ResultPath': '$.ExampleTransfer',
                'WaitTime': 600,
                'End': True
            },
        }
    }

