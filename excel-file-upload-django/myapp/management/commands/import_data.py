from django.core.management.base import BaseCommand
import pandas as pd
from myapp.models import Data

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file',type=str,help='Add bulk data')
    
    def handle(self,*args,**kwargs):
        my_file=kwargs['file']
        excel_file=pd.ExcelFile(my_file)
        all_sheets=excel_file.sheet_names
        df=pd.read_excel(my_file,index_col=None,sheet_name='Sheet1')
        data_index=df.columns.get_loc('application')
        for row in df.values:
            employee_qs=Data.objects.create(application=row[data_index],valuation=row[data_index+1],budget=row[data_index+2])