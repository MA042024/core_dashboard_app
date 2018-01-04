"""
Url router for the administration site
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required

from views.admin import views as admin_views
from views.common import views as common_views
from core_dashboard_app import constants as dashboard_constants

admin_urls = [
    # Admin
    url(r'^records$', staff_member_required(common_views.DashboardRecords.as_view(
        administration=True,
        template=dashboard_constants.ADMIN_DASHBOARD_TEMPLATE)),
        name='core_dashboard_records'),
    url(r'^forms$', admin_views.dashboard_forms, name='core_dashboard_forms'),
    url(r'^dashboard-templates$', admin_views.dashboard_templates, name='core_dashboard_templates'),
    url(r'^dashboard-types$', admin_views.dashboard_types, name='core_dashboard_types'),
    url(r'^files$', admin_views.dashboard_files, name='core_dashboard_files'),
    url(r'^workspaces$', admin_views.dashboard_workspaces, name='core_dashboard_workspaces'),
    url(r'^workspace-list-records/(?P<workspace_id>\w+)$', admin_views.dashboard_workspace_records,
        name='core_dashboard_workspace_list_data')
]


urls = admin.site.get_urls()
admin.site.get_urls = lambda: admin_urls + urls
