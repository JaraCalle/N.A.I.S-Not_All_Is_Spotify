import flet as ft
import utils.generator as gen
from Models.Player import Player

player = Player("src/songs/")
def main(page: ft.Page) -> None:
    # Page settings
    page.title = "N.A.I.S - Not All Is Spotify"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    gen.generate_cover()
    player.load_first_song()
    img = ft.Image(
        src=f"src/images/cover.jpg",
        width=300,
        height=300,
        border_radius=10,
        fit=ft.ImageFit.COVER,
    )

    controls = ft.Row(
            [
                ft.IconButton(icon=ft.icons.SKIP_PREVIOUS_ROUNDED,
                    icon_color="GREEN_ACCENT_200",
                    icon_size=40,
                    tooltip="Pause",
                    on_click=player.pause,
                ),
                ft.IconButton(
                    icon=ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                    icon_color="#FFFFFF",
                    icon_size=40,
                    tooltip="Pause",
                    on_click=player.pause,
                ),
                ft.IconButton(
                    icon=ft.icons.PLAY_CIRCLE_OUTLINE_ROUNDED,
                    icon_color="#1FDF64",
                    icon_size=40,
                    tooltip="Play",
                    on_click=player.unpause,
                ),
                ft.IconButton(icon=ft.icons.SKIP_NEXT_ROUNDED,
                    icon_color="GREEN_ACCENT_200",
                    icon_size=40,
                    tooltip="Pause",
                    on_click=player.play_next,
                ),
            ], 
            alignment=ft.MainAxisAlignment.CENTER,
        )

    display = ft.Column(
        [
            img,
            controls,
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(display)

ft.app(target=main)