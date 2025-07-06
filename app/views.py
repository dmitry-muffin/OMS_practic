import openpyxl
import re
from django.shortcuts import render

from TatOMS import settings


def parse_houses(houses_str):
    """Разбивает строку домов по запятой и точке с запятой, убирает пробелы."""
    if not houses_str:
        return []
    return [h.strip() for h in re.split('[,;]', houses_str) if h.strip()]

def upload_file(request):
    addresses = []
    filename = None

    if request.method == "POST" and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        filename = excel_file.name
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active

        # Пропускаем заголовок (первая строка)
        for row in sheet.iter_rows(min_row=2, values_only=True):
            group = int(row[0]) if row[0] else None
            city = row[1].strip() if row[1] else ''
            street = row[2].strip() if row[2] else ''
            houses_str = row[3] if row[3] else ''

            houses = parse_houses(houses_str)

            # Если есть дома, то создаём отдельные записи для каждого дома
            if houses:
                for house in houses:
                    addresses.append({
                        'group': group,
                        'city': city,
                        'street': street,
                        'house': house
                    })
            else:
                # Если домов нет, передаём улицу без дома (house=None)
                addresses.append({
                    'group': group,
                    'city': city,
                    'street': street,
                    'house': None
                })

    return render(request, 'upload.html', {
        'addresses': addresses,
        'filename': filename,
        'yandex_api_key': settings.YANDEX_MAPS_API_KEY,
    })
