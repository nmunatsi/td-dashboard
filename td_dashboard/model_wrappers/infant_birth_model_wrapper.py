from django.conf import settings

from edc_model_wrapper import ModelWrapper


class InfantBirthModelWrapper(ModelWrapper):

    model = 'td_infant.infantbirth'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'infant_subject_dashboard_url')
    next_url_attrs = ['subject_identifier']
    querystring_attrs = ['subject_identifier']
