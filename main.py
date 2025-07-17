# By Jonah D. Hadlock

import random

# --- CONFIGURATION ---
# All tweakable parameters are grouped here for easy access.

# 1. CHARACTER & WEIGHT DEFINITIONS
VOWEL_WEIGHTS = {'a': 9, 'e': 7, 'i': 7, 'o': 10}
CONSONANT_WEIGHTS = {
    'l': 6, 'm': 8, 'n': 9, 'r': 7, 's': 6, 'd': 4, 'f': 3,
    'h': 5, 'p': 3, 'v': 3, 'b': 2, 'k': 4, 't': 2
}

# 2. PROHIBITED STRINGS
PROHIBITED_STRINGS = {
    # Awkward/undesirable letter strings
    "ab", "ahef", "ahe", "ahi", "aho", "ak", "aki", "ale", "ame", "anal", "alone", "amen", "ape", "api", "apo", "ase",
    "ato",
    "ave", "bd", "bek", "bib", "bile", "bipe", "bo", "bp", "br", "bt", "chr", "dam", "dl", "df", "dr", "dt", "dv", "eb",
    "efi", "ehe",
    "ehi", "eih", "eka", "eki", "ela", "elohi", "elon", "ep", "epi", "epo", "er", "es", "eso", "eti", "eto", "evil",
    "fap",
    "fat", "fb", "fe", "fik", "fine", "fip", "fis", "fk", "fl", "flip", "fob", "fod", "fok", "fom", "fp", "fr", "fs",
    "ft", "fv",
    "hap", "hasi", "hat", "hel", "hih", "hine", "hip", "hiso", "hot", "hp", "hr", "hs", "ht", "hv", "ib", "icr", "id",
    "ifa", "ifo", "ih", "ihe", "ihi", "ika", "ike", "iki", "iko", "ilan", "ile", "ime", "ine", "ipa", "ipe", "ipo",
    "ir",
    "ise", "isk", "it", "iv", "kas", "kep", "kik", "kite", "kiv", "ko", "kr", "ks", "kt", "lahe", "lake", "lamoni",
    "lase",
    "lb", "ld", "lf", "lh", "lia", "lina", "lk", "lom", "lose", "lp", "lr", "ls", "lt", "maf", "mahe", "md", "mf", "mh",
    "ml", "mofo", "mp", "mt", "mv", "name", "nd", "nf", "nl", "nose", "np", "nr", "nt", "nv", "ob", "ode", "odik",
    "ofa",
    "ofe", "ofi", "oha", "ohe", "ohi", "ok", "ol", "ome", "one", "op", "or", "orn", "osi", "oseh", "oso", "oto", "ov",
    "pb",
    "ped", "pedo", "pefa", "pek", "pena", "penis", "pep", "pf", "phil", "phr", "pib", "pic", "pis", "plit", "pod",
    "porn",
    "pr", "pt", "rape", "rak", "rb", "rd", "rf", "rh", "rib", "rio", "rk", "rl", "rm", "sab", "sak", "sat", "sch",
    "sd", "seman", "semen", "semin", "seb", "sf", "sh", "sik", "sip", "sit", "sk", "sl", "sm",
    "sn", "sob", "sod", "sort", "sp", "sr", "st", "tak", "tah", "tame", "tat", "tb", "td", "te",
    "tf", "th", "timo ", "tit", "tl", "toh", "tor", "tot", "tr", "vab", "vaf", "val", "vef", "vd", "vok", "vk", "vl", "vm",
    "vn", "vp", "vr", "vs", "vt", "afi", "asi", "aso", "bap", "bok", "dad", "dap", "dok", "fan", "fun", "lona", "lel",
    "made", "man",
    "mare", "mem", "men", "nare", "ose", "pak", "pal", "pan", "pen", "pin", "pop", "pot", "ror", "sad", "sare", "sas",
    "ses",
    "sin", "sis", "sos", "tan", "tek", "tik", "tin", "top", "van", "var", "vat",
    # Common names
    "albert", "amanda", "barbara", "brenda", "brian", "daniel", "david", "dennis", "donna", "frank", "harold", "kale",
    "kare", "kevin", "linda", "martin", "melissa", "pamela", "peter", "robert", "sam", "sandra", "sarah", "sharon", "steven",
    "theresa", "thomas", "todd",
    # Undesirable/inappropriate words/concepts
    "areola", "arouse", "ass", "baby", "bitch", "blowjob", "body", "boner", "boob", "butt", "child", "christ", "clit", "corpse",
    "cum", "cunt", "damn", "damis", "dead", "death", "devil", "dildo", "dum", "dumb", "erotic", "evil", "fart", "fecal",
    "flirt", "fuck", "gap", "glute", "god", "handjob", "hedon", "hell", "hot", "idiot", "image", "jesus", "kid", "kill",
    "masturbat", "mental", "minor", "moron", "naked", "negro", "nigger", "nipple", "nude", "off", "oral", "pee", "poop",
    "puss", "relig", "satan", "scrot", "sex", "shit", "spirit", "stupid", "teen", "teet", "testi", "thigh", "toot", "tween",
    "urine", "vagi", "wank"
}

