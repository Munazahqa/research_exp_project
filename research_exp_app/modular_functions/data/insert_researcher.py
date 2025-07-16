def insert_researchers(researcher,cursor):
    #insert data in researchers

    researcher_data = [
        ( data['researcher']['id'], data['researcher']['name'], data['researcher']['department'] )
        for data in researcher
    ]
    if researcher_data:
        cursor.executemany(
            """
        INSERT INTO researchers (id, name, department)
        VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING;""",
        (researcher_data) 
            
        )


    """
    for data in researcher:

        researcher_data = data['researcher']
        researcher_id = researcher_data['id']
        researcher_name = researcher_data['name']
        researcher_dept = researcher_data['department']
        cursor.execute("""
       # INSERT INTO researchers (id, name, department)
        #VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING;""",
       # (researcher_id, researcher_name, researcher_dept) 
 #)
