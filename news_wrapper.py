# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:52:57 2019

@author: Dr. Mark M. Bailey | National Intelligence University
"""

import os
import pickle

#open pickle file
def open_pickle(pickle_path):
    with open(pickle_path, 'r') as pickle_file:
        object_name = pickle.load(pickle_file)
    return object_name

#save object to pickle
def save_pickle(output_path, pickle_object, file_name):
    output_name = os.path.join(output_path, file_name + '.pkl')
    with open(output_name, 'wb') as pkl_object:
        pickle.dump(pickle_object, pkl_object)

#drop duplicates
def drop_duplicates():
    object_path = os.path.join(os.getcwd(), 'news_dump_object.pkl')
    pkl_object = open_pickle(object_path)
    seen = set()
    new_object = []
    for d in pkl_object:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_object.append(d)
    save_pickle(os.getcwd(), new_object, 'news_dump_object')
    return new_object

#find database size
def news_size():
    news_path = os.path.join(os.getcwd(), 'news_dump_object.pkl')
    news_object = open_pickle(news_path)
    total_records = len(news_object)
    return total_records

#get total news additions
def get_adds(original_files):
    total_records = news_size()
    new_records = total_records - original_files
    print('Total new records collected: {}').format(new_records)	

#get python news modules
def get_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file_0 in files:
            if file_0.endswith('.py'):
                file_list.append(os.path.join(root, file_0))
    current_file_path = os.path.join(directory, 'news_wrapper.py')
    file_list.remove(current_file_path)
    return file_list

#execute news modules
def execute_modules(file_list):
    print('Executing news scraping modules...')
    for news_module in file_list:
        try:
            #runfile(news_module, wdir=os.getcwd())
            exec(open(news_module).read(), globals())
        except:
            print('Error executing module {}...skipping...').format(os.path.basename(news_module))
            continue
    print('Finished executing scraping modules.')

#execute main script
def main_script():
    original_files = news_size()
    file_list = get_files(os.getcwd())
    execute_modules(file_list)
    final_output = drop_duplicates()
    get_adds(original_files)
    print('You are a great American!!')
    return final_output

if __name__ == '__main__':
    final_output = main_script()