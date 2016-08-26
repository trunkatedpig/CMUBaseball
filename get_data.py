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

  return map(get_data, feed.entry)

def get_site_data(key):
  raw_data = get_spreadsheet(key)

  def process_heights(height):
    if len(height) >= 3 and height[-3:] == u'"""':
      return height[1:-2]
    return height

  def process_game(game):
    basic_info = game[1][:7]

    basic_info[5] = int(basic_info[5])
    if basic_info[6] == "TRUE":
      basic_info[6] = True
    else:
      basic_info[6] = False

    game_info = basic_info

    score_info = game[4:6]
    away_score_info = [elem for elem in score_info[0][1:] if elem != ""]
    home_score_info = [elem for elem in score_info[1][1:] if elem != ""]
    if len(away_score_info) >= 3 and len(home_score_info) >= 3:
      game_info.append(away_score_info[-3:])
      game_info.append(home_score_info[-3:])
      line_score_info = []
      for i in range (len(away_score_info) - 3):
        if i < len(home_score_info):
          line_score_info.append([away_score_info[i],home_score_info[i]])
        else:
          line_score_info.append([away_score_info[i],0])
      game_info.append(line_score_info)
    else:
      game_info.append([0,0,0])
      game_info.append([0,0,0])
      game_info.append([])


    game_stats = game[8:]
    divider = next((i for i, item in enumerate(game_stats) if not item[0].isdigit()), -1)
    #functional programming has ruined my life
    hitter_stats = map(lambda info: map(lambda element: int(element) if element.isdigit() else element, info),
                       filter(lambda info: info[0].isdigit(), game_stats[:divider]))
    pitcher_stats = map(lambda info: map(lambda element: int(element) if element.isdigit() else element, info),
                        filter(lambda info: info[0].isdigit(), game_stats[(divider + 1):]))

    game_info.append(hitter_stats)
    game_info.append(pitcher_stats)

    return game_info

  raw_data[1] = map(lambda info: info[:7] + [process_heights(info[7]), info[8], int(info[9])], raw_data[1][1:])
  raw_data[2] = map(lambda info: info[:5] + [int(info[5])], raw_data[2][1:])
  raw_data[3] = map(lambda info: info[:4] + [info[4].split('\t')], raw_data[3][1:])[::-1]
  raw_data[4] = map(process_game, raw_data[4:])

  raw_data = raw_data[:5]

  return raw_data
