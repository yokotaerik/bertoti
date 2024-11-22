from difflib import SequenceMatcher

def find_partial_match(cinema_text, user_text, cutoff=0.6):
    # Dividir o user_text em palavras
    words = user_text.split()
    
    # Percorrer todas as subseções do user_text que têm o mesmo comprimento que cinema_text
    for i in range(len(words) - len(cinema_text.split()) + 1):
        # Criar uma subseção do user_text com o mesmo número de palavras que cinema_text
        segment = ' '.join(words[i:i + len(cinema_text.split())])
        
        # Verificar a similaridade entre o cinema_text e a subseção
        similarity = SequenceMatcher(None, cinema_text.lower(), segment.lower()).ratio()
        
        # Retornar verdadeiro se a similaridade atingir o cutoff
        if similarity >= cutoff:
            return True
    
    return False

# Exemplo de uso
user_text = "quero ver os filmes do cinemark Colinas em sao jose dos campos"
cinema_text = "Cinemark Colinas"

if find_partial_match(cinema_text, user_text):
    print("Encontrou uma correspondência aproximada!")
else:
    print("Não encontrou correspondência.")
