from django.conf import settings
from django.urls.conf import path, include
from edc_dashboard import UrlConfig

from .patterns import subject_identifier, screening_identifier, infant_subject_identifier
from .views import (MaternalSubjectListboardView, MaternalSubjectDashboardView,
                    SubjectScreeningListboardView, InfantDashboardView,
                    InfantListBoardView)

app_name = 'td_dashboard'

subject_listboard_url_config = UrlConfig(
    url_name='subject_listboard_url',
    view_class=MaternalSubjectListboardView,
    label='maternal_subject_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)
screening_listboard_url_config = UrlConfig(
    url_name='screening_listboard_url',
    view_class=SubjectScreeningListboardView,
    label='screening_listboard',
    identifier_label='screening_identifier',
    identifier_pattern=screening_identifier)
subject_dashboard_url_config = UrlConfig(
    url_name='subject_dashboard_url',
    view_class=MaternalSubjectDashboardView,
    label='subject_dashboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)

infant_listboard_url_config = UrlConfig(
    url_name='infant_listboard_url',
    view_class=InfantListBoardView,
    label='infant_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=infant_subject_identifier)

infant_subject_dashboard_url_config = UrlConfig(
    url_name='infant_subject_dashboard_url',
    view_class=InfantDashboardView,
    label='infant_subject_dashboard',
    identifier_label='subject_identifier',
    identifier_pattern=infant_subject_identifier)

urlpatterns = []
urlpatterns += subject_listboard_url_config.listboard_urls
urlpatterns += screening_listboard_url_config.listboard_urls
urlpatterns += subject_dashboard_url_config.dashboard_urls
urlpatterns += infant_listboard_url_config.listboard_urls
urlpatterns += infant_subject_dashboard_url_config.dashboard_urls

if settings.APP_NAME == 'td_dashboard':

    from django.views.generic.base import RedirectView
    from edc_base.auth.views import LoginView, LogoutView

    urlpatterns += [
        path('edc_device/', include('edc_device.urls')),
        path('edc_protocol/', include('edc_protocol.urls')),
        path('admininistration/', RedirectView.as_view(url='admin/'),
             name='administration_url'),
        path('login', LoginView.as_view(), name='login_url'),
        path('logout', LogoutView.as_view(
            pattern_name='login_url'), name='logout_url'),
        path(r'', RedirectView.as_view(url='admin/'), name='home_url')]
