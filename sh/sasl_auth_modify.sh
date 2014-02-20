#!/bin/bash

ldapmodify -h ldap0.nmt.edu -ZZ -Y GSSAPI -f $1
