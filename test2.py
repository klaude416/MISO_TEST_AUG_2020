
# Write a command-line program that prints out the sum of two non-negative integers as input arguments. 
# Input arguments are UTF-8 encoded Korean characters only listed as '일이삼사오육칠팔구' and '십백천만억조', 
# and also your program's output should be. The less you use ifs, the higher you get scored. 
# Google Korean Numbering System if you are not familiar with.
# Your program is tested by following python code:

# import sys
# import subprocess

# DATA = [
#   ['오백삼십조칠천팔백구십만천오백삼십구', '삼조사천이만삼천구'],
#   ['육십사억삼천십팔만칠천육백구', '사십삼'],
#   ['구백육십조칠천억팔천백삼십이만칠천일', '사십삼조오천이백억육천구백십만일'],
#   ['이천구백육십조천오백칠십만삼천구백구십', '삼천사백오십조일억이천만육백사십삼'],
#   ['사십오억삼천육십만오백구십', '칠십억천이백삼십오만칠천구십이'],
#   ['천백십일', '구천오백구십구'],
#   ['오억사천', '백십일'],
#   ['만오천사백삼십', '십구만삼천오백'],
#   ['일조', '삼'],
#   ['일억', '만'],
# ]
# for pair in DATA:
#   a, b = pair
#   print(a, '+', b, '=', subprocess.check_output([sys.argv[1], sys.argv[2], a, b], encoding='utf-8').strip())
      
# Your program is supposed to print to stdout following:


# 오백삼십삼조일억천팔백구십이만사천오백사십팔
# 육십사억삼천십팔만칠천육백오십이
# 천사조이천이백일억오천사십이만칠천이
# 육천사백십조일억삼천오백칠십만사천육백삼십삼
# 백십오억사천이백구십오만칠천육백팔십이
# 만칠백십
# 오억사천백십일
# 이십만팔천구백삼십
# 일조삼
# 일억일만
      
# Do not print out anything but result string.

import sys 
import collections

DIC_KOREAN_WON = collections.OrderedDict({
    '조': 10 ** 12, '억': 10 ** 8, '만': 10 ** 4, 
    '천': 10 ** 3, '백': 10 ** 2, '십': 10, '일': 1 })

ARR_KOREAN_STR_NUM = [x for x in '영일이삼사오육칠팔구']

def help_and_exit():
    print('Usage:')
    print(f'{sys.argv[0]} [non-negative integer] [non-negative integer]')
    sys.exit(1)

def _parse_thousand_unit(preunit, num_unit):
    # In case of letter is blank as a big number
    if not preunit and num_unit > 10 ** 3: return num_unit

    str_idx = tot = 0
    for str_unit in '천백십':
        try:
            idx = preunit.index(str_unit)
            num = preunit[str_idx:idx]
            tot += (1 if num == '' else ARR_KOREAN_STR_NUM.index(num)) * DIC_KOREAN_WON[str_unit]
            str_idx = idx + 1
        except ValueError: #when preunit has not index of str_unit
            pass
        except:
            print('unexpected error')
    num = preunit[str_idx:]
    tot += 0 if num == '' else ARR_KOREAN_STR_NUM.index(num)
    return tot * num_unit

def parse_int_from_korean_won(str_won):
    str_idx = 0
    tot = 0
    for str_unit in '조억만':
        try:
            idx = str_won.index(str_unit) #for separate numbers by unit
            tot += _parse_thousand_unit(str_won[str_idx:idx], DIC_KOREAN_WON[str_unit])
            str_idx = idx + 1
        except ValueError: #when str_won has not index of str_unit
            pass
        except:
            print('unexpected error')

    tot += _parse_thousand_unit(str_won[str_idx:], 1)

    return tot

def _parse_korean_won_under_thousand(num, unit = ''):
    str_won = ''
    for small_unit in '천백십':
        curr_num = num // DIC_KOREAN_WON[small_unit]
        if curr_num > 1: 
            str_won += ARR_KOREAN_STR_NUM[curr_num] + small_unit
        elif curr_num == 1:
            str_won += small_unit
        else: # ignore zero
            continue

        num -= curr_num * DIC_KOREAN_WON[small_unit]
    
    # position of units
    if num > 0:
        str_won += ARR_KOREAN_STR_NUM[num]
    
    return str_won + unit

def parse_korean_won(num):
    tot_won = ''
    for won in '조억만':
        quotient = num // DIC_KOREAN_WON[won]
        if quotient == 0: continue # skip 0
        tot_won += _parse_korean_won_under_thousand(quotient, won)
        num -= quotient * DIC_KOREAN_WON[won]
    
    # convert remains
    tot_won += _parse_korean_won_under_thousand(num)

    # There is special case about '만'.
    # It has both '만' and '일만'
    # If number is greater than 20T , 10T displays '일만', else number is letter than 20T then only '만'
    if tot_won[0:2] == '일만':
        tot_won = tot_won[1:]
    
    return tot_won

def test():
    input1 = '오백삼십조칠천팔백구십만천오백삼십구'
    input2 = '삼조사천이만삼천구'
    output = '오백삼십삼조일억천팔백구십이만사천오백사십팔'

    tot = parse_int_from_korean_won(input1) + parse_int_from_korean_won(input2)
    print(tot, parse_korean_won(tot))
    assert output == parse_korean_won(tot)
    print('succeed')

if __name__ == "__main__":
    # test()

    if len(sys.argv) != 3 :
        help_and_exit()

    input1 = parse_int_from_korean_won(sys.argv[1])
    input2 = parse_int_from_korean_won(sys.argv[2])
    output = parse_korean_won(input1 + input2)
    # print(f'inputs: {input1}, {input2}')
    # print(f'output: {output}')
    
    print(output)
    sys.exit(0)