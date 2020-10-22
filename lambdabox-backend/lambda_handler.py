import json
import os
import shutil

from apig_wsgi import make_lambda_handler
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lambdabox.settings")

wsgi_application = get_wsgi_application()
apig_wsgi_handler = make_lambda_handler(wsgi_application, binary_support=True)


def lambda_handler(event, context):
    if not os.path.exists("/tmp/db.sqlite3"):
        shutil.copy("db.sqlite3", "/tmp/db.sqlite3")
        os.chmod("/tmp/db.sqlite3", 0o777)
    # print(json.dumps(event, indent=2, sort_keys=True))
    response = apig_wsgi_handler(event, context)
    # print(json.dumps(response, indent=2, sort_keys=True))
    return response


if __name__ == "__main__":
    pass
