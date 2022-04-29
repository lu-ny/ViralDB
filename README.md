# ViralDB
A viral database that combines sequences from genbank, refseq, and tpa

To initialize, first create a path where the DB will be stored. 
Update the major_update.py with said path, and include the 0.0 folder, which also contains the semantic keywords

Running this py script should download all the necessary sequences. The next scripts to run would be:

PATH/parse_raw_refseq_PIPE.py PATH-DRIVE mo_yr next_major viral.1.1.genomic.fna.gz viral.2.1.genomic.fna.gz && python 
PATH/multiple_gzunzip_PIPE.py PATH-DRIVE mo_yr next_major viral.1.genomic.gbff.gz viral.2.genomic.gbff.gz viral.genomic.gbff && python 
# find duplicates
PATH/fileops_PIPE.py PATH-DRIVE mo_yr next_major gbff 1000000 && python  E:/UPDATE_SCRIPTS_LOGS/rs_acc_mapping_PIPE.py E: apr.2018 13.0 && python 
PATH/VDBunzip_reformat_gb_to_fasta_PIPE.py PATH-DRIVE mo_yr next_major gb && python 
PATHVDBupdate_checkpoint2_PIPE.py  PATH-DRIVE mo_yr next_major gb_releasenotes_v225_apr.2018.txt && python 
PATH/SEM-R_PIPE.py PATH-DRIVE mo_yr next_major poskw gb && python 
PATHSEM-R_PIPE.py PATH-DRIVE mo_yr next_major sizemirna gb && python 
PATH/SEM-R_PIPE.py PATH-DRIVE mo_yr next_major negkw gb
# unzip TPA files and run various screens on the files
PATH/VDBunzip_tpa_PIPE.py PATH-DRIVE mo_yr next_major fsa_nt.gz && python  
PATH/SEM-R_PIPE.py PATH-DRIVE mo_yr next_major poskw tpa && python  
PATH/SEM-R_PIPE.py PATH-DRIVE mo_yr next_major sizemirna tpa && python  
PATH/SEM-R_PIPE.py PATH-DRIVE mo_yr next_major negkw tpa
#for manual revision (if needed)
PATH/prep_manual_review.py PATH-DRIVE mo_yr next_major E:/RVDBv12.2/U-RVDBv12.2.fasta 
# generate fasta file
PATH/create_U-RVDB_file.py PATH-DRIVE mo_yr next_major RVDBv13.0.removeaccs.txt   
# Generate SQL files
PATH/make_alter_build_sqlite3db_v2.py PATH/RVDB_postpub mo_yr next_major U-RVDBv13.0.fasta

Ideally, these commands should be loaded into an AWS EC2 instance and run with a lambda function. Data to be stored in an Amazon S3 bucket with a cloudwatch event rule to trigger the lambda function
