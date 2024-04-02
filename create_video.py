from VideoGenerator import *

media_info = [
    {"image": r"images\20240330\test01.png", "audio_file": r"azure\output_0.wav", "audio_duration": 9.045,
        "intro_texts": {
            "text": "蜿蜒する山道を、李慕は命からがら逃げる。途中で話すキツネの声を聞いたが、不思議に思いつつも、確かめに戻る勇気はなかった。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
    {"image": r"images\20240330\test02.png", "audio_file": r"azure\output_1.wav", "audio_duration": 5.045,
        "intro_texts": {
            "text": "しばらく走った後、彼は山の麓に来ていることに気づき、深い疑問を持った。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
    {"image": r"images\20240330\test03.png", "audio_file": r"azure\output_2.wav", "audio_duration": 8.045,
        "intro_texts": {
            "text": "頭の中の記憶を整理すると、李慕は自分が長生きと神通力を追求する修行者や、妖怪がはびこる奇妙な世界に来ていることを知った。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
    {"image": r"images\20240330\test04.png", "audio_file": r"azure\output_3.wav", "audio_duration": 9,
        "intro_texts": {
            "text": "官道で、数人の捕快が李慕に対して、県役所の公人の身体を乗っ取ったと非難したが、調べた結果、彼がただ三魂が抜けただけであることがわかった。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
    {"image": r"images\20240330\test05.png", "audio_file": r"azure\output_4.wav", "audio_duration": 7.045,
        "intro_texts": {
            "text": "李慕は自分が陽丘県役所の捕快、李慕であることを知り、しかし自分の上司である李清のことしか覚えていなかった。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
    {"image": r"images\20240330\test06.png", "audio_file": r"azure\output_5.wav", "audio_duration": 5.045,
        "intro_texts": {
            "text": "捕快の張山と李肆から、李慕は自分の身世とこの世界の神秘について知った。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
    {"image": r"images\20240330\test07.png", "audio_file": r"azure\output_6.wav", "audio_duration": 7.045,
        "intro_texts": {
            "text": "妖怪が恐ろしく聞こえるかもしれないが、中国の神話に小さい頃から触れていた李慕は、それを非常に刺激的に感じた。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
    {"image": r"images\20240330\test08.png", "audio_file": r"azure\output_7.wav", "audio_duration": 8.045,
        "intro_texts": {
            "text": "家に帰ると、李慕は自分が一文無しであることに気づき、張山と李肆にお金を借りようとしたが、二人は用事があると言って急いで去っていった。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
    {"image": r"images\20240330\test09.png", "audio_file": r"azure\output_8.wav", "audio_duration": 5.045,
        "intro_texts": {
            "text": "李慕は自分が死を経験しただけでなく、新たな困難と挑戦に直面していることを悟った。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
    {"image": r"images\20240330\test10.png", "audio_file": r"azure\output_9.wav", "audio_duration": 16.045,
        "intro_texts": {
            "text": "その一方で、陽丘県の外にある幽谷で、一匹の小さなキツネが李慕への恩返しに悩んでいた。老キツネはそれに対して、キツネ仙族は恩を必ず返すものだが、小キツネの道行が浅すぎるため、とりあえず山で修行を積み、恩返しは後日にするように言った。", 
            "duration": 1, 
            "position": ("center", "bottom")
        }
    },
]
video_generator = VideoGenerator(output_file="final_output.mp4")
video_generator.generate_video(media_info)