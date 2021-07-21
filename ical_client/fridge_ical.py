from datetime import datetime, timedelta
import sys
import yaml
import caldav

stream      = open(sys.argv[1], 'r')
loadedFile  = yaml.load(stream, Loader=yaml.SafeLoader)
_cfg        = loadedFile['fridge_ical']

today   = datetime.now()
delta7  = timedelta(days = 7)
delta21 = timedelta(days = 21)
a = today - delta7
b = today + delta21

client = caldav.DAVClient(url=_cfg['url'], username=_cfg['user'], password=_cfg['passwd'])
principal = client.principal()
calendar = principal.calendar(name=_cfg['name'])

events_fetched = calendar.date_search(a, b, expand=True)

print('BEGIN:VCALENDAR')
print('VERSION:2.0')
print('X-WR-CALNAME:'+_cfg['name'])
print('X-APPLE-CALENDAR-COLOR:#0E61B9FF')

for e in events_fetched:
    print(e.data.replace('BEGIN:VCALENDAR','').replace('END:VCALENDAR',''))

print('END:VCALENDAR')