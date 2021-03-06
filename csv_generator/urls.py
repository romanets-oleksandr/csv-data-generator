from django.urls import path
from .views import schemas, schema, view_schema, delete_schema,\
    get_task_status, generate_csv


urlpatterns = [
    path('', schemas, name="schemas"),
    path('schema/', schema, name="schema"),
    path('schema/<int:schema_id>/', schema, name="schema"),

    path('schema/<int:schema_id>/view', view_schema, name="view_schema"),
    path('schema/<int:schema_id>/delete', delete_schema, name="delete_schema"),

    path('generate-csv/<int:schema_id>/', generate_csv, name="generate_csv"),

    path('task-status/', get_task_status, name="get_task_status"),
    path('task-status/<task_id>', get_task_status, name="get_task_status"),
]
