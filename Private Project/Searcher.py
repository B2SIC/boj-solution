import os
from tkinter import filedialog, Tk


def by_filename_search(path, target):
    for (root, dir, files) in os.walk(path):
        for filename in files:
            full_filename = root + "\\" + filename
            only_name = os.path.splitext(filename)[0].lower()

            if target.lower() == only_name:
                print(full_filename)


def by_file_extension_search(path, target):
    for (root, dir, files) in os.walk(path):
        for filename in files:
            full_filename = root + "\\" + filename
            ext = os.path.splitext(full_filename)[-1].lower()

            if ext.lower() == target:
                print(full_filename)


print("*********************************")
print("반갑습니다. 저는 여러분을 도와줄 Searcher입니다.")
print("메인 명령 코드로 100을 입력하시면 친절하게 사용법을 설명해드릴게요 :)")

while True:
    print("*********************************\n"
          "1. 파일 이름으로 찾기\n"
          "2. 확장자로 찾기 (example => .exe .avi ...)\n"
          "3. 종료\n"
          "*********************************")
    try:
        command = int(input("명령을 내려주세요: "))
    except ValueError:
        print("ERROR: 명령은 숫자로 입력합니다.")
    else:
        if command == 1:
            print("*********************************")
            print("지금부터 파일 이름으로 파일을 찾겠습니다.")
            print("검색을 시작할 출발 경로를 지정해주세요: ", end='')
            root = Tk()
            root.geometry('0x0')
            directory = filedialog.askdirectory()
            root.destroy()
            print(directory)
            condition = input("찾고자 하는 정확한 파일 명(확장자 제외)을 입력해주세요: ")

            print("************ 검색을 시작합니다 ************")
            by_filename_search(directory, condition)
            print("*************** 작업 완료 **************")

        elif command == 2:
            print("*********************************")
            print("지금부터 확장자로 파일을 찾겠습니다.")
            print("검색을 시작할 출발 경로를 지정해주세요: ", end='')
            root = Tk()
            root.geometry('0x0')
            directory2 = filedialog.askdirectory()
            root.destroy()
            print(directory2)
            print("확장자 명은 아래와 같이 dot(.)을 포함해서 입력합니다. (Example => .exe)")
            condition2 = input("찾고자 하는 정확한 확장자 명을 입력해주세요: ")

            print("************ 검색을 시작합니다 ************")
            by_file_extension_search(directory2, condition2)
            print("*************** 작업 완료 **************")

        elif command == 3:
            break

        elif command == 100:
            print("*********************************")
            print("지금부터 Searcher에 대한 사용법을 안내해드리겠습니다.")
            print("우선 기본적으로 파일 이름으로 찾는 방식과 확장자로 찾는 방식이 있습니다.")
            print("여기서 확장자란 filename.exe 에서 .exe 를 말합니다.")
            print("파일 이름으로 찾을 경우에는 시작 경로와 파일 이름이 필요하고")
            print("확장자로 찾을 경우에는 시작 경로와 찾고자 하는 확장자 명이 필요합니다.")
            print("시작 경로는 명령을 내린 후 폴더를 선택하는 창이 나오는데")
            print("해당 창에서 검색을 시작할 폴더를 지정해주시면 됩니다.")
            print("요청하신 파일을 찾을 때는 선택하신 폴더 안에 존재하는 모든 폴더를 검사합니다.")
            print("TIP: 만약 시작 경로를 드라이브(ex=> C:/) 전체로 지정하실 경우 많은 시간이 필요할 수 있습니다.")
            print("TIP: 확장자 명과 파일 명 모두 대소문자 상관없이 검색합니다.")
            print("TIP: 파일 명보다는 확장자 명으로 찾는 것이 빠를 수도 있습니다.")
            print("참고: 파일 명 검사는 유사도 비교가 아닌 정확한 일치 or 불일치만 판정합니다.")
            print("*********************************")

        else:
            print("ERROR: 올바른 명령이 아닙니다.")
