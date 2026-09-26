"""Genera index.html a partir de src/corto.html y la transcripción JSON."""
import json

with open('WhatsApp_Audio_2026-09-26_at_5.44.40_PM_spa.json', encoding='utf-8') as f:
    data = json.load(f)
words = [[w['start_time'], w['end_time'], w['text']]
         for s in data['segments'] for w in s['words'] if w['text'].strip()]
with open('src/corto.html', encoding='utf-8') as f:
    html = f.read()
html = html.replace('__WORDS__', json.dumps(words, ensure_ascii=False, separators=(',', ':')))
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'index.html generado con {len(words)} palabras')
