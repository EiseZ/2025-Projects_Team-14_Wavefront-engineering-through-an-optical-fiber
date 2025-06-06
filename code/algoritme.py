
#%%

import numpy as np
from pypylon import pylon
import matplotlib.pyplot as plt

from slmsuite.hardware.slms.meadowlark import Meadowlark
s = Meadowlark(sdk_path="C:/Program Files/Meadowlark Optics/Blink 1920 HDMI", verbose=True, wav_um=0.633)



#%%
beeld_b = 2048
beeld_h = 1536
beeld = np.empty((beeld_h, beeld_b)) # Vector van intensiteiten van het beeld per pixel
lcd_b = s.shape[1]
lcd_h = s.shape[0]
padding_top = 300
padding_bottom = 400
padding_left = 720
padding_right = 700
slm_b = lcd_b - padding_left - padding_right
slm_h = lcd_h - padding_bottom - padding_top
slm = np.empty((slm_h, slm_b)) # Vector van alle phasen van de pixels van de SLM
segment_pixels = 50*50 # Aantal pixels in een segment, moet een kwadraat zijn en segment_length moet slm_b & slm_h delen
segment_length = int(np.sqrt(segment_pixels))
n_segments = (slm_b * slm_h) // segment_pixels
print(n_segments)

# Coordinaten van het focus punt
focus_x = 1000
focus_y = 800

# Uiteindelijke voltages voor de slm voor de beste phasen
slm_segments_best_phase = np.zeros((slm_h // segment_length, slm_b // segment_length))
slm_final = np.empty((slm_h, slm_b))

phases = [0, np.pi / 2, (np.pi * 3) / 2] # De phasen die we willen testen voor elk segment

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()
camera.ExposureTime.SetValue(20)
converter = pylon.ImageFormatConverter()
# Convert to OpenCV format
converter.OutputPixelFormat = pylon.PixelType_Mono8
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

def padd_slm(slm):
    return np.pad(slm, ((padding_top, padding_bottom), (padding_left, padding_right)))

def get_image():
    img = np.empty((beeld_h, beeld_b))
    camera.StartGrabbingMax(1)
    while camera.IsGrabbing():
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        if grabResult.GrabSucceeded():
            image = converter.Convert(grabResult)
            img = image.GetArray()

        grabResult.Release()
    camera.StopGrabbing()
    return img

def show_image(img):
    
    plt.matshow(img)
    plt.xlim(800, 1200)
    plt.ylim(600, 1000)
    plt.show()
    return

for seg_row in range(0, slm_h // segment_length): # Itereer over elk segment
    for seg_column in range(0, slm_b // segment_length):
        best_phase = 0 # Beste phase nu bekend
        best_intensity = 0 # De intensiteit die daarbij hoort
        for phase in phases:
            slm[seg_row * segment_length : seg_row * segment_length + segment_length][seg_column * segment_length : seg_column * segment_length + segment_length] = phase
            print(seg_row, seg_column, ":", phase)
            s.set_phase(padd_slm(slm), settle=True)
            show_image(beeld)
            beeld = get_image()
            if beeld[focus_y][focus_x] > best_intensity: # Als de phase beter werkt, noteer dit dan, anders negeren we het
                best_phase = phase
                best_intensity = beeld[focus_y][focus_x]
        # Sla de beste phase op
        slm_segments_best_phase[seg_row][seg_column] = best_phase
        slm_final[seg_row * segment_length : seg_row * segment_length + segment_length][seg_column * segment_length : seg_column * segment_length + segment_length] = best_phase 
        
        # Reset slm
        slm = np.empty((slm_h, slm_b))


s.set_phase(padd_slm(slm_final), settle=True)
beeld = get_image()
show_image(beeld)
camera.Close()
