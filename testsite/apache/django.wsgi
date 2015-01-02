    import os, sys

    path = '/var/www/testsite'

    if  path  not in sys.path:

        sys.path.insert(0, '/var/www/testsite')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testsite.settings')

    from django.core.handlers.wsgi import WSGIHandler

    application = WSGIHandler()
