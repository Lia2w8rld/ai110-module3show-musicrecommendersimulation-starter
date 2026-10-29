
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Recommend songs based on a user's preferences."""
        def calculate_score(song: Song) -> float:
            score = 0.0

            if song.genre.lower() == user.favorite_genre.lower():
                score += 2

            if song.mood.lower() == user.favorite_mood.lower():
                score += 1

            score += max(0.0, 1.0 - abs(song.energy - user.target_energy))

            if user.likes_acoustic:
                score += song.acousticness
            else:
                score += 1.0 - song.acousticness

            return score

        return sorted(
            self.songs,
            key=calculate_score,
            reverse=True
        )[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song was recommended."""
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append(f"matches your favorite genre ({song.genre})")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append(f"matches your favorite mood ({song.mood})")

        if abs(song.energy - user.target_energy) <= 0.15:
            reasons.append("has energy close to your target")

        if user.likes_acoustic and song.acousticness >= 0.6:
            reasons.append("has a relatively acoustic sound")
        elif not user.likes_acoustic and song.acousticness < 0.4:
            reasons.append("has a less acoustic sound")

        if not reasons:
            reasons.append("scored well across the selected features")

        return "This song " + " and ".join(reasons) + "."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            for field, converter in numeric_fields.items():
                row[field] = converter(row[field])

            songs.append(row)

    print(f"Loaded {len(songs)} songs from {csv_path}.")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 4
        reasons.append(f"Genre match: {song['genre']} (+4)")

    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1
        reasons.append(f"Mood match: {song['mood']} (+1)")

    target_energy = user_prefs.get("energy", 0.5)
    energy_points = max(0.0, 1.0 - abs(song["energy"] - target_energy))
    score += energy_points
    reasons.append(f"Energy similarity: {energy_points:.2f}/1.00")

    target_valence = user_prefs.get("valence", 0.5)
    valence_points = max(0.0, 1.0 - abs(song["valence"] - target_valence))
    score += valence_points
    reasons.append(f"Valence similarity: {valence_points:.2f}/1.00")

    target_danceability = user_prefs.get("danceability", 0.5)
    dance_points = max(
        0.0, 1.0 - abs(song["danceability"] - target_danceability)
    )
    score += dance_points
    reasons.append(f"Danceability similarity: {dance_points:.2f}/1.00")

    target_acousticness = user_prefs.get("acousticness", 0.5)
    acoustic_points = max(
        0.0, 1.0 - abs(song["acousticness"] - target_acousticness)
    )
    score += acoustic_points
    reasons.append(f"Acousticness similarity: {acoustic_points:.2f}/1.00")

    target_tempo = user_prefs.get("tempo_bpm", 100)
    tempo_points = max(
        0.0, 1.0 - abs(song["tempo_bpm"] - target_tempo) / 100.0
    )
    score += tempo_points
    reasons.append(f"Tempo similarity: {tempo_points:.2f}/1.00")

    return round(score, 2), reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(
        scored_songs,
        key=lambda recommendation: recommendation[1],
        reverse=True
    )

    return ranked_songs[:k]
