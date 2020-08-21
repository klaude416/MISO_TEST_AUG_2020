#run test2.py
#script: python3 test2_run.py python3 test2.py

import sys
import subprocess

DATA = [
  ['오백삼십조칠천팔백구십만천오백삼십구', '삼조사천이만삼천구'],
  ['육십사억삼천십팔만칠천육백구', '사십삼'],
  ['구백육십조칠천억팔천백삼십이만칠천일', '사십삼조오천이백억육천구백십만일'],
  ['이천구백육십조천오백칠십만삼천구백구십', '삼천사백오십조일억이천만육백사십삼'],
  ['사십오억삼천육십만오백구십', '칠십억천이백삼십오만칠천구십이'],
  ['천백십일', '구천오백구십구'],
  ['오억사천', '백십일'],
  ['만오천사백삼십', '십구만삼천오백'],
  ['일조', '삼'],
  ['일억', '만'],
]

DATA_ANSER = [
    '오백삼십삼조일억천팔백구십이만사천오백사십팔'
    ,'육십사억삼천십팔만칠천육백오십이'
    ,'천사조이천이백일억오천사십이만칠천이'
    ,'육천사백십조일억삼천오백칠십만사천육백삼십삼'
    ,'백십오억사천이백구십오만칠천육백팔십이'
    ,'만칠백십'
    ,'오억사천백십일'
    ,'이십만팔천구백삼십'
    ,'일조삼'
    ,'일억일만'
]
i = 0

for pair in DATA:
    a, b = pair
    output = subprocess.check_output([sys.argv[1], sys.argv[2], a, b], encoding='utf-8').strip()
    print(output == DATA_ANSER[i], a, '+', b, '=', output)
    i+=1