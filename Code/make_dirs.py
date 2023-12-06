import os
import re
l = ["RPL12_genome", "RPL18_genome", "RPL19_genome", "RPL1_genome", "RPL20_genome", 
     "RPL23_genome", "RPL2_genome", "RPL35_genome", "RPL40_genome", "RPL41_genome", 
     "RPL42_genome", "RPL43_genome", "RPS11_genome", "RPS16_genome", "RPS18_genome", 
     "RPS23_genome", "RPS24_genome", "RPS30_genome", "RPS4_genome", "RPS6_genome", 
     "RPS8_genome"]


i=1
for term in l:
    pr = re.sub('genome', 'protein', term)
    os.mkdir(pr)
    print(f"{i}. {pr} dir made.")