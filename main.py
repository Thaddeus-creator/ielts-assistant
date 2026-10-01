import sys
import random
from modules.vocab_manager import VocabManager

DATA_FILE = 'data/vocabulary.json'

def main():
    manager = VocabManager(DATA_FILE)
    
    while True:
        print("\n=== IELTS TERMINAL ASSISTANT ===")
        print("1. Thêm từ vựng mới")
        print("2. Xem danh sách từ")
        print("3. Kiểm tra từ vựng (Quiz nhanh)")
        print("4. Thoát")

        choice = input("\nChọn chức năng (1-4): ")
        
        if choice == '1':
            word = input("Nhập từ tiếng Anh: ")
            w_type = input("Từ loại (n/v/adj/adv): ")
            meaning = input("Nghĩa tiếng Việt: ")
            example = input("Ví dụ (nếu có): ")
            
            manager.add_word(word, w_type, meaning, example)
            print(f"[+] Đã lưu '{word}' thành công vào database!")
            
        elif choice == '2':
            words = manager.list_words()
            if not words:
                print("[-] Danh sách từ vựng trống.")
            else:
                for idx, w in enumerate(words, 1):
                    print(f"{idx}. {w['word']} ({w['word_type']}): {w['meaning']}")
                    if w.get('example'):
                        print(f"   Ví dụ: {w['example']}")
                        
        elif choice == '3':
            words = manager.list_words()
            if not words:
                print("[-] Chưa có từ vựng nào để kiểm tra. Hãy thêm từ ở mục 1 trước!")
            else:
                target = random.choice(words)
                print(f"\n--- QUIZ TIME ---")
                print(f"Từ loại: {target['word_type']}")
                print(f"Nghĩa tiếng Việt: {target['meaning']}")
                guess = input("Đố bạn đây là từ tiếng Anh nào?: ").strip()
                
                if guess.lower() == target['word'].lower():
                    print("[+] Chính xác! Quá đỉnh.")
                else:
                    print(f"[-] Chưa chính xác. Đáp án đúng là: '{target['word']}'")
                if target.get('example'):
                    print(f"Gợi ý câu: {target['example']}")

        elif choice == '4':
            print("Tạm dừng hệ thống. Hẹn gặp lại!")
            sys.exit(0)
        else:
            print("[-] Lựa chọn không hợp lệ, vui lòng nhập từ 1 đến 4.")

if __name__ == "__main__":
    main()