# This script is a demonstration of a real world use
# case for regular expressions. We are processing an
# annotated chat file in .cha annotation format. We
# would like to extract the basic information into a
# simpler, easier to process format (json).  Note
# the use of regular expressions in processing text
# line by line in this script (lines 61 to 97).

# Process data from raw CHAT files into
# JSON for annotation for language
import json
import re

years = ["2008", "2020"]
all_utterances = []


def main():
    # Hard coding the file name here for demonstration
    # purposes only
    process_file("2020", "./", "annotated_chat_questions.cha")

    try:
        out = open('utterances.json', 'w')
    except OSError as e:
        print(f"Can't open utterances.json for writing: {e}")
        return

    for utt in all_utterances:
        print(utt)
        out.write(json.dumps(utt)+',\n')


task_langs = {
    "questions": "unspecified",
    "car": "english",
    "dogbowl": "spanish",
    "shinyballs": "english",
    "umbrella": "spanish",
    "wrapup": "unspecified",
    "sizeballs": "english",
    "camelbirds": "spanish",
    "fastfood": "english",
    "monkeys": "spanish",
    "blueball": "english",
    "t-shirt": "spanish",
    "girls": "english",
    "rabbitbear": "spanish"
}


def process_file(year, path, file_name):
    try:
        f = open(path+file_name, 'r')
    except OSError as e:
        print(f"Can't open {path+file_name} for writing: {e}")
        return
    # Define a regex to match parts of the file name
    m = re.match(r".*\_(\w+\-*?\w+)\.cha", file_name)
    speaker_dict = {}
    utterances = []
    if m:
        # Use the regex to extract the task ("questions") from
        # the file name
        task = m.groups(1)[0].lower()
        if task in task_langs.keys():
            expected_lang = task_langs[task]
        else:
            print(task, year, path, file_name)

        utterance = ""
        what_to_do = 'ignore'  # otherwise collect
        for ln in f:
            # Used this inline Perl script to fix some files
            # from the command line (with a regex). Basically
            # this just removes blank newlines.
            # perl -i -pe  's/\@ID\:\s*(\w\w\w)\,\s*\n\s*/\@ID\:   \1\, /g' */*.cha  # noqa: E501

            # Create a regex to match lines beginning with @ID and capture
            # relevant information. The first capture group will get the
            # User id, the second capture group will get the gender,
            # and the third capture group will get "English" or "Spanish"
            id_match = re.match(
                r'@ID:.*(ST.*?)\|\|(\w*).*\|(\w\w\w\wish)\_', ln
                )
            if id_match:
                speaker_dict[id_match.groups(1)[0]] = (
                    id_match.groups(1)[1], id_match.groups(1)[2].lower()
                    )
            # Use a regex to match lines beginning with '@Comment'
            if re.match(r'\@Comment', ln):
                if what_to_do == 'collect':
                    log_utterance(
                        utterances, utterance, year, speaker_dict,
                        path, file_name, task, expected_lang,
                        )
                    what_to_do = 'ignore'
            # Use a regex to match lines beginning with '@mor'
            elif re.match(r'\%mor\:', ln):
                if what_to_do == 'collect':
                    log_utterance(
                        utterances, utterance, year, speaker_dict,
                        path, file_name, task, expected_lang
                        )
                    what_to_do = 'ignore'
            # Use a regex to match lines beginning with '*ST'
            elif re.match(r'\*ST.*?\:', ln):
                # new_line = ln
                if what_to_do == 'collect':
                    log_utterance(
                        utterances, utterance, year, speaker_dict,
                        path, file_name, task, expected_lang
                        )
                utterance = ln.strip()
                what_to_do = 'collect'
            else:
                if what_to_do == 'collect':
                    utterance = utterance + ' ' + ln.strip()

    for ind, utt in enumerate(utterances):
        utt['index'] = ind

        # if len(speaker_dict.keys()) != 2:
        #     print(year, path, file_name)

        all_utterances.append(utt)


def log_utterance(utterances, utterance, year, speaker_dict,
                  path, file_name, task, expected_lang):
    # Use a regex to get speaker ID and utterance content from
    # the line
    ut_match = re.match(r'\*(ST.*?)\:\s*(.*)', utterance)
    speaker = ut_match.groups(1)[0]
    utterance = ut_match.groups(1)[1]

    # Use regexes to strip out unwanted metacharacters
    utterance = re.sub(r'<|>|\[|\]|&=laughs|&.', r'', utterance)
    utterance = re.sub(r'(\w)\@l', r"'\1'", utterance)

    utt_object = {
        'year': year,
        'file': file_name,
        'task': task,
        'task_lang': expected_lang,
        'spkr_id': speaker,
        'spkr_gen': speaker_dict[speaker][0],
        'spkr_l1': speaker_dict[speaker][1],
        'utterance': utterance
    }

    utterances.append(utt_object)


main()
