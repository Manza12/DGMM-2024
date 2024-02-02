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
            'y_lim': (0, 12000),
            'name': 'input',
            'fig_size': (6, 4)
        },
        'noise_zoom': {
            'x_lim': (0.8, 0.97),
            'y_lim': (1900, 2500),
            'fig_size': (4, 4)
        },
        'closing': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'sharexy': False,
        },
        'reconstruction_erosion': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'sharexy': False,
        },

        # Noise
        'opening': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'sharexy': False,
        },
        'input_noise': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'sharexy': False,
        },

        # Sinusoids
        'vertical_thin': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'sharexy': False,
        },
        'vertical_top_hat': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'fig_size': (8., 2.),
            'sharexy': False,
        },
        'vertical_threshold': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'fig_size': (8., 2.),
            'sharexy': False,
        },
        'horizontal_filtered': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'fig_size': (6., 3.),
            'sharexy': False,
        },

        'lines_sinusoids': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
        },
        'input_sinusoids': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
        },

        # Transients
        'horizontal_thin': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'sharexy': False,
        },
        'horizontal_top_hat': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'fig_size': (5., 4.),
            'sharexy': False,
        },
        'horizontal_threshold': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'fig_size': (5., 4.),
            'sharexy': False,
        },
        'vertical_filtered': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'fig_size': (6., 3.),
            'sharexy': False,
        },

        'lines_transient': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
        },
        'input_transient': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
        },

        # Output
        'input_lines': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'fig_size': (4., 4.),
        },
        'input_output': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
            'sharexy': False,
        },
        'input_denoised': {
            'x_lim': (1.1, 1.9),
            'y_lim': (250, 2500),
        },
    }
}

toccata_fuga = {
    'start': 0.,
    'end': 3.5,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {},
}

gong = {}

luis_alonso = {
    'start': 70.,
    'end': 74.0,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {
        'input': {},
        'input_noise': {},
        'input_sinusoids': {},
        'input_lines': {
            'name': 'input_lines',
            'x_lim': (1., 2.),
            'y_lim': (0, 5000),
            'fig_size': (4., 4.),
        },
    },
}

flute_bach = {
    'start': 0.,
    'end': 4.2,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {},
}

partita_b_minor = {
    'start': 813.8,
    'end': 818.2,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {},
}

violin_vibrato = {
    'start': 0.,
    'end': 2.,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {
        'input_lines': {
            'x_lim': (1.1, 1.9),
            'y_lim': (700, 3000),
            'fig_size': (4., 4.),
            'vertical': False,
            'name': 'input_lines',
        },
    },
}

marimba = {
    'start': 0.,
    'end': 4.,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {},
}

piano = {
    'start': 0.,
    'end': 4.,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {
        'input_lines': {
            'x_lim': (0.4, 0.8),
            'y_lim': (0, 5000),
            'fig_size': (4., 4.),
            # 'vertical': False,
            'name': 'input_lines',
        },
        'input_output': {
            'x_lim': (0.4, 0.8),
            'y_lim': (0, 5000),
            'fig_size': (8., 4.),
            'sharexy': True,
            'name': 'input_output'
        },
        'input_transient': {
            'x_lim': (0.4, 0.8),
            'y_lim': (0, 5000),
            'fig_size': (8., 4.),
            'sharexy': True,
            'name': 'input_output'
        }
    },
}

woodblock = {
    'start': 0.,
    'end': 4.,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {},
}

flute = {
    'start': 0.,
    'end': 4.,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {
        'input_lines': {
            'x_lim': (0., 1.5),
            'y_lim': (0, 4000),
            'fig_size': (4., 4.),
            # 'vertical': False,
            'name': 'input_lines',
        },
        'input_noise': {
            'name': 'input_noise'
        },
    },
}

trombone = {
    'start': 0.,
    'end': 4.,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {
        'input_lines': {
            # 'x_lim': (0., 1.5),
            # 'y_lim': (0, 4000),
            'fig_size': (4., 4.),
            'vertical': False,
            'name': 'input_lines',
        },
    },
}

snap = {
    'start': 0.,
    'end': 0.5,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {
        'input_lines': {
            # 'x_lim': (0., 1.5),
            # 'y_lim': (0, 4000),
            'fig_size': (4., 4.),
            # 'vertical': False,
            'name': 'input_lines',
        },

    },
}

triangle = {
    'start': 0.,
    'end': 1.,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {
        'input_lines': {
            # 'x_lim': (0., 1.5),
            # 'y_lim': (0, 4000),
            'fig_size': (4., 4.),
            # 'vertical': False,
            'name': 'input_lines',
        },

    },
}

guiro = {
    'start': 0.,
    'end': 1.,
    'parameters': {
        'closing_time_width': 0.025,
        'closing_frequency_width': 75,
    },
    'plot': {
        'input_lines': {
            'x_lim': (0.3, 1.),
            'y_lim': (0, 4000),
            'fig_size': (4., 4.),
            # 'vertical': False,
            'name': 'input_lines',
        },
        'input_noise': {
            'name': 'input_noise'
        },
        'input_output': {
            'name': 'input_output'
        },
    },
}
