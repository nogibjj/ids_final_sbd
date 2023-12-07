from flask import Flask, render_template
import pandas as pd
import os

# Read the dataset

app = Flask(__name__)

@app.route("/")
def index():
  # Create a dictionary to store showName and corresponding episode audio URLs
    shows_and_urls = {'Bad Friends': ['https://podz-content.spotifycdn.com/audio/clips/5zDlaJrt21nSbNvTew70W0/clip_2215100_2266600.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/6JFAiBOueSwh3Puyr89yf8/clip_3344100_3416600.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/4PlfzYZTftxz848MIuCYTS/clip_1902700_1956700.mp3'],
 'Call Her Daddy': ['https://podz-content.spotifycdn.com/audio/clips/4BjokGoSiSD61Mq99vdkr0/clip_587850_632850.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/6aDzlDnNaqhplVCYI7nWWF/clip_2609500_2667600.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/1CxpuyukjsNS4kTGxSaoDj/clip_2417400_2467700.mp3'],
 'Huberman Lab': ['https://podz-content.spotifycdn.com/audio/clips/0hStP6Fv1h0AeKWq7YhFIs/clip_2463000_2534800.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/1RirXlMrQTFpvUeuDt1mUB/clip_656750_704650.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/02m9tjqKfSSUn1NXmMTaXo/clip_1736800_1796700.mp3'],
 'New Heights with Jason and Travis Kelce': ['https://podz-content.spotifycdn.com/audio/clips/1LClRmxBm64D95vEBMFDID/clip_2970200_3039050.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/3Eja8YBG8Ab6HF3IqkEcOv/clip_3526400_3587800.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/5rS9c1jGqHGEJoquVw2l01/clip_1999150_2068949.mp3'],
 'The Joe Rogan Experience': ['https://podz-content.spotifycdn.com/audio/clips/4LIP98lu8RxvuW1U4E2Lxe/clip_2436994_2484398.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/3lwSgYy2U5pHnBJPiLEsQY/clip_160802_226197.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/6ER3FdrVjahM9r2PMUHE7G/clip_3088120_3160800.mp3'],
 "The President's Daily Brief": ['https://podz-content.spotifycdn.com/audio/clips/24x9Rbm0ShvlAfzJkKC0Ec/clip_322392_382392.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/1jZX12S6mCNNnk1WcpB1Bi/clip_52000_103400.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/1XgU7TTcP3LxZ1vMyjbyIB/clip_164800_225500.mp3'],
 'This Past Weekend w/ Theo Von': ['https://podz-content.spotifycdn.com/audio/clips/5KcqCbnKduS7raienvCTxV/clip_2732450_2786000.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/1OZ66KpOqkAARUIiWuuQAD/clip_735650_805300.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/0XWkJ836Mbhf0j6BXhpdUU/clip_3270500_3331500.mp3'],
 'Tosh Show': ['https://podz-content.spotifycdn.com/audio/clips/7rS4yFqW5TX7N5Z9LfML59/clip_0_60000.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/2RuXEx7OstxqbAhY1AV9jG/clip_1598000_1648650.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/6LF5K2FxVFXmQ6Rv1G74z8/clip_545037_605037.mp3'],
 'What Now? with Trevor Noah': ['https://podz-content.spotifycdn.com/audio/clips/6twDxOjbfy4HYqoy7i5In5/clip_1373400_1417932.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/6cVpbp2WlMytx1Yo0M7y8d/clip_2469300_2540600.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/65qx4N4423KajHGX8BkUGK/clip_1366950_1410900.mp3'],
 'Who Killed JFK?': ['https://podz-content.spotifycdn.com/audio/clips/7djYaYwZ68KsZDhRHyQGMM/clip_35224_95224.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/2k2BpVnO1ovZ8iRSvjS5CF/clip_1860950_1920500.mp3',
  'https://podz-content.spotifycdn.com/audio/clips/3ASqdzRvCPWDr5NPiDJI5q/clip_1757500_1813800.mp3']}
 
    return render_template('index.html', shows_and_urls=shows_and_urls)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

