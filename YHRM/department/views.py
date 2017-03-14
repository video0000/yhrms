from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

from department.filters import DepartmentFilter
from department.forms import DepartmentAddForm, DepartmentChangeForm
from department.models import Department
from .tables import DepartmentList


# Create your views here.
@login_required
def department_list(request):
    filters = DepartmentFilter(request.GET, queryset=Department.objects.all())
    table = DepartmentList(filters.qs)
    if request.method == 'POST':
        form = DepartmentAddForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.has_key('save_and_reutrn'):
                return render(request, 'department/department_list.html',
                              {'table': table,
                               'filters': filters,
                               'form': form,})
        else:
            return render(request, 'department/department_list.html',
                          {'table': table,
                           'filters': filters,
                           'form': form,})
    else:
        form = DepartmentAddForm()
        return render(request, 'department/department_list.html',
                      {'table': table,
                       'filters': filters,
                       'form': form, })


@login_required
def department_detail(request, department_number):
    department = get_object_or_404(Department, pk=department_number)
    return render(request, "department/department_detail.html",
                  {'department': department,})


#


@login_required
def department_change(request, department_number):
    department = get_object_or_404(Department, pk=department_number)
    form = DepartmentChangeForm(instance=department)
    if request.method == 'POST':
        form = DepartmentChangeForm(request.POST,instance=department)
        if form.is_valid():
            department = form.save()
            return redirect(reverse('DEPARTMENT:DEPARTMENT_DETAIL', args={department_number}))
    return render(request, "department/department_change.html",
                  {'department': department,
                   'form': form})


@login_required
def department_delete(request, department_number):
    department = get_object_or_404(Department, pk=department_number)
    department.delete()
    return redirect(reverse('DEPARTMENT:DEPARTMENT_LIST'))
