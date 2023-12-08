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
RELATIVE_PATH_FOR_SCREENSHOTS = Path("./docs/source/tutorials/images/brainglobe-segmentation/")    
    
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
def clean_configure_segmentation_widget(tmp_path, standard_size_viewer, take_viewer_screenshot):
    """Returns an inner function that
    - opens the brainglobe-segmentation widget
    - configures the widget so an example project is loaded in atlas space
    - saves a screenshot after each of the above steps
    - returns the viewer and the widget
    """
    def _clean_configure_segmentation_widget():
        viewer = standard_size_viewer
        _, segmentation_widget = viewer.window.add_plugin_dock_widget(
            plugin_name="brainglobe-segmentation", 
            widget_name="Region/track segmentation"
        )
        segmentation_widget.viewer = viewer
        viewer.show()
    
        screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "brainglobe-segmentation-open-plugin.png"
        take_viewer_screenshot(viewer, screenshot_file)

        brainreg_dir = Path.home() / "dev/brainglobe-segmentation/tests/data" / "brainreg_output"

        tmp_input_dir = tmp_path / "brainreg_output"
        shutil.copytree(brainreg_dir, tmp_input_dir)
        shutil.rmtree(brainreg_dir/"segmentation"/"atlas_space", ignore_errors=True)
        shutil.rmtree(brainreg_dir/"segmentation"/"sample_space", ignore_errors=True)

        segmentation_widget.atlas_space = True
        segmentation_widget.plugin = (
            "brainglobe-napari-io.brainreg_read_dir_atlas_space"
        )
        segmentation_widget.directory = Path(tmp_input_dir)
        segmentation_widget.load_brainreg_directory()
        # delete segmentation data to ensure it's saved correctly in tests
        shutil.rmtree(segmentation_widget.paths.main_directory)
        viewer.layers['Registered image'].contrast_limits=(0, 600)
        
        screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "brainglobe-segmentation-loaded-data.png"
        take_viewer_screenshot(viewer, screenshot_file)
        return viewer, segmentation_widget

    return _clean_configure_segmentation_widget

def test_segmentation_widget_screenshot_3d(take_viewer_screenshot, clean_configure_segmentation_widget):
    viewer, segmentation_widget = clean_configure_segmentation_widget()
    
    segmentation_widget.show_regionseg_button.click()
    segmentation_widget.region_seg.add_new_region()
    
    # this setting to zero is needed, weirdly
    viewer.layers["region_0"].data = np.zeros_like(viewer.layers["region_0"].data)

    screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "brainglobe-segmentation-added-new-region.png"
    take_viewer_screenshot(viewer, screenshot_file)

    rr, cc = disk((70, 30), 10, shape=viewer.layers["region_0"].data.shape)
    viewer.layers["region_0"].data[132, cc, rr] = 1
    viewer.layers["region_0"].refresh()

    screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "brainglobe-segmentation-painted-new-region.png"
    take_viewer_screenshot(viewer, screenshot_file)


def test_segmentation_widget_screenshot_1d(take_viewer_screenshot, clean_configure_segmentation_widget):
    viewer, segmentation_widget = clean_configure_segmentation_widget()
    
    segmentation_widget.show_trackseg_button.click()
    segmentation_widget.track_seg.add_track()

    screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "brainglobe-segmentation-added-new-track.png"
    take_viewer_screenshot(viewer, screenshot_file)

    viewer.layers["track_0"].data = [[132,30,70],[132,50,80],[132, 60, 90],[132, 70, 130]]
    viewer.layers["track_0"].refresh()

    screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "brainglobe-segmentation-added-points.png"
    take_viewer_screenshot(viewer, screenshot_file)

    segmentation_widget.track_seg.run_track_analysis()

    screenshot_file = RELATIVE_PATH_FOR_SCREENSHOTS / "brainglobe-segmentation-fitted-points.png"
    take_viewer_screenshot(viewer, screenshot_file)
    