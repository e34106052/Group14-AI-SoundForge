import flet as ft
import os
import random
#import base64
from music_gen.generate import generate_and_predict
# 忽略所有警告
#def load_image_base64(path):
#    with open(path, "rb") as f:
#        data = f.read()
#    return f"data:image/jpeg;base64,{base64.b64encode(data).decode()}"

def get_result_screen(page, audio_player, last_genre, last_length, optimized_prompts, duration_dict, last_generated_path, result_info, switch_to):
    
    result_text = ft.Text(selectable=True)
    feedback_text = ft.Text("", size=16, weight="bold", color=ft.colors.GREEN)
    back_button = ft.ElevatedButton("⬅️ Go back to 🎼 Generate Music", visible=False, on_click=lambda e: switch_to("interaction"))
    #genre_image = ft.Image(src="", width=300, height=300, fit=ft.ImageFit.CONTAIN)

    def update_result_info():
        result_text.value = result_info["value"]
        result_text.update()
    
#        genre = last_genre["value"]
#        print(f"[DEBUG] Current genre: {genre}")
    
#        genre_img_folder = os.path.join("image", genre)
#        print(f"[DEBUG] Checking folder: {genre_img_folder}")
    
#        if os.path.exists(genre_img_folder):
#            image_files = [f for f in os.listdir(genre_img_folder)
#                       if f.lower().endswith((".jpg", ".jpeg"))]
#            print(f"[DEBUG] Found image files: {image_files}")
        
#            if image_files:
#                chosen = random.choice(image_files)
#                image_path = os.path.join(genre_img_folder, chosen)
#                print(f"[DEBUG] Selected image path: {image_path}")

#                genre_image.src = load_image_base64(image_path)
#            else:
#                print("[DEBUG] No image files found.")
#                genre_image.src = ""  # 清除圖片
#        else:
#            print("[DEBUG] Genre folder does not exist.")
#            genre_image.src = ""  # 清除圖片

#        genre_image.update()
#        page.update()


    def like_music(e):
        feedback_text.value = "Thank you! We’re glad you liked this track 😊"
        feedback_text.color = ft.colors.GREEN
        feedback_text.update()
        back_button.visible = False
        back_button.update()
    
    def dislike_music(e):
        feedback_text.value = (
            "Not satisfied?\nWould you like to regenerate a new track with the same style and length?\n"
            "Please Go back to Generate Music~"
        )
        feedback_text.color = ft.colors.RED
        feedback_text.update()
        back_button.visible = True
        back_button.update()
    
    def go_back(e):
        switch_to("initial")

    result_screen = ft.Column(
        [
            ft.Row(
                [
                    ft.Text("🎼 Listen to the music you generate!", size=24, weight="bold"),
                    ft.IconButton(ft.icons.ARROW_BACK, on_click=go_back),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Text("🔊 Output Preview", size=16, weight="bold"),
            #genre_image,    # 加入圖片顯示
            audio_player,
            ft.Row(
                [
                    ft.ElevatedButton("▶️ Play", on_click=lambda e: audio_player.play()),
                    ft.ElevatedButton("⏸ Pause", on_click=lambda e: audio_player.pause()),
                ],
                alignment=ft.MainAxisAlignment.CENTER
                  ),
            result_text,
            feedback_text,
            ft.Row(
                [
                    ft.ElevatedButton("👍 Like", on_click=like_music),
                    ft.ElevatedButton("👎 Dislike", on_click=dislike_music),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            back_button,
        ],
        alignment=ft.MainAxisAlignment.START,
        visible=False
    )

    return result_screen, update_result_info, result_text
