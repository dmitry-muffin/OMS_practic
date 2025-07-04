from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from openpyxl import load_workbook
# Create your views here.

def upload_file(request):
    first_row = ""
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        fs = FileSystemStorage()
        filename = fs.save(excel_file.name, excel_file)
        file_path = fs.path(filename)

        # читаем первую строку
        wb = load_workbook(file_path, read_only=True)
        ws = wb.active
        first_row = [cell.value for cell in next(ws.iter_rows(min_row=1, max_row=1))]
        first_row = ', '.join(map(str, first_row))
        wb.close()

    return render(request, 'upload.html', {'first_row': first_row})