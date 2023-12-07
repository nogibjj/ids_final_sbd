from flask import Flask, render_template
import pandas as pd
import os

# Read the dataset

app = Flask(__name__)

@app.route("/")
def index():
  # Create a dictionary to store showName and corresponding episode audio URLs
    shows_and_data = {'The Joe Rogan Experience': {'total_episodes': 2228,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/4LIP98lu8RxvuW1U4E2Lxe/clip_2436994_2484398.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/3lwSgYy2U5pHnBJPiLEsQY/clip_160802_226197.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/6ER3FdrVjahM9r2PMUHE7G/clip_3088120_3160800.mp3'],
  'external_url': 'https://open.spotify.com/show/4rOoJ6Egrf8K2IrywzwOMk',
  'description': 'The official podcast of comedian Joe Rogan. Follow The Joe Rogan Clips show page for some of the best moments from the episodes.',
  'duration': 138},
 'Call Her Daddy': {'total_episodes': 314,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/4BjokGoSiSD61Mq99vdkr0/clip_587850_632850.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/6aDzlDnNaqhplVCYI7nWWF/clip_2609500_2667600.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/1CxpuyukjsNS4kTGxSaoDj/clip_2417400_2467700.mp3'],
  'external_url': 'https://open.spotify.com/show/7bnjJ7Va1nM07Um4Od55dW',
  'description': 'The most-listened to podcast by women on Spotify, Alex Cooper’s Call Her Daddy has been creating conversation since 2018. Cooper cuts through the bullshit with the topics and guests who are breaking the mold—and asking the burning questions you want the answers to. There will be joy, there will be tears. There will be everything in between. New episodes drop on Wednesday only on Spotify. Want more? Join the Daddy Gang @callherdaddy',
  'duration': 46},
 'New Heights with Jason and Travis Kelce': {'total_episodes': 67,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/1LClRmxBm64D95vEBMFDID/clip_2970200_3039050.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/3Eja8YBG8Ab6HF3IqkEcOv/clip_3526400_3587800.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/5rS9c1jGqHGEJoquVw2l01/clip_1999150_2068949.mp3'],
  'external_url': 'https://open.spotify.com/show/1y3SUbFMUSESC1N43tBleK',
  'description': 'Football’s funniest family duo — Jason Kelce from the Philadelphia Eagles and Travis Kelce from the Kansas City Chiefs —\xa0team up to provide next-level access to life in the league as it unfolds. The two brothers and Super Bowl champions drop weekly insights about their games and share unique perspectives on trending NFL news and sports headlines. Plus, entertaining stories from a combined 21 years in the league, off-field interests, and engaging conversations with special guests.\xa0\xa0\xa0  Watch and listen to new episodes every Wednesday during the NFL season & check us out on Instagram, Twitter and Tiktok for all the best moments from the show.',
  'duration': 68},
 'Tosh Show': {'total_episodes': 5,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/7rS4yFqW5TX7N5Z9LfML59/clip_0_60000.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/2RuXEx7OstxqbAhY1AV9jG/clip_1598000_1648650.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/6LF5K2FxVFXmQ6Rv1G74z8/clip_545037_605037.mp3'],
  'external_url': 'https://open.spotify.com/show/2zzBL9Oe9bygUGlOban5fW',
  'description': "Tosh Show is a window into the mind of comedian Daniel Tosh. Each week Daniel interviews people from all walks of life that he finds interesting, shares his take on current events, and gives you a little insight into his world. Nothing is off limits and with endless topics to explore, Tosh and his guests will satisfy everyone's curiosity.",
  'duration': 39},
 "The President's Daily Brief": {'total_episodes': 321,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/24x9Rbm0ShvlAfzJkKC0Ec/clip_322392_382392.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/1jZX12S6mCNNnk1WcpB1Bi/clip_52000_103400.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/1XgU7TTcP3LxZ1vMyjbyIB/clip_164800_225500.mp3'],
  'external_url': 'https://open.spotify.com/show/6VpV9ZlbQTzMngKilhJlZs',
  'description': "Each morning, the President of the United States receives a highly classified briefing on the most important issues facing the country -- The President's Daily Brief. Now you can hear your very own PDB, in the form of a podcast, every morning at 6am Eastern, and every afternoon at 4pm Eastern. You'll get 20 minutes of the most important topics of the day and why you should care, arming you with what you need to know to help solve America's most pressing challenges. Former CIA Operations Officer Mike Baker hosts new episodes daily.",
  'duration': 16},
 'Huberman Lab': {'total_episodes': 182,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/0hStP6Fv1h0AeKWq7YhFIs/clip_2463000_2534800.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/1RirXlMrQTFpvUeuDt1mUB/clip_656750_704650.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/02m9tjqKfSSUn1NXmMTaXo/clip_1736800_1796700.mp3'],
  'external_url': 'https://open.spotify.com/show/79CkJF3UJTHFV8Dse3Oy0P',
  'description': 'Huberman Lab discusses neuroscience — how our brain and its connections with the organs of our body control our perceptions, our behaviors, and our health. We also discuss existing and emerging tools for measuring and changing how our nervous system works.  Andrew Huberman, Ph.D., is a neuroscientist and tenured professor in the department of neurobiology, and by courtesy, psychiatry and behavioral sciences at Stanford School of Medicine. He has made numerous significant contributions to the fields of brain development, brain function and neural plasticity, which is the ability of our nervous system to rewire and learn new behaviors, skills and cognitive functioning.\xa0 Huberman\xa0is a McKnight Foundation and Pew Foundation Fellow and was awarded the Cogan Award, given to the scientist making the most significant discoveries in the study of vision, in 2017. His lab’s most recent work focuses on the influence of vision and respiration on human performance and brain states such as fear and courage. He also works on neural regeneration and directs a clinical trial to promote visual restoration in diseases that cause blindness.\xa0Huberman is also actively involved in developing tools now in use by the elite military in the U.S. and Canada, athletes, and technology industries to optimize performance in high stress environments, enhance neural plasticity, mitigate stress and optimize sleep.\xa0\xa0 Work from the\xa0Huberman\xa0Laboratory at Stanford School of Medicine has been published in top journals including Nature, Science and Cell and has been featured in TIME, BBC, Scientific American, Discover and other top media outlets.\xa0 In 2021, Dr. Huberman launched the Huberman Lab podcast. The podcast is frequently ranked in the top 5 of all podcasts globally and is often ranked #1 in the categories of Science, Education, and Health & Fitness.',
  'duration': 112},
 'This Past Weekend w/ Theo Von': {'total_episodes': 357,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/5KcqCbnKduS7raienvCTxV/clip_2732450_2786000.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/1OZ66KpOqkAARUIiWuuQAD/clip_735650_805300.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/0XWkJ836Mbhf0j6BXhpdUU/clip_3270500_3331500.mp3'],
  'external_url': 'https://open.spotify.com/show/6PwE1CIZsgfrhX6Bw96PUN',
  'description': 'What happened this past weekend. And sometimes what happened on other days.',
  'duration': 83},
 'Who Killed JFK?': {'total_episodes': 5,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/7djYaYwZ68KsZDhRHyQGMM/clip_35224_95224.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/2k2BpVnO1ovZ8iRSvjS5CF/clip_1860950_1920500.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/3ASqdzRvCPWDr5NPiDJI5q/clip_1757500_1813800.mp3'],
  'external_url': 'https://open.spotify.com/show/6hD4xxJbvSRRyYoG196aSw',
  'description': "Who Killed JFK? For 60 years, we are still asking that question. In commemoration of the 60th anniversary of President John F. Kennedy's tragic assassination, legendary filmmaker Rob Reiner teams up with award-winning journalist Soledad O’Brien to tell the history of America’s greatest murder mystery. They interview CIA officials, medical experts, Pulitzer-prize winning journalists, eyewitnesses and a former Secret Service agent who, in 2023, came forward with groundbreaking new evidence. They dig deep into the layers of the 60-year-old question ‘Who Killed JFK?’, how that question has shaped America, and why it matters that we’re still asking it today.",
  'duration': 34},
 'What Now? with Trevor Noah': {'total_episodes': 5,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/6twDxOjbfy4HYqoy7i5In5/clip_1373400_1417932.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/6cVpbp2WlMytx1Yo0M7y8d/clip_2469300_2540600.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/65qx4N4423KajHGX8BkUGK/clip_1366950_1410900.mp3'],
  'external_url': 'https://open.spotify.com/show/122imavATqSE7eCyXIcqZL',
  'description': "Hear Trevor Noah in a way you’ve never heard him before. “What Now? with Trevor Noah” is a show wherein each episode Trevor will go deep with a special guest, including entertainers, CEOs, actors, athletes, and thought leaders. These are the kind of conversations that happen behind the scenes, full of radical candor, authentic back-and-forths, and honest reactions, with Trevor bringing to bear his classic, effortlessly playful and equally probing style. Produced by Spotify Studios in partnership with Day Zero Productions, Fulwell 73, and Audacy's Pineapple Street Studios.",
  'duration': 46},
 'Bad Friends': {'total_episodes': 200,
  'urls': ['https://podz-content.spotifycdn.com/audio/clips/5zDlaJrt21nSbNvTew70W0/clip_2215100_2266600.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/6JFAiBOueSwh3Puyr89yf8/clip_3344100_3416600.mp3',
   'https://podz-content.spotifycdn.com/audio/clips/4PlfzYZTftxz848MIuCYTS/clip_1902700_1956700.mp3'],
  'external_url': 'https://open.spotify.com/show/3gaGfrqgnVqUBNDdtv5p3S',
  'description': 'Andrew Santino and Bobby Lee present BAD FRIENDS. New episodes every Monday!FOLLOW US!Bad Friends:https://www.instagram.com/badfriendspodhttps://twitter.com/badfriends_podhttp://www.badfriendspod.comAndrew Santino:https://www.instagram.com/cheetosantinohttps://twitter.com/CheetoSantinohttps://www.youtube.com/andrewsantinowhiskeygingerBobby Lee:https://www.instagram.com/bobbyleelivehttps://twitter.com/bobbyleelivehttp://bit.ly/SubscribeToTigerBelly',
  'duration': 69}}
 
    return render_template('index.html', shows_and_data=shows_and_data)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

