# -*-coding:utf-8-*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.decorators.cache import cache_page

from .forms import *
from .models import *
from employee.filters import EmployeeFilter
from employee.tables import EmployeeList, TransferOrderList, DimissionList, DimissionEmployeeList


@cache_page(60 * 150)
def employee_list(request, content_show='contract'):
    filters = EmployeeFilter(request.GET, queryset=Employee.objects.exclude(
        employee_number__in=Dimission.objects.values_list('employee')))
    table = EmployeeList(filters.qs)
    return render(request, 'employee/employee_list.html',
                  {'table': table, 'filters': filters, 'content_show': content_show})


def employee_detail(request, employee_number, content_type='workexperience'):
    employee = get_object_or_404(Employee, employee_number=employee_number)
    return render(request, 'employee/employ_detail.html',
                  {'employee': employee, 'content_type': content_type})


def employee_resume(request, employee_number, ):
    employee = get_object_or_404(Employee, employee_number=employee_number)
    return render(request, 'employee/resume.html',
                  {'employee': employee,})


def form_change_type(change_content_type):
    if change_content_type == 'basic_information':
        return EmployeeChangeFormBasicInformation
    elif change_content_type == 'avatar':
        return EmployeeChangeFormAvatar
    elif change_content_type == 'contract':
        return EmployeeChangeFormContract
    elif change_content_type == 'remark':
        return EmployeeChangeFormRemark
    elif change_content_type == 'eduction':
        return EmployeeChangeFormEduction
    elif change_content_type == 'workexperience':
        return EmployeeChangeFormWorkExperience
    elif change_content_type == 'relationship':
        return EmployeeChangeFormRelationShip


def form_add_type(change_content_type):
    if change_content_type == 'eduction':
        return EmployeeAddFormEduction
    elif change_content_type == 'workexperience':
        return EmployeeAddFormWorkExperience
    elif change_content_type == 'relationship':
        return EmployeAddFormRelationShip
    elif change_content_type == 'remark':
        return EmployeeAddFormRemark
    elif change_content_type == 'contract':
        return EmployeeAddFormContract


def content_type(employee_number, change_content_type, content_id=1):
    employee = get_object_or_404(Employee, employee_number=employee_number)
    if change_content_type == 'basic_information':
        return employee
    elif change_content_type == 'avatar':
        return employee
    elif change_content_type == 'contract':
        return employee.contracts.get(id=content_id)
    elif change_content_type == 'remark':
        return employee.remarks
    elif change_content_type == 'eduction':
        return employee.eductions.get(id=content_id)
    elif change_content_type == 'workexperience':
        return employee.work_experiences.get(id=content_id)
    elif change_content_type == 'relationship':
        return employee.relationships.get(id=content_id)


def employee_content_change(request, employee_number, change_content_type, content_id=1):
    employee = get_object_or_404(Employee, employee_number=employee_number)
    form = form_change_type(change_content_type)(
        instance=content_type(employee_number, change_content_type, content_id))
    if request.method == 'POST':
        form = form_change_type(change_content_type)(request.POST, request.FILES,
                                                     instance=content_type(employee_number, change_content_type,
                                                                           content_id))
        if form.is_valid():
            form.save()
            print employee_number, change_content_type
            print reverse('EMPLOYEE:EMPLOYEE_DETAIL', args=[employee_number, change_content_type])
            return redirect(reverse('EMPLOYEE:EMPLOYEE_DETAIL', args=[employee_number, change_content_type]))
    return render(request, 'employee/employee_content_change.html',
                  {'employee': employee, 'form': form, 'content_type': change_content_type})


def employee_content_delete_confirm(request, employee_number, change_content_type, content_id=1):
    employee = get_object_or_404(Employee, employee_number=employee_number)

    return render(request, 'employee/employee_content_delete_confirm.html',
                  {'employee': employee, 'content_type': change_content_type, 'content_id': content_id})


def employee_content_delete(request, employee_number, change_content_type, content_id=1):
    content = content_type(employee_number, change_content_type, content_id)
    content.delete()
    return redirect(reverse('EMPLOYEE:EMPLOYEE_DETAIL', args=[employee_number, change_content_type]))


