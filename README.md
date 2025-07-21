## Inpainting

OpenCV implementation of Telea and Navier-Stokes

A **simple demonstration** of image inpainting using **OpenCV** and **NumPy**. This tool loads a single image and allows you to **inpaint** small areas by clicking on the image. You can choose from two OpenCV inpainting methods:

1. **Telea**  
2. **Navier–Stokes (NS)**  

Additionally, an **interactive** OpenCV window is displayed, where clicks prompt automatic inpainting operations.

---

### Features

1. **Image Validation**:
   - Ensures the provided image path exists and is a valid image format.

3. **Choice of Methods**:
   - **Telea (INPAINT_TELEA)**—fast marching, good for small/smooth areas.
   - **Navier–Stokes (INPAINT_NS)**—partial differential equations (PDEs), better for preserving texture in large areas.

3. **Interactive Mode**:
   - Left‐click on the displayed image to inpaint that region.
   - A circle is defined around the click coordinates, and inpainting is applied automatically.

4. **Console Feedback**:
   - Prints the chosen method, coordinates, and status.

---

### Installation

1. **Clone or Download**:
```bash
git clone https://github.com/YourName/ImageInpaintingTool.git
cd ImageInpaintingTool
```

2. **Dependencies**: 
	- Python >= 3.7
	- OpenCV (opencv-python)
	- NumPy
	- Tkinter (often included with Python on Windows/macOS; on some Linux distros, install python3-tk)

Install via pip:
```bash
pip install opencv-python numpy
```

3. **Run**: 
```bash
python inpainting.py
```

--- 

## Usage

- Left‐Click on the image to apply inpainting at the clicked coordinates.
A small circle (default radius=10) is drawn around that point, then either Telea or NS inpainting is performed (Telea by default).
- Press ESC in the OpenCV window to exit.

### Changing Inpainting Parameters

Inside the code:
```bash
def apply_inpainting(self, target_coords: tuple, radius: int = 10, method: str = 'telea') -> None:
    ...
```
- ***radius***: sets how large an area around your click is inpainted (circle).
- ***method***: 'telea' (default) or 'ns'.

### Detailed Method Notes

- Telea
  - Fast marching technique
  - Prioritizes nearby pixels
  - Less computationally intensive
  - Good for small/smooth areas
- Navier–Stokes (NS)
  - Uses PDEs to propagate linear structures
  - Slower, but better for edges or detailed textures
  - Good for larger areas
 
---   

## Credits & License

Author: Anelia Gaydardzhieva (https://github.com/anphiriel)

(c) 2025, MIT License

## Contact

For questions, suggestions, or contributions, please open an issue in this repository or reach out via GitHub. Feedback is welcomed.
