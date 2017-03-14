from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from employee.models import Employee, Dimission
from leave.forms import LeaveAddForm, LeaveChangeForm
from leave.tables import LeaveEmployeeList, LeaveList
from .models import Leave
import datetime


def leave_list(request):
    table = LeaveEmployeeList(Employee.objects.exclude(employee_number__in=Dimission.objects.values_list('employee')))
    table2 = LeaveList(Leave.objects.filter(start_date__year=datetime.datetime.today().year))
    return render(request, 'leave/leave_list.html',
                  {'table': table, 'table2': table2})


def leave_add(request, employee_number):
    employee = get_object_or_404(Employee, employee_number=employee_number)
    table = LeaveEmployeeList(Employee.objects.exclude(employee_number__in=Dimission.objects.values_list('employee')))
    table2 = LeaveList(Leave.objects.filter(start_date__year=datetime.datetime.today().year))
    form = LeaveAddForm(initial={'employee': employee,})
    form.fields['employee'].widget.attrs['style'] = 'display:none'
    form.fields['employee'].label = ''
    # instance = content_type(employee_number, change_content_type, content_id)
    if request.method == 'POST':
        form = LeaveAddForm(request.POST, initial={'employee': employee,})
        if form.is_valid():
            form.save()
            return redirect(reverse("LEAVE:LEAVE_LIST"))
    return render(request, 'leave/leave_add.html',
                  {'form': form, 'table': table, 'table2': table2, 'employee': employee})


def leave_delete(request, id):
    leave = get_object_or_404(Leave, id=id)
    leave.delete()
    return redirect(reverse('LEAVE:LEAVE_LIST', ))


def leave_change(request, id):
    leave = get_object_or_404(Leave, id=id)
    form = LeaveChangeForm(instance=leave)
    # form.fields['employee'].widget.attrs['style'] = 'display:none'
    # form.fields['employee'].label = ''
    # # form.fields['id'].widget.attrs['style'] = 'display:none'
    # # form.fields['id'].label = ''
    table = LeaveEmployeeList(Employee.objects.exclude(employee_number__in=Dimission.objects.values_list('employee')))
    table2 = LeaveList(Leave.objects.filter(start_date__year=datetime.datetime.today().year))
    if request.method == 'POST':
        form = LeaveChangeForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            return redirect(reverse('LEAVE:LEAVE_LIST', ))
    return render(request, 'leave/leave_change.html',
                  {'employee': leave.employee, 'form': form, 'table': table, 'table2': table2,'leave':leave})
