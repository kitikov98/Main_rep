import json

writen_dict={
    'id':('Name','Age'),
    655138:('John',32),
    562231:('Arthur', 42),
    623845:('Tomas', 41),
    562462:('Michael', 26),
    213123:('Finn',29),
    321521:('Polly',58)
}

with open('json_dict.json','w') as f:
    json.dump(writen_dict,f)
