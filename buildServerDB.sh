#!/bin/bash
echo "deleting last build"
rm -rf /tmp/dataplusBuild

echo "copying directory"
cp -r ~/Google\ Drive/Dev/dataplus /tmp/dataplusBuild

echo "removing unnecessary files"
rm /tmp/dataplusBuild/buildServerDB.sh
rm -rf /tmp/dataplusBuild/__pycashe__
rm /tmp/dataplusBuild/*.pyc
rm -rf /tmp/dataplusBuild/project.bbprojectd
rm /tmp/dataplusBuild/database.db
rm -r /tmp/dataplusBuild/serverDBSpecific
rm -f /tmp/dataplusBuild/dataplusServerDB.zip

echo "copying in build specific files"
rsync -av ~/Google\ Drive/Dev/dataplus/serverDBSpecific/* /tmp/dataplusBuild

echo "zipping build"
cd /tmp/dataplusBuild
zip -r /tmp/dataplusServerDB.zip .

echo "moving zip to dataplus directory"
mv /tmp/dataplusServerDB.zip ~/Google\ Drive/Dev/dataplus/dataplusServerDB.zip

echo "completed"