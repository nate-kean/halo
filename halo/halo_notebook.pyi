from typing import Any, Optional, TextIO

from .halo import Halo, SpinnerType

class HaloNotebook(Halo):
    output: Any

    def __init__(
        self,
        text: str = ...,
        color: str = ...,
        text_color: Optional[str] = ...,
        spinner: Optional[SpinnerType] = ...,
        placement: str = ...,
        animation: Optional[str] = ...,
        interval: float = ...,
        enabled: bool = ...,
        stream: TextIO = ...,
    ) -> None: ...
    def _make_output_widget(self) -> Any: ...
    def clear(self) -> Halo: ...
    def _render_frame(self) -> None: ...
    def start(self, text: Optional[str] = ...) -> Halo: ...
    def stop_and_persist(self, symbol: str = ..., text: Optional[str] = ...) -> Halo: ...
