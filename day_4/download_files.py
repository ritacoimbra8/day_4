'''
Created on 08/02/2018

@author: rita
'''
import sys
from Bio import Entrez, SeqIO
import os
from urllib.error import HTTPError

FILE_FORMAT_ALLOWED = ['gb','fasta']

if __name__ == '__main__':

    ### show arguments
    print(sys.argv)
    
    if (len(sys.argv) != 3):
        print("usage: {} <file id> <file format>".format(os.path.basename(sys.argv[0])))
        sys.exit(1)
        
    ## get id from command line
    id_by_arg = sys.argv[1]
    file_format = sys.argv[2] 
    
    if (file_format not in FILE_FORMAT_ALLOWED):
        print('Formats allowed: {}'.format(', '.join(FILE_FORMAT_ALLOWED))) 
    
    try:
        Entrez.email = 'ritacoimbra@ua.pt'
        handle = Entrez.efetch(db='nucleotide', rettype=file_format, retmode='text',\
                           id=id_by_arg)
        
    except HTTPError as e:
        print(e)
        print('Error: {}'.format(e.msg))
        sys.exit(1)
           
    lst_seq_record = SeqIO.read(handle, file_format)
    print("#sequences: {}".format(len(lst_seq_record)))
    with open('{}.{}'.format(id_by_arg,file_format), 'w') as handle_out:
        SeqIO.write(lst_seq_record, handle_out, file_format)
    print('File saved: {}.gb'.format(id_by_arg))
    
    