class BlockTranspositionCipher:
    def __init__(self, text, key, decrypt=False):
        self.text = text
        self.key = self._validate_key(key)
        self.decrypt = decrypt
        self.block_size = len(key)
        self.current_pos = 0
        
        self.permutation = self._create_permutation()
        if decrypt:
            self.permutation = self._inverse_permutation()
    
    def _validate_key(self, key):
        if not isinstance(key, str) or not key.isalpha():
            raise ValueError("Ключ должен содержать только буквы английского алфавита")
        
        lower_key = key.lower()
        if len(set(lower_key)) != len(lower_key):
            raise ValueError("Ключ должен содержать уникальные буквы (регистр не учитывается)")
        
        return lower_key
    
    def _create_permutation(self):
        sorted_chars = sorted((char, idx) for idx, char in enumerate(self.key))
        return [idx for char, idx in sorted_chars]
    
    def _inverse_permutation(self):
        inverse = [0] * len(self.permutation)
        for new_pos, old_pos in enumerate(self.permutation):
            inverse[old_pos] = new_pos
        return inverse
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_pos >= len(self.text):
            raise StopIteration
        
        block = self.text[self.current_pos:self.current_pos + self.block_size]
        block = block.ljust(self.block_size)
        self.current_pos += self.block_size
        
        result = [''] * self.block_size
        for new_pos, old_pos in enumerate(self.permutation):
            result[new_pos] = block[old_pos]
        
        return ''.join(result)

try:
    # Пример 1: Шифрование с явной итерацией по блокам
    text = "HELLOWORLD"
    key = "bAc"
    print("Процесс шифрования по блокам:")
    cipher = BlockTranspositionCipher(text, key)
    for i, encrypted_block in enumerate(cipher, 1):
        print(f"Блок {i}: '{encrypted_block}'")
    
    # Пример 2: Полное шифрование
    cipher = BlockTranspositionCipher(text, key)
    encrypted = ''.join(cipher)
    print(f"\nПолный зашифрованный текст: '{encrypted}'")
    
    # Пример 3: Дешифрование с итерацией
    print("\nПроцесс дешифрования по блокам:")
    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    for i, decrypted_block in enumerate(decipher, 1):
        print(f"Блок {i}: '{decrypted_block}'")
    
    # Пример 4: Полное дешифрование с обрезкой пробелов
    decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
    decrypted = ''.join(decipher).rstrip()
    print(f"\nПолный расшифрованный текст: '{decrypted}'")

except ValueError as e:
    print(f"Ошибка: {e}")