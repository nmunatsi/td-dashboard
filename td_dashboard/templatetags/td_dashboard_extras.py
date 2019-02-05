from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('td_dashboard/buttons/screening_button.html')
def screening_button(model_wrapper):
    title = ['Edit subject\' screening form.']
    return dict(
        screening_identifier=model_wrapper.object.screening_identifier,
        href=model_wrapper.href,
        title=' '.join(title))


@register.inclusion_tag('td_dashboard/buttons/eligibility_button.html')
def eligibility_button(subject_screening_model_wrapper):
    comment = []
    obj = subject_screening_model_wrapper.object
    tooltip = None
    if not obj.is_eligible:
        comment = obj.ineligibility.split(',')
    comment = list(set(comment))
    comment.sort()
    return dict(eligible=obj.is_eligible, comment=comment, tooltip=tooltip)


@register.inclusion_tag('td_dashboard/buttons/eligibility_button.html')
def antenatal_enrol_eligibility_button(model_wrapper):
    comment = []
    obj = model_wrapper.antenatal_enrollment
    tooltip = None
    if not obj.is_eligible:
        comment = obj.unenrolled.split(',')
    comment = list(set(comment))
    comment.sort()
    return dict(eligible=obj.is_eligible, comment=comment, tooltip=tooltip)


@register.inclusion_tag('td_dashboard/buttons/consent_version_add_button.html')
def consent_version_button(model_wrapper):
    title = ['Add Consent Version.']
    return dict(
        consent_versioned=model_wrapper.consent_version,
        screening_identifier=model_wrapper.object.screening_identifier,
        add_consent_version_href=model_wrapper.consent_version.href,
        title=' '.join(title))


@register.inclusion_tag('td_dashboard/buttons/consent_button.html')
def consent_button(model_wrapper):
    title = ['Consent subject to participate.']
    consent_version = model_wrapper.consent.version
    return dict(
        screening_identifier=model_wrapper.object.screening_identifier,
        add_consent_href=model_wrapper.consent.href,
        consent_version=consent_version,
        title=' '.join(title))


@register.inclusion_tag('td_dashboard/buttons/specimen_consent_button.html')
def specimen_consent_button(model_wrapper):
    title = ['Add Specimen Consent.']
    return dict(
        subject_identifier=model_wrapper.object.subject_identifier,
        screening_identifier=model_wrapper.object.screening_identifier,
        add_specimen_consent_href=model_wrapper.specimen_consent.href,
        specimen_consented=model_wrapper.specimen_consent,
        title=' '.join(title))


@register.inclusion_tag('td_dashboard/buttons/antenatal_enrollment_button.html')
def antenatal_enrollment_button(model_wrapper):
    title = ['subject antenatal enrollment.']
    return dict(
        subject_identifier=model_wrapper.object.subject_identifier,
        add_anternatal_enrollment_href=model_wrapper.antenatal_enrollment.href,
        antenatal_enrollment_model_obj=model_wrapper.antenatal_enrollment_model_obj,
        screening_identifier=model_wrapper.object.screening_identifier,
        title=' '.join(title),)


@register.inclusion_tag('td_dashboard/buttons/antenatal_visit_membership_button.html')
def antenatal_visit_membership_button(model_wrapper):
    title = ['subject antenatal visit membership.']
    return dict(
        subject_identifier=model_wrapper.object.subject_identifier,
        add_antenatal_visit_membership_href=model_wrapper.antenatal_visit_membership.href,
        antenatal_visit_membership_model_obj=model_wrapper.antenatal_visit_membership_model_obj,
        title=' '.join(title),)


@register.inclusion_tag('td_dashboard/buttons/maternal_labour_del_button.html')
def maternal_labour_del_button(model_wrapper):
    title = ['subject maternal labour del.']
    return dict(
        subject_identifier=model_wrapper.object.subject_identifier,
        add_maternal_labour_del_href=model_wrapper.maternal_labour_del.href,
        maternal_labour_del_model_obj=model_wrapper.maternal_labour_del_model_obj,
        title=' '.join(title),)


@register.inclusion_tag('td_dashboard/buttons/dashboard_button.html')
def dashboard_button(model_wrapper):
    subject_dashboard_url = settings.DASHBOARD_URL_NAMES.get(
        'subject_dashboard_url')
    return dict(
        subject_dashboard_url=subject_dashboard_url,
        subject_identifier=model_wrapper.subject_identifier)


@register.inclusion_tag('td_dashboard/buttons/infant_birth_button.html')
def infant_birth_button(infant_birth_values):
    title = ['infant birth.']
    return dict(
        subject_identifier=infant_birth_values.subject_identifier,
        add_infant_birth_href=infant_birth_values.infant_birth.href,
        infant_birth_model_obj=infant_birth_values.infant_birth_obj,
        title=' '.join(title),)


@register.inclusion_tag('td_dashboard/buttons/infant_dashboard_button.html')
def infant_dashboard_button(model_wrapper):
    infant_subject_dashboard_url = settings.DASHBOARD_URL_NAMES.get(
        'infant_subject_dashboard_url')
    return dict(
        subject_dashboard_url=infant_subject_dashboard_url,
        subject_identifier=model_wrapper.subject_identifier)
