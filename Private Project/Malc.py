def weapon_calc():
      result = 0
      print("********************************\n"
            "1. 히어로, 팔라딘, 다크나이트, 바이퍼, 캐논슈터, 아란, 은월, 소울마스터, 미하일, 스트라이커, 데몬슬레이어, 카이저, 제로, 아크\n"
            "2. 보우마스터, 신궁, 캡틴, 메르세데스, 윈드브레이커, 와일드헌터, 메카닉, 엔젤릭버스터\n"
            "3. 아크메이지(불/독), 아크메이지 (썬/콜), 비숍, 에반, 루미너스, 플레임위자드, 배틀메이지, 키네시스, 일리움\n"
            "4. 나이트로드, 나이트워커, 팬텀, 듀얼블레이드, 제논\n"
            "5. 여기에 제 직업이 없어요.\n"
            "********************************")

      job = int(input("SYSTEM: 해당 무기와 알맞는 직업을 선택해주세요: "))

      if job == 1:
            count = int(input("SYSTEM: 해당 무기는 몇 작입니까: "))
            STR = int(input("추옵 제외, 증가된 STR은 몇 입니까: "))
            DEX = int(input("추옵 제외, 증가된 DEX는 몇 입니까: "))

            if ((STR - DEX) % count) != 0:
                  print("RESULT: 해당 무기는 섞작입니다.")
                  return 0
            else:
                  result = int((STR - DEX) / count)
      elif job == 2:
            count = int(input("SYSTEM: 해당 무기는 몇 작입니까: "))
            DEX = int(input("추옵 제외, 증가된 DEX은 몇 입니까: "))
            STR = int(input("추옵 제외, 증가된 STR는 몇 입니까: "))

            if ((DEX - STR) % count) != 0:
                  print("RESULT: 해당 무기는 섞작입니다.")
                  return 0
            else:
                  result = int((DEX - STR) / count)
      elif job == 3:
            count = int(input("SYSTEM: 해당 무기는 몇 작입니까: "))
            INT = int(input("추옵 제외, 증가된 INT은 몇 입니까: "))
            LUK = int(input("추옵 제외, 증가된 LUK는 몇 입니까: "))

            if ((INT - LUK) % count) != 0:
                  print("RESULT: 해당 무기는 섞작입니다.")
                  return 0
            else:
                  result = int((INT - LUK) / count)
      elif job == 4:
            count = int(input("SYSTEM: 해당 무기는 몇 작입니까: "))
            LUK = int(input("추옵 제외, 증가된 LUK은 몇 입니까: "))
            DEX = int(input("추옵 제외, 증가된 DEX는 몇 입니까: "))

            if ((LUK - DEX) % count) != 0:
                  print("RESULT: 해당 무기는 섞작입니다.")
                  return 0
            else:
                  result = int((LUK - DEX) / count)
      elif job == 5:
            print("SYSTEM: 지원하지 않는다는 뜻입니다 ^~^ ")

      if result == 1:
            print("RESULT: 해당 무기는 100% 떡작입니다.")
      elif result == 2:
            print("RESULT: 해당 무기는 70% 떡작입니다.")
      elif result == 3:
            print("RESULT: 해당 무기는 30% 완작입니다.")
      elif result == 4:
            print("RESULT: 해당 무기는 15% 완작입니다.")

def defense_calc():
      result = 0
      print("********************************\n"
            "1. 히어로, 팔라딘, 다크나이트, 바이퍼, 캐논슈터, 아란, 은월, 소울마스터, 미하일, 스트라이커, 데몬슬레이어, 카이저, 제로, 아크\n"
            "2. 보우마스터, 신궁, 캡틴, 메르세데스, 윈드브레이커, 와일드헌터, 메카닉, 엔젤릭버스터\n"
            "3. 아크메이지(불/독), 아크메이지 (썬/콜), 비숍, 에반, 루미너스, 플레임위자드, 배틀메이지, 키네시스, 일리움\n"
            "4. 나이트로드, 나이트워커, 팬텀, 듀얼블레이드, 제논\n"
            "5. 여기에 제 직업이 없어요.\n"
            "********************************")

      job = int(input("SYSTEM: 해당 방어구와 알맞는 직업을 선택해주세요: "))

      if job == 1:
            count = int(input("SYSTEM: 해당 방어구는 몇 작입니까: "))
            STR = int(input("추옵 제외, 증가된 STR은 몇 입니까: "))
            DEX = int(input("추옵 제외, 증가된 DEX는 몇 입니까: "))

            if ((STR - DEX) % count) != 0:
                  print("RESULT: 해당 방어구는 섞작입니다.")
                  return 0
            else:
                  result = int((STR - DEX) / count)
      elif job == 2:
            count = int(input("SYSTEM: 해당 방어구는 몇 작입니까: "))
            DEX = int(input("추옵 제외, 증가된 DEX은 몇 입니까: "))
            STR = int(input("추옵 제외, 증가된 STR는 몇 입니까: "))

            if ((DEX - STR) % count) != 0:
                  print("RESULT: 해당 방어구는 섞작입니다.")
                  return 0
            else:
                  result = int((DEX - STR) / count)
      elif job == 3:
            count = int(input("SYSTEM: 해당 방어구는 몇 작입니까: "))
            INT = int(input("추옵 제외, 증가된 INT은 몇 입니까: "))
            LUK = int(input("추옵 제외, 증가된 LUK는 몇 입니까: "))

            if ((INT - LUK) % count) != 0:
                  print("RESULT: 해당 방어구는 섞작입니다.")
                  return 0
            else:
                  result = int((INT - LUK) / count)
      elif job == 4:
            count = int(input("SYSTEM: 해당 방어구는 몇 작입니까: "))
            LUK = int(input("추옵 제외, 증가된 LUK은 몇 입니까: "))
            DEX = int(input("추옵 제외, 증가된 DEX는 몇 입니까: "))

            if ((LUK - DEX) % count) != 0:
                  print("RESULT: 해당 방어구는 섞작입니다.")
                  return 0
            else:
                  result = int((LUK - DEX) / count)
      elif job == 5:
            print("SYSTEM: 지원하지 않는다는 뜻입니다 ^~^ ")

      if result == 3:
            print("RESULT: 해당 방어구는 100% 떡작입니다.")
      elif result == 4:
            print("RESULT: 해당 방어구는 70% 완작입니다.")
      elif result == 7:
            print("RESULT: 해당 방어구는 30% 완작입니다.")


print("********************************")
print("********************************")
print("Malc는 메이플스토리 게임에서의 계산을 돕기 위해 제작된 프로그램입니다.")

while True:
      print("******************\n"
            "1. 무기작 계산\n"
            "2. 방어구작 계산\n"
            "3. 종료\n"
            "******************")
      try:
            command = int(input("SYSTEM: 명령을 내려주세요: "))
      except:
            print("ERROR: 올바른 명령이 아닙니다.")
      else:
            if command == 1:
                  weapon_calc()
            elif command == 2:
                  defense_calc()
            elif command == 3:
                  break
            else:
                  print("ERROR: 올바른 명령이 아닙니다.")
