import csv
import json

with open('json_dict.json', 'r') as f:
  output_data = json.load(f)

phone = ['phone', 5553535, 6585312, 1234567, 8765123, 2315987, 9944777]

with open('quest_four.csv', mode='w', encoding='utf-8', newline='') as func_csv:
  data_file = csv.writer(func_csv, delimiter=',')
  count=0
  for i in output_data.items():
      data_file.writerow([i[0],i[1][0],i[1][1]]+phone[0+count:count+1])
      count+=1















