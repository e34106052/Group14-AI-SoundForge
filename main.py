import flet as ft
from music_gen.prompt import generate_optimized_prompts

#匯入四個畫面模組
from initial import get_initial_screen
from interaction import get_interaction_screen
from result import get_result_screen
from settings import get_settings_screen


def main(page: ft.Page):
    page.title = "AI SoundForge"
    page.theme_mode = "light"

    # ✅ 一開始就初始化 optimized_prompts
    optimized_prompts = generate_optimized_prompts()
    
    # 狀態變數，共用資料
    last_genre = {"value": None}
    last_length = {"value": None}
    music_save_path = {"value": None}

    # 初始化所有共用元件
    genre_dropdown = ft.Dropdown(
        label="Genre",
        width=300,
        options=[ft.dropdown.Option(genre) for genre in optimized_prompts.keys()]
    )
    length_dropdown = ft.Dropdown(
        label="Length (sec)",
        width=200,
        options=[
            ft.dropdown.Option("30"),
            ft.dropdown.Option("21"),
            ft.dropdown.Option("15"),
            ft.dropdown.Option("9"),
        ]
    )

    #需要建立兩個不同的audio player，一個在interaction screen，一個在result screen
    audio_player_interaction = ft.Audio(autoplay=True)
    audio_player_result = ft.Audio(autoplay=True)


    #音樂生成進度條
    progress_bar = ft.ProgressBar(visible=False)
    generated_text = ft.Text("Create your own music!")
    # interaction screen sample playlist
    sample_playlist = ft.ListView(controls=[], height=200, expand=True)
    save_path_text = ft.Text("No folder selected")
    # result screen需要用
    last_generated_path = {"value": None}
    result_info = {"value": ""}

    # 訓練後的 prompt 與音樂長度對應表
    duration_dict = {"30": 1503, "21": 1051 ,"15": 751, "9": 451, }

    # 切換畫面函式
    def switch_to(target):
        initial_screen.visible = target == "initial"
        interaction_screen.visible = target == "interaction"
        result_screen.visible = target == "result"
        settings_screen.visible = target == "settings"

        # 如果切換到 result，就更新 audio 播放器一次，每次畫面切換到 Result 都會更新一次
        if target == "result":
            update_result_info()
            audio_player_result.update()
            
        page.update()
    
    # 畫面建構
    initial_screen = get_initial_screen(switch_to)
    interaction_screen = get_interaction_screen(
        page, genre_dropdown, length_dropdown,
        audio_player_interaction, audio_player_result,
        progress_bar, generated_text,
        sample_playlist, optimized_prompts, duration_dict,
        music_save_path, last_genre, last_length,
        result_info,
        last_generated_path,
        switch_to
    )
    interaction_screen.visible = False
    result_screen, update_result_info, result_text = get_result_screen(
        page, audio_player_result, last_genre, last_length,
        optimized_prompts, duration_dict, last_generated_path, result_info,
        switch_to
    )
    result_screen.visible = False
    settings_screen = get_settings_screen(page, save_path_text, music_save_path, switch_to)
    settings_screen.visible = False


    # 畫面加入，顯示畫面
    page.add(
        initial_screen,
        interaction_screen,
        result_screen,
        settings_screen
    )

if __name__ == "__main__":
    ft.app(target=main)
