import json
import random
from typing import Dict, List


class VocabManager:
	def __init__(self, file_path: str) -> None:
		self.file_path = file_path

	def add_word(
		self, word: str, word_type: str, meaning: str, example: str = ""
	) -> bool:
		try:
			with open(self.file_path, "r", encoding="utf-8") as file:
				words = json.load(file)

			words.append(
				{
					"word": word,
					"word_type": word_type,
					"meaning": meaning,
					"example": example,
				}
			)

			with open(self.file_path, "w", encoding="utf-8") as file:
				json.dump(words, file, ensure_ascii=False, indent=2)

			return True
		except FileNotFoundError as error:
			print(f"Lỗi: Không tìm thấy file từ vựng: {error}")
			return False
		except json.JSONDecodeError as error:
			print(f"Lỗi: File JSON không hợp lệ: {error}")
			return False

	def list_words(self) -> List[Dict]:
		try:
			with open(self.file_path, "r", encoding="utf-8") as file:
				return json.load(file)
		except FileNotFoundError as error:
			print(f"Lỗi: Không tìm thấy file từ vựng: {error}")
			return []
		except json.JSONDecodeError as error:
			print(f"Lỗi: File JSON không hợp lệ: {error}")
			return []

	def get_random_word(self) -> dict | None:
		words = self.list_words()
		if not words:
			return None
		return random.choice(words)
