import importlib.metadata as importlib_metadata

try:
    # This will read version from pyproject.toml
    __version__ = importlib_metadata.version(__package__ or __name__)
except importlib_metadata.PackageNotFoundError:
    __version__ = "development"

from super.annotators.core import (
    BlurAnnotator,
    BoundingBoxAnnotator,
    BoxCornerAnnotator,
    CircleAnnotator,
    ColorAnnotator,
    DotAnnotator,
    EllipseAnnotator,
    HaloAnnotator,
    HeatMapAnnotator,
    LabelAnnotator,
    MaskAnnotator,
    PixelateAnnotator,
    PolygonAnnotator,
    TraceAnnotator,
    TriangleAnnotator,
)
from super.annotators.utils import ColorLookup
from super.classification.core import Classifications
from super.dataset.core import (
    BaseDataset,
    ClassificationDataset,
    DetectionDataset,
)
from super.detection.annotate import BoxAnnotator
from super.detection.core import Detections
from super.detection.line_counter import LineZone, LineZoneAnnotator
from super.detection.tools.inference_slicer import InferenceSlicer
from super.detection.tools.polygon_zone import PolygonZone, PolygonZoneAnnotator
from super.detection.utils import (
    box_iou_batch,
    calculate_masks_centroids,
    filter_polygons_by_area,
    mask_to_polygons,
    mask_to_xyxy,
    move_boxes,
    non_max_suppression,
    polygon_to_mask,
    polygon_to_xyxy,
    scale_boxes,
)
from super.draw.color import Color, ColorPalette
from super.draw.utils import (
    calculate_dynamic_line_thickness,
    calculate_dynamic_text_scale,
    draw_filled_rectangle,
    draw_image,
    draw_line,
    draw_polygon,
    draw_rectangle,
    draw_text,
)
from super.geometry.core import Point, Position, Rect
from super.geometry.utils import get_polygon_center
from super.metrics.detection import ConfusionMatrix, MeanAveragePrecision
from super.tracker.byte_tracker.core import ByteTrack
from super.utils.file import list_files_with_extensions
from super.utils.image import ImageSink, crop_image
from super.utils.notebook import plot_image, plot_images_grid
from super.utils.video import (
    FPSMonitor,
    VideoInfo,
    VideoSink,
    get_video_frames_generator,
    process_video,
)
