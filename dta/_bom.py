from dataclasses import dataclass

from ._core import SERVER, VERSION

BOM_ROOT_DIR = '/bom'
BOM_ROOT_URL = f'{SERVER}{VERSION}{BOM_ROOT_DIR}'

BOM_PUT_ERRORS = {
    400: 'Invalid BOM',
    401: 'Unauthorized',
    403: 'Access to the specified project is forbidden',
    404: 'Project not found',
}

def put_bom(project, bom, **kwargs):
    
