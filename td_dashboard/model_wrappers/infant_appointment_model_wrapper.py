from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from edc_subject_dashboard import AppointmentModelWrapper as BaseAppointmentModelWrapper

from .infant_visit_model_wrapper import InfantVisitModelWrapper


class InfantAppointmentModelWrapper(BaseAppointmentModelWrapper):

    dashboard_url_name = settings.DASHBOARD_URL_NAMES.get(
        'infant_subject_dashboard_url')
    next_url_name = settings.DASHBOARD_URL_NAMES.get('infant_subject_dashboard_url')
    next_url_attrs = ['subject_identifier']
    querystring_attrs = ['subject_identifier', 'reason']
    unscheduled_appointment_url_name = 'edc_appointment:unscheduled_appointment_url'
    visit_model_wrapper_cls = InfantVisitModelWrapper

    @property
    def wrapped_visit(self):
        """Returns a wrapped persistent or non-persistent visit instance.
        """
        try:
            model_obj = self.object.infantvisit
        except ObjectDoesNotExist:
            visit_model = django_apps.get_model(
                self.visit_model_wrapper_cls.model)
            model_obj = visit_model(
                appointment=self.object,
                subject_identifier=self.subject_identifier,
                reason=self.object.appt_reason)
        return self.visit_model_wrapper_cls(model_obj=model_obj)
