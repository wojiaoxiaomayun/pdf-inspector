"""Type stubs for pdf_inspector."""

from enum import IntEnum
from typing import Optional

class ImageFormat(IntEnum):
    """Image format extracted from PDF."""
    Jpeg = 0
    Png = 1

class ExtractedImage:
    """An image extracted from a PDF."""
    page: int
    """Page number (1-indexed)."""
    x: float
    """X position on page (PDF points)."""
    y: float
    """Y position on page (PDF points)."""
    width: int
    """Pixel width."""
    height: int
    """Pixel height."""
    format: ImageFormat
    """Image format (jpeg or png)."""
    data: bytes
    """Raw image bytes (valid JPEG or PNG file)."""

class PdfResultWithImages:
    """PDF processing result with extracted images.

    The markdown contains ``![image](pdf-image://N)`` placeholders where N
    is the index into the ``images`` array.
    """
    pdf_type: str
    """'text_based', 'scanned', 'image_based', or 'mixed'."""
    markdown: Optional[str]
    page_count: int
    processing_time_ms: int
    pages_needing_ocr: list[int]
    title: Optional[str]
    confidence: float
    is_complex_layout: bool
    pages_with_tables: list[int]
    pages_with_columns: list[int]
    has_encoding_issues: bool
    images: list[ExtractedImage]
    """Extracted images. Indices match ``pdf-image://N`` placeholders in markdown."""

class PdfResult:
    """Result of processing a PDF file."""
    pdf_type: str
    """'text_based', 'scanned', 'image_based', or 'mixed'."""
    markdown: Optional[str]
    page_count: int
    processing_time_ms: int
    pages_needing_ocr: list[int]
    title: Optional[str]
    confidence: float
    is_complex_layout: bool
    pages_with_tables: list[int]
    pages_with_columns: list[int]
    has_encoding_issues: bool

class PdfClassification:
    """Lightweight PDF classification result."""
    pdf_type: str
    """'text_based', 'scanned', 'image_based', or 'mixed'."""
    page_count: int
    pages_needing_ocr: list[int]
    """0-indexed page numbers that need OCR."""
    confidence: float

class TextItem:
    """A positioned text item extracted from a PDF."""
    text: str
    x: float
    y: float
    width: float
    height: float
    font: str
    font_size: float
    page: int
    is_bold: bool
    is_italic: bool
    item_type: str

class RegionText:
    """Extracted text for a single region."""
    text: str
    needs_ocr: bool
    """True when the text should not be trusted."""

class PageRegionTexts:
    """Extracted text for one page's regions."""
    page: int
    """0-indexed page number."""
    regions: list[RegionText]

class PageMarkdown:
    """Per-page markdown extraction result."""
    page: int
    """0-indexed page number."""
    markdown: str
    """Formatted markdown for this page (empty string when needs_ocr is True)."""
    needs_ocr: bool
    """True when text on this page is unreliable and OCR should be used instead."""

class PagesExtractionResult:
    """Per-page markdown output with document-wide layout classification."""
    pages: list[PageMarkdown]
    """Per-page markdown results, in the order requested."""
    pages_with_tables: list[int]
    """1-indexed pages where tables were detected."""
    pages_with_columns: list[int]
    """1-indexed pages where multi-column layout was detected."""
    pages_needing_ocr: list[int]
    """1-indexed pages that need OCR."""
    is_complex: bool
    """True if any page has tables or multi-column layout."""

def process_pdf(path: str, pages: Optional[list[int]] = None) -> PdfResult:
    """Process a PDF: detect type, extract text, convert to Markdown."""
    ...

def process_pdf_bytes(data: bytes, pages: Optional[list[int]] = None) -> PdfResult:
    """Process a PDF from bytes in memory."""
    ...

def detect_pdf(path: str) -> PdfResult:
    """Fast detection only — no text extraction."""
    ...

def detect_pdf_bytes(data: bytes) -> PdfResult:
    """Fast detection from bytes."""
    ...

def classify_pdf(path: str) -> PdfClassification:
    """Lightweight classification — type, page count, and OCR pages (0-indexed)."""
    ...

def classify_pdf_bytes(data: bytes) -> PdfClassification:
    """Lightweight classification from bytes."""
    ...

def extract_text(path: str) -> str:
    """Extract plain text from a PDF."""
    ...

def extract_text_bytes(data: bytes) -> str:
    """Extract plain text from PDF bytes."""
    ...

def extract_text_with_positions(path: str, pages: Optional[list[int]] = None) -> list[TextItem]:
    """Extract text with position information."""
    ...

def extract_text_with_positions_bytes(data: bytes, pages: Optional[list[int]] = None) -> list[TextItem]:
    """Extract text with position information from bytes."""
    ...

def extract_text_in_regions(
    path: str,
    page_regions: list[tuple[int, list[list[float]]]],
) -> list[PageRegionTexts]:
    """Extract text within bounding-box regions from a PDF file.

    Args:
        path: Path to the PDF file.
        page_regions: List of (page_0indexed, [[x1, y1, x2, y2], ...]) tuples.
    """
    ...

def extract_text_in_regions_bytes(
    data: bytes,
    page_regions: list[tuple[int, list[list[float]]]],
) -> list[PageRegionTexts]:
    """Extract text within bounding-box regions from PDF bytes.

    Args:
        data: PDF file contents as bytes.
        page_regions: List of (page_0indexed, [[x1, y1, x2, y2], ...]) tuples.
    """
    ...

def extract_pages_markdown(
    path: str,
    pages: Optional[list[int]] = None,
) -> PagesExtractionResult:
    """Extract formatted markdown for pages of a PDF, with layout classification.

    Args:
        path: Path to the PDF file.
        pages: Optional list of 0-indexed pages. When ``None`` (default), every
            page is returned in document order. Otherwise, output matches the
            caller-supplied order.

    Returns:
        PagesExtractionResult with per-page markdown and document-wide layout
        classification (tables, columns, OCR needs).
    """
    ...

def extract_pages_markdown_bytes(
    data: bytes,
    pages: Optional[list[int]] = None,
) -> PagesExtractionResult:
    """Extract formatted markdown for pages of a PDF from bytes.

    See :func:`extract_pages_markdown` for details.
    """
    ...

def extract_images(path: str) -> list[ExtractedImage]:
    """Extract images from a PDF file.

    Extracts JPEG (DCTDecode) and PNG (FlateDecode) images with position
    and dimension metadata. Returns raw image bytes as valid JPEG/PNG files.
    """
    ...

def extract_images_bytes(data: bytes) -> list[ExtractedImage]:
    """Extract images from PDF bytes.

    See :func:`extract_images` for details.
    """
    ...

def process_pdf_with_images(
    path: str,
    pages: Optional[list[int]] = None,
) -> PdfResultWithImages:
    """Process a PDF and extract both markdown and images.

    The markdown contains ``![image](pdf-image://N)`` placeholders where N
    is the index into the returned ``images`` array.
    """
    ...

def process_pdf_with_images_bytes(
    data: bytes,
    pages: Optional[list[int]] = None,
) -> PdfResultWithImages:
    """Process a PDF from bytes and extract both markdown and images.

    See :func:`process_pdf_with_images` for details.
    """
    ...
