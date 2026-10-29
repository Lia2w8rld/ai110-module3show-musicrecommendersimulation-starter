
"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    
    # Three user profiles for comparison
    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85,
            "valence": 0.80,
            "danceability": 0.85,
            "acousticness": 0.25,
            "tempo_bpm": 125,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "valence": 0.60,
            "danceability": 0.45,
            "acousticness": 0.80,
            "tempo_bpm": 75,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.90,
            "valence": 0.40,
            "danceability": 0.60,
            "acousticness": 0.15,
            "tempo_bpm": 150,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nTop 5 recommendations for {profile_name}:\n")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()



if __name__ == "__main__":
    main()
