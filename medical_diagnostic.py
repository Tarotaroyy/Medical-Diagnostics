
def get_key1(item):
    """
    Args:
        A tuple of 2 objects, where the second is an integer
    returns:
        The value of the second member of the tuple, 
        plus a value between 0 and 0.01 obtained from the first
        member of the tuple. This second term is only useful
        to break ties in a deterministic manner. This is a detail
        you can afford to ignore.
    """
    return item[1] + item[0] / 100000000000


def symptom_similarity(symptomsA, symptomsB):
    """
    Compute symptom similiarity between patients A and B.
    
    Args:
        symptomsA: a tuple (present, absent) for patient A
                   where present is a set of symptoms present
                   and absent is a set of symptoms absent
        symptomsB: Same format as above but for patient B
    
    Returns:
        (present_present + absent_absent - present_absent - absent_present)
        
        where present_present is the number of symptoms present in both patients,
        absent_absent is the number of symptoms absent in both patients,
        present_absent is the number of symptoms present in patientA and absent          
        in patientB,
        absent_present is the number of symptoms absent in patientA and present         
        in patientB
    """
    
    presentA= set(symptomsA[0])
    absentA = set(symptomsA[1])
    presentB =set(symptomsB[0])
    absentB = set(symptomsB[1])
    
    present_present= len(presentA.intersection(presentB))
    absent_absent = len(absentA.intersection(absentB))
    present_absent = len(presentA.intersection(absentB))
    absent_present = len(presentB.intersection(absentA))
    
    returns = present_present + absent_absent - present_absent - absent_present
    return(returns)
    
def similarity_to_patients(my_symptoms, all_patients):
    """
    Args:
        my_symptoms: tuple of symptoms present and absent
        all_patients: dictionary of patients IDs (key) and associated tuple of
                      present and absent symptoms
    Returns:
        List of tuples. Each tuple is of the form: (patientID, similarity), 
        with one tuple per patient in all_patients. 
        For each patient in all_patients, similarity is the symptom similarity 
        between my_symptoms and the patient’s symptoms. The list should be 
        sorted in decreasing order of similarity.
    """
    SIM = []
    all_patient_IDs = all_patients.keys()
    
    for patientID in all_patient_IDs:
        similarity = symptom_similarity(my_symptoms,all_patients[patientID] )
        
        SIM.append((patientID,similarity))
    
    SIM.sort(key=get_key1, reverse = True)
    
    return SIM



def most_similar_patients(my_symptoms, all_patients, n_top):
    """
    Args:
        my_symptoms: tuple of a set of symptoms present and absent
        all_patients: dictionary of patients IDs (key) and associated tuple of
                      present and absent symptoms
        n_top: Maximum number of patients to return
    Returns:
        The set of up to n_top patient IDs from all_patients 
        with the highest similarity to my_symptoms
    """
    similarity_with_ID = similarity_to_patients(my_symptoms, all_patients)
    s = set()
    for n in range(0,n_top+1,1):
        s.add(similarity_with_ID[n-1][0])
        if n ==0:
            s=set()
    return s

def count_diagnostics(patient_set, diagnostic_by_patient):
    """
    Args:
        patient_set: A set of patient IDs
        diagnostic_by_patient: A dictionary with key = patient_ID
                               and values = diseases
    Returns:
        A dictionary with keys = diagnostic and 
        values = fraction of patients in patient_set with that diagnostic
    """
    
    diagnostic = []
    value = []
    
    for patientID in patient_set:
        diseases = diagnostic_by_patient[patientID]
        diagnostic.append(diseases)
        
    diagnostic_count = {i:diagnostic.count(i) for i in diagnostic}
    for x  in diagnostic_count.items():
        key = x[0]
        valu=x[1]
        
        value.append((key,valu/len(patient_set)))
    return dict(value)
    
    
def diagnostics_from_symptoms(my_symptoms, all_patients_symptoms,
                              all_patients_diagnostics, n_top):
    """
    Args:
        my_symptoms: tuple of symptoms present and absent
        all_patients_symptoms:
            dictionary of patients IDs (key) and associated symptoms
        all_patients_diagnostics:
            dictionary of patients IDs (key) and associated diagnostic
        n_top: Number of most similar patients to consider.
    Returns:
        A dictionary with keys = diagnostic and 
            values = fraction of the n_top most similar patients
                     with that diagnostic
    """
    
    
    
def read_data(filename):
    """
    args:
        filename: Name of file containing medical data
    Returns:
        Tuple of a dictionary of symptoms and a dictionary of diagnostics
    """

    lines = open(filename).read().splitlines()  # Do not remove this line
    # print(lines)
    
    # lines is a list of strings containing lines from the file.
    # Write code below that uses lines:
    #   1. Create two dictionaries: one for symptoms and other for diagnostic 
    #   2. Each group of 4 lines represent details for a patient
    #      - Update the dictionaries with the patient's details



