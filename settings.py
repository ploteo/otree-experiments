from os import environ

SESSION_CONFIGS = [
    # dict(
    #     name='LIVE',
    #     app_sequence=['live_pages'],
    #     num_demo_participants=2
    # ),
    # dict(
    #     name='STYLE',
    #     app_sequence=['styles'],
    #     num_demo_participants=2
    # ),
    dict(name='hello_world',
         app_sequence=['hello_world'],
         num_demo_participants=2     
    ),
     dict(
         name='TG',
         app_sequence=['TG'],
         num_demo_participants=2,
         treatment = "method"# play= sequential; method= strategy method
     ),
    # dict(
    #     name='PGG',
    #     app_sequence=['PGG'],
    #     num_demo_participants=3,
    # ),
    # dict(
    #     name='groups_roles',
    #     app_sequence=['groups_roles'],
    #     num_demo_participants=4,
    # ),
    dict(
        name='MPL',
        app_sequence=['MPL'],
        num_demo_participants=4,
    ),
    #     dict(
    #     name='PGG',
    #     app_sequence=['PGG'],
    #     num_demo_participants=3,
    # ),
    # dict(
    #     name='sliders',
    #     app_sequence=['sliders_new'],
    #     num_demo_participants=3,
    # ),
    #     dict(
    #     name='MPL',
    #     app_sequence=['MPL'],
    #     num_demo_participants=3,
    # ),
    # dict(
    #     name='Inputs',
    #     app_sequence=['inputs'],
    #     num_demo_participants=1,
    # ),
    # dict(
    #     name='HelloWorld',
    #     app_sequence=['hello_world'],
    #     num_demo_participants=3,
    # ),
    #     dict(
    #     name='my_first_survey',
    #     app_sequence=['my_first_survey'],
    #     num_demo_participants=3,
    # ),  
    #     dict(
    #     name='inputs',
    #     app_sequence=['inputs'],
    #     num_demo_participants=3,
    # ),  
    #     dict(
    #     name='hello_world',
    #     app_sequence=['hello_world'],
    #     num_demo_participants=3,
    # ),
    # dict(
    #     name='beauty_contest',
    #     app_sequence=['beauty_contest'],
    #     num_demo_participants=3,
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['expiry','counted','target','defaults']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'Tokens'

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3117236745767'
