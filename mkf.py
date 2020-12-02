# make some files
import subprocess

for num in range(3, 26):

    fname = 'day' + str(num)
    subprocess.run(['mkdir', fname])

    q1 = fname + '/day' + str(num) + '_q1.py'
    q2 = fname + '/day' + str(num) + '_q2.py'
    ip = fname + '/input.txt'

    subprocess.run(['touch', q1, q2, ip])