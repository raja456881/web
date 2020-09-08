from django.apps import AppConfig
from django.http import HttpResponse
from web import settings
class CrmConfig(AppConfig):
    name = 'crm'



def pdf_response(draw_funk, file_name, *args, **kwargs):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=\"%s\"" % file_name
    draw_funk(response, *args, **kwargs)
    return response
try:
    from django.utils import importlib
except ImportError:
    import importlib


def header_func(*args, **kwargs):
    inv_module = importlib.import_module(settings.INV_MODULE)
    inv_module.draw_header(*args, **kwargs)


def address_func(*args, **kwargs):
    inv_module = importlib.import_module(settings.INV_MODULE)
    inv_module.draw_address(*args, **kwargs)


def footer_func(*args, **kwargs):
    inv_module = importlib.import_module(settings.INV_MODULE)
    inv_module.draw_footer(*args, **kwargs)


def draw_pdf(*args, **kwargs):
    try:
        inv_module = importlib.import_module(settings.INV_MODULE)
        return inv_module.draw_pdf(*args, **kwargs)
    except:
        return False
