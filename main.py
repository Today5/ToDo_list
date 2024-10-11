import os
import re
import json
from datetime import datetime

#タスクを番号付きで表示する
def display_task(task_list):
    for i, task in enumerate(task_list, start=1):
        status = "(完了)" if task["completed"] in task else "(未完了)"
        print(f"{i}. {task['task']} 期限: {task['due_date']} {status}")

# タスクを1つずつ入力し、終了するためのコマンドを設定
def add_task(task_list):
    while True:
        task_name = input("タスクを入力してください(終了するには'exit'と入力):")
        if task_name.lower() == "exit":
            break

        #タスクの期限を入力する
        while True:
            due_date = input("期限をYYYY-MM-DD形式で入力してください:")
            pattern = r"\d{4}-\d{2}-\d{2}$"

            # 期限が正しい形式か確認する
            if re.match(pattern, due_date):
                print("期限をタスクに追加します")
                break
            else:
                print("期限の形式が正しくありません")
        # タスクをタスクリストに追加する
        task_entry = {"task": task_name, "due_date": due_date, "completed": False}
        task_list.append(task_entry)
    return task_list

# タスクを削除する
def delete_task(task_list):
    while True:
        delete_number = input("削除するタスクの番号を指定する(-1入力で終了する):")

        # 削除処理の終了
        if delete_number == "-1":
            print("削除処理を終了します")
            break

        # 数字かどうかを確認
        if delete_number.isdigit():
            delete_index = int(delete_number) - 1

            # 有効な範囲のインデックスか確認する
            if 0 <= delete_index < len(task_list):
                del task_list[delete_index]
                print(f"タスク {delete_number} が削除されました")
                # 最新のタスクリストを番号付きで表示
                if task_list:
                    display_task(task_list)

                else:
                    print("タスクリストが空です")
            else:
                print("無効な番号です。もう一度試してください")
        else:
            print("無効な入力です。数字を入力してください")

def mark_task_as_complete(task_list):
    # タスクの完了処理
    while True:
        finish_number = input("終了したタスクの番号を指定する(-1入力で終了する):")

        # 完了処理の終了
        if finish_number == "-1":
            print("完了処理を終了します")
            break

        # 数字かどうかを確認
        if finish_number.isdigit():
            finish_index = int(finish_number) - 1
            # 有効な範囲のインデックスか確認する
            if 0 <= finish_index < len(task_list):
                # 既に完了マークがついていない場合にだけ付ける
                task_list[finish_index]['completed'] = True
                print(f"タスク {finish_number} が完了しました")
            # 最新のタスクリストを番号付きで表示
                display_task(task_list)
            else:
                print("無効な番号です。もう一度試してください")
        else:
            print("無効な入力です。数字を入力してください")


def main():
# ファイルからタスクリストを読み込む
    if os.path.exists("task_list.txt"):
        with open("task_list.txt", "r", encoding="utf-8") as file:
            try:
                task_list = json.load(file)
            except json.JSONDecodeError:
                print("タスクリストの読み込み中にエラーが発生しました。ファイル形式を確認してください。")
                task_list = []
    else:
        task_list = []
    
    while True:
        print("1:タスクの追加")
        print("2:タスクの表示")
        print("3:タスクの削除")
        print("4:タスクの完了")
        print("5:タスクの保存")
        print("6:プログラム終了")
        
        choice = input("モードを選択してください:")
    
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            display_task(task_list)
        elif choice == "3":
            delete_task(task_list)
        elif choice == "4":
            mark_task_as_complete(task_list)
        elif choice == "5":
            # タスクリストをテキストファイルに保存
            with open("task_list.txt", "w", encoding="utf-8") as file:
                json.dump(task_list, file, ensure_ascii=False, indent=4)
            print("タスクリストを保存しました。")
        elif choice == "6":
            print("プログラムを終了します")
            break
        else:
            print("入力が間違っています。")

if __name__ == "__main__":
    main()