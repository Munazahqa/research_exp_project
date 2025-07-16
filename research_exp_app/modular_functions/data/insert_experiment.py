def insert_experiments(experiment,cursor):
    #insert data in experiments

    experiment_data = [
        ( data['experiment_id'], data['metadata']['title'], data['researcher']['id'], data['metadata']['submitted_at'] )
        for data in experiment
    ]
    if experiment_data:
        cursor.executemany("""
        INSERT INTO experiments (id, title, researcher_id, submitted_at)
        VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;""",
        (experiment_data) 
            
        )    


"""
    for data in experiment:

        experiment_id = data['experiment_id']
        metadata = data ['metadata']
        title = metadata['title']
        researcher_data = data['researcher']
        researcher_id = researcher_data['id']
        submitted_at = metadata['submitted_at']
         
        
        cursor.execute("""
        #INSERT INTO experiments (id, title, researcher_id, submitted_at)
        #VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;""",
        #(experiment_id, title, researcher_id, submitted_at) 
 #)