anastasia = {
    'start': 8.8,
    'end': 11.8,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {
        # Input
        'input': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'input'
        },
        'closing': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'closing'
        },
        'reconstruction_erosion': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'reconstruction_erosion'
        },
        'erosion': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'erosion'
        },

        # Noise
        'opening': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'opening'
        },
        'input_noise': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'input_noise'
        },

        # Sinusoids
        'vertical_thin': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'vertical_thin'
        },
        'vertical_top_hat': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'vertical_top_hat'
        },
        'vertical_threshold': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'vertical_threshold'
        },
        'horizontal_filtered': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'horizontal_filtered'
        },
        'lines_sinusoids': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'lines_sinusoids'
        },
        'input_sinusoids': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'input_sinusoids'
        },

        # Transients
        'horizontal_thin': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'horizontal_thin',
        },
        'horizontal_top_hat': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'horizontal_top_hat',
        },
        'horizontal_threshold': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'horizontal_threshold',
        },
        'vertical_filtered': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'vertical_filtered',
        },
        'lines_transient': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'lines_transient',
        },
        'input_transient': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'input_transient'
        },

        # Output
        'input_output': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'input_output'
        },
        'input_denoised': {
            'x_lim': (0., 2.),
            'y_lim': (0, 12000),
            'name': 'input_denoised'
        },
    }
}
