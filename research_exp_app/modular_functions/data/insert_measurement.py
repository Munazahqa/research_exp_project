

def insert_measurements(measurement,cursor):
    #insert data in drivers:
    for data in measurement:

        obervation_data = data['observations']
        for sample in obervation_data:
            sample_id = sample['sample_id']
            for time_value in sample['measurements']:
                time = time_value['time']
                value = time_value['value']

        
        
        cursor.execute("""
        INSERT INTO measurements(sample_id, time, value)
        VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING;""",
        (sample_id, time, value) 
 )