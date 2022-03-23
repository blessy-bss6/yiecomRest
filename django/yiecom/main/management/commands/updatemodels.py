import email
from django.core.management.base import BaseCommand
import pandas as pd
from main.models import * 

# import dateutil.parser


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df=pd.read_csv('gold.csv')
        for  user_login,password,user_nicename,email,user_url, user_registered, user_activationKey,user_status, displayname in zip(df.user_login,df.user_pass,df.user_nicename,df.user_email,df.user_url,df.user_registered , df.user_activation_key,df.user_status,df.display_name):
         print(user_registered) 
        #  print(dateutil.parser.parse(user_registered))
        #  print(type(dateutil.parser.parse(user_registered)))
        #    tz = get_current_timezone()
        #    dt = tz.localize(datetime.strptime(user_registered, '%m/%d/%Y'))
        #    print(tz)
        #    models=CustomUser(user_login=user_login, password=password , user_nicename=user_nicename ,email= email, user_url=user_url , user_registered=user_registered, user_activationKey=user_activationKey ,user_status=user_status , displayname=displayname)
        #    models.save()