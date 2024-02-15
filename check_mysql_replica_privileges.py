#!/usr/bin/python3
"""
This script will verify that a student has granted replica_user
replication slave privileges.
"""
import re
import sys

from fabric import Connection
from io import StringIO
from paramiko import RSAKey


host = sys.argv[1]
user = sys.argv[2]
rsa_key_file = sys.argv[3]

rsa_key = RSAKey.from_private_key(open(rsa_key_file))
output = StringIO()

with Connection(host, user=user, connect_kwargs={"pkey": rsa_key}) as c:
    c.run(
        "mysql -uholberton_user -pprojectcorrection280hbtn -e 'select * from mysql.user \G' 2>&1",
        shell="/bin/bash",
        out_stream=output,
        warn=False,
    )

    # This regex matches ******* \d. row ******** in mysql.user table
    regex = re.compile(r"\*+\s+\d+\.\s+row\s+\*+")
    entries = regex.split(output.getvalue())
    for entry in entries:
        if re.search(r"User: replica_user", entry):
            print(re.search(r"Repl_slave_priv:\s+\w", entry).group(0), end="")
            exit(0)
