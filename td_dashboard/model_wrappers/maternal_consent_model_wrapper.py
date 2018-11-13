from django.conf import settings

from edc_model_wrapper import ModelWrapper


class MaternalConsentModelWrapper(ModelWrapper):

    model = 'td_maternal.subjectconsent'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'maternal_subject_dashboard_url')
    next_url_attrs = ['subject_identifier']
    querystring_attrs = ['screening_identifier']
