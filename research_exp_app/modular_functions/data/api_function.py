def retrieval_api_funtion(cursor, experiment_id):
    #reteriving  details for experiment
    cursor.execute("""select 
    e.id as experiment_id, e.title as experiment_title, 
    r.name as researcher_name, r.department,
    s.sample_id, s.temperature, s.ph,
    m.time, m.value 
    from experiments e
    join researchers r on e.researcher_id = r.id
    join samples s on s.experiment_id = e.id
    join measurements m on m.sample_id  = s.id 
    where e.id = %s;
    """, (experiment_id,))
    samples = cursor.fetchall()
    #reteriving  details for measurements
    sample1 = samples[0]  #select 1st  sample
    show  = {          
        "researcher_name": sample1[2],
        "department": sample1[3],
        "experiment_title": sample1[1],
        "number_of_observations": 0,
        "observations": {}
    } 
    for sample in samples:
        sample_id = sample[4]
        if sample_id not in show["observations"]:
            show["observations"][sample_id]={
                "conditions" :{
                    "temperature": sample[5],
                    "ph": sample[6]
                },
                "measurements": []
            }
        show["observations"][sample_id]["measurements"].append({
            "time": sample[7],
            "value": sample[8]
        })
    show["number_of_observations"] = len(show["observations"])
    return show