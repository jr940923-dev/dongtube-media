# 동트베 홀덤TV 제작 도구

복원: 이 폴더를 ~/dongtube 로 복사 (tools, templates, assets, motion).
카드: PYTHONPATH=tools python3 tools/content_jan.py → node tools/shot.js templates/tipNN.html
쇼츠: python3 tools/motion_jan.py → tools/make_short.sh NN (motion/tip01.html 이 쇼츠 틀 원본). make_short.sh가 끝에 배경음(assets/bgm_edu.wav)을 입힌 shorts/tipNN_bgm.mp4 를 만든다. 업로드는 _bgm.mp4 를 쓴다.
정답 스토리: python3 tools/story_jan.py → node tools/story_shot_jan.js
검산: tools/icm.py (ICM), tools/poker.py (승률)
