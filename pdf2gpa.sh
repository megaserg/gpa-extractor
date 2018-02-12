#!/bin/bash
set -euxo pipefail

curl -LO http://central.maven.org/maven2/org/apache/pdfbox/pdfbox-app/1.8.2/pdfbox-app-1.8.2.jar
java -jar pdfbox-app-1.8.2.jar ExtractText -force -startPage 4 -endPage 6 $1 supplement.txt
python txt2gpa.py supplement.txt
