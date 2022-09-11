from model import GenWords
import pickle
import argparse
import os


def main():
    model = GenWords()

    parser = argparse.ArgumentParser(description="Trains word-generating model")
    parser.add_argument("--input_dir", type=str, default="",
                        help="Path to the directory with the files for training the model")
    parser.add_argument("--model", type=str, default=".",
                        help="Path to the directory where the trained model will be stored")
    parser.add_argument("--prefix_size", type=int, default=2,
                        help="Size of prefix")
    args = parser.parse_args()

    input_path = args.input_dir
    model.fit(input_path, prefix_size=args.prefix_size)
    filename = "model.pkl"
    with open(os.path.join(args.model, filename), 'wb') as out:
        pickle.dump(model, out)


if __name__ == "__main__":
    main()