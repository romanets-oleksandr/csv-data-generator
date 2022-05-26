from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Schema
from .forms import SchemaModelForm, ColumnFormset


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
        schema_form = SchemaModelForm(request.POST)
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

    return render(
        request,
        "view_schema.html",
    )
