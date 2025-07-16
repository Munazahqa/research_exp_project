

from research_exp_app.modular_functions.data.insert_measurement import insert_measurements
def insert_samples(measurement,cursor):
    #insert data in samples
    for data in measurement:
        experiment_id = data['experiment_id']
      
        #if ph < 6.5 or ph > 8.0:
         #       continue  #skip that 

        for sample in data['observations']:
            sample_id = sample['sample_id']
            temperature = sample['conditions']['temperature']
            ph = sample['conditions']['ph']
             
            cursor.execute("""
            INSERT INTO samples(experiment_id, sample_id, temperature, ph)
            VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING returning id;""",
            (experiment_id, sample_id, temperature, ph) 
            )

            m_sample_id = cursor.fetchone()[0]

            measure = [
                (m_sample_id, time_value['time'], time_value['value'])
                for time_value in sample['measurements']]

            if measure:
                cursor.executemany("""
                INSERT INTO measurements(sample_id, time, value)
                VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING;""",measure)
        '''
            for time_value in sample['measurements']:
                time = time_value['time']
                value = time_value['value']
                cursor.execute("""
                INSERT INTO measurements(sample_id, time, value)
                VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING;""", (m_sample_id, time, value))
        
'''



