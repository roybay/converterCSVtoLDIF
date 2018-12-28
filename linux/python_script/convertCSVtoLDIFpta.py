# Description: auto converter for CSV to LDIF
#
import sys
import getopt
import ConfigParser
#------------------------------------------------------------
def input_validation(argv):
  container=''
  file=''
  output=''

  try:
    opts, args = getopt.getopt(argv,"hc:f:o:",["container=", "file=", "output="])
  except getopt.GetoptError:
    print 'convertCSVtoLDIF.py -c <container> -f <file path> -o <output.ldif>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'convertCSVtoLDIF.py -c <container> -f <file path> -o <output.ldif>'
      sys.exit()
    elif opt in ("-c", "--container"):
      container = arg
    elif opt in ("-f", "--file"):
      file = arg
    elif opt in ("-o", "--output"):
      output = arg
  if container == '' or file == '' or output == '':
    print 'Missing argument(s). Please use -h menu.'
    exit();
  else:
    print 'Container is ', container
    print 'File path is ', file
    print 'Output file is ', output
    print ''
  return (container, file, output)
#------------------------------------------------------------
def getUserInfo(line):
  line = line.split(",")
  uid = line[0]
  uid = uid.split("\"")
  uid = uid[1]
  ptaSyncId = line[1]

  return (uid, ptaSyncId)
#------------------------------------------------------------
def convertCSVtoLDIF(container, file, output):
  with open(file) as r:
    lines = r.readlines()[1:]
    w = open(output, 'w')  
    for line in lines:
      uid, ptaSyncId = getUserInfo(line);
      w.write('dn: uid=%s,%s\n' % (uid,container))
      w.write('changetype: modify\n')
      w.write('add: ptaSyncId\n')
      w.write('ptaSyncId: %s\n' % ptaSyncId)
    w.close()
#------------------------------------------------------------
if __name__=='__main__' or __name__== 'main':

  container, file, output = input_validation(sys.argv[1:]);
  convertCSVtoLDIF(container, file, output);  

  exit();