def my_test():
    """ This function is used to test the other functions.
        Its expected output is contained in the file my_test_output.txt
        This function will not be graded. We provided it to let you make sure
        that your own functions work properly.
    """

    # pretty print, useful to print nested list, dict, etc.
    from pprint import pprint

    # A small dictionary of patient's symptoms
    all_patients_symptoms = {
        56374: ({"headache", "fever"}, {"coughing", "runny_nose", "sneezing"}),
        45437: ({"coughing", "runny_nose"}, {"headache", "fever"}),
        16372: ({"coughing", "sore_throat"}, {"fever"}),
        54324: ({"vomiting", "coughing", "stomach_pain"}, {"fever"}),
        35249: ({"sore_throat", "coughing",
                 "fever"}, {"stomach_pain", "runny_nose"}),
        44274: ({"fever", "headache"}, {
            "stomach_pain",
            "runny_nose",
            "sore_throat",
            "coughing",
        }),
        74821: ({"vomiting", "fever"}, {"headache"}),
        94231:
        ({"stomach_pain", "fever", "sore_throat", "coughing",
          "headache"}, {"vomiting"}),
    }

    # A small dictionary of patient's diagnostics
    all_patients_diagnostics = {
        45437: "cold",
        56374: "meningitis",
        54324: "food_poisoning",
        16372: "cold",
        35249: "pharyngitis",
        44274: "meningitis",
        74821: "food_poisoning",
        94231: "unknown"
    }

    # Three test patients
    yang = ({"coughing", "runny_nose", "sneezing"}, {"headache", "fever"})
    maria = ({"coughing", "fever", "sore_throat", "sneezing"}, {"muscle_pain"})
    jaspal = ({"headache"}, {"sneezing"})

    ### Testing the symptom_similarity function ###
    print()
    print("*" * 20 + " symptom_similarity " + "*" * 20)

    sim = symptom_similarity(yang, maria)
    print("The similarity between Yang and Maria is", sim)

    sim = symptom_similarity(yang, jaspal)
    print("The similarity between Yang and Jaspal is", sim)

    sim = symptom_similarity(maria, jaspal)
    print("The similarity between Maria and Jaspal is", sim)

    ### Testing the similarity_to_patients function ###
    print()
    print("*" * 20 + " similarity_to_patients " + "*" * 20)

    sim_list = similarity_to_patients(yang, all_patients_symptoms)
    print("similarity list for Yang is")
    pprint(sim_list)

    sim_list = similarity_to_patients(maria, all_patients_symptoms)
    print("Similarity list for Maria is")
    pprint(sim_list)

    sim_list = similarity_to_patients(jaspal, all_patients_symptoms)
    print("Similarity list for Jaspal is")
    pprint(sim_list)

    ### Testing the most_similar_patients function ###
    print()
    print("*" * 20 + " most_similar_patients " + "*" * 20)

    best_matches = most_similar_patients(yang, all_patients_symptoms, 4)
    print("Yang's best matches:")
    pprint(best_matches)

    best_matches = most_similar_patients(maria, all_patients_symptoms, 4)
    print("Maria's best matches:")
    pprint(best_matches)

    best_matches = most_similar_patients(jaspal, all_patients_symptoms, 4)
    print("Jaspal's best matches:")
    pprint(best_matches)

    ### Testing the count_diagnostics function ###
    print()
    print("*" * 20 + " count_diagnostics " + "*" * 20)

    diagnostics = count_diagnostics({16372, 45437, 54324},
                                    all_patients_diagnostics)
    print("Diagnostics for Yang:")
    pprint(diagnostics)

    diagnostics = count_diagnostics({35249, 16372, 74821, 94231},
                                    all_patients_diagnostics)
    print("Diagnostics for Maria:")
    pprint(diagnostics)

    diagnostics = count_diagnostics({44274, 56374}, all_patients_diagnostics)
    print("Diagnostics for Jaspal:")
    pprint(diagnostics)

    ### Testing the diagnostics_from_symptoms function ###
    print()
    print("*" * 20 + " diagnostics_from_symptoms " + "*" * 20)

    diagnostics = diagnostics_from_symptoms(yang, all_patients_symptoms,
                                            all_patients_diagnostics, 4)
    print("Diagnostics for Yang:")
    pprint(diagnostics)

    diagnostics = diagnostics_from_symptoms(maria, all_patients_symptoms,
                                            all_patients_diagnostics, 4)
    print("Diagnostics for Maria:")
    pprint(diagnostics)

    diagnostics = diagnostics_from_symptoms(jaspal, all_patients_symptoms,
                                            all_patients_diagnostics, 4)
    print("Diagnostics for Jaspal:")
    pprint(diagnostics)

    ### Reading from file ###
    print()
    print("*" * 20 + " read_data " + "*" * 20)

    all_patients_symptoms, all_patients_diagnostics = read_data(
        'medicalData.txt')
    print("all_patients_symptoms:")
    pprint(all_patients_symptoms)

    print("\nall_patients_diagnostics:")
    pprint(all_patients_diagnostics)


# Do not change anything below
if __name__ == "__main__":
    my_test()

    


