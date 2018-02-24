"""All processing functions for rendering views"""

from datetime import datetime

from bias_tracker.models import Descriptor
from bias_tracker.models import Incident
from bias_tracker.models import Person


def grab_subject_options():
    """grab incident subject choices for page"""
    return Person.objects.all()


def grab_descriptor_options():
    """grab incident descriptor choices for page"""
    return Descriptor.objects.all()


def grab_type_options():
    """grab incident type choices for page"""
    incident_types = Incident.TYPE_CHOICES
    # is this necessary?
    incident_type_choices = create_incident_type_list(incident_types)
    return incident_type_choices


def grab_incidents_list(author_id):
    """return all Incidents for author"""
    return Incident.objects.filter(author__exact=author_id)


def grab_incident(incident_id):
    """return single selected incident"""
    return Incident.objects.get(id__exact=incident_id)


def create_edit_incident_page_fill(incident_id):
    """create dictionary with all necessary items for page_fill"""
    my_incident = grab_incident(incident_id)
    # page_fill = {
    #     'filing_date': my_incident.filing_date,
    #     'subjects': my_incident.subjects.all(),
    #     'incident_date': my_incident.incident_date,
    #     'incident_time': my_incident.incident_time,
    #     'incident_type': my_incident.incident_type,
    #     'descriptors': my_incident.descriptors.all(),
    #     'text_description': my_incident.text_description,
    # }
    return my_incident


def test_for_zero_div(type_count, total_incidents):
    """take in two numbers and check/correct for ZeroDivisionError"""
    try:
        percent_div = type_count / total_incidents
    except ZeroDivisionError:
        return 0
    return percent_div


def test_time_input(time):
    """take in time input and if None return 00:00"""
    if time == '':
        return '00:00'
    else:
        return time


def get_total_incidents_as_author(user_id):
    """take in id, return number of incidents logged as author"""
    total_incidents_as_author = \
        Incident.objects.filter(author__exact=user_id).count()
    return total_incidents_as_author


def get_total_incidents_as_subject(subject_id):
    """take in selected id, return number of incidents logged as subject"""
    total_incidents_as_subject = \
        Incident.objects.filter(subjects__exact=subject_id).count()
    return total_incidents_as_subject


def get_subject_name(subject_id):
    """take in id string, return name value for Person instance"""
    subject = Person.objects.get(id__exact=subject_id)
    return subject.name


def get_percent_exclusion_logged_as_author(user_id):
    """take in User.id and return incident percent for exclusionary"""
    total_incidents_as_author = get_total_incidents_as_author(user_id)
    count_exclusive_as_author = Incident.objects.filter(
        author__exact=user_id, incident_type__exact='Exclusion'
    ).count()
    pre_percent = test_for_zero_div(
        count_exclusive_as_author,
        total_incidents_as_author
    )
    percent = round(
        pre_percent * 100, 1
    )
    return percent


def get_percent_inclusion_logged_as_author(user_id):
    """take in User.id and return incident percent for inclusionary"""
    total_incidents_as_author = get_total_incidents_as_author(user_id)
    count_inclusive_as_author = Incident.objects.filter(
        author__exact=user_id, incident_type__exact='Inclusion'
    ).count()
    pre_percent = test_for_zero_div(
        count_inclusive_as_author,
        total_incidents_as_author
    )
    percent = round(
        pre_percent * 100, 1
    )
    return percent


def get_percent_exclusion_logged_as_subject(subject_id):
    """take in selected id and return incident percent for exclusionary"""
    total_incidents_as_subject = get_total_incidents_as_subject(subject_id)
    count_exclusive_as_subject = Incident.objects.filter(
        subjects__exact=subject_id, incident_type__exact='Exclusion'
    ).count()
    pre_percent = test_for_zero_div(
        count_exclusive_as_subject,
        total_incidents_as_subject
    )
    percent = round(
        pre_percent * 100, 1
    )
    return percent


def get_percent_inclusion_logged_as_subject(subject_id):
    """take in selected id and return incident percent for inclusionary"""
    total_incidents_as_subject = get_total_incidents_as_subject(subject_id)
    count_inclusive_as_subject = Incident.objects.filter(
        subjects__exact=subject_id, incident_type__exact='Inclusion'
    ).count()
    pre_percent = test_for_zero_div(
        count_inclusive_as_subject,
        total_incidents_as_subject
    )
    percent = round(
        pre_percent * 100, 1
    )
    return percent


def count_descriptors_for_author(incidents_as_author):
    """take Incidents, return dict of descriptors with their counts"""
    descriptor_counts = {}
    for incident in incidents_as_author:
        descriptors = incident.descriptors.all()
        for descriptor in descriptors:
            if descriptor.descriptor not in descriptor_counts:
                descriptor_counts[descriptor.descriptor] = 1
            else:
                descriptor_counts[descriptor.descriptor] += 1
    return descriptor_counts


