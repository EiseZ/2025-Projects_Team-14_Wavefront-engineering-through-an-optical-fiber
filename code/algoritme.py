#%%

import numpy as np
from pypylon import pylon
import matplotlib.pyplot as plt
from tqdm import tqdm

from slmsuite.hardware.slms.meadowlark import Meadowlark
s = Meadowlark(sdk_path="C:/Program Files/Meadowlark Optics/Blink 1920 HDMI", wav_um=0.633)



#%%
algoritm = 0

beeld_b = 2048
beeld_h = 1536
beeld = np.empty((beeld_h, beeld_b)) # Vector van intensiteiten van het beeld per pixel
lcd_b = s.shape[1]
lcd_h = s.shape[0]
padding_top = 200
padding_bottom = 400
padding_left = 520
padding_right = 800
padding_top = 230 # 210 # 300
padding_bottom = 570 # 450
padding_left = 620
padding_right = 820 # 760 # 900
slm_b = lcd_b - padding_left - padding_right
slm_h = lcd_h - padding_bottom - padding_top
slm = np.empty((slm_h, slm_b)) # Vector van alle phasen van de pixels van de SLM
segment_pixels = 16*16 #20*20 # Aantal pixels in een segment, moet een kwadraat zijn en segment_length moet slm_b & slm_h delen
segment_length = int(np.sqrt(segment_pixels))
n_segments = (slm_b * slm_h) // segment_pixels
print(n_segments)

# Coordinaten van het focus punt
focus_x = 1100
focus_y = 850

# Uiteindelijke voltages voor de slm voor de beste phasen
slm_segments_best_phase = np.zeros((slm_h // segment_length, slm_b // segment_length))
slm_segments_best_intensity = np.zeros((slm_h // segment_length, slm_b // segment_length))
slm_final = np.empty((slm_h, slm_b))

#phases = [2 * np.pi, (2 * np.pi / 5), (4 * np.pi / 5), (6 * np.pi / 5), (8 * np.pi / 5)] # De phasen die we willen testen voor elk segment
phases = [np.pi / 2, 3/2 * np.pi, np.pi]

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()
camera.ExposureTime.SetValue(300)
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

def show_image(img, seg_x, seg_y, phase):
    # A cicle mask to calculate the intensity at the beam
    w = beeld.shape[1]
    h = beeld.shape[0]
    radius = 5
    center = (focus_x, focus_y)

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    
    intensity_beeld = beeld.copy()
    intensity_beeld[~mask] = 0
    intensity = np.sum(intensity_beeld)
    
    fig, axes = plt.subplots(1, 2)
    axes[0].matshow(img)
    axes[0].set_xlim(800, 1200)
    axes[0].set_ylim(600, 1000)
    axes[0].set_title(f"x: {seg_x}, y: {seg_y}, phi: {phase:.3f}, i: {intensity:.5e}, r: {intensity / np.sum(beeld):.5e}")
    axes[1].matshow(slm_segments_best_intensity)
    #slm_map(axes[1][0])
    #s.plot(ax=axes[1][1])
    plt.show()
    return

slm_mapping = np.zeros((slm_h // segment_length, slm_b // segment_length))
oud_beeld = np.empty(beeld.shape)
def slm_map(ax):
    counter = 0
    verschil = beeld - oud_beeld
    delta = 2
    for _, val in np.ndenumerate(verschil):
        if np.abs(val) > delta:
            counter += 1
    if counter >= 1:
        slm_mapping[seg_row][seg_column] = 1
    else:
        slm_mapping[seg_row][seg_column] = 0
    
    ax.matshow(slm_mapping)
    return

def set_matrix(mat, val, from_x, to_x, from_y, to_y):
    for x in range(from_x, to_x):
        for y in range(from_y, to_y):
            mat[x][y] = val
    return mat

s.set_phase(padd_slm(slm), settle=True)
beeld = get_image()
ref_intensity = beeld[focus_y][focus_x] + beeld[focus_y - 1][focus_x] + beeld[focus_y + 1][focus_x] + beeld[focus_y - 1][focus_x - 1] + beeld[focus_y + 1][focus_x - 1]  + beeld[focus_y - 1][focus_x + 1] + beeld[focus_y + 1][focus_x + 1] + beeld[focus_y][focus_x - 1] + beeld[focus_y][focus_x + 1]
if algoritm < 2:
    for seg_row in tqdm(range(0, slm_h // segment_length)): # Itereer over elk segment
        for seg_column in range(0, slm_b // segment_length):
            best_phase = 0 # Beste phase nu bekend
            best_intensity = ref_intensity
            for phase in phases:
                set_matrix(slm, phase, seg_row * segment_length, seg_row * segment_length + segment_length, seg_column * segment_length,  seg_column * segment_length + segment_length)
                s.set_phase(padd_slm(slm), settle=True)
                #oud_beeld = beeld
                beeld = get_image()
                beeld = beeld.astype(np.int64)
                intensity = beeld[focus_y][focus_x] + beeld[focus_y - 1][focus_x] + beeld[focus_y + 1][focus_x] + beeld[focus_y - 1][focus_x - 1] + beeld[focus_y + 1][focus_x - 1]  + beeld[focus_y - 1][focus_x + 1] + beeld[focus_y + 1][focus_x + 1] + beeld[focus_y][focus_x - 1] + beeld[focus_y][focus_x + 1]
                show_image(beeld, seg_column, seg_row, phase)
                if intensity > best_intensity: # Als de phase beter werkt, noteer dit dan, anders negeren we het
                    best_phase = phase
                    best_intensity = intensity
            # Sla de beste phase op
            slm_segments_best_phase[seg_row][seg_column] = best_phase
            slm_segments_best_intensity[seg_row][seg_column] = best_intensity
            set_matrix(slm_final, best_phase, seg_row * segment_length, seg_row * segment_length + segment_length, seg_column * segment_length,  seg_column * segment_length + segment_length)
                
            if algoritm == 0:
                # Reset slm
                slm = np.empty((slm_h, slm_b))
                s.set_phase(padd_slm(slm), settle=True)
            else:
                slm = slm_final
                s.set_phase(padd_slm(slm_final), settle=True)
    

else:
    a = 1

s.set_phase(padd_slm(slm_final), settle=True)
s.save_phase()
beeld = get_image()
intensity = beeld[focus_y][focus_x] + beeld[focus_y - 1][focus_x] + beeld[focus_y + 1][focus_x] + beeld[focus_y - 1][focus_x - 1] + beeld[focus_y + 1][focus_x - 1]  + beeld[focus_y - 1][focus_x + 1] + beeld[focus_y + 1][focus_x + 1] + beeld[focus_y][focus_x - 1] + beeld[focus_y][focus_x + 1]
show_image(beeld, 0, 0, 0)
camera.ExposureTime.SetValue(70)
beeld = get_image()
intensity = beeld[focus_y][focus_x] + beeld[focus_y - 1][focus_x] + beeld[focus_y + 1][focus_x] + beeld[focus_y - 1][focus_x - 1] + beeld[focus_y + 1][focus_x - 1]  + beeld[focus_y - 1][focus_x + 1] + beeld[focus_y + 1][focus_x + 1] + beeld[focus_y][focus_x - 1] + beeld[focus_y][focus_x + 1]
show_image(beeld, 0, 0, 0)
plt.matshow(slm_segments_best_intensity)
plt.show()
s.plot()
plt.show()
camera.Close()
