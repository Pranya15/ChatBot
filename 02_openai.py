import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

command = """
Wow yrrr
Par aaja bhai
Abhi ek do school friend ki entry bhi karani hai fest mei
😭😭
Idr tho mera hogayaa
Aab
54 attendance hai jana hi nhi meko yarr
Par aaja bhai
Hn kri hu try mei
Aab
Aana toh hai
54 attendance hai jana hi nhi meko yarr
Aacha
Kha nhi jana
Clg
Akele
Hogaya aab Mera 2 saal Boht bhai
Aacha
Abhi ek do school friend ki entry bhi karani hai fest mei
Meko bhi 😭😭😭😭😭
Db ki fee kitni hai wha
Db kya hai
Kon aara hai tumhare yha fest mei
Db kya hai
Debard
Nhi pta yar
Aacha
Kon aara hai tumhare yha fest mei
Bhai idr dj vj wala hota 2 din dance gana wala games wala
Abhi kuch hb
Tho mei nhi Jaa rhi
Dress bhi lena padega
+ koi h hi nhi
Kya karungu
Ja kar
Nitya or uski bandi ko nhi dekhna meko
Aacha
Mtlb koi celebrity nhi aata
Singer
Eha
Wha*
Ghanta
Jbp mei hi nhi aata
Aaxha
Abe yrr
😭😭
😔
Yha pure dehradun mei khi bpraak talwinder amaan malik
Tabhi tho mumbai gai thi
Indore bhi jaate hai
Aacha
Pass hai vo tho
Udr sab hota
Bhai fee mei hota hai yha
Ipl bhi 😮‍💨
Bhai fee mei hota hai yha
Bhai tho fees bhi tho itne lete
Hn woh toh hai
😭😭😭
Ipl bhi 
Hn
Idr 70 k mei
Kon kon le kar
Aayenge
Bhai
Mera yearly hai
70 k bhi yearly
Hein
Han babu
Aacha
"""

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are Pranya, an Indian coder who speaks Hindi and English and replies casually."},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)