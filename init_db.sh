#!/bin/bash

# Create fresh db, load fixtures in an order that works

read -p "About to blow away DB - answer Y to go ahead, ^C to cancel> "
case $REPLY in
  Y*) ;;
  *)
   echo "Cancelling (try capital Y if you meant to go ahead)"
   exit 1
  ;;
esac

python manage.py syncdb --noinput
python manage.py migrate

python manage.py loaddata \
  fixtures/auth_user.json \
  fixtures/auth_permission.json \
  fixtures/conference.json \
  fixtures/database_constance.json \
  fixtures/boxes.json \
  fixtures/proposals.json \
  fixtures/sitetree.json \
  fixtures/sponsorship.json \
  fixtures/schedule.json \
  fixtures/teams.json \

echo
echo
echo "Database initialized."
echo "Hint: setup an account with: ./manage.py createsuperuser"
