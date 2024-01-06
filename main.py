import flet as ft
import utils.generator as gen
from Models.Player import Player

player = Player("src/songs/")
def main(page: ft.Page) -> None:
    # Page settings
    page.title = "N.A.I.S - Not All Is Spotify"
    page.window_height, page.window_width = 110, 320
    page.window_maximizable, page.window_resizable = False, False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    player.load_random_song()
    controls = ft.Row(
            [
                ft.IconButton(icon=ft.icons.SKIP_PREVIOUS_ROUNDED,
                    icon_color="GREEN_ACCENT_200",
                    icon_size=40,
                    on_click=player.pause,
                ),
                ft.IconButton(
                    icon=ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                    icon_color="#FFFFFF",
                    icon_size=40,
                    on_click=player.pause,
                ),
                ft.IconButton(
                    icon=ft.icons.PLAY_CIRCLE_OUTLINE_ROUNDED,
                    icon_color="#1FDF64",
                    icon_size=40,
                    on_click=player.unpause,
                ),
                ft.IconButton(icon=ft.icons.SKIP_NEXT_ROUNDED,
                    icon_color="GREEN_ACCENT_200",
                    icon_size=40,
                    on_click=player.play_random_next,
                ),
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
        )

    display = ft.Column(
        [
            controls,
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(display)

ft.app(target=main)