#------------------------------------------------------------------------------
# connect.py (Section 1.2 and 1.3)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright (c) 2017, 2018, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import commands
import re
import os
import cx_Oracle


class TestOracleConnect(object):
    
    con = cx_Oracle.connect('TDRCORE', get_password(), 'dpxdt02a-scan.austest.thenational.com:1621/pptesor_olt')
    print("Database version:", con.version)

    PHRASE_FILE_PATH = '/opt/sas/hdp/uat/sfmsor/tdrcore/parms/tdrphrase'
    ENCRYPTED_PASS_PATH = '/opt/sas/hdp/uat/sfmsor/tdrcore/parms/tdrcore_cred.enc'

def get_password(self):
        if hasattr(self, 'ORACLE_PASS'):
            return self.ORACLE_PASS
        phrase = open(self.PHRASE_FILE_PATH, 'rb').read().split('\n')[0]
        command = 'openssl aes-256-cbc -d -a -in %s -pass pass:%s' % (
            self.ENCRYPTED_PASS_PATH,
            phrase
        )
        status, output = commands.getstatusoutput(command)
        return output
