#%%

import numpy as np
from pypylon import pylon
import matplotlib.pyplot as plt
from tqdm import tqdm
import time

start_time = time.time()

from slmsuite.hardware.slms.meadowlark import Meadowlark
s = Meadowlark(sdk_path="C:/Program Files/Meadowlark Optics/Blink 1920 HDMI", wav_um=0.633)



#%%
algoritm = 0

beeld_b = 2048
beeld_h = 1536
beeld = np.empty((beeld_h, beeld_b)) # Vector van intensiteiten van het beeld per pixel
lcd_b = s.shape[1]
lcd_h = s.shape[0]
padding_top = 100 #100 #102 #106 #110
padding_bottom = 450 #450 #452 #456 #460
padding_left = 520 #520 #522 #526 #530
padding_right = 750 #750 #752 #756 #760
#padding_top = 100
#padding_bottom = 450
#padding_left = 520
#padding_right = 750
slm_b = lcd_b - padding_left - padding_right
slm_h = lcd_h - padding_bottom - padding_top
slm = np.empty((slm_h, slm_b)) # Vector van alle phasen van de pixels van de SLM
segment_pixels =25*25 #25*25 #19*19 # #29*29 #38*38 #21*21 Aantal pixels in een segment, moet een kwadraat zijn en segment_length moet slm_b & slm_h delen
segment_length = int(np.sqrt(segment_pixels))
n_segments = (slm_b * slm_h) // segment_pixels
print(n_segments)

# Coordinaten van het focus punt
focus_x = 1050
focus_y = 750

