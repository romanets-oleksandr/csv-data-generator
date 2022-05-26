from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from celery.result import AsyncResult

from .models import Schema
from .forms import SchemaModelForm, ColumnFormset, DataSetForm
from .tasks import generate_csv_task


@login_required
def schemas(request):
    schemas_ = Schema.objects.order_by('pk')
    return render(
        request,
        "schemas.html",
        {
            "schemas": schemas_
        }
    )


@login_required
def schema(request, schema_id=None):
    schema_ = get_object_or_404(Schema, pk=schema_id) if schema_id else None
    if request.method == 'POST':
        schema_form = SchemaModelForm(request.POST, instance=schema_)
        column_formset = ColumnFormset(request.POST)
        if schema_form.is_valid() and column_formset.is_valid():
            schema_ = schema_form.save()
            for form in column_formset:
                column = form.save(commit=False)
                column.schema = schema_
                column.save()
            return redirect('schemas')
    else:
        schema_form = SchemaModelForm(instance=schema_)
        column_formset = ColumnFormset(queryset=schema_.column_set.all() if schema_ else None)

    return render(
        request,
        "schema.html",
        {
            "schema": schema_,
            "schema_form": schema_form,
            "column_formset": column_formset,
        }
    )


@login_required
def delete_schema(request, schema_id):
    schema_ = get_object_or_404(Schema, pk=schema_id)
    schema_.delete()
    return redirect('schemas')


@login_required
def view_schema(request, schema_id):
    schema_ = get_object_or_404(Schema, pk=schema_id)
    data_sets = schema_.dataset_set.all()
    form = DataSetForm()

    return render(
        request,
        "view_schema.html",
        {
            "schema": schema_,
            "data_sets": data_sets,
            "form": form,
        }
    )


@login_required
def generate_csv(request, schema_id):
    schema_ = get_object_or_404(Schema, pk=schema_id)
    if request.POST:
        form = DataSetForm(request.POST)
        if form.is_valid():
            task = generate_csv_task.delay(schema_.id, form.cleaned_data.get('records'))
            return JsonResponse({"task_id": task.id}, status=202)


@login_required
def get_task_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)
