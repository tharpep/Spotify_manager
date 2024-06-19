from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": """Take in a list of songs first, this is a playlist given to you by the user.
                                  Take this playlist of and give back the top 5 most popular songs, make sure to read
                                  the entire list first, then sort the popularity. Give the new playlist the same format. Similar to:
                                      [(song, popularity), ..., (song, popularity)]
     
     
                                  Think?"""},
    {"role": "user", "content": """[('GONE, GONE / THANK YOU', 71), ('See You Again (feat. Kali Uchis)', 85), ('90210 (feat. Kacy Hill)', 75), ('Ninety', 51), ('Mr. Rager', 65), ('Tequila Shots', 61), ('Sundress', 81), ('Ivy', 79), ('Bad Habit', 71), ("Surfin'", 24), ('Lemonade (feat. Gunna, Don Toliver & NAV)', 6), ('Alright', 53), ('Dancing in My Room', 62), ('I. Flight of the Navigator', 0), ('Chanel', 72), ('Redbone', 5), ('waves - Tame Impala Remix', 59), ('Biking', 62), ('Heaven Only Knows', 37), ('Mirror', 0), ('United In Grief', 0), ('Lost', 78), ('I THINK', 67), ('New Person, Same Old Mistakes', 72), ('L$D', 
66), ('Backseat Freestyle', 64), ('Sweet Life', 65), ('Retro [ROUGH]', 0), ('Do What I Want', 41), ("Day 'N' Nite (nightmare)", 66), ('Eventually', 70), ('Sacrifice', 65), ('Gasoline', 63), ('NEW MAGIC WAND', 74), ('IMY2 (with Kid Cudi)', 57), ('OUTERSPACE (feat. Baby Keem)', 50), ('Just What I Am', 60), ('Blue World', 68), ('Hell N Back', 71), ('Pursuit Of Happiness (Nightmare)', 65), ('Paradise', 45), ('HIT EM WHERE IT HURTS', 0), ('Guilty Conscience - Tame Impala Remix', 26), ('Feel Good Inc.', 79), ('Dang! (feat. Anderson .Paak)', 68), ('All The Stars (with SZA)', 82), ('Long Beach', 52), ('Amber', 0), ('No Role Modelz', 6), ('505', 74), ('Rollin (feat. Future & Khalid)', 58), ('Summertime Magic', 57), ('3005', 2), ('Alright', 76), ('Heartbeat', 1), ('i', 65), ('Money Trees', 76), ('Everybody Talks', 0), ('You 
Know It', 32), ('Freaking Out the Neighborhood', 0), ('Blinding Lights', 84), ('Brazil', 78), ('Walking On A Dream', 75), ('Eleven', 51), ('The Less I Know The Better', 81), ('Poison', 66), ('Fluorescent Adolescent', 65), ("Let's Go", 49), ('Humility (feat. George Benson)', 59), ('EARFQUAKE', 77), ('Slide (feat. Frank Ocean & Migos)', 70), ('Sweater Weather', 86), ('Location', 71), ('Nights', 74), ('In My Room', 69), ('Super Rich Kids', 72), ('Pink + White', 83), ('Mystery Lady', 65), ("Wesley's Theory", 68), ('No More Parties In LA', 66), ('Triple Double', 18), ('Man On The Moon', 51), ('Neighbors', 65), ('HIGHEST IN THE ROOM', 79), ('ELEMENT.', 67), ('Maytag (Tax Free)', 0), ('family ties (with Kendrick Lamar)', 77), ('King Kunta', 71), ('Self Care', 71), ('16', 71), ('She Knows This', 45), ('Sober', 64), ('Novacane', 76), ('Pyramids', 73), ('Die Hard', 71), ('Father Time (feat. Sampha)', 67), ('love.', 57), ('By Design', 51), ('Passionfruit', 78), ("Livin' My Truth", 47)]"""}
  ]
)

print(completion.choices[0].message)