def create_descriptors_and_counts_as_author(user_id):
    """take id, return list of tuples with descriptors and their counts

    1. find all incidents where id was author, then 2. get all descriptors in
    those incidents and their counts and 3. break that dict into a list of
    tuple pairs of (descriptor name, count)
    """
    incidents_as_author = Incident.objects.filter(author__exact=user_id)
    descriptor_counts = count_descriptors_for_author(incidents_as_author)
    descriptors_and_counts = descriptor_counts.items()
    return descriptors_and_counts


def count_descriptors_for_subject(incidents_as_subject):
    """take Incidents, return dict of descriptors with their counts"""
    descriptor_counts = {}
    for incident in incidents_as_subject:
        descriptors = incident.descriptors.all()
        for descriptor in descriptors:
            if descriptor.descriptor not in descriptor_counts:
                descriptor_counts[descriptor.descriptor] = 1
            else:
                descriptor_counts[descriptor.descriptor] += 1
    return descriptor_counts


def create_descriptors_and_counts_as_subject(subject_id):
    """take id, return list of tuples with descriptors and their counts

    1. find all incidents where id was subject, then 2. get all descriptors in
    those incidents and their counts and 3. break that dict into a list of
    tuple pairs of (descriptor name, count)
    """
    incidents_as_subject = Incident.objects.filter(subjects__exact=subject_id)
    descriptor_counts = count_descriptors_for_subject(incidents_as_subject)
    descriptors_and_counts = descriptor_counts.items()
    return descriptors_and_counts


def create_json_ready_descriptors_and_counts(subject_id):
    """take in id, return JSON-ready list with descriptor name & counts

    NOTE:  This isn't the JSON object, just preparing the most complicated
    piece that will go into the object.
    """
    descriptors_and_counts = create_descriptors_and_counts_as_subject(
        subject_id
    )
    json_ready_list = []
    for i in descriptors_and_counts:
        dict_item = {'descriptor': i[0], 'count': i[1]}
        json_ready_list.append(dict_item)
    return json_ready_list


def convert_subject_stats_to_json_obj(
    subject_name,
    recorded_incident_total,
    percent_exclusion_as_subject,
    percent_inclusion_as_subject,
    descriptor_counts
):
    """Convert a subject stats data into a JSON-encodable object."""
    return {
        'subName': subject_name,
        'total': recorded_incident_total,
        'inclusion': percent_inclusion_as_subject,
        'exclusion': percent_exclusion_as_subject,
        'descriptors': descriptor_counts
    }


def create_descriptors_list(incident):
    """return descriptors as a list for specific incident"""
    descriptors = incident.descriptors.all()
    descriptors_list = []
    for i in descriptors:
        descriptors_list.append(i.descriptor)
    return descriptors_list


def create_subjects_list(incident):
    """return subject name(s) as a list for specific incident"""
    subjects = incident.subjects.all()
    subjects_list = []
    for i in subjects:
        subjects_list.append(i.name)
    return subjects_list


def convert_incident_stats_to_json_obj(
    filing_date,
    incident_date,
    incident_time,
    subjects,
    incident_type,
    descriptors,
    text_description
):
    """Convert a incident stats data into a JSON-encodable object."""
    return {
        'filingDate': filing_date,
        'incidentDate': incident_date,
        'incidentTime': incident_time,
        'subjects': subjects,
        'incidentType': incident_type,
        'descriptors': descriptors,
        'textDescription': text_description
    }


def create_incident_type_list(incident_types):
    """take in tuple pairs and return single list of two items"""
    incident_type_choices = []
    for item in incident_types:
        incident_type_choices.append(item[0])
    return incident_type_choices


def test_for_blank_value(value):
    """take in value and return False if ''"""
    if value == '':
        return False
    elif value is None:
        return False
    elif value == []:
        return False
    else:
        return True


def test_and_correct_date(incident_date):
    """take in date and return default val if ''"""
    if test_for_blank_value(incident_date) is False:
        return datetime.today().date()
    else:
        return incident_date


def test_and_correct_type(incident_type):
    """take in type and return default val if ''"""
    if test_for_blank_value(incident_type) is False:
        return 'Exclusion'
    else:
        return incident_type


def test_and_correct_empty_list(item_list):
    """take in subject and return default val if ''"""
    if test_for_blank_value(item_list) is False:
        return ['1']
    else:
        return item_list


def log_new_incident(
    author,
    subjects,
    incident_date,
    incident_time,
    incident_type,
    descriptors,
    text_description
):
    """take in incident fields and instantiate new incident"""
    incident_date = test_and_correct_date(incident_date)
    incident_time = test_time_input(incident_time)
    incident_type = test_and_correct_type(incident_type)
    subjects = test_and_correct_empty_list(subjects)
    descriptors = test_and_correct_empty_list(descriptors)
    new_incident = Incident(
        author=author,
        incident_date=incident_date,
        incident_time=incident_time,
        incident_type=incident_type,
        text_description=text_description
    )
    # cannot add many to many fields until base Incident is saved
    new_incident.save()
    for subject in subjects:
        sub_id = int(subject)
        new_incident.subjects.add(sub_id)
    for descriptor in descriptors:
        desc_id = int(descriptor)
        new_incident.descriptors.add(desc_id)
    return 'New Incident Submitted'
