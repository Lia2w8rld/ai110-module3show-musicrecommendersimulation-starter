# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0: Music Recommender Simulation**

VibeFinder is a content-based music recommender that ranks songs according to a user's preferred genre, mood, and musical characteristics.

---

## 2. Intended Use

VibeFinder is designed to recommend songs that match a user's stated music preferences. It is intended for classroom exploration of recommendation algorithms and how scoring decisions influence the results.

The system considers a user's preferred genre and mood, target energy, valence, danceability, acousticness, and tempo. It assumes that these preferences provide a useful representation of the music the user wants to hear.

The system generates a ranked list of the top five songs from its catalog and explains why each song received its score. It does not learn from listening history, and it should not be treated as a replacement for a commercial music streaming recommendation system.

---

## 3. How the Model Works

VibeFinder compares the user's preferences with the attributes of each song. It awards points when a song matches the preferred genre or mood and calculates similarity scores for energy, valence, danceability, acousticness, and tempo.

The current scoring approach gives four points for a genre match, one point for a mood match, and up to one point for each of the five musical attribute similarities. The system then sorts songs from highest to lowest score and returns the top five recommendations, along with explanations of the scores.

Compared with the original starter logic, which returned the first songs in the catalog, I implemented CSV loading, numeric conversion, a scoring function, ranked recommendations, and explanations. I also expanded the dataset to 20 songs and tested multiple user profiles.

I experimented with increasing the genre-match bonus from two points to four points. This made genre preference more influential in the overall score.

---

## 4. Data

The recommender uses a CSV dataset containing **20 songs**. Each song has an ID, title, artist, genre, mood, energy, tempo in beats per minute, valence, danceability, and acousticness.

I expanded the starter dataset by adding songs to create a larger catalog for testing. The catalog includes genres and moods represented by the three profiles I tested: pop and happy, lofi and chill, and rock and intense.

The dataset is small and does not represent the full range of musical styles or listening preferences. Musical taste can also depend on lyrics, culture, memories, language, familiarity, production style, and personal experiences, none of which are fully captured by the current attributes.

---

## 5. Strengths

VibeFinder produces different recommendations for different preference profiles and provides explanations for its rankings.

The High-Energy Pop profile ranked *Sunrise City* first, the Chill Lofi profile ranked *Library Rain* first, and the Deep Intense Rock profile ranked *Wildfire Run* first. These results generally matched the preferences specified in each profile.

The model is also relatively easy to understand because its scoring rules are explicit. Changing a scoring weight makes it possible to observe how design decisions affect the scores and rankings.

---

## 6. Limitations and Bias

The system relies on a small catalog of 20 songs, so its recommendations are limited to the available data. Genres and moods that are not represented adequately cannot receive equally meaningful recommendations.

The genre-match bonus is four points, while each individual musical similarity contributes at most one point. This means genre can have a stronger influence than any single musical characteristic. As a result, a song in the preferred genre may receive a higher score even when another song matches several other preferences more closely.

The system does not consider listening history, explicit user feedback, lyrics, cultural context, or changes in a person's mood over time. It also does not currently prioritize diversity among artists or recommendations. Because the user profiles and song attributes are predefined, the results may not accurately represent the preferences of real listeners.

---

## 7. Evaluation

I tested VibeFinder using three profiles:

- **High-Energy Pop:** Ranked *Sunrise City* first, with a score of 9.73.
- **Chill Lofi:** Ranked *Library Rain* first, with a score of 9.78.
- **Deep Intense Rock:** Ranked *Wildfire Run* first, with a score of 9.89.

I checked that the program loaded all 20 songs, returned five recommendations per profile, sorted the results by score, and provided explanations. I also ran the project's automated tests, which passed.

For an additional experiment, I increased the genre-match bonus from two points to four points. Songs matching the preferred genre gained two points, but the top-five ordering stayed the same for the three profiles I tested.

I learned that changing a scoring rule does not always change the ranking. It can still affect the distance between scores and the relative importance of different preferences. The tests confirm that the program runs as expected, but they do not establish whether real listeners would enjoy the recommendations.

---

## 8. Future Work

I would improve VibeFinder by expanding the dataset to include more songs, genres, artists, and moods. I would also test additional profiles and compare their recommendations.

Another improvement would be adding diversity to the ranking so that the top five results do not become repetitive. The model could also support more complex preferences, such as combining multiple favorite genres or allowing users to adjust the importance of different musical attributes.

Finally, I would collect feedback from listeners to determine whether the recommendations match their actual tastes rather than relying only on predefined profiles.

---

## 9. Personal Reflection

This project taught me that a recommendation system reflects the choices made by the person designing its scoring rules. Even though the system uses numerical scores, those scores depend on decisions about which preferences matter most.

I was interested to discover that increasing the genre-match bonus changed the scores without changing the top-five rankings for my three test profiles. This helped me understand why it is important to examine both scores and rankings when evaluating a recommender.

The project also changed how I think about music recommendation apps. A ranked list may appear objective, but the results depend on the available data, the features being considered, and the weights assigned to different preferences. I would like to explore how recommendation systems can account for more complex musical tastes while offering both relevant and diverse suggestions.