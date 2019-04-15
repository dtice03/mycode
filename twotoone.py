#!/usr/bin/python3

#exercise is as follows:  you have 2 files, open the data, parse, combine data, spit it to single file

# open file1 - "bunker east"
bunkereast = open('bunkereast.txt')

# open file2 - "bunker west"
bunkerwest = open('bunkerwest.txt')

# read file1 - "bunker east"
eastlist = bunkereast.readlines()

# read file2 - "bunker west"
westlist = bunkerwest.readlines()

# close file1 - "bunker east"
bunkereast.close()

# close file2 - "bunker west"
bunkerwest.close()

# combine data sets
# lists [] and dict {key:value}
# [{"sw1": 10.0.0.1, "sw2": "10.0.0.2", ...}, {"sw1: 192.168.0.1, "sw2": 192.168.0.2, ....}]

# {"east":{"sw1": "10.0.0.1, "sw2": "10.0.0.2"}, "west":{"sw1": 192.168.0.1, "sw2": "192.168.0.2}}

# write out to file3 - "bunkerallfile"
bunkerallfile = open('bunker_all.txt', 'w')

#push bunkereast to bunker all
for data1 in eastlist:
	# push mylist to outdata (01-newlists.txt)
	bunkerallfile.write('e-' + data1.rstrip('\n') + '\n')
		
#push bunkerwest to bunker all	
for data2 in westlist:
	# push mylist to outdata (01-newlists.txt)
	bunkerallfile.write('w-' + data2.rstrip('\n') + '\n')
	
# close bunkerallfile
bunkerallfile.close()                    

bunkerallfile = open('bunker_all.txt', 'r')
balines = bunkerallfile.readlines()
bafileip = open('bunkerips.txt', 'w') # create a new file of ips only
for line in balines:
    bafileip.write(line.split(' ')[1]) # just write out ips

bafileip.close()
bunkerallfile.close()

bunkerdict = {}
bedata = open('bunkereast.txt', 'r')
belist = bedata.readlines()
bedata.close()
for line in belist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')

eastwest = {}
eastwest.update({"east": = bunkerdict})

bunkerdict2 = {}
bwdata = open('bunkerwest.txt', 'r')
bwlist = bwdata.readlines()
bwdata.close()
for line in bwlist:
    hostip = line.split(' ')
    bunkerdict[hostip[0]] = hostip[1].rstrip('\n')

eastwest.update({"west": bunkerdict2})
print(eastwest)
