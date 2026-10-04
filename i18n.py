"""
Internationalization (i18n) module for MKV Lossless Editor.
Supports Korean, English, Japanese, and Simplified Chinese.
Language preferences are stored and loaded via QSettings.
"""

from PySide6.QtCore import QSettings

SUPPORTED_LANGUAGES = {
    "ko": "한국어 (Korean)",
    "en": "English",
    "ja": "日本語 (Japanese)",
    "zh": "简体中文 (Chinese)"
}

TRANSLATIONS = {
    "ko": {
        # App Title
        "app_title": "MKV Lossless Cutter",
        "app_title_file": "MKV Lossless Cutter - {name}",
        "multi_merge_title": "MKV Lossless Cutter - 다중 파일 병합 모드",
        
        # Tooltips - Playback controls
        "tooltip_pre_frame": "1프레임 뒤로 (D)",
        "tooltip_rewind": "5초 뒤로 (←)",
        "tooltip_play": "재생 (Space)",
        "tooltip_pause": "일시정지 (Space)",
        "tooltip_play_or_open": "재생 / 닫힌 상태에선 열기 (Space)",
        "tooltip_stop": "정지 및 초기화 (Esc)",
        "tooltip_fast_forward": "5초 앞으로 (→)",
        "tooltip_next_frame": "1프레임 앞으로 (F)",
        "tooltip_open": "파일 열기 (Ctrl+O)",
        "tooltip_mute": "음소거 토글 (M)",
        "tooltip_unmute": "음소거 해제 (M)",
        
        # Tooltips - Cut controls
        "tooltip_set_start": "시작점 ([)",
        "tooltip_set_end": "끝점 (])",
        "tooltip_jump_start": "시작점으로 이동 (,)",
        "tooltip_jump_end": "끝점으로 이동 (.)",
        "tooltip_inverse": "선택 영역 반전",
        "tooltip_clear": "선택 초기화",
        "tooltip_maximize": "창 최대화 / 복원 (비디오 더블클릭)",
        "tooltip_fullscreen": "순수 전체화면 모드 (Alt+Enter)",
        
        # List controls
        "tooltip_item_up": "위로 이동",
        "tooltip_item_down": "아래로 이동",
        "tooltip_item_delete": "삭제",

        # Labels & Buttons
        "merge_checkbox": "다중 구간 병합 (Merge)",
        "btn_export": "내보내기",
        "btn_start_merge": "병합 시작",
        "label_tracks": "트랙, 챕터와 태그",
        "label_segments": "선택된 자르기 구간 목록",
        "label_merge_queue": "다중 파일 병합 대기열",
        
        # Table Headers
        "col_select": "",
        "col_type": "유형",
        "col_codec": "코덱",
        "col_copy": "항목 복사",
        "col_lang": "언어",
        "col_name": "이름",
        "col_id": "ID",
        "col_default": "기본 트랙",
        "col_forced": "Forced display",
        "type_all": "유형 전체 선택",
        "type_video": "비디오",
        "type_audio": "오디오",
        "type_sub": "자막",
        "yes": "예",
        "no": "아니오",
        
        # Context Menu
        "menu_open": "파일 열기... (Ctrl+O)",
        "menu_play_pause": "재생 / 일시정지 (Space)",
        "menu_stop": "정지 (S)",
        "menu_audio": "오디오",
        "menu_mute": "음소거",
        "menu_current_audio": "현재 재생중인 오디오: {title}",
        "menu_sub": "자막",
        "menu_open_sub": "자막 열기...",
        "menu_show_sub": "자막 보이기",
        "menu_current_sub": "현재 재생중인 자막: {title}",
        "menu_not_used": "사용 안 함",
        "menu_none": "없음",
        "menu_track_format": "트랙 {id}",
        "menu_language": "언어 (Language)",
        "menu_fullscreen": "전체 화면 (Alt+Enter)",
        "menu_normal_screen": "기본 화면 (Alt+Enter)",
        "menu_shortcuts": "단축키 안내",
        "menu_exit": "종료 (Esc)",
        
        # Segments list items
        "segment_prefix": "구간",
        "segment_active_prefix": "> 현재 활성화: {start} ~ {end}",
        "segment_unspecified": "미지정",
        
        # Status Bar Messages
        "status_ready": "준비 완료",
        "status_playing": "재생",
        "status_paused": "일시정지",
        "status_sub_show": "자막 보이기",
        "status_sub_hide": "자막 끄기",
        "status_fullscreen": "전체화면 모드",
        "status_maximized": "최대화 모드",
        "status_normal": "기본 화면으로 복귀",
        "status_file_loaded": "파일 불러옴: {name}",
        "status_files_added": "{count}개의 파일이 병합 대기열에 추가되었습니다.",
        "status_external_sub": "외부 자막 적용됨: {name}",
        "status_muted": "음소거 설정됨",
        "status_unmuted": "음소거 해제됨",
        "status_volume": "볼륨: {value}%",
        "status_step_back": "1프레임 뒤로",
        "status_step_fwd": "1프레임 앞으로",
        "status_skip_back": "5초 뒤로",
        "status_skip_fwd": "5초 앞으로",
        "status_jump_start": "구간 시작점으로 이동: {time}",
        "status_active_cleared": "현재 임시 설정 구간이 취소/삭제 되었습니다.",
        "status_segment_deleted": "구간 {idx} 항목이 삭제되었습니다.",
        "status_start_set": "시작 지점 설정됨: {time}",
        "status_segment_saved": "구간 임시 저장됨: {start} ~ {end}",
        "status_all_cleared": "전체 자르기 구간이 초기화되었습니다.",
        "status_inverse": "선택 영역이 반전되었습니다.",
        "status_task_complete": "작업이 완료되었습니다.",
        "status_task_failed": "작업 취소 또는 실패",
        "status_lang_changed": "언어가 변경되었습니다: {lang}",

        # Dialogs & Prompts
        "dialog_unsupported_title": "지원하지 않는 파일",
        "dialog_unsupported_msg": "비디오 파일(.mkv, .mp4, .avi)만 열 수 있습니다.",
        "dialog_sub_fail_title": "자막 열기 실패",
        "dialog_sub_fail_msg": "자막 파일을 적용할 수 없습니다:\n{error}",
        "dialog_warn_title": "경고",
        "dialog_warn_end_before_start": "끝점은 시작점보다 뒤에 있어야 합니다.",
        "dialog_diff_ext_title": "경고: 확장자 불일치",
        "dialog_diff_ext_msg": "병합하려는 파일들의 확장자가 서로 다릅니다.\n이 경우 병합된 영상이 재생되지 않거나 파일이 손상될 수 있습니다.\n\n강제로 병합을 진행하시겠습니까?",
        "dialog_btn_force_merge": "강제 병합",
        "dialog_btn_cancel": "병합 취소",
        "dialog_export_fail_title": "실패",
        "dialog_pgs_warn_title": "자막 형식 경고",
        "dialog_pgs_warn_msg": "선택한 자막(PGS/이미지 자막)은 텍스트가 아닌 이미지 형식의 자막입니다.\n.srt/.ass 텍스트 자막으로 직접 내보낼 수 없습니다.\n.sup 또는 .mks 확장자로 저장해 주세요.",
        "dialog_open_file": "파일 열기",
        "dialog_open_sub": "자막 파일 열기",
        "dialog_save_file": "저장할 파일 선택",
        "dialog_save_merge": "병합 파일 저장",
        "dialog_export_progress_title": "내보내기 진행 상황",
        "dialog_preparing": "작업을 준비 중...",
        "dialog_cancel": "취소",
        "dialog_done_title": "완료",
        
        # Worker Tasks
        "task_export_sub": "자막 내보내기 중...",
        "task_export_part": "구간 내보내기 중... ({curr}/{total})",
        "task_merge_parts": "조각 파일 묶음 병합 중...",
        "task_merge_multi": "다중 파일 병합 중...",
        
        # File Filters
        "filter_video_files": "비디오 파일",
        "filter_sub_files": "자막 파일",
        "filter_audio_files": "오디오 파일",
        "filter_all_files": "모든 파일",
        
        # Shortcuts Guide HTML
        "shortcuts_title": "단축키 안내",
        "shortcuts_html": (
            "<b>단축키 목록</b><br><br>"
            "<b>Space</b> : 재생 / 일시정지<br>"
            "<b>Esc</b> : 정지 / 영상 닫기 / 전체화면 해제<br>"
            "<b>← / →</b> : 5초 이동<br>"
            "<b>D / F</b> : 1프레임 이동<br>"
            "<b>[ / ]</b> : 시작점 / 끝점 설정<br>"
            "<b>, / .</b> : 시작점 / 끝점으로 이동<br>"
            "<b>M</b> : 음소거 토글<br>"
            "<b>위/아래 방향키</b> : 볼륨 조절<br>"
            "<b>Alt+Enter</b> : 전체화면 전환<br>"
            "<b>Ctrl+O</b> : 파일 열기<br>"
        ),
        # Extra Type Menu & Mode Strings
        "menu_type_all": "유형 전체 선택",
        "menu_type_vid": "비디오만 선택",
        "menu_type_aud": "오디오만 선택",
        "menu_type_sub": "자막만 선택",
        "status_error": "오류 발생",
        "label_segments_merge_disabled": " (병합 모드 - 구간 설정 불가)",
        "multi_merge_title_idx": "MKV Lossless Cutter - 다중 파일 미리보기 ({curr}/{total})",
        "filter_merge_media": "미디어 파일",
        "task_cancelled_user": "사용자에 의해 취소됨",
        "task_all_complete": "모든 작업 완료",
    },
    
    "en": {
        # App Title
        "app_title": "MKV Lossless Cutter",
        "app_title_file": "MKV Lossless Cutter - {name}",
        "multi_merge_title": "MKV Lossless Cutter - Multi-File Merge Mode",
        
        # Tooltips - Playback controls
        "tooltip_pre_frame": "1 frame backward (D)",
        "tooltip_rewind": "5 seconds backward (←)",
        "tooltip_play": "Play (Space)",
        "tooltip_pause": "Pause (Space)",
        "tooltip_play_or_open": "Play / Open file if empty (Space)",
        "tooltip_stop": "Stop & Clear (Esc)",
        "tooltip_fast_forward": "5 seconds forward (→)",
        "tooltip_next_frame": "1 frame forward (F)",
        "tooltip_open": "Open File (Ctrl+O)",
        "tooltip_mute": "Toggle Mute (M)",
        "tooltip_unmute": "Unmute (M)",
        
        # Tooltips - Cut controls
        "tooltip_set_start": "Set Start Mark ([)",
        "tooltip_set_end": "Set End Mark (])",
        "tooltip_jump_start": "Jump to Start Mark (,)",
        "tooltip_jump_end": "Jump to End Mark (.)",
        "tooltip_inverse": "Invert Selection",
        "tooltip_clear": "Clear Selection",
        "tooltip_maximize": "Maximize / Restore (Double-click video)",
        "tooltip_fullscreen": "Borderless Fullscreen (Alt+Enter)",
        
        # List controls
        "tooltip_item_up": "Move Up",
        "tooltip_item_down": "Move Down",
        "tooltip_item_delete": "Delete",

        # Labels & Buttons
        "merge_checkbox": "Merge Segments (Concat)",
        "btn_export": "Export",
        "btn_start_merge": "Start Merge",
        "label_tracks": "Tracks, Chapters & Tags",
        "label_segments": "Cut Segments List",
        "label_merge_queue": "Multi-File Merge Queue",
        
        # Table Headers
        "col_select": "",
        "col_type": "Type",
        "col_codec": "Codec",
        "col_copy": "Copy",
        "col_lang": "Language",
        "col_name": "Name",
        "col_id": "ID",
        "col_default": "Default Track",
        "col_forced": "Forced Display",
        "type_all": "Select All Types",
        "type_video": "Video",
        "type_audio": "Audio",
        "type_sub": "Subtitle",
        "yes": "Yes",
        "no": "No",
        
        # Context Menu
        "menu_open": "Open File... (Ctrl+O)",
        "menu_play_pause": "Play / Pause (Space)",
        "menu_stop": "Stop (S)",
        "menu_audio": "Audio",
        "menu_mute": "Mute",
        "menu_current_audio": "Currently Playing Audio: {title}",
        "menu_sub": "Subtitles",
        "menu_open_sub": "Open External Subtitle...",
        "menu_show_sub": "Show Subtitles",
        "menu_current_sub": "Currently Playing Subtitle: {title}",
        "menu_not_used": "Disabled",
        "menu_none": "None",
        "menu_track_format": "Track {id}",
        "menu_language": "Language (언어)",
        "menu_fullscreen": "Fullscreen (Alt+Enter)",
        "menu_normal_screen": "Normal Window (Alt+Enter)",
        "menu_shortcuts": "Keyboard Shortcuts",
        "menu_exit": "Exit (Esc)",
        
        # Segments list items
        "segment_prefix": "Segment",
        "segment_active_prefix": "> Active: {start} ~ {end}",
        "segment_unspecified": "Unspecified",
        
        # Status Bar Messages
        "status_ready": "Ready",
        "status_playing": "Playing",
        "status_paused": "Paused",
        "status_sub_show": "Subtitles Enabled",
        "status_sub_hide": "Subtitles Disabled",
        "status_fullscreen": "Fullscreen Mode",
        "status_maximized": "Maximized Mode",
        "status_normal": "Restored Normal Window",
        "status_file_loaded": "Loaded file: {name}",
        "status_files_added": "{count} file(s) added to merge queue.",
        "status_external_sub": "External subtitle loaded: {name}",
        "status_muted": "Muted",
        "status_unmuted": "Unmuted",
        "status_volume": "Volume: {value}%",
        "status_step_back": "1 frame backward",
        "status_step_fwd": "1 frame forward",
        "status_skip_back": "5 seconds backward",
        "status_skip_fwd": "5 seconds forward",
        "status_jump_start": "Jumped to segment start: {time}",
        "status_active_cleared": "Current active mark cancelled.",
        "status_segment_deleted": "Segment {idx} removed.",
        "status_start_set": "Start point set: {time}",
        "status_segment_saved": "Segment added: {start} ~ {end}",
        "status_all_cleared": "All segments cleared.",
        "status_inverse": "Selection inverted.",
        "status_task_complete": "Operation completed successfully.",
        "status_task_failed": "Operation cancelled or failed.",
        "status_lang_changed": "Language changed: {lang}",

        # Dialogs & Prompts
        "dialog_unsupported_title": "Unsupported File",
        "dialog_unsupported_msg": "Only video files (.mkv, .mp4, .avi) are supported.",
        "dialog_sub_fail_title": "Subtitle Load Failed",
        "dialog_sub_fail_msg": "Could not apply subtitle file:\n{error}",
        "dialog_warn_title": "Warning",
        "dialog_warn_end_before_start": "End point must be later than start point.",
        "dialog_diff_ext_title": "Warning: Extension Mismatch",
        "dialog_diff_ext_msg": "The files to merge have different extensions.\nPlayback may fail or files may become corrupted.\n\nDo you want to proceed anyway?",
        "dialog_btn_force_merge": "Force Merge",
        "dialog_btn_cancel": "Cancel",
        "dialog_export_fail_title": "Failed",
        "dialog_pgs_warn_title": "Subtitle Format Warning",
        "dialog_pgs_warn_msg": "Selected subtitle track is bitmap-based (PGS/VobSub).\nIt cannot be exported directly to text (.srt/.ass).\nPlease export as .sup or .mks format.",
        "dialog_open_file": "Open Video File",
        "dialog_open_sub": "Open Subtitle File",
        "dialog_save_file": "Save Output File",
        "dialog_save_merge": "Save Merged File",
        "dialog_export_progress_title": "Export Progress",
        "dialog_preparing": "Preparing task...",
        "dialog_cancel": "Cancel",
        "dialog_done_title": "Done",
        
        # Worker Tasks
        "task_export_sub": "Exporting subtitle...",
        "task_export_part": "Exporting segment... ({curr}/{total})",
        "task_merge_parts": "Concatenating segments...",
        "task_merge_multi": "Merging multiple files...",
        
        # File Filters
        "filter_video_files": "Video Files",
        "filter_sub_files": "Subtitle Files",
        "filter_audio_files": "Audio Files",
        "filter_all_files": "All Files",
        
        # Shortcuts Guide HTML
        "shortcuts_title": "Keyboard Shortcuts Guide",
        "shortcuts_html": (
            "<b>Keyboard Shortcuts</b><br><br>"
            "<b>Space</b> : Play / Pause<br>"
            "<b>Esc</b> : Stop / Close file / Exit Fullscreen<br>"
            "<b>← / →</b> : Seek 5 seconds backward / forward<br>"
            "<b>D / F</b> : Step 1 frame backward / forward<br>"
            "<b>[ / ]</b> : Set Start mark / End mark<br>"
            "<b>, / .</b> : Jump to Start / End mark<br>"
            "<b>M</b> : Toggle Mute<br>"
            "<b>Up / Down Arrow</b> : Volume Up / Down<br>"
            "<b>Alt+Enter</b> : Toggle Fullscreen<br>"
            "<b>Ctrl+O</b> : Open file<br>"
        ),
        # Extra Type Menu & Mode Strings
        "menu_type_all": "Select All Types",
        "menu_type_vid": "Select Videos Only",
        "menu_type_aud": "Select Audio Only",
        "menu_type_sub": "Select Subtitles Only",
        "status_error": "Error occurred",
        "label_segments_merge_disabled": " (Merge Mode - Segment Setting Disabled)",
        "multi_merge_title_idx": "MKV Lossless Cutter - Multi-File Preview ({curr}/{total})",
        "filter_merge_media": "Media Files",
        "task_cancelled_user": "Cancelled by user",
        "task_all_complete": "All tasks completed",
    },
    
    "ja": {
        # App Title
        "app_title": "MKV Lossless Cutter",
        "app_title_file": "MKV Lossless Cutter - {name}",
        "multi_merge_title": "MKV Lossless Cutter - 複数ファイル結合モード",
        
        # Tooltips - Playback controls
        "tooltip_pre_frame": "1フレーム戻る (D)",
        "tooltip_rewind": "5秒戻る (←)",
        "tooltip_play": "再生 (Space)",
        "tooltip_pause": "一時停止 (Space)",
        "tooltip_play_or_open": "再生 / 停止時は開く (Space)",
        "tooltip_stop": "停止およびリセット (Esc)",
        "tooltip_fast_forward": "5秒進む (→)",
        "tooltip_next_frame": "1フレーム進む (F)",
        "tooltip_open": "ファイルを開く (Ctrl+O)",
        "tooltip_mute": "消音切替 (M)",
        "tooltip_unmute": "消音解除 (M)",
        
        # Tooltips - Cut controls
        "tooltip_set_start": "開始点設定 ([)",
        "tooltip_set_end": "終了点設定 (])",
        "tooltip_jump_start": "開始点へ移動 (,)",
        "tooltip_jump_end": "終了点へ移動 (.)",
        "tooltip_inverse": "選択範囲の反転",
        "tooltip_clear": "選択解除",
        "tooltip_maximize": "最大化 / 元に戻す (ダブルクリック)",
        "tooltip_fullscreen": "全画面表示 (Alt+Enter)",
        
        # List controls
        "tooltip_item_up": "上へ移動",
        "tooltip_item_down": "下へ移動",
        "tooltip_item_delete": "削除",

        # Labels & Buttons
        "merge_checkbox": "複数区間の結合 (Merge)",
        "btn_export": "出力",
        "btn_start_merge": "結合開始",
        "label_tracks": "トラック・チャプター・タグ",
        "label_segments": "切り出し区間リスト",
        "label_merge_queue": "ファイル結合キュー",
        
        # Table Headers
        "col_select": "",
        "col_type": "種類",
        "col_codec": "コーデック",
        "col_copy": "コピー",
        "col_lang": "言語",
        "col_name": "名称",
        "col_id": "ID",
        "col_default": "デフォルト",
        "col_forced": "強制表示",
        "type_all": "すべての種類を選択",
        "type_video": "映像",
        "type_audio": "音声",
        "type_sub": "字幕",
        "yes": "はい",
        "no": "いいえ",
        
        # Context Menu
        "menu_open": "ファイルを開く... (Ctrl+O)",
        "menu_play_pause": "再生 / 一時停止 (Space)",
        "menu_stop": "停止 (S)",
        "menu_audio": "音声",
        "menu_mute": "消音",
        "menu_current_audio": "再生中の音声: {title}",
        "menu_sub": "字幕",
        "menu_open_sub": "字幕ファイルを開く...",
        "menu_show_sub": "字幕を表示",
        "menu_current_sub": "再生中の字幕: {title}",
        "menu_not_used": "無効",
        "menu_none": "なし",
        "menu_track_format": "トラック {id}",
        "menu_language": "言語 (Language)",
        "menu_fullscreen": "全画面表示 (Alt+Enter)",
        "menu_normal_screen": "通常ウィンドウ (Alt+Enter)",
        "menu_shortcuts": "ショートカット案内",
        "menu_exit": "終了 (Esc)",
        
        # Segments list items
        "segment_prefix": "区間",
        "segment_active_prefix": "> 現在選択中: {start} ~ {end}",
        "segment_unspecified": "未指定",
        
        # Status Bar Messages
        "status_ready": "準備完了",
        "status_playing": "再生中",
        "status_paused": "一時停止",
        "status_sub_show": "字幕表示",
        "status_sub_hide": "字幕非表示",
        "status_fullscreen": "全画面モード",
        "status_maximized": "最大化モード",
        "status_normal": "標準ウィンドウに戻りました",
        "status_file_loaded": "ファイルを読み込みました: {name}",
        "status_files_added": "{count}個のファイルを結合キューに追加しました。",
        "status_external_sub": "外部字幕を適用しました: {name}",
        "status_muted": "消音設定",
        "status_unmuted": "消音解除",
        "status_volume": "音量: {value}%",
        "status_step_back": "1フレーム戻る",
        "status_step_fwd": "1フレーム進む",
        "status_skip_back": "5秒戻る",
        "status_skip_fwd": "5秒進む",
        "status_jump_start": "開始位置へ移動: {time}",
        "status_active_cleared": "現在の選択マークを解除しました。",
        "status_segment_deleted": "区間 {idx} を削除しました。",
        "status_start_set": "開始点を設定: {time}",
        "status_segment_saved": "区間を追加保存: {start} ~ {end}",
        "status_all_cleared": "全区間をリセットしました。",
        "status_inverse": "選択範囲を反転しました。",
        "status_task_complete": "処理が完了しました。",
        "status_task_failed": "処理が中止または失敗しました。",
        "status_lang_changed": "言語を変更しました: {lang}",

        # Dialogs & Prompts
        "dialog_unsupported_title": "非対応ファイル",
        "dialog_unsupported_msg": "動画ファイル(.mkv, .mp4, .avi)のみ対応しています。",
        "dialog_sub_fail_title": "字幕読み込み失敗",
        "dialog_sub_fail_msg": "字幕ファイルを適用できませんでした:\n{error}",
        "dialog_warn_title": "警告",
        "dialog_warn_end_before_start": "終了点は開始点より後に設定してください。",
        "dialog_diff_ext_title": "警告: 拡張子の不一致",
        "dialog_diff_ext_msg": "結合するファイルの拡張子が一致していません。\n結合後に再生できないか破損する恐れがあります。\n\n処理を続行しますか？",
        "dialog_btn_force_merge": "強制結合",
        "dialog_btn_cancel": "キャンセル",
        "dialog_export_fail_title": "失敗",
        "dialog_pgs_warn_title": "字幕形式の警告",
        "dialog_pgs_warn_msg": "選択した字幕(PGS/画像字幕)はテキスト形式ではありません。\n.srt/.ass などのテキスト字幕に直接変換することはできません。\n.sup または .mks 形式で保存してください。",
        "dialog_open_file": "動画ファイルを開く",
        "dialog_open_sub": "字幕ファイルを開く",
        "dialog_save_file": "保存先ファイルを選択",
        "dialog_save_merge": "結合ファイルの保存先",
        "dialog_export_progress_title": "出力の進行状況",
        "dialog_preparing": "準備中...",
        "dialog_cancel": "キャンセル",
        "dialog_done_title": "完了",
        
        # Worker Tasks
        "task_export_sub": "字幕を出力中...",
        "task_export_part": "区間を出力中... ({curr}/{total})",
        "task_merge_parts": "区間クリップを結合中...",
        "task_merge_multi": "複数ファイルを結合中...",
        
        # File Filters
        "filter_video_files": "動画ファイル",
        "filter_sub_files": "字幕ファイル",
        "filter_audio_files": "音声ファイル",
        "filter_all_files": "すべてのファイル",
        
        # Shortcuts Guide HTML
        "shortcuts_title": "ショートカットキー案内",
        "shortcuts_html": (
            "<b>ショートカットキー一覧</b><br><br>"
            "<b>Space</b> : 再生 / 一時停止<br>"
            "<b>Esc</b> : 停止 / 動画を閉じる / 全画面解除<br>"
            "<b>← / →</b> : 5秒 戻る / 進む<br>"
            "<b>D / F</b> : 1フレーム 戻る / 進む<br>"
            "<b>[ / ]</b> : 開始点 / 終了点の設定<br>"
            "<b>, / .</b> : 開始点 / 終了点へ移動<br>"
            "<b>M</b> : 消音切替<br>"
            "<b>↑ / ↓</b> : 音量調整<br>"
            "<b>Alt+Enter</b> : 全画面切替<br>"
            "<b>Ctrl+O</b> : ファイルを開く<br>"
        ),
        # Extra Type Menu & Mode Strings
        "menu_type_all": "すべての種類を選択",
        "menu_type_vid": "動画のみ選択",
        "menu_type_aud": "音声のみ選択",
        "menu_type_sub": "字幕のみ選択",
        "status_error": "エラーが発生しました",
        "label_segments_merge_disabled": "（結合モード - 区間設定不可）",
        "multi_merge_title_idx": "MKV Lossless Cutter - 複数ファイルプレビュー ({curr}/{total})",
        "filter_merge_media": "メディアファイル",
        "task_cancelled_user": "ユーザーによってキャンセルされました",
        "task_all_complete": "すべてのタスクが完了しました",
    },
    
    "zh": {
        # App Title
        "app_title": "MKV Lossless Cutter",
        "app_title_file": "MKV Lossless Cutter - {name}",
        "multi_merge_title": "MKV Lossless Cutter - 多文件合并模式",
        
        # Tooltips - Playback controls
        "tooltip_pre_frame": "后退1帧 (D)",
        "tooltip_rewind": "快退5秒 (←)",
        "tooltip_play": "播放 (Space)",
        "tooltip_pause": "暂停 (Space)",
        "tooltip_play_or_open": "播放 / 未打开文件时打开 (Space)",
        "tooltip_stop": "停止并重置 (Esc)",
        "tooltip_fast_forward": "快进5秒 (→)",
        "tooltip_next_frame": "前进1帧 (F)",
        "tooltip_open": "打开文件 (Ctrl+O)",
        "tooltip_mute": "静音切换 (M)",
        "tooltip_unmute": "取消静音 (M)",
        
        # Tooltips - Cut controls
        "tooltip_set_start": "设为起点 ([)",
        "tooltip_set_end": "设为终点 (])",
        "tooltip_jump_start": "跳到起点 (,)",
        "tooltip_jump_end": "跳到终点 (.)",
        "tooltip_inverse": "反向选择",
        "tooltip_clear": "清除选择",
        "tooltip_maximize": "窗口最大化 / 还原 (双击画面)",
        "tooltip_fullscreen": "纯全屏模式 (Alt+Enter)",
        
        # List controls
        "tooltip_item_up": "上移",
        "tooltip_item_down": "下移",
        "tooltip_item_delete": "删除",

        # Labels & Buttons
        "merge_checkbox": "多片段合并 (Merge)",
        "btn_export": "导出",
        "btn_start_merge": "开始合并",
        "label_tracks": "轨道、章节与标签",
        "label_segments": "裁剪片段列表",
        "label_merge_queue": "多文件合并队列",
        
        # Table Headers
        "col_select": "",
        "col_type": "类型",
        "col_codec": "编解码器",
        "col_copy": "复制",
        "col_lang": "语言",
        "col_name": "名称",
        "col_id": "ID",
        "col_default": "默认轨道",
        "col_forced": "强制显示",
        "type_all": "全选类型",
        "type_video": "视频",
        "type_audio": "音频",
        "type_sub": "字幕",
        "yes": "是",
        "no": "否",
        
        # Context Menu
        "menu_open": "打开文件... (Ctrl+O)",
        "menu_play_pause": "播放 / 暂停 (Space)",
        "menu_stop": "停止 (S)",
        "menu_audio": "音频",
        "menu_mute": "静音",
        "menu_current_audio": "正在播放音频: {title}",
        "menu_sub": "字幕",
        "menu_open_sub": "打开外挂字幕...",
        "menu_show_sub": "显示字幕",
        "menu_current_sub": "正在播放字幕: {title}",
        "menu_not_used": "禁用",
        "menu_none": "无",
        "menu_track_format": "轨道 {id}",
        "menu_language": "语言 (Language)",
        "menu_fullscreen": "全屏显示 (Alt+Enter)",
        "menu_normal_screen": "还原窗口 (Alt+Enter)",
        "menu_shortcuts": "快捷键说明",
        "menu_exit": "退出 (Esc)",
        
        # Segments list items
        "segment_prefix": "片段",
        "segment_active_prefix": "> 当前选中: {start} ~ {end}",
        "segment_unspecified": "未指定",
        
        # Status Bar Messages
        "status_ready": "准备就绪",
        "status_playing": "播放中",
        "status_paused": "已暂停",
        "status_sub_show": "显示字幕",
        "status_sub_hide": "关闭字幕",
        "status_fullscreen": "全屏模式",
        "status_maximized": "最大化模式",
        "status_normal": "恢复常规窗口",
        "status_file_loaded": "已载入文件: {name}",
        "status_files_added": "已将 {count} 个文件添加到合并队列。",
        "status_external_sub": "已应用外部字幕: {name}",
        "status_muted": "已静音",
        "status_unmuted": "已取消静音",
        "status_volume": "音量: {value}%",
        "status_step_back": "后退1帧",
        "status_step_fwd": "前进1帧",
        "status_skip_back": "后退5秒",
        "status_skip_fwd": "前进5秒",
        "status_jump_start": "移动到片段起点: {time}",
        "status_active_cleared": "已取消当前临时标记。",
        "status_segment_deleted": "片段 {idx} 已删除。",
        "status_start_set": "已设置起点: {time}",
        "status_segment_saved": "已添加片段: {start} ~ {end}",
        "status_all_cleared": "已重置所有裁剪片段。",
        "status_inverse": "已反转选择区域。",
        "status_task_complete": "操作已完成。",
        "status_task_failed": "操作已取消或失败。",
        "status_lang_changed": "语言已切换: {lang}",

        # Dialogs & Prompts
        "dialog_unsupported_title": "不支持的文件",
        "dialog_unsupported_msg": "仅支持视频文件 (.mkv, .mp4, .avi)。",
        "dialog_sub_fail_title": "字幕载入失败",
        "dialog_sub_fail_msg": "无法应用字幕文件:\n{error}",
        "dialog_warn_title": "警告",
        "dialog_warn_end_before_start": "终点必须在起点之后。",
        "dialog_diff_ext_title": "警告: 扩展名不一致",
        "dialog_diff_ext_msg": "合并的文件扩展名不一致。\n可能导致合并后的视频无法播放或损坏。\n\n是否仍然强制合并？",
        "dialog_btn_force_merge": "强制合并",
        "dialog_btn_cancel": "取消",
        "dialog_export_fail_title": "失败",
        "dialog_pgs_warn_title": "字幕格式警告",
        "dialog_pgs_warn_msg": "所选字幕(PGS/图像字幕)非纯文本格式。\n无法直接导出为 .srt/.ass 文本字幕。\n请保存为 .sup 或 .mks 格式。",
        "dialog_open_file": "打开视频文件",
        "dialog_open_sub": "打开字幕文件",
        "dialog_save_file": "选择保存文件",
        "dialog_save_merge": "保存合并文件",
        "dialog_export_progress_title": "导出进度",
        "dialog_preparing": "正在准备任务...",
        "dialog_cancel": "取消",
        "dialog_done_title": "完成",
        
        # Worker Tasks
        "task_export_sub": "正在导出字幕...",
        "task_export_part": "正在导出片段... ({curr}/{total})",
        "task_merge_parts": "正在合并分段文件...",
        "task_merge_multi": "正在合并多文件...",
        
        # File Filters
        "filter_video_files": "视频文件",
        "filter_sub_files": "字幕文件",
        "filter_audio_files": "音频文件",
        "filter_all_files": "所有文件",
        
        # Shortcuts Guide HTML
        "shortcuts_title": "快捷键说明",
        "shortcuts_html": (
            "<b>快捷键列表</b><br><br>"
            "<b>Space</b> : 播放 / 暂停<br>"
            "<b>Esc</b> : 停止 / 关闭文件 / 退出全屏<br>"
            "<b>← / →</b> : 快退 / 快进 5秒<br>"
            "<b>D / F</b> : 后退 / 前进 1帧<br>"
            "<b>[ / ]</b> : 设置起点 / 终点<br>"
            "<b>, / .</b> : 跳至起点 / 终点<br>"
            "<b>M</b> : 静音切换<br>"
            "<b>上 / 下方向键</b> : 音量调节<br>"
            "<b>Alt+Enter</b> : 切换全屏<br>"
            "<b>Ctrl+O</b> : 打开文件<br>"
        ),
        # Extra Type Menu & Mode Strings
        "menu_type_all": "选择所有类型",
        "menu_type_vid": "仅选择视频",
        "menu_type_aud": "仅选择音频",
        "menu_type_sub": "仅选择字幕",
        "status_error": "发生错误",
        "label_segments_merge_disabled": "（合并模式 - 禁用片段设置）",
        "multi_merge_title_idx": "MKV Lossless Cutter - 多文件预览 ({curr}/{total})",
        "filter_merge_media": "媒体文件",
        "task_cancelled_user": "已被用户取消",
        "task_all_complete": "所有任务已完成",
    }
}

_current_language = "ko"

def init_language():
    global _current_language
    settings = QSettings("MKVLosslessEditor", "MKVLosslessEditor")
    saved_lang = settings.value("language", "ko")
    if saved_lang in SUPPORTED_LANGUAGES:
        _current_language = saved_lang
    else:
        _current_language = "ko"
    return _current_language

def get_current_language():
    return _current_language

def set_current_language(lang_code):
    global _current_language
    if lang_code in SUPPORTED_LANGUAGES:
        _current_language = lang_code
        settings = QSettings("MKVLosslessEditor", "MKVLosslessEditor")
        settings.setValue("language", lang_code)
        return True
    return False

def tr(key, **kwargs):
    """
    Translates key for the current language.
    Falls back to Korean if missing in current language, or returns key if not found.
    Supports .format(**kwargs) substitutions.
    """
    lang_dict = TRANSLATIONS.get(_current_language, TRANSLATIONS["ko"])
    text = lang_dict.get(key)
    if text is None:
        text = TRANSLATIONS["ko"].get(key, key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text
