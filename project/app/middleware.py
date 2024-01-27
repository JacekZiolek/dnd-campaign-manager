# The _excluded_paths list is used to exclude certain paths from being added to the breadcrumbs.
# This is hopefully a temporary solution.
# Reaserch is needed on how htmx iteracts with Django and to find a better solution.
from django.utils.deprecation import MiddlewareMixin

_excluded_paths = [
    'player',
    'dungeon_master',
    'profile_pictures',
    'favicon.ico',
    'admin'
]


class BreadcrumbsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        '''This middleware adds breadcrumbs to the session.
        The breadcrumbs are used to display a breadcrumb navigation bar.

        :param request: the request object
        '''
        path = request.path
        crumb_name = path.split('/')[-2].replace('_', ' ').capitalize()
        crumb = {
            'url': path,
            'name': crumb_name if crumb_name else 'Home'
        }
        breadcrumbs = request.session.get('breadcrumbs', [])
        if path == '/':
            breadcrumbs = [crumb]
        elif crumb != breadcrumbs[-1]:
            breadcrumbs.append(crumb)

        for ep in _excluded_paths:
            if ep in path:
                breadcrumbs.remove(crumb)

        if len(breadcrumbs) > 10:
            breadcrumbs = [breadcrumbs[0]] + breadcrumbs[-9:]

        request.session['breadcrumbs'] = breadcrumbs
