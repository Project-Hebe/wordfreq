from wordfreq_builder.word_counts import count_tokens, write_wordlist
import argparse


def handle_counts(filename_in, filename_out, lang):
    counts = count_tokens(filename_in, lang)
    write_wordlist(counts, filename_out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename_in', help='name of input file containing tokens')
    parser.add_argument('filename_out', help='name of output file')
    parser.add_argument('lang', help='language of input file')
    args = parser.parse_args()
    handle_counts(args.filename_in, args.filename_out, args.lang)
