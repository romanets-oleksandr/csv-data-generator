from django.urls import path
from .views import schemas, schema, view_schema, delete_schema


urlpatterns = [
    path('', schemas, name="schemas"),
    path('schema/', schema, name="schema"),
    path('schema/<int:schema_id>/', schema, name="schema"),
    path('schema/<int:schema_id>/view', view_schema, name="view_schema"),
    path('schema/<int:schema_id>/delete', delete_schema, name="delete_schema"),
]