# 3. CONSONANT CLASH RULES
# A list of sets. Each set defines characters that shouldn't appear together.
CLASH_RULES = [
    {'k', 'v', 't'},
    {'p', 'f', 't'},
    {'b', 't', 'k', 's'},
    {'t', 'd', 'k'},
    {'d', 'b'},
    {'b', 'p'},
    {'p', 's'},
    {'p', 'k'},
    {'f', 'b'},
    {'f', 'k'}
]

# 4. ENDING PREFERENCES
PREFERRED_ENDING_VOWELS = {'a': 9, 'o': 8, 'i': 7, 'e': 4}
PREFERRED_ENDING_CONSONANTS = {'n': 9, 'l': 3, 'm': 6, 'h': 7, 's': 5}

# --- PRE-CALCULATED LISTS FOR RANDOM.CHOICES ---
# These are derived from the configuration above.
VOWELS_POPULATION = list(VOWEL_WEIGHTS.keys())
VOWELS_WEIGHTS_LIST = list(VOWEL_WEIGHTS.values())
CONSONANTS_POPULATION = list(CONSONANT_WEIGHTS.keys())
CONSONANTS_WEIGHTS_LIST = list(CONSONANT_WEIGHTS.values())


def generate_trophy_name():
    """Generates a name using the rules defined in the configuration."""
    while True:
        name_length = random.randint(5, 7)
        name = []
        is_vowel_turn = random.choice([True, False])

        for i in range(name_length):
            is_last_char = (i == name_length - 1)

            for _ in range(10):  # Retry loop
                if is_vowel_turn:
                    char_map = PREFERRED_ENDING_VOWELS if is_last_char and random.random() < 0.75 else VOWEL_WEIGHTS
                else:  # Consonant's turn
                    char_map = PREFERRED_ENDING_CONSONANTS if is_last_char else CONSONANT_WEIGHTS

                # Create a pool of characters not already used in the name
                available_chars = [c for c in char_map if c not in name]
                if not available_chars:
                    continue

                available_weights = [char_map[c] for c in available_chars]
                selected_char = random.choices(available_chars, weights=available_weights, k=1)[0]
                temp_name = "".join(name + [selected_char])

                if not any(ps in temp_name for ps in PROHIBITED_STRINGS):
                    name.append(selected_char)
                    break
            else:
                name = None
                break

            if name is None:
                break

            is_vowel_turn = not is_vowel_turn

        if name and len(name) == name_length:
            final_name_str = "".join(name)

            # Check for 4+ syllables
            if sum(1 for char in final_name_str if char in VOWEL_WEIGHTS) >= 4:
                continue

            # Check all consonant clash rules dynamically
            is_invalid = any(len({c for c in final_name_str if c in rule_set}) > 1 for rule_set in CLASH_RULES)
            if is_invalid:
                continue

            return final_name_str.capitalize()


def run_generator_session():
    """Handles the interactive session of generating names."""
    while True:
        print("--- Generated Names ---")
        for _ in range(5):
            print(generate_trophy_name())

        # Ask the user if they want to generate more names
        while True:
            again = input("\nGenerate 5 more? (y/n): ").lower()
            if again in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if again == 'n':
            print("Exiting generator. Goodbye!")
            break
        print()


def main():
    """The main entry point for the program."""
    # The original list is not used by the generator, but kept for reference.
    OFFICIAL_TROPHY_NAMES = ["Akaleh", "Alina", "Aram", "Baso", "Benah", "Daian", "Desarim", "Elisio", "Esfahen",
                             "Fion",
                             "Foret", "Ifori", "Inda", "Kasien", "Kel", "Kiva", "Lora", "Mahera", "Masero", "Moradi",
                             "Neven",
                             "Nima", "Obeha", "Orlen", "Osto", "Parda", "Pela", "Rasei", "Revel", "Sareh", "Sibil",
                             "Talia",
                             "Teodan", "Toram", "Valen", "Vero"]

    run_generator_session()


# --- MAIN EXECUTION BLOCK ---
# This line checks if the script is being run directly (not imported)
if __name__ == "__main__":
    main()