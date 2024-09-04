import os
import django
from django.core.management import call_command
from django.apps import apps
from django.db import connection
import tempfile
import re
from collections import defaultdict
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_system.settings")
django.setup()

def get_model_fields(model):
    return {f.name: type(f).__name__ for f in model._meta.fields}

def get_db_table_name(model):
    return model._meta.db_table

def get_db_fields():
    with tempfile.NamedTemporaryFile(mode='w+') as tmp:
        call_command('inspectdb', stdout=tmp)
        tmp.seek(0)
        content = tmp.read()
    
    db_models = {}
    current_model = None
    class_pattern = re.compile(r'class\s+(\w+)\(')
    field_pattern = re.compile(r'(\w+)\s*=\s*models\.(\w+)')
    db_table_pattern = re.compile(r"db_table\s*=\s*['\"](.+?)['\"]")

    for line in content.split('\n'):
        class_match = class_pattern.search(line)
        if class_match:
            current_model = class_match.group(1)
            db_models[current_model] = {'fields': {}, 'db_table': None}
        elif current_model:
            field_match = field_pattern.search(line)
            if field_match:
                field_name, field_type = field_match.groups()
                db_models[current_model]['fields'][field_name] = field_type
            else:
                db_table_match = db_table_pattern.search(line)
                if db_table_match:
                    db_models[current_model]['db_table'] = db_table_match.group(1)

    return db_models

def are_types_equivalent(django_type, db_type):
    text_types = ['CharField', 'TextField', 'EmailField', 'URLField']
    if django_type in text_types and db_type in text_types:
        return True
    
    int_types = ['IntegerField', 'SmallIntegerField', 'BigIntegerField', 'PositiveIntegerField', 'PositiveSmallIntegerField']
    if django_type in int_types and db_type in int_types:
        return True
    
    return django_type == db_type

def are_fields_equivalent(django_field, db_field):
    # Manejar la convención de nombrado de claves foráneas en PostgreSQL
    if django_field.endswith('_id'):
        return django_field == db_field
    else:
        return django_field == db_field or f"{django_field}_id" == db_field

def compare_models():
    django_models = {model.__name__: {'fields': get_model_fields(model), 'db_table': get_db_table_name(model), 'app_label': model._meta.app_label} for model in apps.get_models()}
    db_models = get_db_fields()

    differences = defaultdict(list)

    db_table_to_django_model = {info['db_table']: model_name for model_name, info in django_models.items() if info['db_table']}

    for model_name, info in django_models.items():
        db_table = info['db_table']
        if db_table.lower().startswith(('django_', 'auth_')):
            continue
        if db_table in [data['db_table'] for data in db_models.values() if data['db_table']]:
            db_model_name = next((name for name, data in db_models.items() if data['db_table'] == db_table), None)
            if db_model_name:
                for field_name, field_type in info['fields'].items():
                    db_fields = db_models[db_model_name]['fields']
                    if not any(are_fields_equivalent(field_name, db_field) for db_field in db_fields):
                        differences['missing_in_db'].append((model_name, field_name, info['app_label'], db_table))
                    else:
                        db_field_name = next((db_field for db_field in db_fields if are_fields_equivalent(field_name, db_field)), None)
                        if db_field_name and not are_types_equivalent(field_type, db_fields[db_field_name]):
                            differences['type_mismatch'].append((model_name, field_name, field_type, db_fields[db_field_name], db_table))
                
                for field_name in db_models[db_model_name]['fields']:
                    if not any(are_fields_equivalent(django_field, field_name) for django_field in info['fields']):
                        differences['missing_in_django'].append((model_name, field_name, db_table))
            else:
                differences['missing_in_db'].append((model_name, None, info['app_label'], db_table))
        else:
            differences['missing_in_db'].append((model_name, None, info['app_label'], db_table))

    for db_model_name, info in db_models.items():
        if info['db_table'] and not info['db_table'].lower().startswith(('django_', 'auth_')) and info['db_table'] not in db_table_to_django_model:
            differences['missing_in_django'].append((db_model_name, None, info['db_table']))

    return differences

def print_organized_differences(differences):
    print("\nResumen de discrepancias encontradas:")
    
    if differences['missing_in_db']:
        print("\nObjetos faltantes en la base de datos:")
        for model_name, field_name, app_label, db_table in differences['missing_in_db']:
            if field_name:
                print(f"- Campo '{field_name}' faltante en el modelo '{model_name}' (App: {app_label}, Tabla: {db_table})")
            else:
                print(f"- Modelo '{model_name}' faltante (App: {app_label}, Tabla: {db_table})")
    
    if differences['missing_in_django']:
        print("\nObjetos en la base de datos no presentes en los modelos de Django:")
        for model_name, field_name, db_table in differences['missing_in_django']:
            if field_name:
                print(f"- Campo '{field_name}' en el modelo '{model_name}' existe en la BD pero no en Django (Tabla: {db_table})")
            else:
                print(f"- Modelo '{model_name}' existe en la BD pero no en Django (Tabla: {db_table})")
    
    if differences['type_mismatch']:
        print("\nDiferencias en tipos de datos:")
        for model_name, field_name, django_type, db_type, db_table in differences['type_mismatch']:
            print(f"- Campo '{field_name}' en modelo '{model_name}': tipo '{django_type}' en Django, '{db_type}' en BD (Tabla: {db_table})")

if __name__ == "__main__":
    try:
        differences = compare_models()
        print_organized_differences(differences)
    except Exception as e:
        logging.exception("Se produjo un error durante la comparación de modelos:")
        print(f"Se produjo un error: {str(e)}. Consulta los logs para más detalles.")