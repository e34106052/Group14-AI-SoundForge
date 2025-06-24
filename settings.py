import flet as ft

def get_settings_screen(page, save_path_text, music_save_path, switch_to):
    def browse_folder(e):
        async def pick_folder_result(e: ft.FilePickerResultEvent):
            if e.path:
                music_save_path["value"] = e.path
                save_path_text.value = f"Selected folder: {e.path}"
                page.update()

        pick_folder = ft.FilePicker(on_result=pick_folder_result)
        page.overlay.append(pick_folder)
        page.update()
        pick_folder.get_directory_path()

    def go_back(e):
        switch_to("initial")  # ✅ 改為使用 switch_to

    return ft.Column(
        [
            ft.Row(
                [
                    ft.Text("⚙️ Settings", size=24, weight="bold"),
                    ft.IconButton(ft.icons.ARROW_BACK, on_click=go_back),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Divider(),

            ft.Text("🎨 Theme"),
            ft.ElevatedButton(
                text="Toggle Theme",
                on_click=lambda e: (
                    setattr(page, "theme_mode", "dark" if page.theme_mode == "light" else "light"),
                    page.update()
                )
            ),

            ft.Text("💾 Save File"),
            save_path_text,
            ft.ElevatedButton("Browse Folder", on_click=browse_folder),
        ],
        spacing=20,
        visible=False
    )