def employee_detail_add(request, employee_number, change_content_type, content_id=1):
    employee = get_object_or_404(Employee, employee_number=employee_number)
    form = form_add_type(change_content_type)(initial={'employee': employee})
    form.fields['employee'].widget.attrs['style'] = 'display:none'
    form.fields['employee'].label = ''
    # instance = content_type(employee_number, change_content_type, content_id)
    if request.method == 'POST':
        form = form_add_type(change_content_type)(request.POST, initial={
            'employee': get_object_or_404(Employee, employee_number=employee_number)})

        if form.is_valid():
            form.save()
            print employee_number, change_content_type
            print reverse('EMPLOYEE:EMPLOYEE_DETAIL', args=[employee_number, change_content_type])
            return redirect(reverse('EMPLOYEE:EMPLOYEE_DETAIL', args=[employee_number, change_content_type]))
    return render(request, 'employee/employee_content_add.html',
                  {'employee': employee, 'form': form, 'content_type': change_content_type})


def transfer_order_add(request, employee_number):
    employee = get_object_or_404(Employee, employee_number=employee_number)
    table = TransferOrderList(TransferOrder.objects.all())
    form = TransferOrderAddForm(
        initial={'employee': employee, 'old_department': employee.department, 'old_job': employee.job})
    form.fields['employee'].widget.attrs['style'] = 'display:none'
    form.fields['employee'].label = ''
    form.fields['old_department'].widget.attrs['style'] = 'display:none'
    form.fields['old_department'].label = ''
    form.fields['old_job'].widget.attrs['style'] = 'display:none'
    form.fields['old_job'].label = ''
    form.fields['confirm'].widget.attrs['style'] = 'display:none'
    form.fields['confirm'].label = ''
    # instance = content_type(employee_number, change_content_type, content_id)
    if request.method == 'POST':
        form = TransferOrderAddForm(request.POST, initial={'employee': employee, 'old_department': employee.department,
                                                           'old_job': employee.job})
        transfer_number = request.POST.get('transfer_number')
        if form.is_valid():
            form.save()
            return redirect(reverse('EMPLOYEE:TRANSFER_DETAIL', args=[transfer_number, ]))
    return render(request, 'employee/transfer_add.html',
                  {'form': form, 'table': table, 'employee': employee})


def transfer_order_list(request):
    table = TransferOrderList(TransferOrder.objects.all())
    return render(request, 'employee/transfer_order_list.html',
                  {'table': table,})


def transfer_order_detail(request, transfer_number):
    transfer_order = get_object_or_404(TransferOrder, transfer_number=transfer_number)
    return render(request, 'employee/transfer_detail.html',
                  {'transfer_order': transfer_order,})


def transfer_order_synchro(request, transfer_number):
    transfer_order = get_object_or_404(TransferOrder, transfer_number=transfer_number)
    print transfer_order.transfer_number
    print TransferOrder.objects.filter(employee=transfer_order.employee).last().transfer_number
    print transfer_order == TransferOrder.objects.filter(employee=transfer_order.employee).last()
    if not transfer_order == TransferOrder.objects.filter(employee=transfer_order.employee).last():
        return render(request, 'employee/transfer_detail.html', {'transfer_order': transfer_order, 'show': True})
    transfer_order.confirm = True
    transfer_order.save()
    employee = get_object_or_404(Employee, employee_number=transfer_order.employee.employee_number)
    employee.department = transfer_order.new_department
    employee.job = transfer_order.new_job
    employee.save()
    workexperience = WorkExperience(employee=employee, department=transfer_order.new_department,
                                    job=transfer_order.new_job, start_date=transfer_order.transfer_date,
                                    transfer_order_number=transfer_order.transfer_number)
    workexperience.save()
    return redirect(reverse('EMPLOYEE:TRANSFER_DETAIL', args=[transfer_number, ]))


