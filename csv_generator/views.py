from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Schema
from .forms import SchemaForm, ColumnsFormSet


@login_required
def schemas(request):
    schemas_ = Schema.objects.order_by('-modified')
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
        form = SchemaForm(request.POST)
        formset = ColumnsFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            pass
    else:
        form = SchemaForm()
        formset = ColumnsFormSet()

    return render(
        request,
        "schema.html",
        {
            "schema": schema_,
            "form": form,
            "formset": formset,
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
