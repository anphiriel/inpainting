"""
inpainting.py

Inpainting demo

Author: Anelia Gaydardzhieva (https://github.com/Anelia1)
(c) 2025, MIT License 

A straightforward image inpainting tool built on OpenCV. 
This module defines an ImageInpaintingTool class that loads an image, 
supports both Telea and Navier-Stokes (NS) inpainting methods, 
and provides an interactive OpenCV session for inpainting by clicking on the image. 
It serves as a practical example of how to handle user input, 
apply inpainting algorithms, and display updated results in real-time.
"""

import cv2
import os
import numpy as np

class ImageInpaintingTool:
    def __init__(self, image_path: str):
        '''
        Initialize the ImageInpaintingTool class and validate the input image.

        Parameters:
        image_path: str
            Path to the input image.

        Raises:
        FileNotFoundError: If the image path does not exist.
        ValueError: If the image cannot be loaded or is in an invalid format.
        '''
        self.image_path = image_path
        self.image = self._load_image()

    def _load_image(self) -> np.ndarray:
        '''
        Load and validate the image file.

        Returns:
        np.ndarray
            The loaded image.

        Raises:
        FileNotFoundError: If the image path does not exist.
        ValueError: If the image cannot be loaded or is in an invalid format.
        '''
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Error: The image path '{self.image_path}' does not exist.")

        image = cv2.imread(self.image_path)
        if image is None:
            raise ValueError("Error: Could not load the image. Ensure the file is a valid image format.")

        return image

    def apply_inpainting(self, target_coords: tuple, radius: int = 10, method: str = 'telea') -> None:
        '''
        Apply inpainting to the specified coordinates.

        Parameters:
        target_coords: tuple
            Coordinates (x, y) of the area to be inpainted.
        radius: int, optional
            Radius of the area to be inpainted (default is 10).
        method: str, optional
            Inpainting method to use ('telea' or 'ns').
        
        Notes:
            Telea:  
                Uses fast marching
                Propagates pixel values from the boundary of the masked region inward
                Prioritises nearby pixels 
                Computationally less intensive than NS (faster)
                Efficient and effective for small, smooth regions

            Navier-Stokes (NS): 
                Uses partial differential equations (PDEs)
                Propagates linear structures (e.g. edges)
                Computationally more intensive (slower)
                Aims to preserve both texture and structural information 
                Better for detailed textures and larger areas

        Raises:
        ValueError: If the specified inpainting method is invalid.
        '''
        mask = self._create_mask(target_coords, radius)
        flags = self._get_inpainting_flags(method)
        self.image = cv2.inpaint(self.image, mask, inpaintRadius=radius, flags=flags)
        print(f"Inpainting applied at {target_coords} using '{method}' method.")

    def _create_mask(self, target_coords: tuple, radius: int) -> np.ndarray:
        '''
        Create a mask for the inpainting process.

        Parameters:
        target_coords: tuple
            Coordinates (x, y) of the target area.
        radius: int
            Radius of the target area.

        Returns:
        np.ndarray
            A mask with the target area marked.
        '''
        mask = np.zeros(self.image.shape[:2], dtype=np.uint8)
        cv2.circle(mask, target_coords, radius, 255, -1)
        return mask

    def _get_inpainting_flags(self, method: str) -> int:
        '''
        Get the appropriate inpainting flags based on the method.

        Parameters:
        method: str
            Inpainting method ('telea' or 'ns').

        Returns:
        int
            OpenCV flag for the specified inpainting method.

        Raises:
        ValueError: If the method is not 'telea' or 'ns'.
        '''
        if method.lower() == 'telea':
            return cv2.INPAINT_TELEA
        elif method.lower() == 'ns':
            return cv2.INPAINT_NS
        else:
            raise ValueError("Invalid method. Choose 'telea' or 'ns'.")

    def _handle_mouse_click(self, event, x, y, flags, param):
        '''
        Mouse callback to handle click events for inpainting.

        Parameters:
        event: int
            OpenCV mouse event type.
        x: int
            X-coordinate of the click.
        y: int
            Y-coordinate of the click.
        flags: int
            Flags associated with the mouse event.
        param: any
            Additional parameters (not used).
        '''
        if event == cv2.EVENT_LBUTTONDOWN:
            click_coords = (x, y)
            print(f"Coordinates received: {click_coords}")
            self.apply_inpainting(click_coords)

    def _initialize_interactive_session(self):
        '''
        Set up the OpenCV interactive session with mouse callback.
        '''
        cv2.namedWindow("Image Inpainting")
        cv2.setMouseCallback("Image Inpainting", self._handle_mouse_click)

    def run_interactive_session(self) -> None:
        '''
        Run an interactive OpenCV window for inpainting.
        '''
        self._initialize_interactive_session()
        print("Press ESC to exit.")

        while True:
            cv2.imshow("Image Inpainting", self.image)
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC key to exit
                break

        cv2.destroyAllWindows()
        print("Interactive session ended.")

if __name__ == '__main__':
    image_path = "data/example.png"  # Replace with your image path

    try:
        inpainting_tool = ImageInpaintingTool(image_path)
        print("Image loaded successfully.")
        inpainting_tool.run_interactive_session()
    except Exception as e:
        print(e)

