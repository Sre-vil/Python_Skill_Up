import os
import datetime

# --- 설정 (사용자화 가능) ---
base_dir_path = "/Users/srevil/For Me/0. Study/3. VSCode/Sre-vil.github.io/_posts"
favorites = {
    1: {"name": "BOJ 문제 풀이", "path": "CS/Programming"},
    2: {"name": "네트워크 임시", "path": "CS/Network"},
    3: {"name": "웹 해킹 초급", "path": "Security/Web hacking/Beginner"},
    4: {"name": "웹 해킹 Lv1", "path": "Security/Web hacking/Lv1"}
}

# --- 함수 정의 ---
def get_subdirectories(path):
    """지정된 경로의 하위 디렉터리 목록을 스캔하여 정렬된 리스트로 반환합니다."""
    sub_dirs = []
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir() and not entry.name.startswith('.'):
                    sub_dirs.append(entry.name)
    except FileNotFoundError:
        return []
    sub_dirs.sort()
    return sub_dirs

# --- 스크립트 본문 ---
try:
    final_path = ""
    path_parts = []

    # --- 메인 메뉴 (즐겨찾기 / 직접 선택) ---
    print("========================================")
    print("작업을 선택하세요.")
    print("1. 즐겨찾기에서 선택")
    print("2. 직접 경로 선택")
    print("========================================")
    main_choice = int(input("번호 입력: "))

    if main_choice == 1:
        # ... 즐겨찾기 선택 로직 (이전과 동일) ...
        print("\n----------------------------------------")
        print("즐겨찾기 목록")
        for key, fav in favorites.items():
            print(f"{key}. {fav['name']}  ({fav['path']})")
        print("----------------------------------------")
        fav_choice = int(input("번호 입력: "))
        selected_fav = favorites.get(fav_choice)
        if not selected_fav:
            print("Error: 잘못된 번호입니다."); exit()
        path_parts = selected_fav['path'].split('/')
        final_path = os.path.join(base_dir_path, *path_parts)

    elif main_choice == 2:
        # ... 동적 경로 선택 로직 (이전과 동일) ...
        current_path = base_dir_path
        while True:
            sub_dirs = get_subdirectories(current_path)
            if not sub_dirs:
                print(f"\n현재 위치({current_path})에 파일을 생성합니다."); break
            print("\n----------------------------------------")
            print(f"현재 위치: {current_path}")
            print("이동할 하위 폴더를 선택하세요.")
            print("0. [ 현재 위치에 파일 생성 ]")
            for i, dir_name in enumerate(sub_dirs, 1): print(f"{i}. {dir_name}")
            print("----------------------------------------")
            choice = int(input("번호 입력: "))
            if choice == 0: break
            selected_dir = sub_dirs[choice - 1]
            path_parts.append(selected_dir)
            current_path = os.path.join(current_path, selected_dir)
        final_path = current_path
    else:
        print("Error: 1 또는 2를 입력해야 합니다."); exit()

    # --- 경로에 따른 파일명 및 내용 생성 (규칙 기반) ---
    print("\n----------------------------------------")
    today_str = datetime.date.today().strftime('%Y-%m-%d')
    file_content = ""
    file_name = ""

    # 규칙 1: /CS/Network 경로
    if final_path.endswith("CS/Network"):
        print("'/CS/Network' 경로 규칙을 적용합니다.")
        file_name = f"{today_str}-tmp.md"
        file_content = f'''---
title: "[tmp].tmp"
categories: [CS, Network]
tags: [네트워크, tmp]
mermaid: true
---
'''
    # 규칙 2: /Security/Web hacking 경로
    elif "Security/Web hacking" in final_path:
        print("'/Security/Web hacking' 경로 규칙을 적용합니다.")
        file_name = f"{today_str}-tmp.md"
        sub_path_name = path_parts[-1] # 예: Beginner, Lv1
        
        # Lv1 -> Level1, Lv2 -> Level2 변환
        if "Lv" in sub_path_name:
            display_name = sub_path_name.replace("Lv", "Level")
        else:
            display_name = sub_path_name
            
        file_content = f'''---
title: "[{display_name}]tmp"
categories: [Security, Web]
tags: [Dreamhack, {display_name}]
mermaid: true
---
'''
    # 규칙 3: /CS/Programming 경로 (BOJ)
    elif final_path.endswith("CS/Programming"):
        print("'/CS/Programming' 경로 규칙을 적용합니다. (BOJ)")
        problem_number = input("BOJ 문제 번호를 입력하세요: ")
        problem_name = input("BOJ 문제 이름을 입력하세요: ")
        language = input("사용한 언어를 입력하세요 (e.g., Python): ")
        problem_class = input("문제 클래스 또는 난이도를 입력하세요 (e.g., Class2): ")
        
        file_name = f"{today_str}-BOJ-{problem_number}.md"
        file_content = f'''---
title: "[BOJ]{problem_number}.{problem_name}"
categories: [{path_parts[-2]}, {path_parts[-1]}]
tags: [{language}, BOJ, {problem_class}]
mermaid: true
---

# [{problem_number}] {problem_name}
'''
    # 규칙 4: 그 외 모든 일반 경로
    else:
        print("일반 규칙을 적용합니다.")
        filename_input = input("파일명을 입력하세요: ")
        file_name = f"{today_str}-{filename_input}.md"
        
        # Security 하위 폴더의 경우 categories 규칙 변경
        if len(path_parts) >= 2 and path_parts[0] == "Security":
            second_cat = path_parts[1].split(' ')[0] # 'System hacking' -> 'System'
            categories_str = f"[{path_parts[0]}, {second_cat}]"
        else:
            categories_str = f"[{', '.join(path_parts)}]"

        file_content = f'''---
title: "{filename_input}"
categories: {categories_str}
tags: []
mermaid: true
---

# {filename_input}
'''
    # --- 최종 파일 생성 ---
    full_file_path = os.path.join(final_path, file_name)
    os.makedirs(final_path, exist_ok=True)
    with open(full_file_path, 'w', encoding='utf-8') as f:
        f.write(file_content)
    print("\n✅ 파일 생성 완료!")
    print(f"   위치: {full_file_path}")

except (ValueError, IndexError, KeyError):
    print("\nError: 숫자로 된 번호를 정확히 입력해주세요.")
except OSError as e:
    print(f"\nError: 파일 또는 디렉터리 생성 중 오류가 발생했습니다 - {e}")