# Uiteindelijke voltages voor de slm voor de beste phasen
slm_segments_best_phase = np.zeros((slm_h // segment_length, slm_b // segment_length))
slm_segments_best_intensity = np.zeros((slm_h // segment_length, slm_b // segment_length))
slm_final = np.empty((slm_h, slm_b))

# Matrix voor intensiteitsverandring per segment
diff_mat = np.zeros((slm_h // segment_length, slm_b // segment_length), dtype=np.uint64)

#phases = [np.pi] #[np.pi] #[(2*np.pi)/3, (4*np.pi)/3] [(2*np.pi)/5, (4*np.pi)/5,(6*np.pi)/5, (8*np.pi)/5 ] [(2*np.pi)/4, (4*np.pi)/4,(6*np.pi)/4] # De phasen die we willen testen voor elk segment
#phases = [(np.pi)]
phases = [(2*np.pi)/4, (4*np.pi)/4,(6*np.pi)/4]
#phases = [(2*np.pi)/5, (4*np.pi)/5,(6*np.pi)/5, (8*np.pi)/5 ]
#phases = [(2*np.pi)/3, (4*np.pi)/3]

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

radius = 0
def calc_power_ratio(beeld):
    # A cicle mask to calculate the intensity at the beam
    w = beeld.shape[1]
    h = beeld.shape[0]
    i = 0
    j = 0
    k = 0
    l = 0
    while beeld[focus_y + i][focus_x] > beeld[focus_y][focus_x] * 0.135:
        i += 1
    while beeld[focus_y - j][focus_x] > beeld[focus_y][focus_x] * 0.135:
        j += 1
    while beeld[focus_y][focus_x + k] > beeld[focus_y][focus_x] * 0.135:
        k += 1
    while beeld[focus_y][focus_x - l] > beeld[focus_y][focus_x] * 0.135:
        l += 1
    radius = max(i,j,k,l)
    center = (focus_x, focus_y)
    print(radius)

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    
    intensity_beeld = beeld.copy()
    intensity_beeld[~mask] = 0
    intensity = np.sum(intensity_beeld)
    
    return intensity / np.sum(beeld)

def show_image(img, seg_x, seg_y, phase, del_int_max):
    
    diff(seg_x, seg_y, del_int_max)
    fig, axes = plt.subplots(2, 2)
    axes[0][0].matshow(img)
    axes[0][0].set_xlim(800, 1200)
    axes[0][0].set_ylim(600, 1000)
    axes[0][0].set_title(f"x: {seg_x}, y: {seg_y}, phi: {phase:.3f}, r: {calc_power_ratio(beeld):.5e}")
    axes[0][1].matshow(slm_segments_best_intensity)
    axes[1][0].matshow(diff_mat)
    #s.plot(ax=axes[1][1])
    plt.show()
    return

def show_image(img, seg_x, seg_y, phase, del_int_max):
    plt.matshow(img)
    plt.xlim(800, 1200)
    plt.ylim(600, 1000)
    plt.title(f"x: {seg_x}, y: {seg_y}, phi: {phase:.3f}")
    plt.show()
    return

def show_final_image(img, seg_x, seg_y, phase, del_int_max):
    fig, axes = plt.subplots(1, 2)
    axes[0].matshow(img,cmap="hot")
    axes[0].set_xlim(800, 1200)
    axes[0].set_ylim(600, 1000)
    axes[0].set_title(f"x: {seg_x}, y: {seg_y}, phi: {phase:.3f}, r: {calc_power_ratio(beeld):.5e}")
    axes[1].matshow(slm_segments_best_intensity)
    #s.plot(ax=axes[1][1])
    plt.show()

def diff(seg_row, seg_column, del_int_max):
    del_int = beeld - ref_beeld_intensity
    del_int[del_int < 0] = 0
    del_int = np.sum(del_int)
    if del_int > del_int_max:
        del_int_max = del_int
        diff_mat[seg_row][seg_column] = del_int_max

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
ref_beeld_intensity = beeld.copy()
ref_intensity = beeld[focus_y][focus_x]
if algoritm < 2:
    for seg_row in tqdm(range(0, slm_h // segment_length)): # Itereer over elk segment
        for seg_column in range(0, slm_b // segment_length):
            del_int_max = 0
            best_phase = 0 # Beste phase nu bekend
            best_intensity = ref_intensity
            for phase in phases:
                set_matrix(slm, phase, seg_row * segment_length, seg_row * segment_length + segment_length, seg_column * segment_length,  seg_column * segment_length + segment_length)
                s.set_phase(padd_slm(slm), settle=True)
                #oud_beeld = beeld
                beeld = get_image()
                beeld = beeld.astype(np.int64)
                intensity = beeld[focus_y][focus_x]
                show_image(beeld, seg_column, seg_row, phase, del_int_max)
                if intensity > best_intensity: # Als de phase beter werkt, noteer dit dan, anders negeren we het
                    best_phase = phase
                    best_intensity = intensity
                np.save("speckle", beeld)
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
end_time = time.time()
s.set_phase(padd_slm(slm_final), settle=True)
s.save_phase()
beeld = get_image()
show_final_image(beeld, 0, 0, 0, del_int_max)

exposure_time = 200
camera.ExposureTime.SetValue(exposure_time)
beeld = get_image()

while np.any(beeld[focus_y-5:focus_y+5,focus_x-5:focus_x+5] >= 255):
    print(f"OVERBELICHT! We proberen {exposure_time - 5}")
    exposure_time -= 5
    print(exposure_time)
    camera.ExposureTime.SetValue(exposure_time)
    beeld = get_image()
    if exposure_time < 30:
        exposure_time = 200
        _ = input("Stop de nieuwe filter erop van 0.6")
        continue

new_focus_y, new_focus_x = np.unravel_index(np.argmax(beeld[focus_y-5:focus_y+5,focus_x-5:focus_x+5]), (10, 10))
new_focus_y += focus_y - 5
new_focus_x += focus_x - 5
focus_y, focus_x = new_focus_y, new_focus_x
show_final_image(beeld, 0, 0, 0, del_int_max)         

plt.matshow(slm_segments_best_intensity)
plt.show()
s.plot()
plt.show()
camera.Close()


with open("last_result.txt", "w") as f:
    f.write(f"Number of segments: {n_segments}\nAmount of phases: {len(phases)}\nPower ratio: {calc_power_ratio(beeld)}\nTotal time: {end_time - start_time}")
np.save("last_beeld", beeld)