def transfer_order_synchro_back(request, transfer_number):
    transfer_order = get_object_or_404(TransferOrder, transfer_number=transfer_number)
    print transfer_order.transfer_number
    print TransferOrder.objects.filter(employee=transfer_order.employee).last().transfer_number
    print transfer_order == TransferOrder.objects.filter(employee=transfer_order.employee).last()
    if not transfer_order == TransferOrder.objects.filter(employee=transfer_order.employee).last():
        return render(request, 'employee/transfer_detail.html', {'transfer_order': transfer_order, 'show': True})
    transfer_order.confirm = False
    transfer_order.save()
    employee = get_object_or_404(Employee, employee_number=transfer_order.employee.employee_number)
    employee.department = transfer_order.old_department
    employee.job = transfer_order.old_job
    employee.save()
    try:
        workexperienct = WorkExperience.objects.get(transfer_order_number=transfer_number)
        workexperienct.delete()
    except:
        pass
    return redirect(reverse('EMPLOYEE:TRANSFER_DETAIL', args=[transfer_number, ]))


def transfer_order_delete(request, transfer_number):
    transfer_order = get_object_or_404(TransferOrder, transfer_number=transfer_number)
    print transfer_order.transfer_number
    print TransferOrder.objects.filter(employee=transfer_order.employee).last().transfer_number
    print transfer_order == TransferOrder.objects.filter(employee=transfer_order.employee).last()
    if not transfer_order == TransferOrder.objects.filter(employee=transfer_order.employee).last():
        return render(request, 'employee/transfer_detail.html', {'transfer_order': transfer_order, 'show': True})
    if transfer_order.confirm:
        return render(request, 'employee/transfer_detail.html', {'transfer_order': transfer_order, 'delete': True})
    transfer_order.delete()
    return redirect(reverse('EMPLOYEE:TRANSFER_LIST', ))


def transfer_order_change(request, transfer_number, ):
    transfer_order = get_object_or_404(TransferOrder, transfer_number=transfer_number)
    if not transfer_order == TransferOrder.objects.filter(employee=transfer_order.employee).last():
        return render(request, 'employee/transfer_detail.html', {'transfer_order': transfer_order, 'show': True})
    if transfer_order.confirm:
        return render(request, 'employee/transfer_detail.html', {'transfer_order': transfer_order, 'synchro': True})
    form = TransferOrderChangeForm(instance=transfer_order)
    if request.method == 'POST':
        form = TransferOrderChangeForm(request.POST, instance=transfer_order)
        if form.is_valid():
            form.save()
            return redirect(reverse('EMPLOYEE:TRANSFER_DETAIL', args=[transfer_number, ]))
    return render(request, 'employee/transfer_detail_change.html',
                  {'transfer_order': transfer_order, 'form': form,})


def transfer_order_doc(request, transfer_number, ):
    transfer_order = get_object_or_404(TransferOrder, transfer_number=transfer_number)
    return render(request, 'employee/transfer_order_doc.html',
                  {'transfer_order': transfer_order, 'today': datetime.datetime.today().date()})


def dimission_list(request):
    table = DimissionList(Dimission.objects.all())
    table2 = DimissionEmployeeList(
        Employee.objects.exclude(employee_number__in=Dimission.objects.values_list('employee')))
    return render(request, 'employee/dimission_list.html',
                  {'table': table, 'table2': table2})


def dimission_add(request, employee_number):
    employee = get_object_or_404(Employee, employee_number=employee_number)
    table = DimissionList(Dimission.objects.all())
    table2 = EmployeeList(Employee.objects.exclude(employee_number__in=Dimission.objects.values_list('employee')))
    form = DimissionAddForm(initial={'employee': employee,})
    form.fields['employee'].widget.attrs['style'] = 'display:none'
    form.fields['employee'].label = ''
    # instance = content_type(employee_number, change_content_type, content_id)
    if request.method == 'POST':
        form = DimissionAddForm(request.POST, initial={'employee': employee,})
        if form.is_valid():
            form.save()
            return redirect(reverse("EMPLOYEE:DIMISSION_LIST"))
    return render(request, 'employee/dimission_add.html',
                  {'form': form, 'table': table, 'table2': table2, 'employee': employee})


def dimission_delete(request, id):
    dimission = get_object_or_404(Dimission, id=id)
    dimission.delete()
    return redirect(reverse('EMPLOYEE:DIMISSION_LIST', ))
