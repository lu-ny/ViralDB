#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


# imports
import os
import numpy as np
import datetime
import ftplib
from ftplib import FTP


# In[2]:


# set parent directory where all versions wil be held
parent_dir='D:/Viral_DB/'


# In[3]:


# get all the past versions and find the latest version
versions = os.listdir(parent_dir)
last_version = max(versions)
last_version_num = float(last_version.split('v')[1])

#go ahead and get the next major and minor update version numbers 
# (so, only 9 minor version updates permitted under this naming schema)
next_major = np.floor(last_version_num)+1


# In[4]:


# convert next major version number to string & make the directory
major_dir = 'v'+str(next_major)
path = os.path.join(parent_dir, major_dir)
os.mkdir(path)


# In[5]:


# make directories for genbank, tpa, and refseq

# get the current system month and year to append to the folders
today = str(datetime. date. today())
curr_year = today[:4] 
curr_month = today[5:7]
mo_yr=(curr_month+'.'+curr_year)

# set folder names
gb_my = 'Genbank_raw_data_'+mo_yr
tpa_my = 'TPA_raw_data_'+mo_yr
rs_my = 'RefSeq_raw_data_'+mo_yr

# create folders for each database with "_"$month.$year format"
# All db folders will have  log and scripts folder; genbank and tpa also have 
# poskw_out_”$month”.”$year”, sizemirna_out_”$month”.”$year”, and negkw_out_”$month”.”$year sub-folders
databases = [gb_my,tpa_my, rs_my]
for db in databases:
    path = os.path.join(parent_dir, major_dir, db)
    os.mkdir(path)
    log_path = os.path.join(path, 'log')
    os.mkdir(log_path)
    scripts_path = os.path.join(path, 'scripts')
    os.mkdir(scripts_path)
    
gb_tpa_dbs = [gb_my,tpa_my]
for db in gb_tpa_dbs:
    path = os.path.join(parent_dir, major_dir, db)
    for sub_folder in ['poskw_out_', 'sizemrna_out_', 'negkw_out_']:
        sub_path = os.path.join(path, sub_folder+mo_yr)
        os.mkdir(sub_path)


# In[63]:


local_path = os.path.join(parent_dir, major_dir, rs_my)

global ftp
ftp = FTP('ftp.ncbi.nih.gov')
ftp.login('anonymous','anonymous')
source_path = '/refseq/release/viral'
ftp.cwd(source_path)


# In[64]:


#download the refseq files

files_list = ftp.nlst(source_path)
substring = "genomic"
genomic_files = [files_list for files_list in files_list if substring in files_list]

for filename in genomic_files:
    print("local_path :" + local_path)
    local_fn = os.path.join(local_path)
    print(local_fn)
    print('Downloading files from remote server :' + filename)
    with open (local_fn, "wb") as f:
        ftp.retrbinary('RETR %s' % filename, file.write)
        filename.close()
        

ftp.quit()


# In[65]:


# download the genbank files
local_path = os.path.join(parent_dir, major_dir, gb_my)

global ftp
ftp = FTP('ftp.ncbi.nih.gov')
ftp.login('anonymous','anonymous')
source_path = '/genbank'
ftp.cwd(source_path)

files_list = ftp.nlst(source_path)
substring_list = ['env', 'htc', 'inv', 'mam', 'pln', 'pri', 'rod', 'vrl', 'vrt']
gb_files=[]

for substr in substring_list:
    gb_files.append([files_list for files_list in files_list if substr in files_list])

#flatten into a 1-d list
gb_list = [item for sublist in gb_files for item in sublist]

for filename in gb_list:
    print("local_path :" + local_path)
    local_fn = os.path.join(local_path)
    print(local_fn)
    print('Downloading files from remote server :' + filename)
    with open (local_fn, "wb") as f:
        ftp.retrbinary('RETR %s' % filename, file.write)
        filename.close()
        

ftp.quit()


# In[67]:


#download tpa files

local_path = os.path.join(parent_dir, major_dir, tpa_my)

global ftp
ftp = FTP('ftp.ncbi.nih.gov')
ftp.login('anonymous','anonymous')
source_path = '/tpa/release'
ftp.cwd(source_path)

files_list = ftp.nlst(source_path)
substr = 'nt'
tpa_files = [files_list for files_list in files_list if substr in files_list]

for filename in tpa_files:
    print("local_path :" + local_path)
    local_fn = os.path.join(local_path)
    print(local_fn)
    print('Downloading files from remote server :' + filename)
    with open (local_fn, "wb") as f:
        ftp.retrbinary('RETR %s' % filename, file.write)
        filename.close()
        

ftp.quit()


# In[ ]:




