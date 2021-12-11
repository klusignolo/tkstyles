from dataclasses import dataclass
from enum import Enum

@dataclass
class ThemeConfig():
    background: str
    button_background: str
    button_hover_background: str
    entry_background: str
    disabled_entry_background: str
    radio_checkbox_background: str
    font_color: str
    button_font_color: str
    entry_font_color: str

class Color(Enum):
    WHITE = "#ffffff"
    BLACK = "#000000"
    RED = "#ed1818"
    FREE_SPEECH_RED = "#DB1010"
    DARK_RED = "#9E0A0A"
    SUNDOWN = "#FCACAC"
    RED_SMOKE = "#FFEEEE"
    DARK_TEXT = "#1E1E1E"
    DISABLED_DARK_TEXT = "#707070"
    LIGHT_TEXT = "#F0F0F0"
    DISABLED_LIGHT_TEXT = "#B9B9BC"

class Theme:
    RED = ThemeConfig(
        background=Color.FREE_SPEECH_RED.value,
        button_background=Color.DARK_RED.value,
        button_hover_background=Color.RED.value,
        entry_background=Color.RED_SMOKE.value,
        disabled_entry_background=Color.SUNDOWN.value, 
        radio_checkbox_background=Color.RED_SMOKE.value, 
        font_color=Color.DARK_TEXT.value, 
        button_font_color=Color.DARK_TEXT.value, 
        entry_font_color=Color.DARK_TEXT.value
        )
    GREEN = ThemeConfig(
        background="#f2fff9",
        button_background="#dcede0",
        button_hover_background="#23e046",
        entry_background="#d9ffd8",
        disabled_entry_background="#d2efe4", 
        radio_checkbox_background="#d9ffd8", 
        font_color="#242624", 
        button_font_color="#242624", 
        entry_font_color="#242624"
        )
    BLUE = ThemeConfig(
        background="#5895fc",
        button_background="#2e62f2",
        button_hover_background="#023bd9",
        entry_background="#5e89ff",
        disabled_entry_background="#b8c8f5", 
        radio_checkbox_background="#5e89ff", 
        font_color=Color.DARK_TEXT.value, 
        button_font_color=Color.LIGHT_TEXT.value, 
        entry_font_color=Color.DARK_TEXT.value
        )
    YELLOW = ThemeConfig(
        background="#fffef2",
        button_background="#efe2d0",
        button_hover_background="#ffd52d",
        entry_background="#fff7d8",
        disabled_entry_background="#f2eede", 
        radio_checkbox_background="#fff7d8", 
        font_color="#262524", 
        button_font_color="#262524", 
        entry_font_color="#262524"
        )
    PINK = ThemeConfig(
        background="#ff3f79",
        button_background="#e81253",
        button_hover_background="#ce002c",
        entry_background="#fca9c2",
        disabled_entry_background="#e5d0d7", 
        radio_checkbox_background="#fca9c2", 
        font_color="#440014", 
        button_font_color="#440014", 
        entry_font_color="#440014"
        )
    PURPLE = ThemeConfig(
        background="#b48efa",
        button_background="#e7d3ff",
        button_hover_background="#9c38ff",
        entry_background="#d8a1ff",
        disabled_entry_background="#eed9f9", 
        radio_checkbox_background="#d8a1ff", 
        font_color=Color.DARK_TEXT.value, 
        button_font_color=Color.DARK_TEXT.value, 
        entry_font_color=Color.DARK_TEXT.value
        )
    GOLD = ThemeConfig(
        background="#ffaf2d",
        button_background="#ffb005",
        button_hover_background="#ff9800",
        entry_background="#f7be4a",
        disabled_entry_background="#edc572", 
        radio_checkbox_background="#f7be4a", 
        font_color="#4d2e00", 
        button_font_color="#4d2e00", 
        entry_font_color="#4d2e00"
        )
    DARK = ThemeConfig(
        background="#191919",
        button_background="#232323",
        button_hover_background="#0c0c0c",
        entry_background="#474747",
        disabled_entry_background="#0c0c0c", 
        radio_checkbox_background="#474747", 
        font_color="#efefef", 
        button_font_color="#efefef", 
        entry_font_color="#efefef"
        )
    LIGHT = ThemeConfig(
        background=Color.WHITE.value,
        button_background="#b3f2ff",
        button_hover_background="#d1f7ff",
        entry_background="#f5feff",
        disabled_entry_background=Color.LIGHT_TEXT.value, 
        radio_checkbox_background="#e0faff", 
        font_color=Color.DARK_TEXT.value, 
        button_font_color=Color.DARK_TEXT.value, 
        entry_font_color=Color.DARK_TEXT.value
        )
    BLACK_AND_WHITE = ThemeConfig(
        background=Color.BLACK.value,
        button_background=Color.WHITE.value,
        button_hover_background="#ededed",
        entry_background=Color.WHITE.value,
        disabled_entry_background="#ededed", 
        radio_checkbox_background="#474747", 
        font_color=Color.LIGHT_TEXT.value, 
        button_font_color=Color.DARK_TEXT.value, 
        entry_font_color=Color.DARK_TEXT.value
        )
    HUFFLEPUFF = ThemeConfig(
        background="#dcab20",
        button_background="#181818",
        button_hover_background="#535353",
        entry_background="#feeb9f",
        disabled_entry_background="#fceaaa", 
        radio_checkbox_background="#feeb9f", 
        font_color="#1c1c1c", 
        button_font_color="#f0e095", 
        entry_font_color="#1c1c1c"
        )
    GRYFFINDOR = ThemeConfig(
        background="#5c0000",
        button_background="#fb8800",
        button_hover_background="#fbb100",
        entry_background="#ab4e4e",
        disabled_entry_background="#936a6a", 
        radio_checkbox_background="#ab4e4e", 
        font_color="#d08400", 
        button_font_color="#3c0101", 
        entry_font_color="#3c0101"
        )
    SLYTHERIN = ThemeConfig(
        background="#2a623d",
        button_background="#474747",
        button_hover_background="#1a472a",
        entry_background="#8ddaa7",
        disabled_entry_background="#add0b9", 
        radio_checkbox_background="#8ddaa7", 
        font_color=Color.DARK_TEXT.value, 
        button_font_color="#d3e4d3", 
        entry_font_color=Color.DARK_TEXT.value
        )
    RAVENCLAW = ThemeConfig(
        background="#222f5b",
        button_background="#946b2d",
        button_hover_background="#9a610a",
        entry_background="#a98957",
        disabled_entry_background="#ad9673", 
        radio_checkbox_background="#ad9673", 
        font_color="#b8740e", 
        button_font_color="#08143a", 
        entry_font_color="#060c1f"
        )