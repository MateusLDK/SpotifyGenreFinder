"""
Genre Classifier Module

Este módulo contém a lógica de classificação de gêneros musicais.
Mapeia os gêneros do Spotify para categorias mais amplas e organizadas.
"""

def classify_genre(genres):
    """
    Classifica uma lista de gêneros em uma categoria principal.
    
    Args:
        genres (list): Lista de gêneros retornados pela API do Spotify
        
    Returns:
        str: Categoria de gênero classificada
    """
    genre_map = [
        ('metal', 'Metal'),
        ('core', 'Metal'),
        ('djent', 'Metal'),
        ('rock', 'Rock'),
        ('punk', 'Punk'),
        ('emo', 'Emo'),
        ('pop', 'Pop'),
        ('hip-hop', 'Hip-Hop'),
        ('rap', 'Rap'),
        ('indie', 'Indie'),
        ('alternative', 'Alternative'),
        ('folk', 'Folk'),
        ('jazz', 'Jazz'),
        ('blues', 'Blues'),
        ('country', 'Country'),
        ('reggae', 'Reggae'),
        ('electronic', 'Electronic'),
        ('house', 'House'),
        ('techno', 'Techno'),
        ('edm', 'EDM'),
        ('grunge', 'Grunge'),
        ('funk', 'Funk'),
        ('soul', 'Soul'),
        ('disco', 'Disco'),
        ('trap', 'Trap'),
        ('gospel', 'Gospel'),
        ('classical', 'Classical'),
        ('opera', 'Opera'),
        ('ambient', 'Ambient'),
        ('drum and bass', 'Drum & Bass'),
        ('dubstep', 'Dubstep'),
        ('samba', 'Samba'),
        ('pagode', 'Pagode'),
        ('sertanejo', 'Sertanejo'),
        ('forro', 'Forró'),
        ('axé', 'Axé'),
        ('mpb', 'MPB'),
        ('bossa nova', 'Bossa Nova'),
        ('reggaeton', 'Reggaeton'),
        ('latin', 'Latin'),
        ('k-pop', 'K-Pop'),
        ('j-pop', 'J-Pop'),
        ('lo-fi', 'Lo-Fi'),
        ('hardcore', 'Hardcore'),
        ('ska', 'Ska'),
        ('bluegrass', 'Bluegrass'),
        ('world', 'World'),
        ('new age', 'New Age'),
    ]
    
    if not genres:
        return 'Unknown'
    
    for key, value in genre_map:
        if any(key in genre for genre in genres):
            return value
    
    return 'Other'
