"""
    Django settings for core_dashboard_app app
"""

from django.conf import settings

if not settings.configured:
    settings.configure()

SERVER_URI = getattr(settings, 'SERVER_URI', "http://localhost")

INSTALLED_APPS = getattr(settings, 'INSTALLED_APPS', [])

menu = {'My Files': 'core_dashboard_files',
        'My Templates': 'core_dashboard_templates',
        'My Records': 'core_dashboard_records',
        'My Profile': 'core_dashboard_profile'}

if 'core_composer_app' in INSTALLED_APPS:
    menu['My Types'] = 'core_dashboard_types'
if 'core_curate_app' in INSTALLED_APPS:
    menu['My Forms'] = 'core_dashboard_forms'
if 'core_workspace_app' in INSTALLED_APPS:
    menu['My Workspaces'] = 'core_dashboard_workspaces'

# Menu
DASHBOARD_MENU = getattr(settings, 'DASHBOARD_MENU', menu)
