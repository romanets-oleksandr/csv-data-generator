import io
import csv
from uuid import uuid4

from django.core.files.base import ContentFile
from celery import shared_task

from .models import Schema, DataSet
from . import data_type


@shared_task
def generate_csv_task(schema_id, records):
    schema = Schema.objects.get(pk=schema_id)

    columns = schema.column_set.order_by('order').all()
    header = [c.name for c in columns]
    generators = [data_type.get_generator(c) for c in columns]

    csv_content = io.BytesIO()
    buffer = io.TextIOWrapper(csv_content, 'utf-8', newline='')
    writer = csv.writer(buffer)
    writer.writerow(header)
    for _ in range(records):
        row = [g.generate_value() for g in generators]
        writer.writerow(row)

    buffer.flush()
    csv_content.seek(0)

    data_set = DataSet(
        schema=schema,
    )
    data_set.csv_file.save(f'Schema-{schema.id}-{uuid4()}.csv', ContentFile(csv_content.read()))
    data_set.save()
    return data_set.csv_file.url
