import getpass
import os
from django.shortcuts import render
from django.shortcuts import render, redirect
import openpyxl
import pandas as pd  
from employee.forms import EmployeeForm  
from employee.models import Employee  
#Excel file name
excel_file_name="employee_data.xlsx"


def handle_uploaded_file(f, path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
def storefle(request):
    excel_file = request.FILES["excel_file"]
    
    #make the final directory path
    file_path=os.path.join(getExcelDirectory()+excel_file_name)
        #store the file
    handle_uploaded_file(excel_file,file_path)
        
    return redirect('/show')


def emp(request):  
    if request.method == "POST":  
        # form = EmployeeForm(request.POST)
        try:  
            application=request.POST['application']
            valuation=request.POST['valuation']
            budget=request.POST['budget']  
            new_emp=Employee(application=application,valuation=valuation,budget=budget)
            addEmployee(new_emp)  
            return redirect('/show')
        except Exception:
            pass
         
                  
    
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})


def getExcelDirectory():
    #get the machine user name
    username=getpass.getuser();
    dir_path=os.path.join('C:/Users/{}/Desktop/Excelfile/'.format(username)) 
    
    # create directory if it does not exist
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def fetchEmployeeFromExcel():
    try:
        file_path=os.path.join(getExcelDirectory()+excel_file_name)
    # Load the Excel file
        workbook = openpyxl.load_workbook(file_path)
            
        emp_list=[]
    # Select the first worksheet
        worksheet = workbook.active
        for row in worksheet.iter_rows(min_row=2):
            row_dict = {}
            
            for cell in row:
                row_dict[cell.column_letter] = cell.value   
            emp_id=row_dict['A']
            application=row_dict['B']
            valuation=row_dict['C']
            budget=row_dict['D']
              
            emp_data=Employee(eid=emp_id,application=application,valuation=valuation,budget=budget)
            emp_list.append(emp_data)
        return emp_list
    except Exception:
        return []

def editEmployee(employee:Employee,id:int):
    file_path=os.path.join(getExcelDirectory()+excel_file_name)        
    # open the Excel file and select the sheet
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
            
    # find the row with the matching ID in the first column
    # id_found=False
    for row in sheet.iter_rows(min_row=2, values_only=True):
        print(row)
        if  row[0] == id:
            # update the row with the new data
            row_data = list(row)
            row_data[1]="{}".format(employee.application)
            row_data[2]="{}".format(employee.budget)
            row_data[3]="{}".format(employee.valuation)
            print(row_data)
            for col_idx, cell in enumerate(row_data, start=1):
                print(cell)
                sheet.cell(row=row[0]+1, column=col_idx, value=cell)
                wb.save(file_path)     
            break


def readLastId(file_path):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)

    # Select the worksheet
    worksheet = workbook.active

    # Find the last row in the column
    last_row = worksheet.max_row

    # Read the value of the last cell in the column
    last_cell_value = worksheet.cell(row=last_row, column=1).value
    
    return last_cell_value

def addEmployee(employee:Employee):
      
    #make the final directory path
    file_path=os.path.join(getExcelDirectory()+excel_file_name)
    loadedExcelFile = pd.read_excel(file_path)
            
    #Insert
    last_id=readLastId(file_path)
    #create new row
    new_row={'ID':last_id+1,'APLLICATION':employee.application,'BUDGET':"${}".format(employee.budget),'VALUATION':"${}".format(employee.valuation)}
    #append the new row to data frame
    loadedExcelFile = loadedExcelFile.append(new_row, ignore_index=True)
            
    # save modified Excel file
    loadedExcelFile.to_excel(file_path,index=False)
            
    employee.save()

def getEmployeeById(id):
    file_path=os.path.join(getExcelDirectory()+excel_file_name)
    # Load the Excel file
    workbook = openpyxl.load_workbook(file_path)
            
    # Select the first worksheet
    worksheet = workbook.active
                
    # Loop through the rows and search for a matching ID
    for row in worksheet.iter_rows(min_row=2):
        if  row[0].value == id:
            # If a matching ID is found, create a dictionary representing the row
            row_dict = {}
                        
            for cell in row:
                row_dict[cell.column_letter] = cell.value
            emp_id=row_dict['A']
            application=row_dict['B']
            valuation=row_dict['C']
            budget=row_dict['D']  
            emp_data=Employee(eid=emp_id,application=application,valuation=valuation,budget=budget)
            return emp_data

def show(request):     
    employees = fetchEmployeeFromExcel()  
    # employees = Employee.objects.all()
    if len(employees)==0:
        return render(request,"upload.html")   
    else:
        return render(request,"show.html",{'employees':employees})  


def edit(request, id):  
    # employee = Employee.objects.get(id=id)  
    employee= getEmployeeById(id)
    return render(request,'edit.html', {'employee':employee}) 



def update(request, id): 
    # employee= getEmployeeById(id)
    # form = EmployeeForm(request.POST, instance = employee)  
    # if form.is_valid():  
    #     form.save()  
    try:
        application=request.POST['application']
        valuation=request.POST['valuation']
        budget=request.POST['budget'] 
        updatedData=Employee(eid=id,application=application,valuation=valuation,budget=budget)
        editEmployee(updatedData,id)
        return redirect("/show")  
    except Exception: 
        # return render(request, 'edit.html', {'employee': employee}) 
        return redirect("/show")  



def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")