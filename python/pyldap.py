#!/bin/env python

###
### http://www.python-ldap.org/docs.shtml
###


import ldap
import os,sys
import ldap.sasl
import getpass


URI     = "ldap://ldap0.nmt.edu"
UID     = getpass.getuser()
BASE    = "ou=accounts,dc=tcc,dc=nmt,dc=edu"
BINDDN  = "uid=%s,%s"%(UID,BASE)


def init():
  #Establish LDAP connection
  try:
    l = ldap.initialize(URI)
    l.start_tls_s()
  except ldap.SERVER_DOWN, e:
    print e 
    sys.exit(1)

  #Try to SASL bind
  try:
    token = ldap.sasl.gssapi()
    l.sasl_interactive_bind_s(BINDDN,token)
  except ldap.LOCAL_ERROR,e:
    print e
    print "Cannot get Authed Access:\nTry running kinit"
    sys.exit(1)
  except ldap.INSUFFICIENT_ACCESS,e:
    print e
    print "Cannot get Authed Access:\nTry running kinit"
    sys.exit(1)
  return l

def search(l):
  #Ldap Search - ou=accounts subtree for tccAccountType = sys.argv[1]
  results = l.search_s( BASE,
                        ldap.SCOPE_SUBTREE,
                        '(objectClass=tccAccount)',
                        ['uid','gecos','tccBannerId'],
                      )
  print results[0]


def mod(l):
  dn = BINDDN
  mod_attrs = [ (ldap.MOD_REPLACE, 'gecos', 'MY GECOS'),
                ]
  l.modify_s(BINDDN,mod_attrs)

if __name__ == "__main__":
  l = init()
  search(l)
#  mod(l)

