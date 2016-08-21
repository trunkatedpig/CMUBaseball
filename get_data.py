#!/usr/bin/python
from gdata.spreadsheet.service import SpreadsheetsService
from csv import reader
import requests

def get_spreadsheet(key):

  client = SpreadsheetsService()
  feed = client.GetWorksheetsFeed(key, visibility='public', projection='basic')

  def get_data(sheet): 
    raw = reader(requests.get(sheet.link[3].href).text.split('\n'))
    processed = []
    for row in raw:
      processed.append(row)
    return processed

  print map(get_data, feed.entry)
  return map(get_data, feed.entry)

def get_site_data(key):
  raw_data = get_spreadsheet(key)

  def process_heights(height):
    if len(height) >= 3 and height[-3:] == u'"""':
      return height[1:-2]
    return height

  raw_data[1] = map(lambda info: info[:7] + [process_heights(info[7]), info[8], int(info[9])], raw_data[1][1:])
  raw_data[2] = map(lambda info: info[:5] + [int(info[5])], raw_data[2][1:])
  raw_data[3] = map(lambda info: info[:4] + [info[4].split('\t')], raw_data[3][1:])[::-1]
  raw_data[4] = raw_data[4:]

  raw_data = raw_data[:5]

  return raw_data

