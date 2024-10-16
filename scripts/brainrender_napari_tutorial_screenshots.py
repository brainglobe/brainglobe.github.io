import napari
from skimage.io import imsave
from skimage.draw import disk
import pytest
import numpy as np
import shutil
from pathlib import Path

VIEWPORT_WIDTH = 1400
VIEWPORT_HEIGHT = 700

COMPARE_OR_REGENERATE = "REGENERATE"
RELATIVE_PATH_FOR_SCREENSHOTS = Path("./docs/source/tutorials/images/brainrender-napari/")    

@pytest.fixture
def standard_size_viewer(qtbot):
    viewer = napari.Viewer()
    viewer.window.resize(VIEWPORT_WIDTH, VIEWPORT_HEIGHT)
    yield viewer
    viewer.close()

@pytest.fixture
def take_viewer_screenshot(qtbot):
    def _take_viewer_screenshot(viewer, path):
        qtbot.wait(2000) # figure out how replace with qtbot.wait_exposed instead
        screenshot = viewer.window.screenshot()
        # hackily stick in a green point (or later, a cursor) at (x,y) with:
        # screenshot[y, x] = [0, 255, 0, 255]
        imsave(path, screenshot)
    return _take_viewer_screenshot

@pytest.fixture
def clean_atlas_manager_widget(tmp_path, standard_size_viewer, take_viewer_screenshot):
    """Returns an inner function that
    - opens the brainglobe-segmentation widget
    - configures the widget so an example project is loaded in atlas space
    - saves a screenshot after each of the above steps
    - returns the viewer and the widget
    """
    def _clean_atlas_manager_widget():
        viewer = standard_size_viewer
        _, atlas_manager_widget = viewer.window.add_plugin_dock_widget(
            plugin_name="brainrender-napari", 
            widget_name="Manage atlas versions"
        )
        atlas_manager_widget.viewer = viewer
        viewer.show()
    
        screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "open-manager-widget.png"
        take_viewer_screenshot(viewer, screenshot_file)
        return viewer, atlas_manager_widget

    return _clean_atlas_manager_widget

@pytest.fixture
def clean_brainrender_widget(tmp_path, standard_size_viewer, take_viewer_screenshot):
    """Returns an inner function that
    - opens the brainglobe-segmentation widget
    - configures the widget so an example project is loaded in atlas space
    - saves a screenshot after each of the above steps
    - returns the viewer and the widget
    """
    def _clean_brainrender_widget():
        viewer = standard_size_viewer
        _, brainrender_widget = viewer.window.add_plugin_dock_widget(
            plugin_name="brainrender-napari", 
            widget_name="Brainrender"
        )
        brainrender_widget.viewer = viewer
        viewer.show()
    
        screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "plugin-menu-brainrender-napari.png"
        take_viewer_screenshot(viewer, screenshot_file)
        return viewer, brainrender_widget

    return _clean_brainrender_widget

def test_manager_widget(tmp_path, take_viewer_screenshot, clean_atlas_manager_widget):
    viewer, atlas_manager_widget = clean_atlas_manager_widget()

def test_brainrender_widget(qtbot, tmp_path, take_viewer_screenshot, clean_brainrender_widget):
    viewer, brainrender_widget = clean_brainrender_widget() # has already taken basic screenshot
    fish_index = brainrender_widget.atlas_viewer_view.model().index(5,0) # fish is 5th row (some rows are hidden but still count!)
    brainrender_widget.atlas_viewer_view.setCurrentIndex(fish_index)
    brainrender_widget.atlas_viewer_view.doubleClicked.emit(fish_index)
    screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "added-brainrender-napari.png"
    take_viewer_screenshot(viewer, screenshot_file)
         
    viewer.dims.ndisplay = 3
    screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "toggle-ndisplay-brainrender-napari.png"
    take_viewer_screenshot(viewer, screenshot_file)

    root_index = brainrender_widget.structure_view.model().index(0,0)
    forebrain_index = brainrender_widget.structure_view.model().index(0,0, root_index) 
    telencephalon_index = brainrender_widget.structure_view.model().index(1,0, forebrain_index)
    brainrender_widget.structure_view.setCurrentIndex(telencephalon_index)
    brainrender_widget.structure_view.doubleClicked.emit(telencephalon_index)
    screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "add-region-brainrender-napari.png"
    take_viewer_screenshot(viewer, screenshot_file)
    
    brainrender_widget.atlas_viewer_view.additional_reference_requested.emit("GAD1b")
    screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "additional-reference-brainrender-napari.png"
    take_viewer_screenshot(viewer, screenshot_file)
    
    
