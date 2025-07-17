# Trophy Dark Name Generator

A procedural name generator written in Python that creates unique, thematic names in the somber, melancholic style of the TTRPG [*Trophy Dark*](https://trophyrpg.com/) by [Jesse Ross](https://jesseross.com/) and published by [The Gauntlet](https://www.gauntlet-rpg.com/).

---
## About The Project

The names in the TTRPG *Trophy Dark* have a distinct sonic identity—melodic yet somber, and ancient-feeling. This project was built to programmatically capture that unique aesthetic. Instead of just picking random letters, this generator uses a layered system of rules, weights, and phonetic constraints to produce names that feel authentic to the game's setting of a grim, haunted forest. The original list of 36 names is included in the main code for easy reference.

The goal was not just to create names, but to build a **procedural language engine** that understands and speaks the stylistic language of *Trophy Dark*.

---
## Features

This generator uses a combination of techniques to ensure high-quality, thematic output:

* **Weighted Character Selection:** Common letters from the source material (like 'o', 'n', 'a', 'm', 's') appear more frequently.
* **Strict Vowel/Consonant Alternation:** Every name follows a perfect V-C-V-C... structure, which is the foundational rule for its melodic feel.
* **Complex Consonant Clash Rules:** A sophisticated set of rules prevents "hard" or phonetically awkward consonants (like 'k' and 't', or 'b' and 'p') from appearing in the same name, ensuring a consistently "soft" and flowing sound.
* **Thematic Ending Preferences:** Names are weighted to end in "trailing-off" sounds (like '-oh', '-ah', '-os', '-in'), contributing to the melancholic mood.
* **Extensive Prohibited Strings List:** A large set of hundreds of strings prevents the formation of awkward syllables, common English words and names, and inappropriate or offensive terms.
* **Syllable and Length Constraints:** Names are kept between 5-7 letters and capped at 3 syllables to feel substantial but not cumbersome.

---
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.x

### Usage

1.  Clone the repository or download the `main.py` file.
2.  Open a terminal or command prompt in the project directory.
3.  Run the script:
    ```sh
    python main.py
    ```
4.  The script will generate a batch of names and prompt you to generate more by entering `y` or `n`.

---
## Customization

The generator's style is controlled by the **`CONFIGURATION`** section at the top of `main.py`. You can easily change the "voice" of the generator by tweaking these parameters.

* **`VOWEL_WEIGHTS` & `CONSONANT_WEIGHTS`:** Change the letters or their numerical values to make certain letters more or less common.
* **`PROHIBITED_STRINGS`:** Add any word or letter combination you want to prevent from ever appearing.
* **`CLASH_RULES`:** Add or remove sets of letters to control which consonants can appear together in a single name. For example, to prevent 'd' and 'v' from appearing in the same name, simply add `{'d', 'v'},` to the list.
* **`PREFERRED_ENDING_VOWELS` & `PREFERRED_ENDING_CONSONANTS`:** Adjust the weights to change the probability of how names will end.

---
## Creating a Standalone Executable

You can package this script into a single `.exe` file for Windows that runs without needing Python installed.

1.  Install PyInstaller:
    ```sh
    pip install pyinstaller
    ```
2.  Run the command from your project directory:
    ```sh
    pyinstaller --onefile main.py
    ```
3.  The final `.exe` file will be located in the `dist` folder.

---
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

---
## Acknowledgments

* This project is a fan work inspired by the excellent TTRPG [*Trophy Dark*](https://trophyrpg.com/) created by [Jesse Ross](https://jesseross.com/) and published by [The Gauntlet](https://www.gauntlet-rpg.com/).
