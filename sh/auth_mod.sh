#!/bin/bash

DN="uid=`whoami`,ou=accounts,dc=tcc,dc=nmt,dc=edu"

ldapsearch -h ldap0.nmt.edu -xZZLLL -D $DN  -W $1
