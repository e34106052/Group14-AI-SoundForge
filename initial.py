 # ===============================
    # === 1️⃣ Initial Screen ===
    # ===============================
import flet as ft

def get_initial_screen(switch_to):

    intro_text = ft.Text(
        "🎶 Hello! Welcome to AI Sound Forge! 🎶\n"
        "Here, you can explore and preview music samples from various genres, and even create a new track in your favorite style.\n"
        "Before you start generating music, please visit the Settings page to confirm your music save location and choose your preferred theme.\n"
        "Once you're all set, enjoy making music!",
        size=14,
        weight="bold",
        italic=True,
        font_family="Georgia",
        color=ft.colors.BLUE_GREY_800,
        text_align=ft.TextAlign.JUSTIFY,
        selectable=True,
    )

    intro_box = ft.Container(
        content=intro_text,
        padding=20,
        bgcolor=ft.colors.AMBER_50,
        border_radius=15,
        border=ft.border.all(1, ft.colors.AMBER),
        width=500,
        alignment=ft.alignment.center,
    )
    
    return ft.Column(
            [
                ft.Text("🎵 AI SoundForge", size=30, weight="bold"),
                intro_box,
                ft.Row(
                    [
                        ft.ElevatedButton("🎼 Generate Music", on_click=lambda e: switch_to("interaction")),
                        ft.ElevatedButton("🎧 Output Preview", on_click=lambda e: switch_to("result")),
                        ft.ElevatedButton("⚙️ Settings", on_click=lambda e: switch_to("settings")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )
            ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30,
        visible=True)
