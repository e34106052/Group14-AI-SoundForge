import flet as ft
import os
import random



def get_interaction_screen(page, genre_dropdown, length_dropdown,
                           audio_player_interaction, audio_player_result,
                           progress_bar, generated_text,
                           sample_playlist, optimized_prompts, duration_dict,
                           music_save_path, last_genre, last_length,
                           result_info,
                           last_generated_path,
                           switch_to):


    # 使用者下拉選擇想要預覽的風格
    sample_genre_dropdown = ft.Dropdown(
        label="Sample Genre",
        options=[ft.dropdown.Option(g) for g in os.listdir("sample")
                 if os.path.isdir(os.path.join("sample", g)) and not g.startswith(".")],
        width=300
    )

    # 播放 sample 音樂的函式
    def load_sample_music(e):
        genre = sample_genre_dropdown.value
        if not genre:
            return

        genre_path = os.path.join("sample", genre)
        sample_files = [f for f in os.listdir(genre_path) if f.endswith(".wav")]
        
        if not sample_files:
            return
            
        selected_file = random.choice(sample_files)
        full_path = os.path.join(genre_path, selected_file)
                
        # 更新 Playlist
        sample_playlist.controls.clear()
        sample_playlist.controls.append(
            ft.ListTile(
                leading=ft.Icon(ft.icons.MUSIC_NOTE),
                title=ft.Text(f"{genre} - {selected_file}"),
                on_click=lambda e, f=full_path: play_sample(f)
            )
        )
        sample_playlist.update()

    #播放按鈕使用的播放函式
    def play_sample(filepath):
        audio_player_interaction.src = filepath
        audio_player_interaction.update()

    
    def generate_music(e):
        genre = genre_dropdown.value
        length_sec = length_dropdown.value
        last_genre["value"] = genre
        last_length["value"] = length_sec

        audio_player_interaction.pause()# 停止 interaction 的音樂播放

        if not genre or not length_sec:
            generated_text.value = "⚠️ Please select music genre and length!"
            page.update()
            return

        save_dir = music_save_path["value"] or "C:\\AI_SoundForge"
        os.makedirs(save_dir, exist_ok=True)

        progress_bar.visible = True
        generated_text.value = "🎶 Generating music, please wait..."
        page.update()

        from music_gen.generate import generate_and_predict
        prompt = optimized_prompts[genre]
        duration_tokens = duration_dict[length_sec]
        filename = f"{genre.lower()}.wav"
        result = generate_and_predict(prompt, filename, duration_tokens, save_dir=save_dir)

        progress_bar.visible = False

        if result["predicted_genre"]:

            # 儲存音樂檔案路徑，傳給 result 畫面
            last_generated_path["value"] = result["filename"]
            # 設定 audio_player_result 播放
            audio_player_result.src = result["filename"]
            audio_player_result.update()

            # 記錄 metadata
            filename = result["filename"]
            predicted_genre = result["predicted_genre"]

            result_info["value"] = (
                f"✅ Music generation completed!\n"
                f"📂 Saved as: {filename}\n"
                f"🎯 Requested Genre: {genre}\n"
                f"🔍 Predicted Genre: {predicted_genre}"
            )
            
            # 自動切換畫面到 Result
            switch_to("result")

        else:
            generated_text.value = f"❌ Something wrong, please try again：{result.get('error')}"
            page.update()

    def go_back(e):
        switch_to("initial")

    interaction_screen = ft.Column(
        [
            ft.Row(
                [
                    #頁面標題和返回鍵
                    ft.Text("🎼 Music Generator", size=24, weight="bold"),
                    ft.IconButton(ft.icons.ARROW_BACK, on_click=go_back),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Row([
                    #左側：試聽sample
                    ft.Column([
                        ft.Text("🎧 Preview Sample Tracks"),
                        sample_genre_dropdown,
                        ft.ElevatedButton("Load Sample", on_click=load_sample_music),
                        ft.Container(
                            sample_playlist,
                            height=120,  # 限制 playlist 高度
                            bgcolor=ft.colors.GREY_100,
                            border_radius=10,
                            padding=5
                        ),
                        ft.Container(
                            audio_player_interaction,
                            height=40  # 控制 audio player 高度
                        ),
                        ft.Row([
                            ft.ElevatedButton("▶️ Play", on_click=lambda e: audio_player_interaction.play()),
                            ft.ElevatedButton("⏸ Pause", on_click=lambda e: audio_player_interaction.pause()),
                        ], alignment=ft.MainAxisAlignment.CENTER)
                    ], expand=1),

                    # 右側：生成
                    ft.Column([
                        ft.Text("🎶 Generate Music"),
                        ft.Text("Select the music style you like!"),
                        genre_dropdown,
                        ft.Text("Select the music length you prefer!"),
                        length_dropdown,
                        ft.ElevatedButton("Generate Music", icon=ft.icons.MUSIC_NOTE, on_click=generate_music),
                        ft.Container(progress_bar, height=10),
                        ft.Container(generated_text, bgcolor="lightgrey", height=100)
                    ], expand=1)
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=30
        )
        ])

    return interaction_screen
