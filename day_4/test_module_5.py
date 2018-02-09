'''
Created on 08/02/2018

@author: asus
'''
import unittest
from module_5 import GetSeq

class Test(unittest.TestCase):


	def test_sequence(self):
		
		get_seq = GetSeq('ANAA', 'CYCC')
		self.assertEqual('TTTTT', get_seq.get_seq_by_fasta('AAAATTTTTCCCC'))
		self.assertEqual('TTTTT', get_seq.get_seq_by_fasta('AAAATTTTTCCCC'))
		self.assertEqual('TTTTT', get_seq.get_seq_by_fasta('GGGGAAAAATTTT'))
		self.assertEqual(None, get_seq.get_seq_by_fasta('GGGAAAAAACTT'))

	def test_get_expansion_bases(self):
		get_seq = GetSeq('AAAA','CCCC')
		self.assertEqual('[ACTG]',get_seq.get_expansion_bases('N'))
		self.assertEqual('CA[ACTG]TC',get_seq.get_expansion_bases('CANTC'))
		self.assertEqual('CA[ACTG]T[CT]',get_seq.get_expansion_bases('CANTY'))
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_sequence']
	unittest.main()