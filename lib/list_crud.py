def create_an_empty_list():
    new_list=list();
    return new_list

def create_a_list():
    new_list=list();
    new_list.append(1);
    new_list.append(2);
    new_list.append(3);
    new_list.append(4);
    return new_list

def add_element_to_end_of_list(l, element):
    l.append(element);
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0,element)
    return l

def remove_element_from_end_of_list(l):
    l.pop();
    return l

def remove_element_from_start_of_list(l):
    del l[0];
    return l

def retrieve_first_element_from_list(l):
    first=l[0]
    return first;

def retrieve_element_from_index(l, index):
    element=l[index];
    return element

def retrieve_last_element_from_list(l):
    last=l[len(l)-1]
    return last
