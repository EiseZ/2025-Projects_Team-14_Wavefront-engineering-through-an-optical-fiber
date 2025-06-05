import numpy as np

beeld-b = 2048
beeld-h = 1536
beeld = np.empty(beeld-b * beeld-h) # Vector van intensiteiten van het beeld per pixel
slm-b = 1920
slm-h = 1200
slm = np.empty(slm-b * slm-h) # Vector van alle phasen van de pixels van de SLM
segment-pixels = 100 # Aantal pixels in een segment, moet een kwadraat zijn en segment-length moet slm-b & slm-h delen
segment-length = np.sqrt(segment-pixels)
n-segments = (slm-b * slm-h) / segment-pixels

# Coordinaten van het focus punt
focus-x = 1000
foxus-y = 1000
focus-i = beeld-b * foxus-y + focus-x # Bereken hiervoor de index van de vector

slm-best-phase = np.empty(slm-b * slm-h) # Uiteindelijke voltages voor de slm voor de beste phasen
slm-segments-best-phase = np.empty(n-segments)
slm-final = np.empty(slm-b * slm-h)

phases = [0, np.pi / 2, (np.pi * 3) / 2] # De phasen die we willen testen voor elk segment

for seg-row in range(0, beeld-b / segment-length): # Itereer over elk segment
    for seg-column in range(0, beeld-h / segment-length):
        best-phase = 0 # Beste phase nu bekend
        best-intensity = 0 # De intensiteit die daarbij hoort
        for phase in phases:
            for row in range(0, segment-length): # Maak in het hele segment de phase zoals we willen
                slm[(seg-row  + row) * slm-b + seg-column * segment-length : [(seg-row  + row) * slm-b + seg-column * segment-length + segment-length] = apply_lut(phase)
            if beeld[focus-i] > best-intensity: # Als de phase beter werkt, noteer dit dan, anders negeren we het
                best-phase = phase
                best-intensity = beeld[focus-i]
        # Sla de beste phase op
        slm-segments-best-phase[seg-row * (slm-b / segment-length) + seg-column] = best-phase
        slm-best-phase[(seg-row  + row) * slm-b + seg-column * segment-length : [(seg-row  + row) * slm-b + seg-column * segment-length + segment-length] = phase 
        slm-final[(seg-row  + row) * slm-b + seg-column * segment-length : [(seg-row  + row) * slm-b + seg-column * segment-length + segment-length] = apply_lut(phase)
