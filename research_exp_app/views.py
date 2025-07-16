
#from django.shortcuts import render
# Create your views here.
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
#from pymongo import cursor

#from project1.research_exp_app.modular_functions.data import insert_experiment
from .models import experiment_collection, postgresql_connection
from research_exp_app.modular_functions.data.insert_researcher import insert_researchers
from research_exp_app.modular_functions.data.insert_experiment import insert_experiments

from research_exp_app.modular_functions.data.insert_sample import insert_samples
from research_exp_app.modular_functions.data.api_function import retrieval_api_funtion
@csrf_exempt

def submit_to_mongo(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        experiment_id = body.get('experiment_id')
        #experiment_collection.create_index("experiment_id")
        experiment_collection.insert_one(body)
        return JsonResponse({"message": "saved to mongodb"})

    else:
        return JsonResponse({"message": "Method not allow"})

        

#def mongo_postgre_experiments(request):
@csrf_exempt
def mongo_postgres(request):
   if request.method == 'GET':
      fetch_data = experiment_collection.find()
      #researcher = fetch_data.get('researcher', [])
      conn = postgresql_connection()   
      cursor = conn.cursor()
      cursor.execute("""
      create index if not exists exp_id_index on experiments (id);
      """)
      #insert_researchers(fetch_data,cursor)
      #insert_experiments(fetch_data, cursor)
      
      insert_samples(fetch_data, cursor)

      conn.commit()   

        
      cursor.close()
      conn.close()
      return JsonResponse({'message': 'sample, measurement, researcher and experiment Data Migrated'})
   else:
      return JsonResponse({'message':'Method not allowed'})


def retrieval_api(request, experiment_id):
    if request.method == 'GET':
        conn = postgresql_connection()
        cursor = conn.cursor()

        show = retrieval_api_funtion(cursor,experiment_id) 
        
        cursor.close()
        conn.close()

        return JsonResponse(show)

