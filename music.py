import pysynth_b as psb # a, b, e, and s variants available

song = (
  ('c', 4), ('c*', 4), ('eb', 4), 
  ('g#', 4),  ('g*', 2), ('g5', 4),
  ('g5*', 4), ('r', 4), ('e5', 16),
  ('f5', 16),  ('e5', 16),  ('d5', 16),
  ('e5*', 4) 
)

# Beats per minute (bpm) is really quarters per minute here
psb.make_wav(song, fn = "danube.wav", leg_stac = .7, bpm = 180)