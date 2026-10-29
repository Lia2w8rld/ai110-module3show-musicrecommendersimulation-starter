# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real-world music recommendation systems use information about listeners and songs to suggest music. Collaborative filtering finds patterns in user behavior, such as listening history, likes, skips, and playlists. Content-based filtering compares song characteristics with a user's preferences.

This project uses content-based filtering. It loads songs from a CSV file, calculates a score for each song based on the user's preferences, and ranks songs to produce recommendations.

### Song Features
- Genre and mood
- Energy
- Tempo in beats per minute
- Valence
- Danceability
- Acousticness

### UserProfile Features
The user profile stores a preferred genre, preferred mood, and target values for energy, tempo, valence, danceability, and acousticness.

### Algorithm Recipe
- Genre match: +2 points.
- Mood match: +1 point.
- Numerical features: award up to 1 point per feature based on similarity to the user's target.
- Calculate a total score for each song.
- Sort by total score in descending order and return the top k songs.

For energy, valence, danceability, and acousticness, similarity is calculated as 1 minus the absolute difference between the song's value and the user's target. For tempo, the difference is normalized because BPM uses a different scale.

### Data Flow
User preferences → Load songs from CSV → Score each song → Rank by score → Display top recommendations with explanations.

### Expected Biases
The dataset is small and may not represent all musical genres or listener preferences. The chosen scoring weights may favor songs that match specific features while overlooking songs a listener might enjoy for other reasons. The system also does not learn from real listening behavior or feedback.

## User Taste Profiles

The recommender uses three simulated user profiles to test how preferences affect recommendations.

1. **High-Energy Pop:** Prefers pop music, happy moods, high energy (0.85), high valence (0.80), high danceability (0.85), and a tempo near 125 BPM.
2. **Chill Lofi:** Prefers lofi music, chill moods, low energy (0.35), moderate valence (0.60), low-to-moderate danceability (0.45), high acousticness (0.80), and a tempo near 75 BPM.
3. **Deep Intense Rock:** Prefers rock music, intense moods, high energy (0.90), lower valence (0.40), moderate danceability (0.60), low acousticness (0.15), and a tempo near 150 BPM.

## Scoring Algorithm

The system assigns points based on how closely each song matches a user's preferences:

- Matching genre: +2 points.
- Matching mood: +1 point.
- Energy similarity: up to +1 point, based on the difference between the song's energy and the user's target energy.
- Valence similarity: up to +1 point.
- Danceability similarity: up to +1 point.
- Acousticness similarity: up to +1 point.
- Tempo similarity: up to +1 point, based on the difference between the song's BPM and the target tempo.

Songs are sorted from highest to lowest score, and the system returns the top K songs. **Scoring** measures how well a song matches the profile; **ranking** orders songs by their scores.

## Data Flow

User profile → load song data from CSV → calculate each song's score and matching reasons → sort by score → display the top K recommendations.

## Expected Limitations and Biases

The dataset contains simulated songs and manually assigned attributes, not listening histories from real users. Genre and mood labels may oversimplify music, and the scoring weights reflect design choices rather than proven preferences. The system may favor songs that match the selected labels and numerical targets while overlooking personal associations, cultural context, and individual interpretations of a song.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
High Energy Pop 
  1. Sunrise City 7.73 
  2. Gym Hero 6.59
  3. Rooftop Lights  5.76
  4. Golden Hour Drive 5.41
  5. Voltage Dreams 5.36

Chill Lofi 
  1. Library Rain 7.78 
  2. Midnight Coding 7.60 
  3. Focus Flow 6.72
  4. Blue Hour Letter 5.78 
  5. Spacewalk Thoughts 5.57

Deep Intense Rock 
  1. Wildfire Run 7.89 
  2. Storm Runner 7.78
  3. Heavy Weather 5.63 
  4. Gym Hero 5.04 
  5. Neon Afterglow 4.23 

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

The initial experiment compared recommendations across three different preference profiles. The leading recommendations changed with the genre, mood, and numerical targets: pop favored Sunrise City, lofi favored Library Rain, and rock favored Wildfire Run.

A further experiment will change the scoring weights to investigate whether genre matches or numerical similarity has a stronger influence on the rankings.

I changed the genre-match bonus from 2 points to 4 points to test how strongly genre preference affects recommendations. Songs matching a user's preferred genre gained 2 additional points, while songs from other genres kept their original scores. For example, Sunrise City scored 9.73 for the High-Energy Pop profile, Library Rain scored 9.78 for Chill Lofi, and Wildfire Run scored 9.89 for Deep Intense Rock. The top-five rankings did not change for these profiles, but the scores of genre-matching songs increased. This demonstrates how changing a scoring weight can make one preference more influential without necessarily changing the final ranking.
## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



